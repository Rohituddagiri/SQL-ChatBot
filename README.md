# SQLChatBot using LangChain Vs ReAct Agent

![image info](chat-mysql.png)



https://github.com/user-attachments/assets/c1b85488-785c-440a-be77-b72872275ee8


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

