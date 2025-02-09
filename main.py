from utils.validate_input import process_description
from agents.meeting_agent import MeetingAgent
from agent_tools.document_generator import DocumentGenerator

def main():
    # Take user input (description of the project)
    description = input("Please enter the description of the project: ") 

    try:
        # Validate the input description
        validation_result = process_description(description)

        # Check if the description is valid
        if not validation_result['valid']:
            raise Exception("The description is invalid. Please make sure to include information about the idea and the client.")
        
        print("The description is valid. Processing the request...")

        # Process description with MeetingAgent class
        meeting_agent = MeetingAgent() 
        agent_output = meeting_agent.process_request(description)

        # Pass the agent output to the DocumentGenerator class to generate project proposal document
        doc_generator = DocumentGenerator()
        doc_generator.generate_document(agent_output)

        print("Document generated successfully!")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
