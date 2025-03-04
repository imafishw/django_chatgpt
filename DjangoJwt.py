import jwt
import time
JWT_KEY = "FASVSKOOIFUPVNXZMIOWQ1"


def create_token(username):
  """
  生成jwt
  :param payload: dict 载荷
  :param expiry: datetime 有效期
  :param JWT_KEY: 密钥
  :return: jwt
  """

  payload = {
      "iat": int(time.time()),
      "exp": int(time.time()) + 3600 * 12,
      "username": username,
  }
  token = jwt.encode(payload, JWT_KEY, algorithm='HS256')
  return token


def verify(token):
  """
  :param token: jwt
  :param JWT_KEY: 密钥
  :return: bool

  """
  try:
      info = jwt.decode(token, JWT_KEY, algorithms='HS256')
      print(info)
      return True
  except jwt.ExpiredSignatureError:
      print('token已失效')
      return False
  except jwt.DecodeError:
      print('token认证失败')
      return False
  except jwt.InvalidTokenError:
      print('非法的token')
      return False

