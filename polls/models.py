from django.db import models
# django 封装好了数据模型 不需要自己写sql
# Create your models here.
# mvc 中的model层 负责数据
class UserLogin(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    # 相当于执行了sql语句
    # create table "appname"_"类名"+ 建表语句
    # 使用python manage.py makemigrations
    # 再使用 python3.9 manage.py migrate
    # 即可完成建表
    # django里面 有独特的方法 删除数据库中的数据 objects.delect
    # django 里面提取数据的方法 返回来的是一个 QuerySet对象类型。这个对象封装好了 表中的数据
    # 获取第一条数据
    # obj  = UserLogin.objects.filter(id = 1).first()
    # UserLogin.update()
    # 重点提及一下 filter方法 封装好了 sql里面的 选择 select * where id = ? phonenum = ? 这种选择、过滤方法