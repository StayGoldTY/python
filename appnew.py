import streamlit as st
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback
import pdfplumber
import os
import glob


def main():
  os.environ["OPENAI_API_KEY"] = "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"
  os.environ["SERPAPI_API_KEY"] = "8518acb926dba80598fe2068390d4608b32b1ebd6ea61faca6a9818d6e72a387"
  os.environ["http_proxy"] = "http://127.0.0.1:10809"
  os.environ["https_proxy"] = "http://127.0.0.1:10809"
  os.environ["LANG"] = "en_US.UTF-8"

  st.set_page_config(page_title="海南审图系统专属知识库")
  st.header("海南审图系统专属知识库💬")

  # Specify the directory you want to use
  directory = "D:\\Downloads"
  #directory = "/app/Downloads"

  # Get all PDF files in the directory
  pdf_files = glob.glob(os.path.join(directory, "*.pdf"))
  text = ""
  print("PDF files to process:", pdf_files)

  # Loop over all PDF files and extract the text
  with st.spinner('正在加载知识库中...'):
    for pdf_file in pdf_files:
      print("pdf_file")
      with pdfplumber.open(pdf_file) as pdf_reader:
        for page in pdf_reader.pages:
          text += page.extract_text()

  # 文本分片
  with st.spinner('正在处理文本...'):
    print("CharacterTextSplitter")
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=100,
        chunk_overlap=50,
        length_function=len 
    )
    print("CharacterTextSplitter2")
    chunks = text_splitter.split_text(text)

    # 创建embeddings
    embeddings = OpenAIEmbeddings()
    knowledge_base = FAISS.from_texts(chunks, embeddings)

  user_question = st.text_input("来向我提问吧：")
  if user_question:
    with st.spinner('正在问题答案...'):
      print("similarity_search")
      docs = knowledge_base.similarity_search(user_question)

      llm = OpenAI(temperature=0.5)
      chain = load_qa_chain(llm, chain_type="stuff")
      with get_openai_callback() as cb:
        response = chain.run(input_documents=docs, question=user_question)
        print(response)
      st.write(response)

if __name__ == '__main__':
  main()
