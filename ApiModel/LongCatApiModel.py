import os

from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("LONGCAT_API_KEY"),
    base_url='https://api.longcat.chat/openai'
)

response = client.chat.completions.create(
    model="LongCat-Flash-Chat",
    messages=[
        {"role": "user", "content": "请介绍一下自己"}
    ]
)

print(response.choices[0].message.content)
