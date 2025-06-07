from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

def main():
    # Load environment variables from .env file
    load_dotenv()
    
    # Check if OpenAI API key is set
    if not os.getenv("OPENAI_API_KEY"):
        print("Please set your OPENAI_API_KEY in the .env file")
        return
    
    # Initialize the chat model
    chat = ChatOpenAI()
    
    # Test the model with a simple message
    response = chat.invoke("Hello! Can you confirm this setup is working?")
    print("Response from OpenAI:", response.content)

if __name__ == "__main__":
    main() 