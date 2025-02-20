import pypandoc 
import os
from openai import OpenAI 
from config import constants

class DocumentGenerator:
    def __init__(self):
        self.client = OpenAI(api_key = constants.OPENAI_API_KEY)
    
    def generate_document(self, agent_output):
        # Format the prompt
        prompt = f"""
            I am giving you some data in python dict format and you will have to add more information in it and convert it in markdown file with below format
            Don't use anything except headings and paragraphs in markdown
            # Project name
            project name
            # Who is the client?
            information about client 
            # How can we help? 
            detailed information about solution 
            # Tech stack 
            information about tech stack. Organize it in bullet points. 
            # Timeline 
            information about timeline 
            Try to add more information by yourself too to make it more detailed and make it around 800 words. Don't return anything except markdown and use proper line breaks.
            Here is the information about fields in the given dict:
            platform name: Name of platform 
            CEO_Info: Background about CEO and information about CEO 
            CEO_Name: Name of CEO 
            idea: project idea 
            solution: solution on how we can solve the given problem statement and how to achive the given idea 
            tech_stack: tech stack used to build the solution 
            timeline: timeline for the project. Oraganize this section strictly in bullet points. 
            Platform_link: link to the platform
            Here is the data:
            {agent_output}  
        """
        # Generate markdown from the agent output
        chat_completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="gpt-4", 
            temperature=0.7,   
        )
        markdown_content = chat_completion.choices[0].message.content 

        file_path = os.path.join("app", "generated_docs", "project_proposal.docx")
        # Covert markdown to Word document 
        pypandoc.convert_text(markdown_content, "docx", format="md", outputfile=file_path)
        return file_path