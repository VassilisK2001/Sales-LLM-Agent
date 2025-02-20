from langchain.agents import initialize_agent
from langchain_openai import ChatOpenAI
from langchain.chains.conversation.memory import ConversationBufferMemory 
from agent_tools.agent_utilities import GetPlatformInfo, GetClientDetails, GetIdeaSolution
from config import constants

class MeetingAgent:
    def __init__(self):
        self.tools = [GetClientDetails(), GetPlatformInfo(), GetIdeaSolution()]
        self.llm =  ChatOpenAI(
            model="gpt-4o",
            temperature=0.6,
            api_key= constants.OPENAI_API_KEY
        ) 
        self.conversational_memory = ConversationBufferMemory(
            memory_key='chat_history',
            k=5,
            return_messages = True
        ) 
        self.agent = initialize_agent(
            tools = self.tools,
            llm = self.llm, 
            agent = "zero-shot-react-description",
            verbose= True, 
            max_iterations = 3,
            early_stopping_method = "generate", 
            memory = self.conversational_memory,
            handle_parsing_errors = True
        )
    def process_request(self, description):
        output = self.agent.run(
            "First find the idea, client name and platform link using Platform info extractor tool and find information about proposed idea about product, goals and achievements of CEO. Once you got the information about their idea then find how we can help them to build it and "
            "fetch realtime data from internet everytime."
            "This information is going to be added in project proposal so please write sections like CEO_Info,idea and solution. "
            "Return your response in structured JSON format like below and please use proper line breaks: "
            """
            {
            "platform_name": <platform_name>,
            "CEO_Info": <ceo_info>,
            "CEO_Name": <ceo_name>,
            "idea": <idea>,
            "solution": <solution>,
            "tech_stack": <tech stack>,
            "timeline": <timeline>,
            "Platform_link": <platform_link>
            }
            """
            "Here is the description: "
            f"{description}" 
        )   
        return output 