import os
import re
import pickle
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from core.lang import Agent
from core.config import sql_file,embeddings_file,glossary_file,output_name

ag = Agent()



sql_cleaned = ag.clean_sql(sql_file)
embeddings = ag.load_embeddings(embeddings_file)  
glossary = ag.load_glossary(glossary_file)
spark_sql = ag.sql_to_spark(sql_cleaned, output_name, embeddings, glossary)


