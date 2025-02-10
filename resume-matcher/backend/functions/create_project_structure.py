import os

def create_project_structure():
    project_structure = {
        "resume-matcher": {
            "backend": {
                "main.py": """from fastapi import FastAPI\nfrom backend.services.resume_parser import extract_resume_data\nfrom backend.services.job_matcher import match_jobs\n\napp = FastAPI()\n\n@app.get(\"/\")\ndef read_root():\n    return {\"message\": \"Resume Matcher API\"}""",
                "services": {
                    "resume_parser.py": """def extract_resume_data(resume_text: str):\n    # Mock function to extract details\n    return {\"name\": \"John Doe\", \"skills\": [\"Python\", \"FastAPI\", \"AI\"]}""",
                    "job_matcher.py": """def match_jobs(resume_data):\n    # Mock function for AI job matching\n    return [\"Software Engineer\", \"AI Researcher\"]"""
                },
                "models": {
                    "embeddings.py": """def generate_embeddings(text: str):\n    # Placeholder for embedding generation\n    return [0.1, 0.2, 0.3]"""
                },
                "database": {
                    "db_handler.py": """def save_to_db(data):\n    # Placeholder for database operations\n    return True"""
                }
            },
            "frontend": {
                "app.js": "console.log(\"Frontend App\");"
            },
            "deployment": {
                "Dockerfile": """FROM python:3.9\nWORKDIR /app\nCOPY . .\nRUN pip install -r requirements.txt\nCMD [\"uvicorn\", \"backend.main:app\", \"--host\", \"0.0.0.0\", \"--port\", \"8000\"]""",
                "k8s.yaml": """apiVersion: apps/v1\nkind: Deployment\nmetadata:\n  name: resume-matcher\nspec:\n  replicas: 2\n  selector:\n    matchLabels:\n      app: resume-matcher\n  template:\n    metadata:\n      labels:\n        app: resume-matcher\n    spec:\n      containers:\n      - name: resume-matcher\n        image: resume-matcher:latest\n        ports:\n        - containerPort: 8000"""
            },
            "requirements.txt": "fastapi\nuvicorn\npymongo",
            "README.md": "# Resume Matcher\nA FastAPI-based resume matcher with AI-powered job matching."
        }
    }
    
    def create_files_and_folders(base_path, structure):
        for name, content in structure.items():
            path = os.path.join(base_path, name)
            if isinstance(content, dict):
                os.makedirs(path, exist_ok=True)
                create_files_and_folders(path, content)
            else:
                with open(path, "w") as f:
                    f.write(content)
    
    base_dir = os.getcwd()
    create_files_and_folders(base_dir, project_structure)
    print("Project structure created successfully.")

if __name__ == "__main__":
    create_project_structure()
