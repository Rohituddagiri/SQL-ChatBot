# SQL-ChatBot Implementation using LangChain Chain Vs ReAct Agent 

This project demonstrates an intelligent SQL chatbot capable of interacting with relational databases using natural language. It is built using two different approaches: a standard LangChain `Chain` and the more dynamic `ReAct` Agent framework. The bot processes user queries, performs reasoning through intermediate steps, generates SQL statements, and returns accurate answers from the database. This comparison showcases how both approaches reason and respond to user queries in real-time.

## 🔍 Chain vs ReAct Agent – What’s the Difference?

### 🧱 Chain
A **Chain** in LangChain is a sequential flow of logic where each step has a predefined role — for example, take user input → format a prompt → send it to the LLM → return the response. It’s fast and efficient when the task is straightforward and doesn't require decision-making or tool usage. Chains are great for simple question answering where the LLM doesn't need to plan or interact with external tools.

Implemented Chain in this project

![image](https://github.com/user-attachments/assets/c1a4c3f2-1eec-47f8-be2c-0654646ffd49)


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

Implemented Agent in this Project

![image](https://github.com/user-attachments/assets/f44dca3d-c8a3-4775-bf36-6e6ab2726b1f)


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


## 🧠 Chain of Thought Prompting (CoT)

This project also implements **Chain of Thought (CoT)** prompting — a reasoning approach where the model generates intermediate reasoning steps before producing the final answer. This improves accuracy, especially for complex SQL questions that require multi-step logic.

![image](https://github.com/user-attachments/assets/31c00743-fc83-4cae-9a09-99c14a6a43c2)


**Diagram Explanation:**
- The second model from the left in the image shows how **CoT** works.
- Instead of directly jumping from input to output, the model walks through intermediate **thoughts** or steps.
- This makes the model's decision process more interpretable and reliable.

> 💡 CoT is the foundation for more advanced reasoning strategies like **Self-Consistency** and **Tree of Thoughts (ToT)**, also shown in the diagram.

In this ReAct Chatbot, you can visually see these reasoning steps when using the ReAct Agent. Each intermediate SQL generation and tool usage is recorded and displayed before the final output.


## 🧪 LangSmith Integration for Traceability & Debugging

To improve transparency and debugging, this project leverages **LangSmith** to trace and visualize each step in the agent's reasoning and tool execution flow.

![langsmith_interpretor](https://github.com/user-attachments/assets/f9f7eb37-7cfc-4197-814c-0a0da1855469)

### ✅ What does this show?

- Each user query (e.g., _“how many artists in the database?”_) is tracked step-by-step.
- You can see **intermediate steps**, such as tool invocations (`sql_db_list_tables`, `sql_db_schema`), prompt formatting, LLM calls (OpenAI), and the resulting parsed outputs.
- The **waterfall view** helps debug slow chains or incorrect tool usage by showing exact timing and sequence of operations.
- LangSmith's UI gives visibility into what tools the agent decided to use and why, using ReAct logic for stepwise decision making.

> 💡 LangSmith acts like a microscope for your LLM apps — letting you fine-tune, evaluate, and productionize agents confidently.

This visibility is especially powerful when combined with **ReAct agents**, allowing you to inspect the thought process of the agent as it reasons and interacts with the SQL database.


# How to run?
### STEPS:

Clone the repository

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

### References:
- https://alejandro-ao.com/chat-with-mysql-using-python-and-langchain/
- https://abvijaykumar.medium.com/prompt-engineering-chain-of-thought-and-react-sql-agent-85fa42575c06
- https://www.promptingguide.ai/techniques/tot

