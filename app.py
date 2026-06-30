import os
import gradio as gr
from google import genai
from google.genai import types

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

chat = client.chats.create(
    model='gemini-2.0-flash',
    config=types.GenerateContentConfig(
        system_instruction="Eres GROXO, narrador experto. Investiga siempre a fondo usando Google antes de responder.",
        tools=[{"google_search": {}}]
    )
)

def groxo_narrator(message, history):
    return chat.send_message(message).text

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.ChatInterface(fn=groxo_narrator, type="messages")

if __name__ == "__main__":
    demo.launch()
  
