import os
import tempfile
import streamlit as st
from dotenv import load_dotenv
# LangChain 0.2.x imports
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
load_dotenv()
st.set_page_config(page_title="Enterprise RAG Assistant",layout="wide")
st.title(" Enterprise RAG Document Assistant")
# Validate API Key
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    st.error("Missing `GROQ_API_KEY`. Please set it in your `.env` file.")
    st.stop()
# Initialize Session State
if "chat" not in st.session_state:
    st.session_state.chat = []
if "db" not in st.session_state:
    st.session_state.db = None

# Sidebar Document Upload
st.sidebar.header(" Document Ingestion")
uploaded_file = st.sidebar.file_uploader("Upload a PDF", 
                                                    type=["pdf"])

if uploaded_file and st.sidebar.button("Index Document"):
    with st.spinner("Processing & indexing PDF..."):
        # Save upload to a temporary file
        with tempfile.NamedTemporaryFile(delete=False, 
                                     suffix=".pdf") as temp_file:
            temp_file.write(uploaded_file.getbuffer())
            pdf_path = temp_file.name

        try:
            # 1. Load PDF
            loader = PyPDFLoader(pdf_path)
            documents = loader.load()

            # 2. Split Text Into Chunks
            splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
            chunks = splitter.split_documents(documents)

            # 3. Guard against empty/scanned PDFs
            if not chunks:
                st.sidebar.error("Could not extract text. The PDF might be empty or image-only.")
            else:
                # 4. Generate Embeddings & Save to Vector DB
                embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
                st.session_state.db = FAISS.from_documents(chunks, embeddings)
                st.sidebar.success(f"Indexed successfully! ({len(chunks)} chunks loaded)")

        except Exception as err:
            st.sidebar.error(f"Failed to process PDF: {err}")
        finally:
            if os.path.exists(pdf_path):
                os.remove(pdf_path)

# LLM setup
llm = ChatGroq(
    groq_api_key=api_key,
    model_name="llama-3.3-70b-versatile",
    temperature=0.2
)

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are an enterprise AI assistant. Answer user questions using the context provided.\n"
        "If the answer is not present in the context, use your general knowledge to answer.\n\n"
        "Context:\n{context}"
    ),
    (
        "human",
        "Conversation History:\n{history}\n\nQuestion:\n{question}"
    )
])

parser = StrOutputParser()

# Render Past Chat Messages
for role, message in st.session_state.chat:
    with st.chat_message(role):
        st.markdown(message)

# Handle Chat Input
query = st.chat_input("Ask a question about your uploaded document...")

if query:
    # Display user query
    st.session_state.chat.append(("user", query))
    with st.chat_message("user"):
        st.markdown(query)

    # Format history (last 6 turns)
    history_str = "\n".join([f"{role}: {msg}" for role, msg in st.session_state.chat[-6:]])

    # Perform Retrieval from FAISS
    context = ""
    if st.session_state.db:
        retrieved_docs = st.session_state.db.similarity_search(query, k=3)
        context = "\n\n".join([doc.page_content for doc in retrieved_docs])

    # Run RAG Chain
    chain = prompt | llm | parser
    response = chain.invoke({
        "context": context,
        "history": history_str,
        "question": query
    })

    # Render Assistant Output
    st.session_state.chat.append(("assistant", response))
    with st.chat_message("assistant"):
        st.markdown(response)

# Sidebar Clear Option
if st.sidebar.button("Clear Chat History"):
    st.session_state.chat = []
    st.rerun()



