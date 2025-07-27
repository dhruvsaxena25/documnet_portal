from datetime import datetime
import structlog
import inspect 
import logging
import os

# class CustomLogger:
#     def __init__(self, log_dir = "logs"):
        
#         # Ensure logs directory exists
#         self.logs_dir = os.path.join(os.getcwd(), log_dir)
#         os.makedirs(self.logs_dir, exist_ok=True)

#         # Create timestamped log file name
#         log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
#         log_file_path = os.path.join(self.logs_dir, log_file)

#         # Configure logging
#         logging.basicConfig(
#             filename=log_file_path,
#             format="[ %(asctime)s ] %(levelname)s %(name)s (line:%(lineno)d) - %(message)s",
#             level=logging.INFO,
#         )
    
#     def get_logger(self, name= __file__):
        
#         return logging.getLogger(os.path.basename(name))

# if __name__ == "__main__":
#     logger=CustomLogger()
#     logger=logger.get_logger(__file__)
#     logger.info("Custom logger initialized.")

class CustomLogger:
    """
    Custom structured logger using structlog, with both console and file output.
    """

    def __init__(self, log_dir="logs"):
        """
        Initializes the logging directory and log file.
        """
        self.logs_dir = os.path.join(os.getcwd(), log_dir)
        os.makedirs(self.logs_dir, exist_ok=True)

        log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
        self.log_file_path = os.path.join(self.logs_dir, log_file)

    def get_logger(self, name=__file__):
        """
        Returns a structured logger configured for console and file logging.
        """
        logger_name = os.path.basename(name)

        # Setup file and console handlers
        file_handler = logging.FileHandler(self.log_file_path)
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(logging.Formatter("%(message)s"))

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(logging.Formatter("%(message)s"))

        logging.basicConfig(
            level=logging.INFO,
            format="%(message)s",
            handlers=[console_handler, file_handler]
        )

        # Configure structlog
        structlog.configure(
            processors=[
                structlog.processors.TimeStamper(fmt="iso", utc=True, key="timestamp"),
                structlog.processors.add_log_level,
                structlog.processors.EventRenamer(to="event"),
                CustomLogger.add_callsite_info,  # Static method call
                structlog.processors.JSONRenderer()
            ],
            logger_factory=structlog.stdlib.LoggerFactory(),
            cache_logger_on_first_use=True,
        )

        return structlog.get_logger(logger_name)

    @staticmethod
    def add_callsite_info(_, __, event_dict):
        """
        Adds caller file, line number, and function name to the log record.
        """
        frame = inspect.currentframe()
        outer_frames = inspect.getouterframes(frame)
        if len(outer_frames) > 6:
            caller = outer_frames[6]
            event_dict["caller_file"] = os.path.basename(caller.filename)
            event_dict["caller_line"] = caller.lineno
            event_dict["caller_func"] = caller.function
        return event_dict


# --- Usage Example ---
if __name__ == "__main__":
    logger = CustomLogger().get_logger(__file__)
    logger.info("User uploaded a file", user_id=123, filename="report.pdf")
    logger.error("Failed to process PDF", error="File not found", user_id=123)