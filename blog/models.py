from datetime import datetime
from django.db import models

class Blogs(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField(blank=True,  max_length=500)
    blog_img = models.ImageField(upload_to ='photos/%Y/%m/%d/', blank=True)
    date_posted = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return self.title

class Comment(models.Model):
    name = models.CharField(max_length=255)
    post_id = models.ForeignKey(Blogs,on_delete=(models.CASCADE))
    email = models.EmailField()
    message = models.TextField('Message')
    date_comment = models.DateTimeField(default=datetime.now, blank=False)