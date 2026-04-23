import ollama

'''
调用千问本地部署的模型
'''
stream = ollama.chat(
    # ollama list 显示的模型名称列表
    model='Qwen2.5-1.5B',
    messages=[{'role': 'user', 'content': '写一首关于春天的短诗，字数控制在200字内。'}],
    stream=True
)

# 逐块打印回复内容
for chunk in stream:
    print(chunk['message']['content'], end='', flush=True)
