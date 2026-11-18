from modes.ai_models import TrainerRequest, TrainerResponse
import json

from config.settings import(
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_API_VERSION,
    AZURE_OPENAI_DEPLOYMENT,
    AZURE_OPENAI_ENDPOINT
)

from  prompts.ai_prompts import SYSTEM_PROMPT, HUMAN_PROMPT
from openai import AzureOpenAI
from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

llm = AzureChatOpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    api_version=AZURE_OPENAI_API_VERSION,
    azure_deployment=AZURE_OPENAI_DEPLOYMENT,
    azure_endpoint=AZURE_OPENAI_ENDPOINT
)

structured_llm = llm.with_structured_output(
    TrainerResponse
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system",SYSTEM_PROMPT),
        ("user",HUMAN_PROMPT)
        
    ]
)

chain = prompt | structured_llm

def analyze(request:TrainerRequest)-> TrainerResponse:
     response = chain.invoke({
        "trainer_name":request.trainer_name,
        "learner_name" : request.learner_name,
        "trainer_topic" :request.trainer_name,
        "trainer_feedback":request.trainer_feedback,
        "trainer_rating" :request.trainer_rating
     }
     )
    
     return response