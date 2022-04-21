import uuid
from django.db import models
from src.users.models import User

class Posts(models.Model):
   id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
   title = models.CharField(max_length=64, blank=True, null=True)
   description = models.TextField(blank=True, null=True)
   
   user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_id")
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)
   
   def liked_count(self):
      return None
   
   def unliked_count(self):
      return None
