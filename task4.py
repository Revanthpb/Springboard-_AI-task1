from groq import Groq
from tavily import TavilyClient
import os
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")



groq_client = Groq(api_key=GROQ_API_KEY)
tavily = TavilyClient(api_key=TAVILY_API_KEY)
MODEL = "llama-3.3-70b-versatile"
def llm(prompt):
    try:
        response = groq_client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=350
        )
        return response.choices[0].message.content

    except Exception as e:
        print("\n Groq API Error:")
        print(e)
        return None
# Generate Sub-Questions

def generate_subquestions(topic):
    prompt = f"Generate exactly 3 research sub-questions about: {topic}. Number them 1, 2, and 3."
    return llm(prompt)

# Tavily Search

def tavily_answer(q):
    try:
        result = tavily.search(query=q, max_results=3)
        if "results" in result and len(result["results"]) > 0:
            return result["results"][0]["content"]
        return "No relevant info found."
    except Exception as e:
        return f"Tavily Error: {e}"

# Summarization

def summarize(text):
    prompt = "Summarize the following into one clear paragraph:\n\n" + text
    return llm(prompt)

topic = input("Enter a research topic: ").strip()

print("\n Generating sub-questions using Groq...\n")
subq = generate_subquestions(topic)

if not subq:
    print("Cannot continue due to Groq error.")
    exit()

print(subq)

subqs = [line.strip() for line in subq.split("\n") if line.strip()]
combined = ""

print("\n Retrieving answers using Tavily...")
for q in subqs:
    print(f"\n {q}")
    ans = tavily_answer(q)
    print(ans)
    combined += f"{q}\n{ans}\n\n"

print("\n Final Summary:")
final = summarize(combined)
print(final)
