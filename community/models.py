from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image= models.ImageField(upload_to='community/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to='community/files/%Y/%m/%d/', blank=True)
    published_date = models.DateTimeField(blank=True, null=True)
    # <Post객체>.publish 입력시, 해당 객체의 published_date에 현재시간을 넣어주는 함수

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/community/{self.pk}'