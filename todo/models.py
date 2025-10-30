from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



from django.db import models
from .signals import user_registered

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Fire signal after saving user
        user_registered.send(sender=self.__class__, instance=self)
        print(f"✅ {self.name} saved successfully.")


class ActivityLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.name} — {self.action} @ {self.created_at:%Y-%m-%d %H:%M}"



