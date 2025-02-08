from langchain.tools import BaseTool
import requests
from config import constants

class GetPlatformInfo(BaseTool):
    name: str = "Platform info extractor"
    description: str = "use this tool when you have given a description about meeting and you have to find the proposed idea, client name or platform link from given description"

    def _run(self, description):
        url = "https://api.perplexity.ai/chat/completions"
        payload = {
            "model": "sonar-pro",
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "You have given a description of meeting and you will have to find out proposed idea, client name and website link mentioned in the given description."
                        "Use client info extractor tool to get more information."
                        "Return it strictly in the following structured JSON format: "
                        "{"
                        "  'Idea': <idea>,"
                        "  'Client Info': <client_info>,"
                        "  'Platform Link': <platform_link>"
                        "}"
                        "Please make sure the response has proper line breaks, no extra spaces, unexpected characters (like \\n, extra quotes), or non-escaped characters."
                    ),
                },
                {
                    "role": "user",
                    "content": (
                        "if anything is not provided in description then use internet and google search to find out the actual information"
                        "Here is the meeting description " 
                        f"{str(description)}"
                    )
                },
            ]
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "Authorization":f"Bearer {constants.PERPLEXITY_API_KEY}"
        }
        response = requests.post(url, json=payload, headers=headers).json()
        return response["choices"][0]["message"]["content"]
    
    def _arun(self, website):
        raise NotImplementedError("This tool does not support async") 
    

class GetClientDetails(BaseTool):
    name: str = "Client details extractor"
    description: str = "use this tool when you have given a platform name, idea or platform link and you want to find more information about CEO of platform and proposed idea"
    def _run(self, website):
        url = "https://api.perplexity.ai/chat/completions"
        payload = {
            "model": "sonar-pro",
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "You are artificial intelligence agent which extracts an information by searching about it online"
                        "and returns information strictly in the following structured JSON format if it exists:"
                        "{"
                        "  'Title of website or platform': <title_of_platform>,"
                        "  'Proposed Idea': <proposed_idea>,"
                        "  'CEO Info': <ceo_info>"
                        "}"
                        "Please make sure the response has proper line breaks, no extra spaces, unexpected characters (like \\n, extra quotes), or non-escaped characters."
                    ),
                },
                {
                    "role": "user",
                    "content": (
                        "I am giving you platform name,idea or platform link and you have to find latest information about" 
                        "the platform by going to given link and return atleast 200 words description about idea and"
                        "atleast 150 words description about CEO, their goal and achievements"
                        "Please try to make it as detailed as you can and always refer to online information"
                        "here is the platform link or name "
                        f"{str(website)}"
                    )
                },
            ],
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "Authorization":f"Bearer {constants.PERPLEXITY_API_KEY}"
        }
        response = requests.post(url, json=payload, headers=headers).json()
        return  response["choices"][0]["message"]["content"]
    
    def _arun(self, website):
        raise NotImplementedError("This tool does not support async")


class GetIdeaSolution(BaseTool):
    name: str = "Solution extractor"
    description: str = "use this tool when you have given an idea description and information about client and you have to find solution on how we can achieve the given idea"

    def _run(self, description):
        url = "https://api.perplexity.ai/chat/completions"
        payload = {
            "model": "sonar-pro",
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "You have given an idea description and you have to find a solution to achieve the given idea using AI-ML"
                        "or webdev technologies. Search online about tech stack, resources, timeline of project and youtube videos and send it with proper formatting strictly in the following structured JSON format with proper line breaks, no extra spaces, unexpected characters (e.g., \\n, extra quotes, unescaped characters), and proper escaping. "
                        "Ensure the response has the following format: "
                        "{"
                        "  'Solution': <solution>,"
                        "  'Tech Stack': <tech_stack>,"
                        "  'Timeline': <timeline>"
                        "}"  
                    ),
                },
                {
                    "role": "user",
                    "content": (
                        "Here is the idea description: " 
                        f"{str(description)}"
                    )
                },
            ]
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "Authorization":f"Bearer {constants.PERPLEXITY_API_KEY}"
        }
        response = requests.post(url, json=payload, headers=headers).json()
        return response["choices"][0]["message"]["content"]
    
    def _arun(self, website):
        raise NotImplementedError("This tool does not support async")
