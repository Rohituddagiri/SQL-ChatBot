# SQLChatBot using Chain Vs ReAct Agent

This project demonstrates an intelligent SQL chatbot capable of interacting with relational databases using natural language. It is built using two different approaches: a standard LangChain `Chain` and the more dynamic `ReAct` Agent framework. The bot processes user queries, performs reasoning through intermediate steps, generates SQL statements, and returns accurate answers from the database. This comparison showcases how both approaches reason and respond to user queries in real-time.

## 🔍 Chain vs ReAct Agent – What’s the Difference?

### 🧱 Chain
A **Chain** in LangChain is a sequential flow of logic where each step has a predefined role — for example, take user input → format a prompt → send it to the LLM → return the response. It’s fast and efficient when the task is straightforward and doesn't require decision-making or tool usage. Chains are great for simple question answering where the LLM doesn't need to plan or interact with external tools.

**Pros:**
- Simple and lightweight
- Easier to implement and debug
- Fast response time

**Cons:**
- Not flexible for complex or multi-step tasks
- Lacks reasoning or decision-making capability

---

### 🤖 ReAct Agent
A **ReAct Agent** combines **reasoning** and **acting**. It breaks down the task, chooses tools (like SQL execution or schema inspection), and iteratively plans and acts based on observations — just like a human would. This is ideal for complex queries where the chatbot needs to decide **what to do next** at each step.

**Pros:**
- Excellent for complex queries and tool use
- Transparent reasoning chain (intermediate steps)
- Flexible and dynamic behavior

**Cons:**
- Slower due to step-by-step planning
- Requires more setup and resources

---

In this project, both approaches are implemented to showcase how they handle SQL queries differently — one with a linear flow, and one with iterative reasoning and action.


### Using Chain  
![Langchain](chat-mysql.png)


### Using Agent
https://github.com/user-attachments/assets/6e6a772c-49d4-49c2-82cd-bb2b45cde58d




# How to run?
### STEPS:

Clone the repository

![langsmith_interpretor](https://github.com/user-attachments/assets/f9f7eb37-7cfc-4197-814c-0a0da1855469)


```bash
Project repo: https://github.com/Rohituddagiri/SQLChatBot.git
```

### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n chatSQLAgent python=3.10 -y
```

```bash
conda activate chatSQLAgent
```

### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


### Create a `.env` file in the root directory and add your Pinecone credentials as follows:

```ini
OPENAI_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
LANGCHAIN_TRACING_V2 = true
LANGSMITH_ENDPOINT="xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
LANGSMITH_API_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
LANGSMITH_PROJECT="xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

```bash
# Finally run the following command
streamlit run app.py
```

Now,
```bash
open up localhost:
```


### Techstack Used:

- Python
- LangChain
- LangSmith
- Streamlit
- OpenAI GPT 3.5
- MySQL

