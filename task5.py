from groq import Groq
from tavily import TavilyClient
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

groq_client = Groq(api_key=os.getenv("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"))
tavily = TavilyClient(api_key=os.getenv("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"))
MODEL = "llama-3.3-70b-versatile"

# ---- LLM Wrapper ----
def llm(prompt):
    try:
        res = groq_client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300
        )
        return res.choices[0].message.content
    except Exception as e:
        return f"Groq Error: {e}"


# ---- Planner Agent ----
def planner_agent(topic):
    prompt = f"""
    Break the topic '{topic}' into 3 clear research sub-questions.
    Number them 1, 2, and 3.
    """
    return llm(prompt)


# ---- Web Search Agent (Tavily) ----
def web_search_agent(question):
    try:
        result = tavily.search(query=question, max_results=2)
        if result.get("results"):
            return result["results"][0]["content"]
    except:
        pass
    return "No web info found."


# ---- Research Paper Agent ----
def research_paper_agent(topic):
    prompt = f"""
    Find 3 research papers related to '{topic}'.
    For each paper, give:
    - Title
    - Year
    - One-line summary
    """
    return llm(prompt)


# ---- Writer Agent ----
def writer_agent(planner, web_answers, papers):
    prompt = f"""
    Combine the following:

    Sub-questions:
    {planner}

    Web search answers:
    {web_answers}

    Research papers:
    {papers}

    Write a clean, structured 2-paragraph summary.
    """
    return llm(prompt)


# ---- Pipeline ----
topic = input("Enter a research topic: ").strip()

print("\n🧠 Planner Agent:")
planner = planner_agent(topic)
print(planner)

sub_questions = [q for q in planner.split("\n") if q.strip()]

print("\n🌐 Web Search Agent:")
web_combined = ""
for q in sub_questions:
    ans = web_search_agent(q)
    print(f"{q}\n{ans}\n")
    web_combined += f"{q}\n{ans}\n\n"

print("\n📚 Research Paper Agent:")
papers = research_paper_agent(topic)
print(papers)

print("\n✍️ Writer Agent (Final Summary):")
final_output = writer_agent(planner, web_combined, papers)
print(final_output)
