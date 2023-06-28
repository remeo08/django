from django.db import models
from common.models import CommonModel

# receiver_id, content, reply, is_view, is_view_num, send_time
class Chatting(models.Model):
    receiver_id = models.CharField(max_length=30)
    content = models.TextField()
    reply = models.TextField()
    is_view = models.BooleanField()
    is_view_num = models.PositiveIntegerField()
    send_time = models.TimeField()