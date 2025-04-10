# SQLChatBot using LangChain Vs ReAct Agent




<div style="display: flex; justify-content: space-between; gap: 10px;">
  <div style="flex: 1; text-align: center;">
    <h3>Using LangChain</h3>
    <img src=chat-mysql.png alt="LangChain" style="width: 100%; border-radius: 10px;">
  </div>
  <div style="flex: 1; text-align: center;">
    <h3>Using ReAct Agent</h3>
    <img src =https://github.com/user-attachments/assets/40a8d11d-21b1-4f73-9dbd-26cbb42b269a alt="ReAct Agent" style="width: 100%; border-radius: 10px;">
  </div>
</div>





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

