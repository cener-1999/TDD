from selenium import webdriver  
import unittest

class NewVisitorTest(unittest.TestCase): #(1)

    def setUp(self):#(3)
        self.browser = webdriver.Firefox() 

    def tearDown(self):#(3)
        self.browser.quit()
        
    def test_can_start_a_list_and_retrieve_it_later(self):#(2)
        #Edith has heard about a cool new online to-do app.She goes
        #to check out its homepage
        self.browser.get('http://localhost:8000')
        
        #She notices the page title and header mention to-do lists
        self.assertIn('To-Do',self.browser.title)#(4)
        self.fail('Finish the test！')#(5)
        
if __name__ =='__main__': #(6)
    unittest.main(warnings='ignore')#(7)

'''
(1)把测试写成类，它继承unittest.TestCase；
(2)测试的主体是一个名为test_can_start_a_list_and_retrieve_it_later的方法。
以test开头的任何方法都是测试方法，将由测试运行器运行。
每个类可以有多个test方法。我们需要给每个测试方法的起一个描述性名称。
看到名称，就知道测试什么。
(3)setUp和tearDown是在每次测试之前和之后运行的特殊方法。使用它们来启动和停止我们的浏览器 
注意它们有点像try / except，即使在测试期间出现错误，tearDown也会运行。
没有多余的Firefox窗口躺在桌面了
(4)使用self.assertIn代替断言。unittest提供了许多像这样的辅助功能来进行测试，
比如assertEqual，assertTrue，assertFalse等等。您可以在unittest文档中找到更多信息。
(5)self.fail无论如何都会失败，产生错误信息。我们用它作为完成测试的提醒。
(6)if __name__ ==‘__ main__’子句，就相当于是 Python 模拟的程序入口。 
我们调用unittest.main（）方法，它启动unittest测试运行器，
它将自动在文件中寻找测试类和方法并运行它们。
(7)warnings ='ignore’防止了在撰写本文时爆出多余的ResourceWarning信息。
'''
