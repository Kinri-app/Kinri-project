from app import mistral

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

    return assistant_message.content, chat_history + [{"role": "user", "content": message}, assistant_dict]
