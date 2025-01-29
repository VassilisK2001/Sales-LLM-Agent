from langchain.tools import BaseTool
import requests
import json 
import sys
import os
from config import constants

class GetPlatformInfo(BaseTool):
    name = "Platform Info extractor"
    description = "use this tool when you have given a description about meeting and you have to find the proposed idea, client name, or platform link from the given description"

    def _run(self, description):
        # it will take meeting description from prompt and pass it in perplexity prompt
        url = "https://api.perplexity.ai/chat/completions"
        payload = {
            "model": "pplx-70b-online",
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "You have given a description of meeting and you will have to find out proposed idea, client name and website link mentioned in the given description."
                        "Use client info extractor tool to get more information."
                        "Return it in this format"
                        "Idea: "
                        "Client Info: "
                        "Platform Link: "
                    ),
                },
                {
                    "role": "user",
                    "content": (
                        "If anything is not provided in the description then use internet and google search to find out actual information"
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
        response = requests.post(url, json=payload, headers=headers)
        return response 
    # We don't care bout async function in this scenario
    def _arun(self, website):
        return NotImplementedError("This tool does not support async") 
    

class GetClientDetails(BaseTool):
    name = "Client details extractor"
    description = "use this tool when you have given a platform name, idea or platform link and you want to find more information about CEO of platform and proposed idea"
    def _run(self, website):
        url = "https://api.perplexity.ai/chat/completions"
        payload = {
            "model": "pplx-70b-online",
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "You are artificial intelligence agent which extracts an information by searching about it online and returns information in this format if it exists"
                        "Title of website or platform: "
                        "Proposed idea:"
                        "CEO Information:"     
                    ),
                },
                {
                    "role": "user",
                    "content": (
                        "I am giving you platform name, idea or platform link and you have to find latest information about"
                        "the platform by going to given link and return atleast 200 words description about idea and"
                        "at least 150 words description about CEO, their goal and achievements"
                        "Please try to make it as detailed as you can and always refer to online information"
                        "here is the platform link or name "
                        f"{str(website)}"
                    )
                },
            ]
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "Authorization": f"Bearer {constants.PERPLEXITY_API_KEY}"
        }
        response = requests.post(url, json=payload, headers=headers)
        return response 
    def _arun(self, website):
        raise NotImplementedError("This tool does not support async")
    
class GetIdeaSolution(BaseTool):
    name = "solution extractor"
    description = "use this tool when you have given an idea description and information about client and you have to find solution on how we can achieve the given idea"

    def _run(self, description):
        url = "https://api.perplexity.ai/chat/completions"
        payload = {
            "model": "pplx-70b-online",
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "You have given an idea description and you have to find around 3-4 solutions to achieve the given idea using AI-ML"
                        "or webdev technologies. Search online about tech stack, resources, timeline of project and youtube videos and send it with proper formatting and line breaks in this format"
                        "Solution: "
                        "Tech stack: "
                        "Timeline "
                    ),
                },
                {
                    "role": "user",
                    "content": (
                        "Here is the idea description "
                        f"{str(description)}"
                    )
                },
            ]
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "Authorization": f"Bearer {constants.PERPLEXITY_API_KEY}"
        }
        response = requests.post(url, json=payload, headers=headers)
        return response 
    
    def _arun(self, website):
        raise NotImplementedError("This tool does not support async")
