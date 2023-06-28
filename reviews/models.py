from django.db import models
from common.models import CommonModel

# 작성자, 날짜, 내용, 좋아요 수
class Review(models.Model):
    like_num = models.PositiveIntegerField()
    # write_date = models.CharField(max_length=50)   # 문자열 데이터다
    # writer = models.CharField(max_length=50)
    content = models.TextField()

    board = models.ForeignKey("boards.Board", on_delete=models.CASCADE)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
