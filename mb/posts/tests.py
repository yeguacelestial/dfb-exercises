from django.test import TestCase
from django.urls import reverse  # new

from .models import Post


# Create your tests here.

class PostModelTest(TestCase):

    def setUp(self):
        Post.objects.create(text="Just a test")

    # The tests should start with 'test_'
    def test_text_content(self):
        post = Post.objects.get(id=1)  # Django assigns IDs automatically
        expected_object_name = f'{post.text}'

        self.assertEqual(expected_object_name, 'Just a test')


class HomePageViewTest(TestCase):

    # Functions with 'test_' as prefix are helper functions
    def setUp(self):
        Post.objects.create(text='this is another test')

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')
