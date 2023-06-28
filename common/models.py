from django.db import models

# Create your models here.
class CommonModel(models.Model):

    # auto_now_add : 객체가 생성되는 시간을 기준
    created = models.DateTimeField(auto_now_add=True)
    
    # auto_now : 객체가 업데이트되는 시간을 기준
    updated = models.DateTimeField(auto_now=True)

    # 위 모델을 추상화(기능을 추가)하겠다.
    # (모델로 사용하는 것이 아니라 다른 모델(객체)에서 활용이 가능하게끔 한다.)
    class Meta:
        abstract = True