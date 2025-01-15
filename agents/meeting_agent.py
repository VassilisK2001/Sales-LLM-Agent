import json 
from langchain.agents import initialize_agent

class MeetingAgent:
    def __init__(self, tools, llm, conversational_memory):
        self.agent = initialize_agent(
            tools = tools,
            llm = llm, 
            agent = "zero-shot-react-description",
            verbose= True, 
            max_iterations = 3,
            early_stopping_method = "generate", 
            memory = conversational_memory,
            handle_parsing_errors = True
        )
    def process_request(self, description):
        para = self.agent(description) 
        output = json.loads(para["output"]) 
        return output 