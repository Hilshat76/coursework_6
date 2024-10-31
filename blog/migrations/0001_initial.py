# Generated by Django 4.2 on 2024-10-31 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=50, verbose_name="Заголовок")),
                ("content", models.TextField(verbose_name="Статья")),
                (
                    "preview",
                    models.ImageField(
                        blank=True, upload_to="blog/post_preview", verbose_name="Превью"
                    ),
                ),
                (
                    "created_at",
                    models.DateField(auto_now_add=True, verbose_name="Дата публикации"),
                ),
                (
                    "number_of_views",
                    models.PositiveIntegerField(
                        default=0, verbose_name="Количество просмотров"
                    ),
                ),
                (
                    "is_published",
                    models.BooleanField(
                        default=False, verbose_name="Добавить к избранным"
                    ),
                ),
            ],
            options={
                "verbose_name": "Статья",
                "verbose_name_plural": "Статьи",
            },
        ),
    ]
