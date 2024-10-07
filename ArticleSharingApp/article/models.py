from django.db import models

class Articles(models.Model):
    article_no = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')
    publisher_name = models.CharField(max_length=100)
    def __str__(self):
        return self.title
