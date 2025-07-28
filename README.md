Zeltron Equipment Manager
Intelligent Fleet Control. Real-Time Insights. Unmatched Efficiency.

Zeltron is a full-stack, enterprise-grade application designed for modern engineering and construction firms to manage their fleet of heavy equipment. It provides a complete ecosystem including a powerful web dashboard for managers, a streamlined mobile app for field personnel, and a professional marketing website, all powered by a secure and scalable backend.

Key Features
The Zeltron platform is built with a rich set of features to provide a complete operational overview and control.

Web Application Dashboard
Real-Time Live Map: Track the GPS location of all equipment in real-time on an interactive map.

Comprehensive CRUD: Full Create, Read, Update, and Delete functionality for all core business entities.

Multi-Assignment Jobs: Create complex jobs, assigning multiple pieces of equipment and multiple operators/drivers to a single task.

Detailed History Logs: View the complete job and service history for every piece of equipment and personnel.

Maintenance Management: Log service events, track costs, and view detailed maintenance reports.

Personnel Status: Manage the active/inactive status of all personnel to know who is available for work.

Role-Based Permissions: The user interface intelligently adapts, showing management features only to authorized admins and managers.

Gemini AI Integration: AI-powered summaries for maintenance logs, providing clear, professional reports from technical notes.

Modern UI/UX: A sleek, professional user interface with a yellow brand theme and a persistent dark mode.

Backend API
Secure Authentication: Built with JWT for secure, stateless authentication.

Role-Based Access Control (RBAC): API endpoints are protected, ensuring users can only access the data and perform actions they are permitted to.

Scalable Architecture: Built with Django and MongoDB to handle large amounts of data and complex queries.

Marketing Website
Professional Design: A modern, dark-themed website to attract and inform potential clients.

Gemini AI Assistant: An interactive "Ask Zeltron" feature that allows potential clients to get instant, intelligent answers to their questions.

Seamless Integration: A "Login" button that transitions clients smoothly to the web application.

Tech Stack
This project is built with a modern, professional stack, just like a senior engineering team would use.

Backend:

Python

Django & Django Rest Framework

MongoDB (with Djongo)

Gunicorn (for production)

Frontend (Web & Mobile Simulation):

React

Tailwind CSS

Leaflet.js (for maps)

Database:

MongoDB Atlas (Cloud-hosted)

AI Integration:

Google Gemini API

Deployment (Planned):

Docker

Amazon Web Services (AWS) - ECR, ECS, Fargate, ALB, S3

Project Structure
The project is organized into three main components within a single repository:

/
├── equipment_backend/      <-- The Django backend API
├── web_app/                <-- The main React web application (app.html)
└── marketing_website/      <-- The public marketing website (index.html)

Getting Started
To run this project locally, you will need Python, Node.js, and Docker installed.

1. Backend Setup
# Navigate to the backend folder
cd equipment_backend

# Create and activate a Python virtual environment
python -m venv venv
source venv/Scripts/activate

# Install all required packages
pip install -r requirements.txt

# Run the development server
python manage.py runserver

2. Frontend Setup
The frontend applications (web_app/app.html and marketing_website/index.html) are self-contained HTML files. You can open them directly in a modern web browser. Ensure the backend server is running for the applications to connect to the API.

Pushing to GitHub
To store your project on GitHub, follow these steps.

1. Create a New Repository on GitHub
Go to GitHub.com and log in.

Click the + icon in the top right corner and select "New repository".

Give your repository a name (e.g., Zeltron-App).

Choose whether to make it public or private.

Do not initialize it with a README, .gitignore, or license. We will do that from the command line.

Click "Create repository".

2. Initialize Your Local Repository
Open your terminal and navigate to your main project folder (the one that contains equipment_backend/, web_app/, etc.).

# Navigate to your main project folder
cd /path/to/your/EquipmentManagerProject

# Initialize a new Git repository
git init -b main

# Add all the files in your project to be tracked
git add .

# Make your first commit
git commit -m "Initial commit of the Zeltron application"

3. Connect to GitHub and Push
Go back to your new repository page on GitHub. You will see a section titled "...or push an existing repository from the command line". Copy those two commands. They will look like this:

# Link your local repository to the remote one on GitHub
git remote add origin https://github.com/your-username/Zeltron-App.git

# Push your code to the main branch on GitHub
git push -u origin main

After running these commands, refresh your GitHub page. You will see all your project files securely stored in your repository.
