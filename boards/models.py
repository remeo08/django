from django.db import models
from common.models import CommonModel

# 작성자, 사진, 글, 위치, 날짜, 좋아요수, 댓글수
class Board(CommonModel):
    like_num = models.PositiveIntegerField()
    review_num = models.PositiveIntegerField()
    write_date = models.CharField(max_length=50)   # 문자열 데이터다

    writer = models.CharField(max_length=50)
    content = models.TextField()

    # user 데이터가 지워지면 게시글도 없애주세요.
    users = models.ForeignKey("users.User", on_delete=models.CASCADE)

    # user 데이터가 지워주면 게시글은 남겨주세요.
    # users = models.ForeignKey("users.User", on_delete=models.SET_NULL)
