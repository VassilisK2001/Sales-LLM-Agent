import os

# If running the Docker container locally and using a .env file for environment variables,
# import load_dotenv from dotenv and call the function to load environment variables.
# Uncomment the lines below:

# from dotenv import load_dotenv
# load_dotenv()

# Access environment variables using os.environ when deployed on cloud services like AWS Elastic Beanstalk.
# If running locally with a .env file, you can also use os.getenv('ENV_VARIABLE') for added flexibility.

OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
SERPAPI_API_KEY = os.environ['SERPAPI_API_KEY']
PERPLEXITY_API_KEY = os.environ['PERPLEXITY_API_KEY']
FLASK_SECRET_KEY = os.environ['FLASK_SECRET_KEY']

# Alternatively, if running locally:
# OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
