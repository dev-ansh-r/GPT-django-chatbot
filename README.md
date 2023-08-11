# Chatbot Project with OpenAI Integration

This project demonstrates the implementation of a chatbot-like interface using Django, where users can interact with the chatbot to ask questions, and the responses are generated using the OpenAI API.

## Features

- User registration and authentication
- Chat interface with messages displayed in a conversation-style format
- Chat messages stored in the database for historical tracking
- Integration with the OpenAI API to generate responses

## Prerequisites

- Python 3.x
- Django (4.2.4 used for this project)
- OpenAI Python library (installed via `pip install openai`)

## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/yourusername/chatbot-django-openai.git
```

2. Navigate to the project directory:

```bash
cd chatbot-django-openai
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate
```

5. Copy code

```bash
python manage.py migrate
```

6. Start the development server:

```bash
python manage.py runserver
```

7. Access the application in your web browser at 

http://localhost:8000


## Configuration

**OpenAI API Key**: To use the OpenAI API, you need to set up an API key from OpenAI. Replace the openai_api_key value in views.py with your actual API key.
Usage

* Register a new user or log in using existing credentials.

* Once logged in, you'll be able to interact with the chatbot interface.

* Type your message in the input field and press "Send".

* The chat messages are displayed in a conversation-style format.

* The chatbot uses the OpenAI API to generate responses to the user's messages.
