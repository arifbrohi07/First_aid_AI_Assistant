from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from prompts.medical_prompt import medical_prompt
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize Groq LLM
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.1-8b-instant"
)

# Create prompt template
prompt = PromptTemplate(
    input_variables=["disease", "days"],
    template=medical_prompt
)

# LCEL chain (modern replacement for LLMChain)
first_aid_chain = prompt | llm

def get_first_aid_response(disease, days):
    response = first_aid_chain.invoke({
        "disease": disease,
        "days": days
    })
    
    # Extract text content (ChatGroq returns AIMessage)
    return response.content