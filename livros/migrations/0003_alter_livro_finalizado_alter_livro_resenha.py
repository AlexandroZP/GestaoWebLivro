# Generated by Django 4.1.7 on 2023-03-11 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0002_rename_livros_livro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='finalizado',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='livro',
            name='resenha',
            field=models.TextField(max_length=450),
        ),
    ]
