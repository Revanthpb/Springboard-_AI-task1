# AI Research Summary Chat (Groq + Streamlit)

This project is an AI-powered research assistant built using Streamlit, Groq LLM API, and Tavily Search. It summarizes research papers, defines concepts, provides bullet points, and fetches references from the web. The system saves chat history with automatic titles for future access.

------------------------------------------------------------
## 1. PROJECT TITLE:- 
AI Research Summary Chat Using Groq and Tavily
------------------------------------------------------------

Purpose: To assist students, researchers, and professionals in quickly understanding academic topics, research papers, and related information through AI-generated responses.

------------------------------------------------------------
## 2. PROJECT OVERVIEW
This system takes a research query from the user and generates:
- Research paper summaries
- One-line definitions
- Key points and feature lists
- Web reference links
- Saved chat history for later review

Objective:
Provide an interactive AI model that acts as a research assistant for academic and contextual understanding.

------------------------------------------------------------
## 3. SOFTWARE AND HARDWARE DEPENDENCIES

Software Requirements:
- Python 3.10 or later
- Streamlit (User Interface framework)
- Groq API (LLM processing)
- Tavily API (Web search augmentation)

Python Libraries Used:
streamlit
groq
tavily-python

Hardware Requirements:
- 4GB RAM or above
- Internet connection required
- GPU not needed (Groq Cloud handles computation)

------------------------------------------------------------
## 4. ARCHITECTURE DIAGRAM

User Input

      |
      
      v
      
Streamlit UI (Frontend)

      |
      
      v
      
Intent Classifier

      |
      
      v
Groq LLM Model -------> Tavily Web Search (optional)
      |                           |
      v                           v
Response Generator         Web Evidence
      |
      v
Chat Output + JSON Storage (History)

------------------------------------------------------------
## 5. WORKFLOW

Step 1: User submits a query in Streamlit chat box.

Step 2: System checks query intent (definition, paper summary, etc).

Step 3: Groq LLM processes the request and generates structured output.

Step 4: Tavily API fetches additional web references when needed.

Step 5: Output is displayed to the user and stored in a JSON file.

Step 6: Chat title is generated from the first input.

------------------------------------------------------------
## 6. AGENT ROLES AND EXPLANATION

Intent Detector:
Determines if the user wants a definition, summary, list, or research paper explanation.

Research Summary Agent:
Generates summaries of multiple papers on a given topic.

Single Paper Agent:
Explains one research paper in detail including methodology.

Web Search Agent:
Finds supporting URLs and evidence for the topic using Tavily Search.

Memory/Chat Storage:
Stores conversations in JSON files with auto-generated titles.

------------------------------------------------------------
## 7. SAMPLE WORKING DEMO

Example Input:
define artificial intelligence

Expected Output:
Artificial Intelligence is the field focused on creating systems capable of learning, reasoning, and decision-making similar to human intelligence.

------------------------------------------------------------
## 8. OUTPUTS AND RESULTS

- Academic research summaries
- Definition and point-based responses
- URL references for further study
- Saved chat logs with titles
- Follow-up query handling

------------------------------------------------------------
## 9. LIMITATIONS

- Requires internet for Tavily search results
- Does not support PDF upload or document extraction
- Dependent on query clarity for best output

------------------------------------------------------------
## 10. FUTURE ENHANCEMENTS

- PDF upload feature to extract research from files
- Vector database support for long-term memory
- Voice to text and text to speech features
- Export summary as PDF or Word document

------------------------------------------------------------
## 11. DEPLOYED PROJECT LINK

(Add your link after deployment)
https://your-app-name.streamlit.app

------------------------------------------------------------
## 12. INSTALLATION AND RUNNING LOCALLY

Step 1: Clone the repository
git clone https://github.com/your-username/your-repo.git
cd your-repo

Step 2: Install dependencies
pip install -r requirements.txt

Step 3: Create a .env file and add:
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key

Step 4: Run the application
streamlit run app.py

------------------------------------------------------------
## 13. DEPLOYMENT (STREAMLIT CLOUD)

1. Push project to GitHub
2. Open streamlit.io and create a new app deployment
3. Add the following in "Secrets" section:
GROQ_API_KEY="your_live_key"
TAVILY_API_KEY="your_live_key"
4. Deploy and run

------------------------------------------------------------
## 14. AUTHOR DETAILS
Name: Your Name
Email: your-email@example.com

------------------------------------------------------------
## 15. LICENSE
MIT License. Free to use, modify, and distribute.

------------------------------------------------------------
END OF README
