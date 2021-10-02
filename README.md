# CoolQ-capture-robots -- a robot could capture keywords in QQ

> Level: middle

> Techniques: based on CoolQ-air robot, including python and C++ version
> 
> my gain:
>
> * developed my first application plug-in that has pramatic purpose
> * try to read official doc to know how to build API-driven application

> deficiencies:
>
> * Official API based on Python is not completed which could not pack the whole application, so users should install develop environment to use
>
> * I am not familiar with C++ during my development(now I am little bit better:) ), so I did not implement the C++ version
> 
## how to use (python version):

> 1. install python environment:
>
>    https://gitee.com/muxiaofei/coolq_sdk_x/wikis/pages
>
> 2. replace the file *CQPlusHandler.py* in directory *酷Q Air\app\cn.muxiaofei.coolq_sdk_x* 
>
> 3. start the CoolQ application *小渣抓取机器人*，and reload the application
>
> 4. send **$readme** to read instructions

## functions:

> 1. the robot could store your chat records by day using text files可以将每天的聊天记录按天以text文本的格式保存
> 2. the robot could search contents by setting keywords and alarm you(other user ID, time, content, sender's name)
> 3. the robot could be set by sending it instruction to add and remove keywords


# 酷Q机器人插件——小渣抓取机器人

> 难度：中等

> 应用技术：基于酷Q机器人Air开发的聊天记录机器人，分别包括Python版本以及C++版本

> 主要收获：
>
> * 开发了自己第一款有实际用途的应用插件
> * 尝试阅读官方文档使用了对应API开发应用

> 不足：
>
> * Python版本的官方接口并不完善，无法进行打包应用，所以需要用户自行安装开发环境
>
> * C++由于开发难度较大，许多功能由于技术原因无法实现，只好暂时搁置

## 使用方法：（Python版本）

> 1. 安装Python环境：
>
>    https://gitee.com/muxiaofei/coolq_sdk_x/wikis/pages
>
> 2. 将 *酷Q Air\app\cn.muxiaofei.coolq_sdk_x*目录下 *CQPlusHandler.py*文件替换
>
> 3. 启用酷Q中的应用*小渣抓取机器人*，并重载应用
>
> 4. 向机器人发送$readme指令，并根据指令来进行操作

## 具体功能：

> 1. 可以将每天的聊天记录按天以text文本的格式保存
> 2. 可以设置关键词（如ID，时间，内容，发送人等等）来在当天消息记录中搜索相关内容
> 3. 通过指令查询，添加，删除关键词
