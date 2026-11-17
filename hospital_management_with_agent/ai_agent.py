from langchain.agents import create_agent
from langchain_openai import AzureChatOpenAI
from config.settings import AZURE_OPENAI_API_KEY,AZURE_OPENAI_API_VERSION,AZURE_OPENAI_DEPLOYMENT,AZURE_OPENAI_ENDPOINT

from tool.ai_tool import *

def create_hospital_agent():

    llm = AzureChatOpenAI(
        api_key=AZURE_OPENAI_API_KEY,
        azure_endpoint=AZURE_OPENAI_ENDPOINT,
        api_version=AZURE_OPENAI_API_VERSION,
        azure_deployment=AZURE_OPENAI_DEPLOYMENT,
    )

    tools = [
        register_patient,
        check_doctor_availability,
        book_appointment,
        get_patient_medical_records,
        calculate_hospital_bill
    ]

    return create_agent(
        model=llm,
        tools=tools
    )
    