import logging
import os # Import os module to access environment variables
from openai import OpenAI

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class SimpleChatbot:
    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            logger.error("OPENAI_API_KEY environment variable not set.")
            raise ValueError("OPENAI_API_KEY environment variable not set.")
        self.client = OpenAI(api_key=api_key) # Pass API key to OpenAI client
        self.chat_history = []
        logger.info("Chatbot initialized.")
    
    def chat(self, user_input):
        logger.info(f"User input received: {user_input}")
        try:
            messages = [{"role": "user", "content": user_input}]
            if self.chat_history:
                messages = self.chat_history + messages

            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages
            )
            
            bot_response_text = response.choices[0].message.content
            
            self.chat_history.extend([
                {"role": "user", "content": user_input},
                {"role": "assistant", "content": bot_response_text}
            ])
            
            logger.info(f"Bot response generated: {bot_response_text}")
            return bot_response_text
        except Exception as e:
            logger.error(f"Error during chat processing: {e}")
            return f"Error: {str(e)}"
    
    def clear_history(self):
        self.chat_history = []
        logger.info("Chat history cleared.")

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
