# Meeting Workflow Automation App

This app automates and enhances the meeting workflow by using AI-powered agents to streamline the process of creating project proposals, preparing meeting materials, and summarizing discussions. By leveraging the capabilities of OpenAI and Perplexity APIs, the app gathers relevant information, structures it into well-organized documents, and provides actionable insights. Built with Python and Flask, the app is designed for ease of deployment using Docker and AWS Elastic Beanstalk. CI/CD pipelines have been set up using AWS CodePipeline to enable seamless deployment and updates.

The app could be highly beneficial for software agencies, helping them generate well-structured project proposals for clients. By automating the information-gathering and proposal-writing process, agencies can save time and ensure consistency and quality in their client communications.

The app is available online at: [http://salesllm-beanstalk-gh-app-env.eba-qcmdky2s.eu-central-1.elasticbeanstalk.com](http://salesllm-beanstalk-gh-app-env.eba-qcmdky2s.eu-central-1.elasticbeanstalk.com)

### Potential Use Cases:
- **Project Proposal Creation:** Automatically generate well-structured project proposals based on input requirements.
- **Software Agencies:** Streamline the process of preparing client proposals and project plans.
- **Meeting Preparation:** Gather and summarize key information about client to prepare for productive discussions.
- **Follow-up Documentation:** Capture meeting highlights and action points, ensuring no detail is overlooked.
- **Research and Analysis:** Summarize research data and create comprehensive reports with minimal manual effort.

## Features
- Automated project proposal generation
- Meeting preparation and material creation
- Discussion and research summarization
- Task and action item extraction
- Easy deployment with Docker and AWS Elastic Beanstalk

## Technologies Used
- Python
- Flask
- Langchain
- OpenAI API
- Perplexity API
- Docker
- AWS Elastic Beanstalk
- AWS CodePipeline

## AI Agent Tools
1. **Platform Info Extractor:** Finds the idea, client name, and platform link from the given meeting description.
2. **Client Details Extractor:** Searches on the internet to get more information about the client, idea, and platform.
3. **Solution Extractor:** Takes the idea and searches online for possible solutions.

## Project Structure
```
project-root
│
├── app/                # Flask application
├── config/             # Configuration files
├── utils/              # Utility functions
├── agent_tools/        # Tools for AI agents
├── agents/             # AI agent scripts
├── requirements.txt    # Python dependencies
├── setup.py            # Setup script
├── main.py             # Application entry point
```

## Running the App Locally with Docker
1. Clone the repository:
```bash
git clone https://github.com/your-repo.git
cd your-repo
```
2. Create a `.env` file and add your environment variables:
```env
OPENAI_API_KEY=your-openai-api-key
PERPLEXITY_API_KEY=your-perplexity-api-key
FLASK_SECRET_KEY=your-flask-secret-key
```
3. Build the Docker image:
```bash
docker build -t meeting-ai-agent .
```
4. Run the Docker container:
```bash
docker run -dp 127.0.0.1:5000:5000 --env-file .env meeting-ai-agent
```
5. Access the app at [http://127.0.0.1:5000](http://127.0.0.1:5000).

## Deploying the App on AWS Elastic Beanstalk
For detailed instructions on deploying a Dockerized app to AWS Elastic Beanstalk, refer to the official AWS documentation: [Deploying Docker Containers on Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/docker-quickstart.html).

## Environment Variables Setup
| Variable            | Description              |
|---------------------|-------------------------|
| `OPENAI_API_KEY`     | API key for OpenAI       |
| `PERPLEXITY_API_KEY` | API key for Perplexity   |
| `FLASK_SECRET_KEY`   | Secret key for Flask sessions |

## API Keys and Configuration
Make sure to add the API keys in your `.env` file or set them in your cloud environment variables. These keys are required for the app’s AI functionality and secure session management.

