# C474 Project 2
Adaptive Multi-Agent Chatbot System using Ollama

### Team Members
Bhavya Bugude - 40270772
<br> Inas Fawzi - 40208675
<br> Sofia Valiante - 40191897
<br> Sana Antoun - 40209806
<br> Omar Alshanyour - 40209637 

### Breakdown
```
multi_agent_chatbot/
├── agents/
│   ├── general_agent.py
│   ├── admissions_agent.py
│   ├── ai_agent.py
│   └── router_agent.py
├── memory/
│   └── memory_manager.py
├── api/
│   └── main.py
├── utils/
│   └── knowledge_integration.py
├── config/
│   └── settings.py
├── technical_report.txt
├── execution_guide.txt
├── requirements.txt
├── demo_video.txt
├── performance_evaluation.txt
└── README.md
```

### Architecture Overview

**Agents**
<br> _General Agent_: Handles generic queries.
<br> _Admissions Agent_: Specializes in answering questions about Concordia University's Computer Science admissions.
<br> _AI Agent_: Focuses on AI-related questions and topics.

**Core Components**
<br> _Router Agent_: Detects user intent and delegates to the appropriate specialized agent.
<br> _Memory Management_: LangChain’s memory modules for maintaining session context.
<br> _External Knowledge_: Wikipedia API or other APIs for up-to-date info.

**Tech Stack**
<br> _LLM Backend_: Ollama (e.g., running LLaMA, Mistral, etc.)
<br> _LangChain_: Agent routing, memory, prompt templates.
<br> _FastAPI_: RESTful API interface.
<br> _Python_: Core logic and orchestration.

<img width="443" alt="Screenshot 2025-03-29 at 10 08 56 PM" src="https://github.com/user-attachments/assets/e858b7d5-e9c7-410e-9a0c-221f2bd90b8a" />

### Execution guide

