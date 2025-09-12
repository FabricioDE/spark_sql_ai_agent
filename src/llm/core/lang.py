import os
import re
import pickle
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain





class Worker:
    def __init__(self, output):
        self.path_output=output
        

    def read_file(self, path: str) -> str:
        with open(path, "r", encoding="utf-8") as f:
            file = f.read()
        return file
    
    def create_dir(self) -> str:
        if not os.path.exists(self.path_output):
            os.makedirs(self.path_output, exist_ok=True)
            
    def write_file(self, name: str, content: str) -> str:
        self.create_dir()
        path = self.path_output + name

        if not path.endswith(".sql"):
            path += ".sql"

        with open(path, "w", encoding="utf-8") as f:
            f.write(content.strip() + "\n")




class Agent(Worker):
    def __init__(self):
        super().__init__(output = "../../output/") 
        self.llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
        

    def clean_sql(self, path: str) -> str:
        sql = self.read_file(path)
        sql = re.sub(r'--.*', '', sql)
        sql = re.sub(r'/\*.*?\*/', '', sql, flags=re.DOTALL)
        return sql.strip()


    def load_embeddings(self, pkl_path: str) -> str:
        if os.path.exists(pkl_path):
            with open(pkl_path, "rb") as f:
                embeddings = pickle.load(f)
            return embeddings
        return None

    def load_glossary(self, pkl_path: str) -> str:
        if os.path.exists(pkl_path):
            with open(pkl_path, "rb") as f:
                embeddings = pickle.load(f)
            return embeddings
        return None

    def sql_to_spark(self, sql_clean: str, output_name: str, embeddings=None, glossary=None) -> str:
        prompt_text = f"""
        Convert the following SQL query to Spark SQL syntax:

        {sql_clean}

        {"Consider these context embeddings: " + str(embeddings) if embeddings else ""}
        {"Consider this context glossary to convert sql to spark sql: " + str(glossary) if glossary else ""}
        """

        prompt = PromptTemplate(input_variables=[], template=prompt_text)
        chain = LLMChain(llm=self.llm, prompt=prompt)
        spark_sql = chain.run({})
        self.write_file(output_name, spark_sql)
        print('File Converted')

    

    