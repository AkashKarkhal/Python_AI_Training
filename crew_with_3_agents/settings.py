import os
from dotenv import load_dotenv
from crewai import LLM

load_dotenv()

AZURE_DEPLOYMENT = os.getenv("OPENAI_DEPLOYMENT")
AZURE_API_KEY = os.getenv("OPENAI_API_KEY")
AZURE_ENDPOINT = os.getenv("OPENAI_ENDPOINT")
AZURE_API_VERSION = os.getenv("OPENAI_API_VERSION")

if not all([
    AZURE_API_KEY,
    AZURE_API_VERSION,
    AZURE_DEPLOYMENT,
    AZURE_ENDPOINT
]):
    raise ValueError("Azure OpenAI configuration is missing")

llm = LLM(
    model=f"azure/{AZURE_DEPLOYMENT}",
    api_key=AZURE_API_KEY,
    endpoint=AZURE_ENDPOINT,
    api_version=AZURE_API_VERSION
)