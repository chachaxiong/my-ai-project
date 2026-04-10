import os

from openai import OpenAI

try:
    client = OpenAI(
        # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx",
        api_key=os.environ.get("DASHSCOPE_API_KEY"),
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )

    completion = client.chat.completions.create(
        model="qwen-plus",
        messages=[
            {"role": "system", "content": "你是一个小助手"},
            {"role": "user", "content": "请介绍一下自己"},
        ])
    print(completion.choices[0].message.content)
except Exception as e:
    print(e)
