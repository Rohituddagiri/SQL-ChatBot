from dotenv import load_dotenv
from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_community.utilities import SQLDatabase
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI


from langchain.agents.agent_types import AgentType

load_dotenv()
def get_response(user_query: str, db: SQLDatabase, chat_history: list):
    
    template = """
    You are a data analyst at a company. You are interacting with a user who is asking you question about the company's database.
    Based on the table schema, question, write a natural language response. Take the conversation history into account.
    Conversation History: {chat_history}
    
    Answer the following questions as best you can. You have access to the following tools:

    {tools}

    Use the following format:

    Question: the input question you must answer
    Thought: you should always think about what to do
    Action: the action to take, should be one of [{tool_names}]
    Action Input: the input to the action
    Observation: the result of the action
    ... (this Thought/Action/Action Input/Observation can repeat N times)
    Thought: I now know the final answer
    Action: Prepare the final answer
    Final Answer: the final answer to the original input question

    Begin!

    Question: {input}
    Thought:{agent_scratchpad}
    """
    
    llm = ChatOpenAI(
        temperature = 0,
        model_name = 'gpt-4o'
        )
    
    toolkit = SQLDatabaseToolkit(
        db=db,
        llm=llm
        )
    
    args = {"return_intermediate_steps" : True}
    
    prompt = PromptTemplate(
        input_variables=["input","chat_history","tools", "tool_names", "agent_scratchpad"],
        template=template
        )
    
    db_agent = create_sql_agent(
        llm=llm,
        toolkit=toolkit,
        prompt=prompt,
        verbose=True,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        agent_executor_kwargs=args
        )
    db_agent.handle_parsing_errors = True

    response = db_agent.invoke({"input": user_query,"chat_history": chat_history})
    
    return response
