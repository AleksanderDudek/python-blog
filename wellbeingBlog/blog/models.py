from django.db import models

# Create your models here.

#title (Charfield(max_length))
#text TextField()
#createDate DateField()
#(opcj) image

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    createDate = models.DateField()
    # upload-to - to jest folder w kotrym chce przechowywac zdjecia
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
            return f'{self.createDate} | {self.title}'