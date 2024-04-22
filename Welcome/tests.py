from django.test import SimpleTestCase
from django.urls import reverse
# Create your tests here.
class WelcomeTest(SimpleTestCase):

    #Test the url
    def test_url(self):
        response = self.client.get("/welcome/")
        self.assertEqual(response.status_code,200)

    #Test the url by name
    def test_ur_byname(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code,200)

    #Test by Template Name
    def test_template_name(self):
        response = self.client.get("/welcome/")
        self.assertTemplateUsed(response,'home.html')

    #Test template Contents
    def test_template_content(self):
        response = self.client.get("/welcome/")
        self.assertContains(response,"<h2>Home Page of Website</h2>")