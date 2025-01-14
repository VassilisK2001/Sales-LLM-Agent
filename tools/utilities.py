from langchain.tools import BaseTool
from config import constants
import requests
import json 
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