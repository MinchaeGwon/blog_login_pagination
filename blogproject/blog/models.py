from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    image = models.ImageField(upload_to='images/') #이미지를 추가할 수 있도록 필드를 만듦
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]
