from django.test import TestCase, Client
from .models import Post, Comments, Likes

class PostTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.post = Post.objects.create(
            title='Test Post',
            description='This is a test post',
            author='Test Author',
            date='2023-06-28',
            img='image/2023/test_image.jpg'
        )



    def test_post_detail_view(self):
        response = self.client.get(f'/{self.post.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'news/news_detail.html')
        self.assertEqual(response.context['post'], self.post)




