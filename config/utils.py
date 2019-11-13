import os
from dotenv import load_dotenv

load_dotenv()

def get_env_vars(variable_name):
  '''
    function to get environment variables. returns none if the environment variable has not been set
  '''
  return os.getenv(variable_name)
