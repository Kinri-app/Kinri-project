from supabase_client import fetch_vault_cards
from app.utils.utils import questionnaire
from mistralai import Mistral
import os

# Initialize Mistral client
api_key = os.environ["MISTRAL_API_KEY"]
model = "open-mistral-7b"
client = Mistral(api_key=api_key)

def ask_mistral(message, model, chat_history):
    response = client.chat.complete(
        model=model,
        messages=chat_history + [{"role": "user", "content": message}],
    )
    assistant_message = response.choices[0].message
    return assistant_message.content, chat_history + [{"role": "user", "content": message}, assistant_message]

def mistral_chat():
    # print("Welcome to Echo – your intuitive mental health companion.")
    # print("Let's begin by completing your mental health assessment.\n")

    # Replace this with questionnaire() when ready
    assessment = questionnaire()
    table_data = fetch_vault_cards("Kinri_Symptom_Prompts_With_Vault_Tags")

    prompt = '''
        * The user has just completed a mental health assessment.
        * You will be shown a list of related educational vault cards. Each contains a question and an answer.
        * You are the user's understanding companion that does not wish to impose but would like to offer some information if they want it.
        * Let them know that one assessment cannot understand all of the intricacies that make them up.
        >>> * Based on the user's highest scored condition, pick ONE vault card that best reflects their likely concern based on the 'Vault Card Tags' 'condition', for example {'condition': ['ADHD', 'Autism'], 'emotion': [], 'narrative_type': ['lived_experience'], 'usage_mode': []}
        >>> * Do not bring up seeking help from professionals only that if they are interested in learning more you are there for them.
        >>> * If they want to find a vault card related to a specific condition, include that condition as a key-value pair in the prompt, for example {'condition': 'CPTSD'}
        * Ask the question associated with the Symptom key and follow it up with the description associated with the Echo friendly description key.
        * Return the id of the vault card you choose. format response as following {"id": {}}
        '''

    # First message sets context and gives the model instructions
    system_message = (
        f"Assessment Results:\n{assessment}\n\n"
        f"Vault Table Data:\n{table_data}\n\n"
        f"Instructions:\n{prompt}"
    )

    chat = []
    assistant_response, chat = ask_mistral(system_message, model, chat)
    print("\nAssistant:", assistant_response)

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye 👋")
            break
        assistant_response, chat = ask_mistral(user_input, model, chat)
        print("Assistant:", assistant_response)

mistral_chat()
