import os
from groq import Groq

my_key = "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"

client = Groq(
    api_key=my_key,
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of fast language models",
        }
    ],
    model="llama3-8b-8192",
)

print(chat_completion.choices[0].message.content)