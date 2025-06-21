from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_anthropic import ChatAnthropic
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatAnthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # Set this in your environment
    model="claude-3-7-sonnet-20250219",
)

conversation = ConversationChain(
    llm=llm,
    memory=ConversationBufferMemory()
)
conversation.predict(input="""List all possible words as substitute for 'artificial' as comma separated.""")
conversation.predict(input = "the next 4 is ")

 