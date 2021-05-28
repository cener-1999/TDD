from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest, response
from django.template.loader import render_to_string
from urllib3.packages.six import assertCountEqual
from lists.views import home_page 
from lists.models import Item

# Create your tests here.

class HomePageTest(TestCase):
    
    '''
    def test_root_url_resolve_to_home_page_view(self):
        found = resolve('/') 
        self.assertEqual(found.func,home_page) 
    '''    
    '''
    def test_home_page_returns_correct_html(self):
        request =HttpRequest() #1
        response = home_page(request) #2
        html = response.content.decode('utf8')#3
        self.assertTrue(html.startswith('<html>'))#4
        self.assertIn('<title>To-Do lists</title>',html)#5
        self.assertTrue(html.endswith('</html>'))#4
        expected_html =render_to_string('home.html')
        self.assertEqual(html.expected_html)
    '''
    
    def test_uses_home_template(self):
        response=self.client.get('/')
        self.assertTemplateUsed(response,'home.html')
       
    '''   
    def test_can_save_a_POST_request(self):
        response = self.client.post('/',data={'item_text':'A new list item'})
        
        self.assertEqual(Item.objects.count(),1)
        new_item=Item.objects.first()
        self.assertEqual(new_item.text,'A new list item')
       
    def test_redirects_after_POST(self):
        response = self.client.post('/',data={'item_text':'A new list item'})
        self.assertEqual(response.status_code,302)
        self.assertEqual(response['location'],'')
       
    '''
        
    '''
    def test_home_page_returns_correct_html(self):
        response =self.client.get('/')#1
        html =response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>',html)
        self.assertTrue(html.strip().endswith('</html>'))
        
        self.assertTemplateUsed(response,'home.html')
    '''
    
    def test_only_saves_items_when_necessary(self):
        self.client.get('/')
        self.assertEqual(Item.objects.count(),0)
    
        
'''
这些代码干了些什么？ (第一版) 
resolve是Django用来解析URL的function，找到URL应该映射到哪个view。 
我们测试这个解析，当用“/”调用时，网站的根目录应该找到一个名为home_page的function。
'''

class ItemModelTest(TestCase):
    
    def test_saving_and_retrieving_items(self):
        first_item =Item()
        first_item.text='The first (ever) list item'
        first_item.save()
        
        second_item=Item()
        second_item.text='Item the second'
        second_item.save()
        
        saved_items=Item.objects.all()
        self.assertEqual(saved_items.count(),2)
        
        first_saved_item=saved_items[0]
        second_saved_item=saved_items[1]
        self.assertEqual(first_saved_item.text,'The first (ever) list item')
        self.assertEqual(second_saved_item.text,'Item the second')
    
    def test_can_save_a_POST_request(self):
        response = self.client.post('/',data={'item_text':'A new list item'})
        
        self.assertEqual(Item.objects.count(),1)
        new_item=Item.objects.first()
        self.assertEqual(new_item.text,'A new list item')
       
    def test_redirects_after_POST(self):
        response = self.client.post('/',data={'item_text':'A new list item'})
        self.assertEqual(response.status_code,302)
        self.assertEqual(response['location'],'/lists/the-only-list-in-the-world')

class ListViewTest(TestCase):

    def test_uses_lists_template(self):
        response = self.client.get('/lists/the-only-list-in-the-world/')
        self.assertTemplateUsed(response,'list.html')

    def test_displays_all_items(self):
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')

        response = self.client.get('/lists/the-only-list-in-the-world/')

        self.assertContains(response,'itemey 1')
        self.assertContains(response,'itemey 2')