import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser

# Load environment variables
load_dotenv()

class SimpleChatbot:
    def __init__(self):
        # Initialize the LLM
        self.llm = ChatOpenAI(
            model_name=os.getenv("MODEL_NAME", "gpt-3.5-turbo"),
            temperature=float(os.getenv("TEMPERATURE", "0.7")),
            openai_api_key=os.getenv("OPENAI_API_KEY")
        )
        
        # Create prompt template
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a helpful AI assistant."),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{input}")
        ])
        
        # Create the chain
        self.chain = self.prompt | self.llm | StrOutputParser()
        
        # Chat history
        self.chat_history = []
    
    def chat(self, user_input):
        try:
            response = self.chain.invoke({
                "input": user_input,
                "chat_history": self.chat_history
            })
            
            # Update history
            self.chat_history.extend([
                HumanMessage(content=user_input),
                AIMessage(content=response)
            ])
            
            return response
        except Exception as e:
            return f"Error: {str(e)}"
    
    def clear_history(self):
        self.chat_history = []

def main():
    print("🤖 Simple Chatbot (type 'quit' to exit)")
    print("-" * 40)
    
    chatbot = SimpleChatbot()
    
    while True:
        user_input = input("\nYou: ").strip()
        
        if user_input.lower() in ['quit', 'exit']:
            print("Goodbye!")
            break
        elif user_input.lower() == 'clear':
            chatbot.clear_history()
            print("History cleared!")
            continue
        
        if user_input:
            response = chatbot.chat(user_input)
            print(f"Bot: {response}")

if __name__ == "__main__":
    main()