from selenium import webdriver  #(1)从selenium引入webdriver

browser = webdriver.Firefox()  #(2)启动一个selenium“webdriver”去弹出一个Firefox窗口
browser.get('http://localhost:8000')  #(3)用它打开本地网页

assert 'Django' in brower.title  #(4)这是测试断言，检查在网页Title中有没有“Django”这个词
