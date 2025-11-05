from app import mistral

EMBED_MODEL = "mistral-embed"

# def ask_mistral(message, chat_history, model="open-mistral-7b"):
#     response = mistral.chat.complete(
#         model=model,
#         messages=chat_history + [{"role": "user", "content": message}],
#     )
#     assistant_message = response.choices[0].message 
    
#     # Convert to plain dict before adding to history
#     assistant_dict = {
#         "role": assistant_message.role,
#         "content": assistant_message.content
#     }

#     updated_history = chat_history + [
#         {"role": "user", "content": message}, 
#         assistant_dict
#     ]

#     texts_to_embed = [message, assistant_dict["content"]]
#     embed_response = mistral.embeddings.create(
#         model=EMBED_MODEL,
#         inputs=texts_to_embed
#     )

#     user_vec = embed_response.data[0].embedding
#     assistant_vec = embed_response.data[1].embedding

#     return assistant_message.content, updated_history, {"user_embedding": user_vec, "assistant_embedding": assistant_vec}

# def embed_content(assistant_message, user_message):
#     texts_to_embed = [assistant_message, user_message]

#     embed_response = mistral.embeddings.create(
#         model = EMBED_MODEL,
#         inputs = texts_to_embed
#     )

#     user_vec = embed_response.data[0].embedding
#     assistant_vec = embed_response.data[1].embedding


def ask_mistral(message, chat_history, model="open-mistral-7b"):
    SYSTEM_MD = (
        "Output MUST be valid GitHub-flavored Markdown only. "
        "Do NOT use HTML. Do NOT wrap the whole reply in triple backticks. "
        "Rules:\n"
        "- Use **bold** for emphasis and *italics* for softer tone.\n"
        "- Use bullet lists (-) and numbered lists (1.) when appropriate.\n"
        "- Use inline code with single backticks for short code.\n"
        "- Use fenced code blocks ONLY for multi-line code; never wrap entire non-code replies in fences.\n"
        "- Use [text](url) for links.\n"
        "- Keep paragraphs separated by a blank line.\n"
    )


    # Hardening: ensure history shape
    if not isinstance(chat_history, list):
        chat_history = []
    # Optionally: validate each item has role/content keys

    messages = [
        {"role": "system", "content": SYSTEM_MD},
        *chat_history,
        {"role": "user", "content": message},
    ]

    response = mistral.chat.complete(model=model, messages=messages)
    assistant_message = response.choices[0].message  # .role, .content

    assistant_dict = {
        "role": assistant_message.role,
        "content": assistant_message.content,
    }

    return assistant_message.content, chat_history + [{"role": "user", "content": message}, assistant_dict]
