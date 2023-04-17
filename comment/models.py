from django.db import models
from user.models import UserModel
from posting.models import Posting


class Comment(models.Model):
    class Meta:
        db_table = 'comments'
    comment_id = models.IntegerField(primary_key=True)
    username = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    posting = models.ForeignKey(Posting, on_delete=models.CASCADE, null=True)
    update_at = models.DateField(auto_now=True)
    create_at = models.DateTimeField(auto_now_add=True)
    comment_content = models.TextField(null=True)
    
    def save(self, *args, **kwargs):
        if not self.pk:
            # 새로운 게시물인 경우
            latest_comment = Comment.objects.order_by('-comment_id').first()
            self.comment_id = latest_comment.comment_id + 1 if latest_comment else 1

        super().save(*args, **kwargs)
