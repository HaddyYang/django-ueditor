django-ueditor
==============

 - 该项目集成ueditor富文本框。配置简单方便，主要解决图片、视频、文件上传问题
 - 该项目基于 https://github.com/huzhicheng/uEditor_django 添加新功能并完善
 - 开发环境 Django1.8、Python2.7
 - 博客地址：http://yshblog.com/blog/80

##目前支持功能：
 - 基本文字、排版等功能
 - 图片上传、文件上传、视频上传功能
 - 在线文件、在线图片功能
 - 可使用UEditor配置参数
 - **图片加水印功能**

##*未实现功能：*
 - *涂鸦功能*
 - *网络图片功能*

目录说明：
-----

Demo是django演示项目，可以直接运行测试
ueditor是本项目封装的django应用

Demo使用方法：
-----

下载这里的完整代码，进入Demo目录。运行`python manage.py runserver`
打开浏览器，访问`http://localhost:8000/`可查看效果演示。


安装使用方法：
-----
 1. 复制ueditor目录到你的django项目中
 2. 打开settings.py，给`INSTALLED_APPS`加入应用`ueditor`
    <pre><code>
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'ueditor', #加入这个
    ]
    </code></pre>
 3. 检查一下settings.py是否设置好static静态目录，可参考如下设置
    <pre><code>
    STATIC_URL = '/static/'
    #静态目录
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, "static"),
    )
    </code></pre>
    记得这里设置，下面对ueditor配置和这个有关系
 4. 打开django项目的urls.py文件，添加ueditor的url路由配置
    <pre><code>
    url(r'^ueditor/', include('ueditor.urls')),
    </code></pre>
    若这些设置看不明白可以看Demo里面的演示django项目
 5. 上面步骤配置完成之后，基本可以使用了。ueditor配置可能需要根据你的项目具体情况修改。
    ueditor前端配置文件，在ueditor/UE/ueditor.config.js
    ueditor后端配置文件，在ueditor/ueconfig.json
    具体配置可参考ueditor官网

至此，配置工作完成，剩下的就是到页面上引用uEditor了，下面是一个简单的html页面，可根据uEditor放置位置调整脚本
和样式的引用路径
```
    <!DOCTYPE html>
    <html lang="en" xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <meta charset='utf-8'>
        <link rel="stylesheet" type="text/css" href="/ueditor/UE/third-party/SyntaxHighlighter/shCoreDefault.css">
        <script type="text/javascript" src="/ueditor/UE/third-party/SyntaxHighlighter/shCore.js"></script>
        <script type="text/javascript" src="/ueditor/UE/ueditor.config.js"></script>
        <script type="text/javascript" src="/ueditor/UE/ueditor.all.min.js"></script>
        <script type="text/javascript" src="/ueditor/UE/lang/zh-cn/zh-cn.js"></script>

        <script type="text/javascript">
            var ue = UE.getEditor('editor');
            SyntaxHighlighter.all();
        </script>
    </head>
    <body>
        <script id="editor" type="text/plain" style="width:100%;height:500px;"></script>
    </body>
    </html>
```
其中：  
`var ue = UE.getEditor('editor');` 是ueditor实例化；  
`SyntaxHighlighter.all();` 是代码高亮。

-----
##上传图片自动加水印
该功能默认没开启。上传图片加水印功能需要安装PIL
pip install pillow

水印相关设置在ueconfig.json末尾：
```
    "openWaterMark": false,  //是否开启
    "waterMarkText": "我的水印\nhttp://xxxxx.com", //水印内容，建议一行文本
    "waterMarkFont": "msyhbd.ttf",  //字体，中文需要字体支持才不会出错
    "waterMarkSize": 15,    //字体大小
    "waterMarkBottom": 45,  //下边距
    "waterMarkRight": 155   //右边距
```