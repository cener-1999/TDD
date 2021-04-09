from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from lists.views import home_page 

# Create your tests here.

class HomePageTest(TestCase):
    
    def test_root_url_resolve_to_home_page_view(self):
        found = resolve('/') 
        self.assertEqual(found.func,home_page) 
        
    def test_home_page_returns_correct_html(self):
        request =HttpRequest() #1
        response = home_page(request) #2
        html = response.content.decode('utf8')#3
        self.assertTrue(html.startswith('<html>'))#4
        self.assertIn('<title>To-Do list</title>',html)#5
        self.assertTrue(html.endswith('</html>'))#4


'''
这些代码干了些什么？ (第一版) 
resolve是Django用来解析URL的function，找到URL应该映射到哪个view。 
我们测试这个解析，当用“/”调用时，网站的根目录应该找到一个名为home_page的function。
'''
