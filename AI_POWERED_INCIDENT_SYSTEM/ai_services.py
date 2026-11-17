from openai import AzureOpenAI
from models.ai_models import IncidentRequest, IncidentAnalysis
from config.settings import *
from prompts.ai_prompts import *

client = AzureOpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    api_version=AZURE_OPENAI_API_VERSION,
    azure_endpoint=AZURE_OPENAI_ENDPOINT
)

def analyze(request: IncidentRequest):


    return IncidentAnalysis(
        category="server",
        priority="critical",
        summary="Production server down",
        business_impact="Users unable to access application",
        suggested_resolution="Restart service and check logs"
    )