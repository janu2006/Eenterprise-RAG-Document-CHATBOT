# 📄 Enterprise RAG Document Assistant

An intelligent **Enterprise Retrieval-Augmented Generation (RAG)** application built with **Streamlit**, **LangChain**, **FAISS**, **Hugging Face Embeddings**, and **Groq Llama 3.3**. Upload PDF documents, create a searchable vector database, and ask natural language questions to receive accurate, context-aware responses.

---

## 🚀 Features

- 📄 Upload and process PDF documents
- ✂️ Automatic document chunking
- 🧠 Semantic embeddings using Hugging Face
- 🔍 FAISS vector database for fast similarity search
- 🤖 AI-powered answers with Groq Llama 3.3
- 💬 Conversational chat interface
- 📝 Maintains recent conversation history
- 🗑️ Clear chat history option
- ⚡ Responsive Streamlit UI

---

## 🛠️ Tech Stack

- Python
- Streamlit
- LangChain
- LangChain Community
- LangChain Groq
- Hugging Face Embeddings
- FAISS
- Groq API
- PyPDF
- python-dotenv

---

## 📂 Project Structure

```
Enterprise-RAG-Assistant/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Enterprise-RAG-Assistant.git

cd Enterprise-RAG-Assistant
```

---

### 2. Create a Virtual Environment

#### Windows

```bash
python -m venv .venv
```

Activate

```bash
.venv\Scripts\activate
```

#### macOS/Linux

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install streamlit python-dotenv langchain langchain-community langchain-core langchain-groq langchain-huggingface langchain-text-splitters faiss-cpu sentence-transformers pypdf
```

---

### 4. Configure Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_groq_api_key_here
```

---

### 5. Run the Application

```bash
streamlit run app.py
```

---

## 📦 Requirements

```text
streamlit
python-dotenv
langchain
langchain-core
langchain-community
langchain-groq
langchain-huggingface
langchain-text-splitters
sentence-transformers
faiss-cpu
pypdf
```

---

## 🧠 How It Works

### Step 1 — Upload a PDF

Upload any text-based PDF document through the sidebar.

↓

### Step 2 — Document Processing

The application extracts text from the PDF using **PyPDFLoader**.

↓

### Step 3 — Text Chunking

Large documents are split into overlapping chunks using **RecursiveCharacterTextSplitter**.

↓

### Step 4 — Embedding Generation

Each chunk is converted into semantic vectors using the **all-MiniLM-L6-v2** sentence transformer model.

↓

### Step 5 — Vector Storage

The generated embeddings are stored in a **FAISS** vector database for efficient similarity search.

↓

### Step 6 — User Query

Ask questions about the uploaded document.

↓

### Step 7 — Retrieval

The most relevant document chunks are retrieved using vector similarity search.

↓

### Step 8 — AI Response

The retrieved context, along with recent chat history, is sent to **Groq Llama 3.3-70B Versatile**, which generates an accurate and context-aware response.

---

## 💡 Example Workflow

### Upload

```
Company Annual Report.pdf
```

### User Question

```
What was the company's total revenue in 2025?
```

### Retrieval

The system retrieves the most relevant sections from the indexed PDF.

### AI Response

```
According to the uploaded document, the company's total revenue for 2025 was...
```

---

## 🔐 Environment Variables

| Variable | Description |
|----------|-------------|
| GROQ_API_KEY | Your Groq API Key |

---

## 🎯 Future Improvements

- 📄 Support multiple PDF uploads
- 📝 Chat history persistence
- 📚 Multi-document retrieval
- 🌐 Web URL ingestion
- 📂 DOCX and TXT support
- 🔍 Metadata filtering
- 📊 Retrieval score visualization
- 📑 Source citations in responses
- ☁️ Cloud deployment support
- 👥 User authentication

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository

2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Added new feature"
```

4. Push to GitHub

```bash
git push origin feature-name
```


## 👨‍💻 Author

**Nekkanti Jahnavi**

Computer Science Engineering Student

GitHub: https://github.com/your-username

---

## ⭐ Support

If you found this project helpful, please consider giving it a ⭐ on GitHub.

Happy Coding! 🚀