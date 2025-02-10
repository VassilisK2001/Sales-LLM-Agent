from flask import render_template, request, redirect, url_for, flash, send_file 
from utils.validate_input import process_description
from agents.meeting_agent import MeetingAgent 
from agent_tools.document_generator import DocumentGenerator 
import os 

def configure_routes(app):
    agent = MeetingAgent() 

    def save_document(content, filename='project_proposal.docx'):
        file_path = os.path.join('generated_docs', filename)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return file_path
    
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
            document_generator = DocumentGenerator()
            document_content = document_generator.generate_document(agent_output)
            file_path = save_document(document_content)

            return render_template('result.html', file_path=file_path)
        
        except Exception as e:
            flash(f"Error processing request: {str(e)}", "error")
            return redirect(url_for("index"))
    
    @app.route('/download/<filename>')
    def download(filename):
        file_path = os.path.join('generated_docs', filename)
        return send_file(file_path, as_attachment=True)



