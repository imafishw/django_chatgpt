#Note: The openai-python library support for Azure OpenAI is in preview.
import os
import openai
openai.api_type = "azure"
# 如果是azure , 此处应该为Microsoft Azure平台
openai.api_base = "https://webserver.openai.azure.com/"
openai.api_version = "2023-05-15"
openai.api_key = "ec0960a4b4d740ce98c56fa4ca756bcc"
#  封锁内部账户
#  明天解决难点 如何使用web进行 数据的传输
response = openai.ChatCompletion.create(
    engine="gpt-35-turbo", # engine = "deployment_name".
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Does Azure OpenAI support customer managed keys?"},
        {"role": "assistant", "content": "Yes, customer managed keys are supported by Azure OpenAI."},
        {"role": "user", "content": "Do other Azure Cognitive Services support this too?"}
    ]
)

print(response)
print(response['choices'][0]['message']['content'])