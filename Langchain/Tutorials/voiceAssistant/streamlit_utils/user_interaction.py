import streamlit as st
from streamlit_chat import message
from elevenlabs.client import ElevenLabs
from io import BytesIO
import os

def get_user_input(transcription):
    return st.text_input("", value=transcription if transcription else "", 
    key="input")


def display_conversation(history):
    for i in range(len(history["generated"])):
        message(history["past"][i], is_user=True, key=str(i) + "_user")
        message(history["generated"][i], key=str(i))
        #Voice using Eleven API
        voice= "Bella"
        client  = ElevenLabs(api_key=os.environ.get('ELEVEN_API_KEY'))
        text= history["generated"][i]
        voices = client.voices.get_all()
        audio = client.text_to_speech.convert(text=text,voice_id = "JBFqnCBsd6RMkjVDRZzb",model_id="eleven_multilingual_v2")
        audio_data = b"".join(audio)
        audio_bytes = BytesIO(audio_data)
        st.audio(audio_bytes, format='audio/mp3')


        # Need to make it work myan
        