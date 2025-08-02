
from langchain_core.output_parsers import JsonOutputParser
from langchain.output_parsers import OutputFixingParser
from exception.custom_exception import DocumentPortalException
from logger.custom_logging import CustomLogger
from model.models import * 
from prompt.prompt_library import PROMPT_REGISTRY
from utils.model_loader import ModelLoader
from dotenv import load_dotenv
import pandas as pd
import sys
import os



class DocumentComparatorLLM:
    
    def __init__(self):
        pass
    
    
    def compare_documents(self):
        pass
    
    
    def _format_response(self):
        pass
    
    