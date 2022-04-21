from django.db import models
import uuid
from src.users.models import User
from django.db.models import JSONField

class Geolocation(models.Model):
   id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
   user_geolocation = JSONField()
   holidays = JSONField()
   
   user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_id_geolocation")
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)