from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_data = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
    def pub_date_pretty(self):
        return self.pub_data.strftime('%b %e %Y')
    def summary(self):
        return self.body[:100]
