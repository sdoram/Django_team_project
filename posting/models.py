from django.db import models
from user.models import UserModel

class Posting(models.Model):
    username = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    post_id = models.ForeignKey('self', on_delete=models.CASCADE)
    main_content = models.TextField(null=True)
    create_at = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=256)
    update_at = models.DateField(auto_now=True)
    categories = (
        ('codereview', '코드리뷰'),
        ('course', '취업진로'),
        ('coding_study', '개발공부'),
        ('study', '스터디'),
        ('free_board', '잡담'),
    )
    category = models.CharField(choices=categories, max_length=256)

    def __str__(self):
        return self.title
