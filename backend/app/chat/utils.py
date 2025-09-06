from app import mistral

EMBED_MODEL = "mistral_embed"

def ask_mistral(message, chat_history, model="open-mistral-7b"):
    response = mistral.chat.complete(
        model=model,
        messages=chat_history + [{"role": "user", "content": message}],
    )
    assistant_message = response.choices[0].message  
    
    # Convert to plain dict before adding to history
    assistant_dict = {
        "role": assistant_message.role,
        "content": assistant_message.content
    }

    updated_history = chat_history + [
        {"role": "user", "content": message}, 
        assistant_dict
    ]

    texts_to_embed = [message, assistant_dict["content"]]
    embed_response = mistral.embeddings.create(
        model=EMBED_MODEL,
        input=texts_to_embed
    )

    user_vec = embed_response.data[0].embedding
    assistant_vec = embed_response.data[1].embedding

    return assistant_message.content, updated_history, {"user_embedding": user_vec, "assistant_embedding": assistant_vec}


