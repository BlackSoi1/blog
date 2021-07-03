from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.


class Post(models.Model):
    # author connect the superuser of the website
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(aprroved_comment=True)

    # Once create the instance of Post what should I do
    # pk primary key
    # go to post_detail page
    def get_absolute_url(self):
        return reverse("post_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.title
    def testMethod(self):
        return 1+1

class Comment(models.Model):
    post = models.ForeignKey('blog.post', related_name='comments')
    # this author can be anyone
    author = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    # Should match with approve_comments()
    approve_comment = models.BooleanFiled(default=False)

    def approve(self):
        self.approve_comment=True
        self.save()

    # go back to main home page to all post lists
    def get_absolute_url(self):
        return reverse('post_list')

    def __str__(self):
        return self.text
