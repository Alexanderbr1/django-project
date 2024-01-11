from django.core.management.base import BaseCommand

from news.models import Post


class Command(BaseCommand):
    help = 'Displays all posts in the console'

    def handle(self, *args, **options):
        posts = Post.objects.all()
        for post in posts:
            self.stdout.write(self.style.SUCCESS(f'Title: {post.title}, Author: {post.author}, Date: {post.date}'))
