# AI Operations Assistant  
### GenAI Intern Assignment

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red)
![LLM](https://img.shields.io/badge/LLM-Google%20Gemini-green)
![APIs](https://img.shields.io/badge/APIs-GitHub%20%7C%20OpenWeather-orange)

An AI-powered operations assistant built using a **multi-agent GenAI architecture**.  
The system converts natural language queries into structured execution plans, calls real-world APIs, verifies outputs using an LLM, and returns reliable structured responses.

---

## 📌 Problem Statement

Design and implement a **production-inspired GenAI system** that:
- Understands user intent from natural language
- Plans execution steps using an LLM
- Interacts with real external APIs
- Verifies correctness before responding

---

## 🚀 Setup Instructions (Run Locally)

### 1. Clone the Repository
```bash
git clone <your-repo-link>
cd ai_ops_assistant

2. Create Virtual Environment (Recommended)
Windows

python -m venv venv
venv\Scripts\activate
Mac / Linux

python -m venv venv
source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Configure Environment Variables
Create a .env file from the template:

cp .env.example .env
Add your API keys inside .env.

5. Run the Application
streamlit run app.py

Open in browser:
http://localhost:8501

🔐 Environment Variables (.env.example)
GOOGLE_API_KEY=your_gemini_api_key
GITHUB_TOKEN=your_github_personal_access_token
WEATHER_API_KEY=your_openweather_api_key


🧠 System Architecture
The system follows a multi-agent execution pipeline with strict separation of responsibilities.

Diagram
flowchart LR
    User --> UI[Streamlit UI]
    UI --> Planner[Planner Agent]
    Planner --> Executor[Executor Agent]
    Executor --> Tools[External APIs]
    Tools --> Executor
    Executor --> Verifier[Verifier Agent]
    Verifier --> UI

🤖 Core Agents
🗂 Planner Agent
Converts user queries into a structured JSON execution plan

Uses Gemini LLM

Determines:

Required tools

Execution order

Input parameters

⚙️ Executor Agent
Executes steps defined in the plan

Calls real APIs via tool wrappers

Normalizes inputs to handle LLM variability

Collects raw API responses

✅ Verifier Agent
Validates API outputs using the LLM

Ensures correctness and completeness

Handles partial or inconsistent results

Formats final user-facing response

🔌 Tools Layer
Each external API is wrapped inside a dedicated module, ensuring:

Loose coupling

Easy extensibility

Production-like design

🌐 Integrated APIs
GitHub REST API
Used to:

Search repositories

Fetch repository metadata

Retrieve star counts and descriptions

OpenWeatherMap API
Used to:

Fetch real-time weather data

Retrieve temperature and conditions by city

🧪 Example Prompts
What is the current weather in Delhi?
Find top 3 Python repositories on GitHub
Find trending AI repositories and current weather in Bangalore
Show most starred JavaScript repositories and weather in Mumbai
Get popular backend framework repositories and weather in Pune


⚠️ Known Limitations / Tradeoffs
Sequential Tool Execution
API calls are executed sequentially to maintain deterministic behavior.

No Response Caching
Repeated queries may increase latency and API cost.

LLM Output Variability
Despite sanitization and normalization, retries may occasionally be required.

Basic UI
Streamlit is used for rapid prototyping rather than production UI.

Limited Tool Set
Currently supports GitHub and Weather APIs only.

🔮 Future Improvements
Parallel API execution

Response caching layer

Cost and latency monitoring

Advanced retry strategies

Web-based dashboard UI

Dynamic tool registry for scalability

📁 Project Structure
ai_ops_assistant/
│
├── app.py
├── agents/
│   ├── planner.py
│   ├── executor.py
│   └── verifier.py
│
├── tools/
│   ├── github_tool.py
│   └── weather_tool.py
│
├── utils/
│   └── helpers.py
│
├── .env.example
├── requirements.txt
└── README.md
📌 Tech Stack
Python

Streamlit

Google Gemini LLM

GitHub REST API

OpenWeatherMap API

🧪 Evaluation Readiness Checklist
✔ Multi-agent architecture
✔ Real API integrations
✔ LLM planning + verification
✔ Modular, scalable design
✔ Clear documentation
✔ Reproducible setup

