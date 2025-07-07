
import os
import requests
from dotenv import load_dotenv

# Config is designed for the supabase connection. Pulls in data from specified "table name"
load_dotenv()

SUPABASE_URL = "https://ksfnoxqnhaknivpizbby.supabase.co"
SUPABASE_KEY = os.getenv("SUPABASE_ANON_KEY")  # ommitted using .env file

table_name = "Kinri_Symptom_Prompts_With_Vault_Tags"  # <-- use real table


headers = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}"
}

def fetch_vault_cards(table_name):
    url = f"{SUPABASE_URL}/rest/v1/{table_name}"

    response = requests.get(url, headers=headers)

    if response.ok:
        print("✅ Connected! Here's your data:")
        return response.json()

    else:
        print("❌ Connection failed:", response.status_code, response.text)
        print("SUPABASE_KEY:", SUPABASE_KEY)  # Just to check

# symptom_prompt_with_vault_tags = fetch_vault_cards(table_name)




