from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import assemblyai as aai
from groq import Groq
from gtts import gTTS
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from groq.types.chat import ChatCompletionUserMessageParam

aai.settings.api_key = "put your assemblyai api key here"
groq_client = Groq(api_key ="put your groq api key here")

from fastapi.staticfiles import StaticFiles
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all for testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
async def chat(file: UploadFile):
    print("📥 Received audio file...")

    # Save uploaded audio
    with open("input.wav", "wb") as f:
        f.write(await file.read())
    print("✅ Saved audio as input.wav")

    # 1. Transcribe with AssemblyAI
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe("input.wav")
    print("📝 Transcript:", transcript.text)

    # 2. Send transcription to Groq
    messages: list[ChatCompletionUserMessageParam] = [
    {"role": "user", "content": transcript.text or ""}
]


    response = groq_client.chat.completions.create(
        model="llama-3.1-8b-instant",   # Groq fast free model
        messages=messages
    )
    ai_reply = response.choices[0].message.content
    print("🤖 AI Reply:", ai_reply)

    # 3. Convert reply to speech
    tts = gTTS(ai_reply)
    tts.save("static/reply.mp3")
    print("🔊 Saved reply as reply.mp3")

    # Return reply
    return {"text": ai_reply, "audio": "static/reply.mp3"}

if __name__ == "__main__":
    print("🚀 Starting server at http://127.0.0.1:8000 ...")
    uvicorn.run(app, host="0.0.0.0", port=8000)