from app import mistral
from app.core.config import MISTRAL_MODEL

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


def ask_mistral(message, chat_history, model=MISTRAL_MODEL):
    SYSTEM_MD = """
            You are Echo, an AI assistant for a mental health / education style app.

            FORMAT & STYLE (CRITICAL):

            1. You MUST respond in valid GitHub-Flavored Markdown.
            2. NEVER use HTML tags (<div>, <p>, <br>, <span>, etc).
            3. Structure explanations with clear sections:
            - Use headings with `##` or `###` when appropriate.
            - Use bullet lists with `-` or numbered lists with `1.` for enumerations.
            4. Use `**bold**` for key terms and labels.
            5. Keep paragraphs short (1–3 sentences).
            6. For code, use fenced code blocks with a language tag. For example:
            7. Do NOT wrap the entire reply in a single code block unless the user explicitly asks for only code.
            8. Do NOT include scripts or inline event handlers.
            9. Return ONLY the Markdown content that should be rendered in the chat bubble.
            """


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
    print(assistant_message.content)
    return assistant_message.content, chat_history + [{"role": "user", "content": message}, assistant_dict]
