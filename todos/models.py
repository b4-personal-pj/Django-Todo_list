from django.db import models
from users.models import User
from django.utils import timezone

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    is_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completion_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.title)
    
    # is_complete가 True가 되는 시점의 시간을 completion_at에 업데이트하기위한 메소드. Model클래스의 save메소드를 오버라이딩 하고있음! 
    def save(self, *args, **kwargs):
        if self.is_complete and not self.completion_at:
            self.completion_at = timezone.now()
        elif not self.is_complete and self.completion_at:
            self.completion_at = None
        super(Todo, self). save(*args, **kwargs)