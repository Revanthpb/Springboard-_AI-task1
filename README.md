📚 AI Research Summary Chat (Groq + Tavily + Streamlit)

An AI-powered academic research assistant built using Streamlit, Groq LLM, and Tavily Web Search.
This application helps users summarize research papers, define concepts, list key points, and combine LLM responses with real web references — all in a chat-based interface.

🚀 Features

💬 Chat-based research assistant

📖 One-line definitions for academic terms

📌 Five-point explanations (features, advantages, lists)

📄 Detailed single research paper summaries

📚 Multi-paper research summaries

🌐 Live web references using Tavily search

🧠 Follow-up query handling (summary, explain, elaborate)

💾 Persistent chat history stored as JSON files

➕ Multiple chat sessions with sidebar navigation

🛠️ Tech Stack

Frontend: Streamlit

LLM Provider: Groq (LLaMA 3.1)

Web Search: Tavily API

Language: Python 3.9+

Storage: Local JSON files

📂 Project Structure
.
├── app.py                  # Main Streamlit application
├── chats/                  # Saved chat history (auto-created)
│   ├── 2024-07-20_12-30.json
│   └── ...
├── README.md               # Project documentation

🔑 API Keys Required

You need the following API keys:

Groq API Key

Tavily API Key

⚠️ Important:
Do NOT hardcode API keys in production. Use environment variables instead.

🔐 Recommended: Environment Variables

Replace hardcoded keys with:

export GROQ_API_KEY="your_groq_api_key"
export TAVILY_API_KEY="your_tavily_api_key"


Update the code:

import os

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

📦 Installation
1️⃣ Clone the Repository
git clone https://github.com/your-username/ai-research-summary-chat.git
cd ai-research-summary-chat

2️⃣ Install Dependencies
pip install streamlit openai tavily-python

▶️ Run the Application
streamlit run app.py


The app will open automatically in your browser.

🧠 How It Works
🔍 Intent Detection

The app detects user intent using keyword-based rules:

Definition queries → one-line explanation

Points queries → five bullet points

Specific paper queries → detailed academic explanation

Follow-up queries → context-aware continuation

🧪 Agents Used

Research Paper Summary Agent

Single Paper Explanation Agent

Web Reference Agent

Final Synthesis Agent

💬 Example Queries

Define transformers in AI

Five points on machine learning

Explain Attention Is All You Need paper

Summarize recent research on computer vision

More

Elaborate

💾 Chat Persistence

Each chat is stored as a .json file in the chats/ directory

Chats can be revisited anytime from the sidebar

New chats can be started instantly

🎓 Ideal Use Cases

Engineering & research students

Academic paper reviews

Exam preparation (GATE, AFCAT, CDS, etc.)

Literature surveys

AI/ML concept revision

⚠️ Limitations

Keyword-based intent detection (not ML-based)

Depends on external APIs (rate limits apply)

Local storage only (no cloud sync)

🛣️ Future Enhancements

🔍 Semantic intent classification

📄 PDF paper upload support

🧠 Citation-aware summarization

☁️ Cloud database (MongoDB/Firebase)

🔐 User authentication

📜 License

This project is licensed under the MIT License.
You are free to use, modify, and distribute it.

👨‍💻 Author

Revanth PB
Computer Science Engineer
Academic & AI Enthusiast
