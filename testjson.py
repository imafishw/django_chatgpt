import jwt
import time
# 系统密钥
JWT_KEY = "FASVSKOOIFUPVNXZMIOWQ1"


def create_token(name,password):
  """
  生成jwt
  :param payload: dict 载荷
  :param expiry: datetime 有效期
  :param JWT_KEY: 密钥
  :return: jwt str
  """
  payload = {
      "iat": int(time.time()),
      "exp": int(time.time()) + 3600 * 12,
      "password": password,
      "username": name,
  }
  token = jwt.encode(payload, JWT_KEY, algorithm='HS256')
  return token


def verify(token):
  """
  :param token: jwt
  :param JWT_KEY: 密钥
  :return: dict: payload
  """
  pyloads = jwt.decode(token,JWT_KEY,algorithms='HS256')
  return pyloads

if __name__ == '__main__':
    a = create_token('11','22')
    print(a)
    print(type(a))
    b = verify(a)
    print(type(b))
    print(b)
    print(time.time())
