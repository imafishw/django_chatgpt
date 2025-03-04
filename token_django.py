import jwt
import time

headers = {
  "alg": "HS256",
  "typ": "JWT"
}
# 设置headers，即加密算法的配置
salt = "asgfdgerher"
# 随机的salt密钥，只有token生成者（同时也是校验者）自己能有，用于校验生成的token是否合法
exp = int(time.time() + 1)
# 设置超时时间：当前时间的100s以后超时
payload = {
  "name": "dawsonenjoy",
  "exp": exp
}
# 配置主体信息，一般是登录成功的用户之类的，因为jwt的主体信息很容易被解码，所以不要放敏感信息
# 当然也可以将敏感信息加密后再放进payload

token = jwt.encode(payload=payload, key=salt, algorithm='HS256', headers=headers)
print(token)
info = jwt.decode(token, salt, algorithms='HS256')
print(info)