from django.test import TestCase
#from django.urls import reverse


#test case for testing that the view rendering the index page works without errors
class viewsTestCase(TestCase):
    def test_index_loads_properly(self): # that uses the Django test client to visit the index page of the website (http://your_server_ip:8000,
        """The index page loads properly"""
        response = self.client.get(' your_server_ip:8000')
        self.assertEqual(response.status_code,404)  #checks whether the response has a status code of 200, which means the page responded without any errors
                                                    # result you can be sure that when the user visits, it will respond without errors too.

#added to test
class PostListViewTest(TestCase):
    def test_view_url_exists_at_desired_location(self):

        response = self.client.get('/blog/')
        self.assertEqual(response.status_code,200)
