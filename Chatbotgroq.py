from groq import Groq # pip install groq 
from os import system, name # To clean the screen

def clean_prompt(): # Clean the terminal
    if name == 'nt':
        _ = system('cls') # windows
    else:
        _ = system('clear') # mac ou linux
        
clean_prompt()
       
client = Groq(api_key="yor_api_key")


def answer_generator(message, message_list=[]):
    
    message_list.append({"role": "system", "content": message})

    answer = client.chat.completions.create(
        messages = message_list,
        model="llama3-8b-8192",
        stream=False,
    )
    return answer.choices[0].message.content

message_list = []

while True:
    user_input = input("Write a message or type 'exit' to exit: ")
    
    if user_input.lower() == "exit":
        print("Exiting the chatbot. Goodbye!")
        break
    else:
        answer = answer_generator(user_input, message_list)
        message_list.append({"role": "system", "content": answer})
        print("\nChatbot:\n",answer)
