# Generated by Django 4.2 on 2023-04-14 17:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posting', '0002_remove_posting_id_alter_posting_main_content_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posting',
            name='username',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='postings', to=settings.AUTH_USER_MODEL),
        ),
    ]