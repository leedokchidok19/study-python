from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    contents = models.TextField()
    img = models.ImageField() # pillow를 설치해야 사용할 수 있다. - pip install pillow
    dataCreat = models.DateTimeField()
    category = models.CharField(max_length=20)
    
    def __str__(self): # Post Objet를 제목으로 바꾼다.
        return self.title
