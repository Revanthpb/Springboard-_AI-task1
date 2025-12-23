from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from tavily import TavilyClient
from groq import Groq
import json
import uuid
from pathlib import Path
from datetime import datetime
import os

# ---------- API KEYS ----------
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

if not GROQ_API_KEY:
    st.error("GROQ_API_KEY not loaded. Check .env file.")
    st.stop()

# ---------- CHAT STORAGE ----------
CHAT_DIR = Path("chats")
CHAT_DIR.mkdir(exist_ok=True)

# ---------- CLIENTS ----------
client = Groq(api_key=GROQ_API_KEY)
MODEL = "llama-3.1-8b-instant"
tavily = TavilyClient(api_key=TAVILY_API_KEY)

# ---------- INTENT CHECK ----------
def is_definition_query(text: str) -> bool:
    return any(k in text.lower() for k in ["definition", "define", "one line", "meaning"])

def is_points_query(text: str) -> bool:
    return any(k in text.lower() for k in ["points", "list", "five", "features", "advantages"])

def is_followup_query(text: str) -> bool:
    return text.strip().lower() in ["summary", "explain", "details", "elaborate", "more"]

def is_specific_paper_query(text: str) -> bool:
    keywords = [
        "by", "et al", "paper", "methodology",
        "pre-training", "bert", "gpt",
        "attention is all you need",
        "transformers"
    ]
    return any(k in text.lower() for k in keywords)

# ---------- LLM ----------
def llm(conversation: list) -> str:
    response = client.chat.completions.create(
        model=MODEL,
        messages=conversation,
        temperature=0.4
    )
    return response.choices[0].message.content.strip()

# ---------- AGENTS ----------
def research_paper_summary_agent(topic: str) -> str:
    return llm(
        st.session_state.conversation +
        [{"role": "user", "content": f"Summarize 3 key research papers on {topic}."}]
    )

def single_paper_summary_agent(paper_query: str) -> str:
    prompt = f"""
Explain ONLY the following research paper in detail:

"{paper_query}"

Rules:
- Focus on this paper only
- Explain methodology clearly
- Do NOT mention other papers
- Academic tone
"""
    return llm(
        st.session_state.conversation +
        [{"role": "user", "content": prompt}]
    )

def web_summary_agent(topic: str) -> str:
    try:
        result = tavily.search(query=topic, max_results=3)
        refs = [f"{i+1}. {r['title']} — {r['url']}" for i, r in enumerate(result["results"])]
        return "\n".join(refs)
    except Exception:
        return "No web information available."

def final_summary_agent(papers: str, web: str) -> str:
    return llm(
        st.session_state.conversation +
        [{"role": "user", "content": f"Create a concise academic summary using:\n{papers}\n{web}"}]
    )

# ---------- SESSION INIT ----------
if "chat_id" not in st.session_state:
    st.session_state.chat_id = str(uuid.uuid4())

if "chat" not in st.session_state:
    st.session_state.chat = []

if "conversation" not in st.session_state:
    st.session_state.conversation = [
        {"role": "system", "content": "You are an academic research assistant."}
    ]

if "last_topic" not in st.session_state:
    st.session_state.last_topic = None

# ---------- SIDEBAR ----------
st.sidebar.title("💬 Your Chats")

chat_files = sorted(CHAT_DIR.glob("*.json"), reverse=True)

for file in chat_files:
    data = json.loads(file.read_text())

    # Backward compatibility
    if isinstance(data, list):
        title = data[0]["content"][:40] if data else "Old Chat"
        messages = data
    else:
        title = data.get("title", "Untitled Chat")
        messages = data.get("messages", [])

    if st.sidebar.button(title, key=f"chat_{file.stem}"):
        st.session_state.chat_id = file.stem
        st.session_state.chat = messages
        st.session_state.conversation = [
            {"role": "system", "content": "You are an academic research assistant."}
        ] + messages
        st.rerun()

if st.sidebar.button("➕ New Chat"):
    st.session_state.chat_id = str(uuid.uuid4())
    st.session_state.chat = []
    st.session_state.conversation = [
        {"role": "system", "content": "You are an academic research assistant."}
    ]
    st.session_state.last_topic = None
    st.rerun()

# ---------- MAIN UI ----------
st.title("🤖 AI Research Summary Chat (Groq)")

for msg in st.session_state.chat:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------- CHAT INPUT ----------
user_input = st.chat_input("Enter a research topic or request...")

if user_input:
    st.session_state.chat.append({"role": "user", "content": user_input})
    st.session_state.conversation.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):

            if is_definition_query(user_input):
                response = llm(
                    st.session_state.conversation +
                    [{"role": "user", "content": f"Define {user_input} in one line."}]
                )
                response = f"**Definition:** {response}"

            elif is_points_query(user_input):
                response = llm(
                    st.session_state.conversation +
                    [{"role": "user", "content": f"Give five points on {user_input}."}]
                )
                st.session_state.last_topic = user_input

            elif is_specific_paper_query(user_input):
                paper = single_paper_summary_agent(user_input)
                web = web_summary_agent(user_input)
                response = f"### 📄 Paper Summary\n{paper}\n\n### 🌐 References\n{web}"

            else:
                topic = st.session_state.last_topic if is_followup_query(user_input) else user_input
                st.session_state.last_topic = topic
                papers = research_paper_summary_agent(topic)
                web = web_summary_agent(topic)
                summary = final_summary_agent(papers, web)
                response = f"### 📚 Research Papers\n{papers}\n\n### 🌐 Web Sources\n{web}\n\n### ✍️ Final Summary\n{summary}"

            st.markdown(response)

    st.session_state.chat.append({"role": "assistant", "content": response})
    st.session_state.conversation.append({"role": "assistant", "content": response})

    # ---------- SAVE CHAT ----------
    
    chat_data = {
        "title": st.session_state.chat[0]["content"][:40],
        "messages": st.session_state.chat
    }

    (CHAT_DIR / f"{st.session_state.chat_id}.json").write_text(
        json.dumps(chat_data, indent=2)
    )
