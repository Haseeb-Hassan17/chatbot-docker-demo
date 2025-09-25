# Chatbot Project

This is a simple chatbot project built with FastAPI, Python, and the OpenAI API, featuring a basic HTML frontend rendered using Jinja2 templates.

## Features

-   **FastAPI Backend**: A robust and fast web framework for building APIs.
-   **OpenAI Chatbot**: Integrates with the OpenAI API to provide conversational AI capabilities.
-   **HTML Frontend**: A simple web interface for interacting with the chatbot.
-   **Jinja2 Templating**: Renders dynamic HTML content for the frontend.
-   **Environment Variable Management**: Securely loads API keys and other configurations from a `.env` file using `python-dotenv`.
-   **Logging**: Basic logging implemented for tracking application events.

## Project Structure

\`\`\`
.
├── .env.example
├── chatbot.py
├── Dockerfile
├── index.html
├── main.py
├── README.md
└── requirements.txt
\`\`\`

## Setup Instructions

Follow these steps to set up and run the project locally.

### 1. Clone the Repository

\`\`\`bash
git clone <your-repository-url>
cd chatbot
\`\`\`

### 2. Create a Virtual Environment

It's recommended to use a virtual environment to manage dependencies.

\`\`\`bash
python -m venv venv
\`\`\`

### 3. Activate the Virtual Environment

-   **On Windows:**
    \`\`\`bash
    .\venv\Scripts\activate
    \`\`\`
-   **On macOS/Linux:**
    \`\`\`bash
    source venv/bin/activate
    \`\`\`

### 4. Install Dependencies

Install the required Python packages using pip:

\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 5. Configure Environment Variables

Create a `.env` file in the root directory of your project and add your OpenAI API key:

\`\`\`
OPENAI_API_KEY="your_openai_api_key_here"
\`\`\`

**Important**: Replace `"your_openai_api_key_here"` with your actual OpenAI API key. You can obtain one from the [OpenAI website](https://platform.openai.com/account/api-keys).

### 6. Run the Application

Start the FastAPI application using Uvicorn:

\`\`\`bash
uvicorn main:app --reload
\`\`\`

The `--reload` flag enables auto-reloading, so the server will restart automatically when you make changes to the code.

### 7. Access the Chatbot

Once the server is running, open your web browser and navigate to:

\`\`\`
http://127.0.0.1:8000
\`\`\`

You should see the chatbot interface, and you can start interacting with it.

## Usage

Type your messages into the input field on the web interface and press Enter or click the "Send" button to get responses from the AI chatbot.

## Logging

The application includes basic logging to the console for tracking requests and chatbot interactions.

## Contributing

Feel free to fork the repository, make improvements, and submit pull requests.
