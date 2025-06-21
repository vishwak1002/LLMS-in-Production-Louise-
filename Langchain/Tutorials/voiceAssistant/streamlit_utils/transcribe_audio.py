# Transcribe audio using OpenAI Whisper API
import whisper
import streamlit as st
import os
from audio_recorder_streamlit import audio_recorder

TEMP_AUDIO_PATH = "temp_audio.wav"
AUDIO_FORMAT = "audio/wav"


def transcribe_audio(audio_file_path):
    try:
        with open(audio_file_path, "rb") as audio_file:
            response = get_transcried_text(audio_file_path)
        return response["text"]
    except Exception as e:
        print(f"Error calling Whisper API: {str(e)}")
        return None



def record_and_transcribe_audio():
    audio_bytes = audio_recorder()
    transcription = None
    if audio_bytes:
        st.audio(audio_bytes, format=AUDIO_FORMAT)
        with open(TEMP_AUDIO_PATH, "wb") as f:
            f.write(audio_bytes)
        if st.button("Transcribe"):
            transcription = transcribe_audio(TEMP_AUDIO_PATH)
            os.remove(TEMP_AUDIO_PATH)
            display_transcription(transcription)
    return transcription

 # Display the transcription of the audio on the app
def display_transcription(transcription):
    if transcription:
        st.write(f"Transcription: {transcription}")
        with open("audio_transcription.txt", "w+") as f:
            f.write(transcription)
    else:
        st.write("Error transcribing audio.")


def get_transcried_text(filename):
    """
    Get the transcribed text
    """
    model = load_whisper_model()
    result = model.transcribe(filename)
    return result['text']


def load_whisper_model():
    """
    Load the Whisper model
    """
    model = whisper.load_model("base")
    return model