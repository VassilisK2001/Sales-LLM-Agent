from flask import render_template, request, redirect, url_for, flash, send_from_directory 
from utils.validate_input import process_description
from agents.meeting_agent import MeetingAgent 
from agent_tools.document_generator import DocumentGenerator 
import os 

def configure_routes(app):
    agent = MeetingAgent() 
    document_generator = DocumentGenerator()

    @app.route("/")
    def index():
        return render_template("index.html")
    
    @app.route("/submit", methods=["POST"])
    def submit():
        description = request.form.get("description")
        if not description:
            flash("Description is required", "error")
            return redirect(url_for("index"))
        
        try:
            validation_result = process_description(description)
            if not validation_result['valid']:
                flash('invalid description. Please include both idea and client information.', 'error')
                return redirect(url_for('index'))
            
            agent_output = agent.process_request(description)
            file_path = document_generator.generate_document(agent_output)

            # Extract just the filename (without the path) to pass to result.html
            filename = file_path.split(os.path.sep)[-1]
            return render_template('result.html', filename=filename)
        
        except Exception as e:
            flash(f"Error processing request: {str(e)}", "error")
            return redirect(url_for("index"))
    
    @app.route('/download/<filename>')
    def download(filename):
        # Define the path to the directory where the generated docs are stored
        docs_directory = os.path.join(app.root_path, 'generated_docs')

        # Return the file using send_from_directory
        return send_from_directory(docs_directory, filename, as_attachment=True)



