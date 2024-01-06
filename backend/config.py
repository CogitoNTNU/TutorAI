import os
from dotenv import load_dotenv

"""
This module provides the Config class to manage configuration variables
from environment files. It also supports fetching test cases 
ifthe configuration is loaded from a test environment file.
"""

#a class for defining the config variables
class Config():
    def __init__(self, path='config.env', gpt_model="gpt-3.5-turbo"):
        self.path = path
        self.GPT_MODEL = gpt_model
        load_dotenv(dotenv_path=path)
        self.API_KEY = os.getenv('OPEN_AI_API_KEY')
    
        
