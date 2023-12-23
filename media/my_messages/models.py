from django.db import models
from django.contrib.auth.models import User
from main.models import profile
class Chat(models.Model):
    user1 = models.ForeignKey(profile, on_delete=models.CASCADE, related_name='user1_chats')
    user2 = models.ForeignKey(profile, on_delete=models.CASCADE, related_name='user2_chats')
    
    def __str__(self):
        return f"Chat between {self.user1.username} and {self.user2.username}"

class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(profile, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.username}: {self.content}"

