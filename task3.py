from tavily import TavilyClient
import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# Create the client using your key
client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
print(os.getenv("TAVILY_API_KEY"))
