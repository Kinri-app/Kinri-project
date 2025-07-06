from supabase_client import fetch_vault_cards
import supabase
from app.utils.utils import questionnaire
from mistralai import Mistral
import json
import os


# assessment = questionnaire()
assessment = [
            {
                "condtion": "cptsd",
                "score": 4.125
            },
            {
                "condtion": "gad",
                "score": 2.5
            },
            {
                "condtion": "autism",
                "score": 1.625
            }
            ]

table_data = fetch_vault_cards("Kinri_Symptom_Prompts_With_Vault_Tags")

prompt = '''
        "You are inquisitive and wanting to know how the user is feeling after the asssessemnt questions.\n"
        "With empathy, let them know what the assessment shows as the top condition.\n"
        "From the vault cards provided, choose the most relevant one and ask them question associated with "Symptom"\n
        "then follow up directly after with the 'Echo-Friendly Description'.\n"
        "Next ask them if they would like to pursue some information about this condition.\n"
'''

api_key = os.environ["MISTRAL_API_KEY"]
model = "open-mistral-7b"

client = Mistral(api_key=api_key)

# user_input = symptom_prompt_with_vault_tags

def run_mistral(assessment, table_data, prompt):

    content = (
        f"Assessment Results:\n{assessment}\n\n"
        f"Vault Table Data:\n{table_data}\n\n"
        f"Instructions:\n{prompt}"
    )

    chat_response = client.chat.complete(
        model= model,
        messages = [
            {
                "role": "user",
                "content": content
            },
        ]
    )
    print(chat_response.choices[0].message.content)
    # print(json.dumps(table_data[0], indent=2))
    



run_mistral(assessment, table_data, prompt)