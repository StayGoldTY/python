# -*- coding: utf-8 -*-
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain import OpenAI, VectorDBQA
import os
import openai
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.chains.question_answering import load_qa_chain
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.document_loaders import UnstructuredFileLoader



os.environ["OPENAI_API_KEY"] = "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"
os.environ["SERPAPI_API_KEY"] = "8518acb926dba80598fe2068390d4608b32b1ebd6ea61faca6a9818d6e72a387"
os.environ["http_proxy"] = "http://127.0.0.1:10809"
os.environ["https_proxy"] = "http://127.0.0.1:10809"
os.environ["LANG"] = "en_US.UTF-8"  # 添加此行

llm = OpenAI(model_name="text-davinci-003", max_tokens=1024)
print("开始")
# prompt = PromptTemplate(
#     input_variables=["product"],
#     template="What is a good name for a company that makes {product}?",
# )

# chain = LLMChain(llm=llm, prompt=prompt)
# #print(chain.run("games"))
# #chat = ChatOpenAI(temperature=0)
# #print(chat([HumanMessage(content="Translate this sentence from English to French. I love programming.")]))

# tools = load_tools(["serpapi", "llm-math"], llm=llm)
# agent = initialize_agent(
#     tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
# print(agent.run("Who is Leo DiCaprio's girlfriend? What is her current age raised to the 0.43 power?"))

loader = UnstructuredFileLoader("D:\Downloads\操作使用指南.pdf")

# 将数据转成 document 对象，每个文件会作为一个 document
documents = loader.load()

# 初始化加载器
text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0)
# 切割加载的 document
split_docs = text_splitter.split_documents(documents)

# 初始化 openai 的 embeddings 对象
embeddings = OpenAIEmbeddings()
# 将 document 通过 openai 的 embeddings 对象计算 embedding 向量信息并临时存入 Chroma 向量数据库，用于后续匹配查询
docsearch = Chroma.from_documents(split_docs, embeddings)

# 创建问答对象
qa = VectorDBQA.from_chain_type(llm=OpenAI(
), chain_type="stuff", vectorstore=docsearch, return_source_documents=True)
# 进行问答
result = qa({"query": "项目经理"})
print(result)

print("结束")
