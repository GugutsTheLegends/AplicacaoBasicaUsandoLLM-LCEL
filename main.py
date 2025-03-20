"""from langchain_core.messages import HumanMessage, SystemMessage

from langchain_core.prompts import ChatMessagePromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from dotenv import load_dotenv, find_dotenv
import os 

load_dotenv(find_dotenv())
groq_api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(

    model = "Gemma2-9b-It",
    groq_api_key = groq_api_key,






)


messages = [
    SystemMessage(content="Translate the following sentence from English to French"),
    HumanMessage(content="Hello, how are you?")




]



result = llm.invoke(messages)
print(result)"""



#IMPORTAÇÃO DAS BIBLIOTECAS
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from dotenv import load_dotenv, find_dotenv
import os
import getpass
import os


#CARREGANDO AS VARIÁVEIS DE AMBIENTE
load_dotenv(find_dotenv())
groq_api_key = os.getenv("GROQ_API_KEY")

#CRIAR O MODELO GROQ
llm = ChatGroq(
    model = "Gemma2-9b-It", # MODELO DE LLM UTILIZADO
    groq_api_key = groq_api_key # CHAVE DE API DO GROQ
)

#CRIAR O PROMPT ** ESTUDAR SOBRE PROMPT ENGINEERING (FEW-SHOT, ZERO-SHOT, ONE-SHOT, CHAIN OF THOUGHTS)


parser = StrOutputParser()

generic_template = "Translate the following sentence into {language}"


prompt = ChatPromptTemplate.from_messages(
    [

        ("system", generic_template),
        ("user", "{text}")

]

)



chain = prompt | llm | parser 


chain.invoke({'language':'German', 'text':'hello'})







