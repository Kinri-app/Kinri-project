import requests
from supabase_client import fetch_vault_cards
import supabase
from app.utils.utils import questionnaire


def ask_ollama(message, model="mistral", chat_history=[]):
    url = "http://localhost:11434/api/chat"

    payload = {
        "model": model,
        "messages": chat_history + [{"role": "user", "content": message}],
        "stream": False
    }

    response = requests.post(url, json=payload)
    response.raise_for_status()
    data = response.json()

    return data["message"]["content"], payload["messages"] + [data["message"]]

def ollama_chat():
    
    print("Welcome to Echo – your intuitive mental health companion.")
    print("Let's begin by completing your mental health assessment.\n")

    # Gathering initial data from the tables as well as the users assessment for there condition scores to pass as preliminary info for the LLM
    assessment = questionnaire()
    table_data = fetch_vault_cards("Kinri_Symptom_Prompts_With_Vault_Tags")

    # Tested prompt to create concise and empathetic responses to maintain user engagement as well as setting conversational tone
    prompt = '''
        "The user has just completed a mental health assessment.\n"
        "You will be shown a list of related educational vault cards. Each contains a question and an answer.\n"
        "You are the users understanding companion that does not wish to impose but would like to offer some information if they want it.\n"
        "Let them know that one assessment cannot understand all of the intracicies that make them up.\n"
        "Based on the user's highest scored condition, pick ONE vault card that best reflects their likely concern.\n"
        "Do not bring up seeking help from professionals only that if they are interested in learning more you are there for them.\n"
        "Ask the question associated with the Symptom key and follow it up with the description associated with the Echo friendly description key\n"
        '''
    # Creating an intial message that will get passed to the LLM model and give guidance to the conversation
    init_message = (
        f"Assessment Results:\n{assessment}\n\n"
        f"Vault Table Data:\n{table_data}\n\n"
        f"Instructions:\n{prompt}"
    )

    chat = []
    # Creating an intial chat history to give model context of how to interact with the client
    assistant_response, chat = ask_ollama(init_message, model="mistral", chat_history=chat)
    print("\nAssistant:", assistant_response)

    # Using a while loop to continue the conversation and add to the chat history using the ask_ollama function
    while True:
        user_input = input("You: ")
        response, chat = ask_ollama(user_input, model="mistral", chat_history=chat)
        print("Assistant:", response)

ollama_chat()