  📚 AI Research Summary Chat (Groq + Tavily + Streamlit)                         
An AI-powered academic research assistant that summarizes research papers, defines concepts, lists key points, and integrates LLM intelligence with real-time web references — all through a chat-based interface.

🚀 Features:-

💬 Interactive chat-based research assistant

📖 One-line definitions for academic terms

📌 Five-point explanations (features, advantages, lists)

📄 Single research paper deep-dive

📚 Multi-paper research summaries

🌐 Live web references via Tavily search

🧠 Context-aware follow-up queries

💾 Persistent chat history (JSON-based)

➕ Multiple chat sessions via sidebar


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
Groq API Key ,
Tavily API Key

📦 Installation
1️⃣ Clone the Repository

git clone https://github.com/your-username/ai-research-summary-chat.git

cd ai-research-summary-chat

2️⃣ Install Dependencies

pip install streamlit openai tavily-python

▶️ Run the Application

streamlit run app.py

🧠 How It Works
🔍 Intent Detection

The app detects user intent using keyword-based rules:

Definition queries → one-line explanation

Points queries → five bullet points

Specific paper queries → detailed academic explanation

Follow-up queries → context-aware continuation

🧪 Agents Used

Research Paper Summary Agent,
Single Paper Explanation Agent,
Web Reference Agent,
Final Synthesis Agent

💬 Example Queries

-Define transformers in AI

-Five points on machine learning

-Explain Attention Is All You Need paper

-Summarize recent research on computer vision

-Elaborate


⚠️ Limitations

*Keyword-based intent detection (not ML-based)

*Depends on external APIs (rate limits apply)

*Local storage only (no cloud sync)

🛣️ Future Enhancements:---

🔍 Semantic intent classification

📄 PDF paper upload support

🧠 Citation-aware summarization

☁️ Cloud database (MongoDB/Firebase)

🔐 User authentication

📜 License

This project is licensed under the MIT License.

👨‍💻 Author

Revanth PB
Computer Science Engineer | AI & Research Enthusiast

