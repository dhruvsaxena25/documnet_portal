from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq

from exception.custom_exception import DocumnetPortalException
from logger.custom_logging import CustomLogger
from utils.config_loader import load_config

from dotenv import load_dotenv
import os


log = CustomLogger().get_logger(__name__)

class ModelLoader:
    
    def __init__(self):
        pass
    
    def _validate_env(self):
        pass
    
    def load_embeddings(self):
        pass
    
    def load_llm(self):
        pass
    
    
    