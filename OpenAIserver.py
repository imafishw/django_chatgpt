import os
import requests
import json
import openai

# 创建一个类可以调用函数完成对话
from openai.error import OpenAIError, Timeout, RateLimitError, APIConnectionError, InvalidRequestError, AuthenticationError, ServiceUnavailableError
openai.api_type = "azure"
# 如果是azure , 此处应该为Microsoft Azure平台
openai.api_base = "https://webserver.openai.azure.com/"
openai.api_version = "2023-05-15"
openai.api_key = "ec0960a4b4d740ce98c56fa4ca756bcc"
mymessages = {
    'msg': [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Does Azure OpenAI support customer managed keys?"},
        {"role": "assistant", "content": "Yes, customer managed keys are supported by Azure OpenAI."},
        {"role": "user", "content": "Do other Azure Cognitive Services support this too?"}
    ]
}
# 提交格式
messages1=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Does Azure OpenAI support customer managed keys?"},
        {"role": "assistant", "content": "Yes, customer managed keys are supported by Azure OpenAI."},
        {"role": "user", "content": "Do other Azure Cognitive Services support this too?"}
    ]


def translate(msg):
    openai.api_type = "azure"
    # 如果是azure , 此处应该为Microsoft Azure平台
    openai.api_base = "https://webserver.openai.azure.com/"
    openai.api_version = "2023-05-15"
    openai.api_key = "ec0960a4b4d740ce98c56fa4ca756bcc"
    data_response = {

    }
    try:

        response = openai.ChatCompletion.create(
            engine="gpt-35-turbo",
            messages=msg
        )
        # gpt 响应
        data_response['errcode'] = 1030
        data_response['msg'] = response['choices'][0]['message']['content']
    except Timeout as e:
        # 处理超时异常
        data_response['errcode'] = 1031
        data_response['errmsg'] = 'Time out'
    except RateLimitError as e:
        data_response['errcode'] = 1032
        data_response['errmsg'] = 'RateLimit'
        # 处理速率限制异常
        # 可以记录日志、返回特定的错误响应等
    except APIConnectionError as e:
        # 处理API连接错误异常
        data_response['errcode'] = 1033
        data_response['errmsg'] = 'APIConnectionError'
    except InvalidRequestError as e:
        # 处理无效请求错误异常
        data_response['errcode'] = 1034
        data_response['errmsg'] = 'InvalidRequestError'
    except AuthenticationError as e:
        # 处理身份验证错误异常
        data_response['errcode'] = 1035
        data_response['errmsg'] = 'AuthenticationError'
    except ServiceUnavailableError as e:
        # 处理服务不可用错误异常
        data_response['errcode'] = 1036
        data_response['errmsg'] = 'ServiceUnavailableError'
    except OpenAIError as e:
        data_response['errcode'] = 1037
        data_response['errmsg'] = 'OpenAIError'
    return data_response

if __name__ == '__main__':
    print(mymessages['msg'])
    print(type(mymessages['msg']))
# 前后端分离的api
# pip install djangorestframework djangorestframework-simplejwt