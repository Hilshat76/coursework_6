# Generated by Django 5.1.1 on 2024-09-24 13:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Client",
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
                ("first_name", models.CharField(max_length=50, verbose_name="Имя")),
                ("last_name", models.CharField(max_length=50, verbose_name="Фамилия")),
                (
                    "third_name",
                    models.CharField(
                        blank=True, max_length=50, verbose_name="Отчество"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="Электронной почты"
                    ),
                ),
                ("comment", models.TextField(blank=True, verbose_name="Комментарий")),
                ("is_active", models.BooleanField(default=False)),
            ],
            options={
                "verbose_name": "Клиент",
                "verbose_name_plural": "Клиенты",
            },
        ),
        migrations.CreateModel(
            name="Message",
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
                (
                    "title",
                    models.CharField(max_length=100, verbose_name="Тема сообщения"),
                ),
                ("message", models.TextField(verbose_name="Сообщение")),
                (
                    "created_at",
                    models.DateField(auto_now_add=True, verbose_name="Дата создания"),
                ),
            ],
            options={
                "verbose_name": "Сообщение",
                "verbose_name_plural": "Сообщения",
            },
        ),
        migrations.CreateModel(
            name="Mailing",
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
                (
                    "title",
                    models.CharField(max_length=100, verbose_name="Название рассылки"),
                ),
                (
                    "created_at",
                    models.DateField(auto_now_add=True, verbose_name="Дата создания"),
                ),
                (
                    "at_start",
                    models.DateTimeField(verbose_name="Дата и время начала отправки"),
                ),
                (
                    "at_end",
                    models.DateTimeField(
                        verbose_name="Дата и время окончания отправки"
                    ),
                ),
                (
                    "periodicity",
                    models.CharField(
                        choices=[
                            ("once", "Однократно"),
                            ("daily", "Ежедневно"),
                            ("weekly", "Еженедельно"),
                            ("monthly", "Ежемесячно"),
                            ("yearly", "Ежегодно"),
                        ],
                        max_length=20,
                        verbose_name="Периодичность",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("create", "Создана"),
                            ("launched", "Запущена"),
                            ("completed", "Завершена"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "clients",
                    models.ManyToManyField(
                        blank=True, to="mailing.client", verbose_name="Список клиентов"
                    ),
                ),
                (
                    "message",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mailing.message",
                        verbose_name="Сообщение",
                    ),
                ),
            ],
            options={
                "verbose_name": "Рассылка",
                "verbose_name_plural": "Рассылки",
            },
        ),
        migrations.CreateModel(
            name="Attempt",
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
                (
                    "at_last_attempt",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата последней попытки"
                    ),
                ),
                (
                    "status_attempt",
                    models.BooleanField(default=False, verbose_name="Статус попытки"),
                ),
                (
                    "answer_mail",
                    models.TextField(
                        blank=True, verbose_name="Ответ почтового сервера"
                    ),
                ),
                (
                    "mailing",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mailing.mailing",
                        verbose_name="Рассылка",
                    ),
                ),
            ],
            options={
                "verbose_name": "Попытка",
                "verbose_name_plural": "Попытки",
            },
        ),
    ]