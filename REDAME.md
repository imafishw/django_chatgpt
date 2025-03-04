## 					基于Django+vue框架的智能聊天机器人

1、核心的业务HTML

![img](file:///C:\Users\86182\AppData\Local\Temp\ksohtml1696\wps1.jpg)3、前端目录架构

在Vue文件夹下面，本地已经部署好了liveserver服务器供前端部署，static目录下存在着静态资源。

![img](file:///C:\Users\86182\AppData\Local\Temp\ksohtml1696\wps2.jpg) 

 

 

### **二、*****\*基于Django Restful framework的\*******\*后端\*******\*设计\****

2.1 Django简介

Python下有许多款不同的 Web 框架。Django是重量级选手中最有代表性的一位。许多成功的网站和APP都基于Django。Django 是一个开放源代码的 Web 应用框架，由 Python 写成。Django 采用了 MVT 的软件设计模式，即模型（Model），视图（View）和模板（Template）。

但由于现代浏览器性能的不断提升，以及以node.js为代表的客户端响应式框架的性能不断变强。Django也诞生了属于他的服务型响应框架Django Restful framework。服务端与客户端采用RESTFul API的交互方式。

在前后端分离的开发模式中，后端仅返回前端所需的数据，前端负责渲染HTML页面，后端不再控制前端的效果，用户看到什么样的效果，从后端请求的数据如何加载到前端中，都由前端自己决定，后端仅仅需要提供一套逻辑对外提供数据即可，并且前端与后端的耦合度相对较低，在这种模式中，我们通常将后端开发的每个视图都成为一个接口，或者API，前端通过访问接口来对数据进行增删改查。总结一句话，后台负责提供数据，前端负责数据展示，职责分离，分工明确。在未来随着前端，浏览器技术的不断迭代增强这种分离的趋势也会越来越明显。

 

![img](file:///C:\Users\86182\AppData\Local\Temp\ksohtml1696\wps3.jpg) 

 

2.2 Django框架的部署

2.2.1 MVT 三层架构

在本次项目中，尽管我们采用的是RESTful API的调用方式，我们会将网站的静态资源搭载到前端，前端通过Ajax请求的方式来获取数据。但对于Django来说views和model 的设置可以大大减免路由配置的麻烦，以及数据库操作的繁琐。

设置本项目的访问路由，在urls.py文件中设置从web所访问的路由，以及对应的视图函数。

![img](file:///C:\Users\86182\AppData\Local\Temp\ksohtml1696\wps4.jpg) 

  ![img](file:///C:\Users\86182\AppData\Local\Temp\ksohtml1696\wps5.jpg)

 

同时配置好项目所使用的数据库，在MySQL中创建好数据库后在model中创建好数据表，Django中有着独特定义的ORM来操作数据库。

 

![img](file:///C:\Users\86182\AppData\Local\Temp\ksohtml1696\wps6.jpg) 

2.3 登录的校验与用户认证

所谓的Token，其实就是服务端生成的一串加密字符串、以作客户端进行请求的一个“令牌”。当用户第一次使用账号密码成功进行登录后，服务器便生成一个Token及Token失效时间并将此返回给客户端，若成功登陆，以后客户端只需在有效时间内带上这个Token前来请求数据即可，无需再次带上用户名和密码。

尤其是在客户端与服务端不同源的情况下。设置了跨域访问

 

​    ![img](file:///C:\Users\86182\AppData\Local\Temp\ksohtml1696\wps7.jpg)

Token也无需保存在本地而是存储在用户的浏览器中，对于高并发、高流量	的服务程序来说也大大减少了服务器的负载开支。

![img](file:///C:\Users\86182\AppData\Local\Temp\ksohtml1696\wps8.jpg) 

2.4 GPT-35-turbo的管理与配置

在微软的Azure平台中创建部署好了语言模型资源之后，调用		  openAI的专用开发者接口开发自己的语言聊天机器人。

 

## **一、** ***\*测试\****

1、接口文档

详情请见接口文档

 

​      ![img](file:///C:\Users\86182\AppData\Local\Temp\ksohtml1696\wps9.jpg)

 

2、Login与Register

![img](file:///C:\Users\86182\AppData\Local\Temp\ksohtml1696\wps10.jpg) 

  ![img](file:///C:\Users\86182\AppData\Local\Temp\ksohtml1696\wps11.jpg)

 

3、测试结果如下

![img](D:\bookfile\Project_pythonweb\wps12.jpg)
