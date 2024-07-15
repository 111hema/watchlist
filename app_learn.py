from flask import Flask
from markupsafe import escape
from flask import url_for

# 首先从 flask 包导入 Flask 类, 通过实例化这个类, 创建一个程序对象 app
app = Flask(__name__)

# 接下来, 要注册一个处理函数, 这个函数是处理某个请求的处理函数
# Flask 官方把它叫做视图函数(view funciton), 可以理解为"请求处理函数"

#"注册", 就是给这个函数戴上一个装饰器帽子, 使用 app.route() 装饰器来为这个函数绑定对应的 URL
# 当用户在浏览器访问这个 URL 的时候, 就会触发这个函数, 获取返回值, 并把返回值显示到浏览器窗口

# 填入 app.route() 装饰器的第一个参数是 URL 规则字符串, 这里的 /指的是根地址
# 只需要写出相对地址, 主机地址, 端口号等都不需要写出

# 一个视图函数也可以绑定多个 URL, 这通过附加多个装饰器实现
@app.route('/')
def hello():
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'


# 之所以把传入 app.route 装饰器的参数称为 URL 规则, 是因为我们也可以在 URL 里定义变量部分

# 注意 用户输入的数据会包含恶意代码, 所以不能直接作为响应返回
# 需要使用 MarkupSafe(Flask 的依赖之一)提供的 escape() 函数对 name 变量进行转义处理
@app.route('/user/<name>')
def user_page(name):
    return f'User: {escape(name)}'


@app.route('/test')
def test_url_for():
    print(url_for('hello')) # 生成 hello 视图函数对应的 URL，将会输出：/
    
    # 注意下面两个调用是如何生成包含 URL 变量的 URL 的
    print(url_for('user_page', name='hema'))  # 输出：/user/hema
    print(url_for('user_page', name='peter'))  # 输出：/user/peter
    print(url_for('test_url_for'))  # 输出：/test
    
    # 下面这个调用传入了多余的关键字参数, 它们会被作为查询字符串附加到 URL 后面
    print(url_for('test_url_for', num=2))  # 输出：/test?num=2
    return 'Test page'