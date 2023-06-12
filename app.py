
import streamlit as st
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback
import pdfplumber
import os

def main():
  os.environ["OPENAI_API_KEY"] = "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"


  os.environ["SERPAPI_API_KEY"] = "8518acb926dba80598fe2068390d4608b32b1ebd6ea61faca6a9818d6e72a387"
  os.environ["http_proxy"] = "http://127.0.0.1:10809"
  os.environ["https_proxy"] = "http://127.0.0.1:10809"
  os.environ["LANG"] = "en_US.UTF-8"  # 添加此行

  # locale.setlocale(locale.LC_ALL, 'zh_CN')
  st.set_page_config(page_title="海南审图系统专属知识库")
  st.header("海南审图系统专属知识库💬")
  # 上传文件
  pdf = st.file_uploader("上传PDF文件", type="pdf")

  # 提取文本
  if pdf is not None:
    text = ""
    with pdfplumber.open(pdf) as pdf_reader:
      for page in pdf_reader.pages:
        text += page.extract_text()

    # 文本分片
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=100,
        chunk_overlap=50,
        length_function=len
    )
    chunks = text_splitter.split_text(text)

    # 创建embeddings
    embeddings = OpenAIEmbeddings()
    knowledge_base = FAISS.from_texts(chunks, embeddings)
    user_question = st.text_input("来向我提问吧：")
    if user_question:
      docs = knowledge_base.similarity_search(user_question)

      llm = OpenAI()
      chain = load_qa_chain(llm, chain_type="stuff")
      with get_openai_callback() as cb:
        response = chain.run(input_documents=docs, question=user_question)
        print(cb)

      st.write(response)


if __name__ == '__main__':
    main()
