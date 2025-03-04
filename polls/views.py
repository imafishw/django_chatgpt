from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from polls.models import UserLogin
import json
import OpenAIserver
# DjangoJwt 自己写的Jsonwebtoken
import DjangoJwt
# request 这里可以分 请求的形式
# Create your views here.
def index(request):
    response = {
        'success': 0,
        'errMsg': "None"
    }

    return render(request,'user.html')
# # 模板语法
# def tpl(request):
#     name = "zq"
#     roles = ["auser", "CEO", "保安"]
#
#     return render(request,"ddd.html" ,{"n1":name})


def register(request):
    # 后端的注册逻辑
    if request.method == 'GET':

        return render(request, "index.html")
    if request.method == 'POST':
        json_response = {

        }
        data = json.loads(request.body.decode('utf-8'))
        if data is None:
            json_response['errcode'] = 1001
            json_response['errmsg'] = 'validation error'
        else:
            name = data['name']
            pw = data['password']
            # 拿到注册信息
            # 存进数据库
            try:
                user = UserLogin.objects.filter(name=name).exists()
                if user:
                    # 账户已经存在
                    json_response['errcode'] = 1002
                    json_response['errmsg'] = 'account exist'
                    return JsonResponse(json_response)
                else:
                    # 避免账户重复
                    UserLogin.objects.create(name=name, password=pw)
                    json_response['errcode'] = 1004
                    json_response['errmsg'] = 'success register'

            except Exception as e:
                print("异常信息为", e)
                json_response['errcode'] = 1003
                json_response['errmsg'] = 'databases error'
            # 拿到注册信息
            # 存进数据库
        return JsonResponse(json_response)


# 验证请求方法：它确保只有通过 POST 方法发送的请求才会调用被装饰的视图函数。如果请求方法不是 POST，DRF 将返回 "405 Method Not Allowed" 响应。
def login(request):
    # 后端的登录逻辑
    # 返回token,后续token存在继续访问，不存在就要重新注册
    #
    if request.method == 'GET':
        return HttpResponse("请使用POST请求")
    if request.method == 'POST':
        json_response = {
        }
        data = json.loads(request.body)
        if data is None:
            json_response['errcode'] = 1001
            json_response['errmsg'] = 'validation error'
            #     未接受到数据
        else:
            name = data['name']
            pw = data['password']
            try:
                userinfor = UserLogin.objects.filter(name=name).exists()
                if userinfor:
                    # 疑问在高并发的开发中会不会导致服务器响应速度很慢
                    user_all = UserLogin.objects.filter(name=name, password=pw).exists()
                    if user_all:
                        #   很慢
                        token_name = name
                        json_response['errcode'] = 1005
                        json_response['errmsg'] = 'success login'
                        token = DjangoJwt.create_token(token_name)
                        json_response['token'] = token
                #   查验账户的密码是否存在
                    else:
                        json_response['errcode'] = 1006
                        json_response['errmsg'] = 'password_error'
                else:
                    json_response['errcode'] = 1007
                    json_response['errmsg'] = 'account not exist'
                    #     未接受到数据
            except Exception as e:
                print(e)
                json_response['errcode'] = 1003
                json_response['errmsg'] = 'databases error'

        return JsonResponse(json_response)


def translate(request):
    # 核心的业务逻辑
    if request.method == 'GET':
        1
    if request.method == 'POST':
        json_response = {
        }
        token = request.META.get("HTTP_AUTHORIZATION")
        token = token.replace('Bearer ','')
        print(token)
        print(type(token))
        if DjangoJwt.verify(token):
            data = json.loads(request.body)
            if data is None:
                json_response['errcode'] = 1001
                json_response['errmsg'] = 'validation error'
                return JsonResponse(json_response)
            # 取得数据
            msg = data['msg']
            rtmsg = OpenAIserver.translate(msg)
            json_response['errcode'] = 1009
            json_response['rtmsg'] = rtmsg
        else:
            json_response['errcode'] = 1008
            json_response['errmsg'] = "Token is not valid please make connect with admin or login it again"
    return JsonResponse(json_response)

