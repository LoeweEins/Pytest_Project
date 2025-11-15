#  使用命令 
python3 -m pytest cases -sv --html=report.html --self-contained-html
    制定当前目录设置为模块搜索路径
    -s 显示代码中 print 的内容，用于调试
    -v 显示测试类、测试函数的名字
    -sv 两参数合并

python3 -m pytest cases 指定目录为 cases
python3 -m pytest cases --html=report.html --self-contained-html 产生 html

python3 -m pytest cases1  cases2/登录 **指定多个目录**
python3 -m pytest cases/登录/test_错误登录.py::Test_错误密码 **指定一个类**
python3 -m pytest cases/登录/test_错误登录.py::Test_错误密码::test_C001001 **指定一个类里的方法**

# 根据名字
python3 -m pytest -k C001001 -s
    **可以是方法名 类名 模块文件名 目录名**
    **大小写敏感**
    **部分匹配**
    **not 表示不包含**
    python3 -m pytest -k "not C001001" -s **不包含**
    python3 -m pytest -k "错 and 密码2" -s **同时包含**
    python3 -m pytest -k "错 or 密码2" -s **包含其中之一**

# 根据标签
python3 -m pytest cases -m webtest -s

运行 pytest 助手：
    python3 -m pytest_assist
    python3 -m pytest_assist --lang en **英文启动**

只产生报告，不启动图形界面：
    python3 -m pytest -p pytest_assist.plugin --assist-report=myreport.html
**详细的用法再参考 blog**

# 截屏功能 **Selenium**
selenium_screenshot(wd) 在代码行中加入

**加粗文字**
*斜体文字*
~~删除线~~
`行内代码`

> 这是引用内容。
>> 可以嵌套引用。

```bash 
# 示例 代码块
python main.py


```
系统测试 回归测试 对比新旧版本的报告 输出
Pytest 单元测试 开发自测功能
