from langchain_ollama import OllamaLLM
from dotenv import load_dotenv
import os

def main():
    # Load environment variables from .env file
    load_dotenv()
    
    # Initialize the chat model using Ollama with Llama 3.2
    chat = OllamaLLM(model="llama3.2")
    
    # Test the model with a simple message
    response = chat.invoke("Hello! What model are you? What is your version? What is your temperature? What is the capital of France?")
    print("Response from Llama:", response)

if __name__ == "__main__":
    main() 