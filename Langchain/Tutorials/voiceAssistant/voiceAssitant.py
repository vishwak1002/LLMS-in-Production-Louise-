



import streamlit as st
from utils.load_embedding import load_embeddings_and_database
from utils.deeplake import get_dataset_path, search_db
from streamlit_utils.transcribe_audio import record_and_transcribe_audio
from streamlit_utils.user_interaction import get_user_input, display_conversation
import os
from dotenv import load_dotenv

load_dotenv()
 # Constants


def main():
    # Initialize Streamlit app with a title
    st.write("# JarvisBase ??")
    load_dotenv()
        # Load embeddings and the DeepLake database
    db = load_embeddings_and_database(get_dataset_path())
# Record and transcribe audio
    transcription = record_and_transcribe_audio()
     # Get user input from text input or audio transcription
    user_input = get_user_input(transcription)
     # Initialize session state for generated responses and past messages
    if "generated" not in st.session_state:
        st.session_state["generated"] = ["I am ready to help you"]
    if "past" not in st.session_state:
        st.session_state["past"] = ["Hey there!"]
             # Search the database for a response based on user input and update the 
    # session state
    if user_input:
        output = search_db(user_input, db)
        print(output['source_documents'])
        st.session_state.past.append(user_input)
        response = str(output["result"])
        st.session_state.generated.append(response)
     #Display conversation history using Streamlit messages
    if st.session_state["generated"]:
        display_conversation(st.session_state)
 # Run the main function when the script is executed
if __name__ == "__main__":
    main()

 

