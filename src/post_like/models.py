import uuid
from django.db import models
from src.users.models import User
from src.posts.models import Posts

# Create your models here.
class PostLike(models.Model):
   id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
   liked = models.BooleanField(default=False) # True as like and False as unlike
   
   post_id = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name="post_id")
   liked_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="liked_by")
   created_at = models.DateTimeField(auto_now_add=True)
