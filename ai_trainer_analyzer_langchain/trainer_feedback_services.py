from models.trainer_feedback_models import TrainerFeedbackRequest, TrainerFeedbackResponse
import json

from config.settings import (
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_API_VERSION,
    AZURE_OPENAI_DEPLOYMENT,
    AZURE_OPENAI_ENDPOINT
)

from  prompts.trainer_feedback_prompts import SYSTEM_PROMPT, HUMAN_PROMPT
from openai import AzureOpenAI
from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

llm = AzureChatOpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    api_version=AZURE_OPENAI_API_VERSION,
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    azure_deployment=AZURE_OPENAI_DEPLOYMENT
)

structured_llm = llm.with_structured_output(
    TrainerFeedbackResponse
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system",SYSTEM_PROMPT),
        ("user",HUMAN_PROMPT)
        
    ]
)

chain = prompt | structured_llm



def anallyze(request:TrainerFeedbackRequest) -> TrainerFeedbackResponse:
    response = chain.invoke(
        {
            "trainer_name":request.trainer_name,
            "training_topic":request.training_topic,
            "learner_name": request.learner_name,
            "rating":request.rating,
            "feedback":request.feedback
                
        }
    )
    return response
    
    
    
  
    