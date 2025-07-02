from supabase_client import fetch_vault_cards
from app.utils.utils import questionnaire
from mistralai import Mistral
import numpy as np
import faiss
import os
from getpass import getpass

assessment = questionnaire()
table_data = fetch_vault_cards("Kinri_Symptom_Prompts_With_Vault_Tags")

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
    print("\n[Vault Card Prompt]\n")
    print(chat_response.choices[0].message.content)


run_mistral(assessment, table_data, """You are a therapeutic assistant helping users explore their emotions through personalized questions./

                                    /You have been given:
                                    - A JSON array of vault cards, each containing a question and tags (conditions and emotions).
                                    - Three condition names that reflect a user’s assessment score.

                                    Your task is to:
                                    1. Analyze the three conditions and select the **single most relevant vault card**.
                                    2. Respond **only** with the question from that vault card.
                                    3. Politely ask the user to elaborate on their answer.

                                    Wait for the user’s response. Then:
                                    4. Do your best to identify the user's **primary emotion** using **Plutchik's Wheel of Emotions**.
                                    5. Ask the user:  
                                    _“Would you like to explore things related to [detected emotion]?”_

                                    Important constraints:
                                    - Do **not** explain your reasoning unless asked.
                                    - Do **not** reference JSON or conditions directly in your response.
                                    - Always respond like a calm, curious emotional support guide.

                                    Begin only after receiving the vault card JSON and conditions list.""")