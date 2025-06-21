
import yt_dlp
import whisper


def download_mp4_from_youtube(url,filename):
    # Set the options for the download
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',
        'outtmpl': filename,
        'quiet': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(url, download=True)


def load_whisper_model():
    """
    Load the Whisper model
    """
    model = whisper.load_model("base")
    return model


def get_transcried_text(filename):
    """
    Get the transcribed text
    """
    model = load_whisper_model()
    result = model.transcribe(filename)
    return result['text']

def save_transcribed_text_to_file(text, filename):
    """
    Save the transcribed text to a file
    """
    with open(filename, 'w') as f:
        f.write(text)