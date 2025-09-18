🎤 Voice Chatbot

A simple voice chatbot built with FastAPI, AssemblyAI, Groq, and gTTS.
It listens to your speech 🎙️, transcribes it, sends it to an AI model 🤖, and replies back in both text and audio 🔊.

🚀 Features

Record your voice in the browser

Transcription using AssemblyAI

AI-powered responses from Groq

Speech reply using gTTS

Clean FastAPI backend + simple HTML/JS frontend

⚙️ Installation & Setup
1. Clone the repository
git clone https://github.com/naeemkhan555/voice-chatbot.git
cd voice-chatbot

2. Create a virtual environment
python -m venv venv


Activate it:

On Windows (PowerShell):

venv\Scripts\activate


On Mac/Linux:

source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Add your API keys

Edit main.py and replace:

aai.settings.api_key = "your_assemblyai_key"
groq_client = Groq(api_key="your_groq_key")

5. Run the backend
uvicorn main:app --reload


The API will be available at:

http://127.0.0.1:8000

6. Open the frontend

Open index.html in your browser.
(Just double-click it or right-click → "Open With Browser".)

🎯 Usage

Click Start Recording

Speak into your microphone

Click Stop Recording

The bot will show a text reply and play the audio reply

📂 Project Structure
voice-chatbot/
│── main.py           # FastAPI backend
│── requirements.txt  # Python dependencies
│── index.html        # Frontend UI
│── script.js         # Frontend logic
│── static/           # Stores reply.mp3 for audio output
