import json

data = {
    "name": "John",
    "age": 30,
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "state": "NY"
    },
    "hobbies": ["reading", "traveling", "photography"]
}
data2 = {'msg': [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Does Azure OpenAI support customer managed keys?"},
        {"role": "assistant", "content": "Yes, customer managed keys are supported by Azure OpenAI."},
        {"role": "user", "content": "Do other Azure Cognitive Services support this too?"}
    ]
}
data3 = json.dumps(data2)
data5 = json.loads(data3)
print(data3)
print(type(data5))
print(data5)