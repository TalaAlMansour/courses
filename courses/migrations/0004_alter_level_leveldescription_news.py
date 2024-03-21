# Generated by Django 5.0.3 on 2024-03-14 12:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_level_created_at_level_update_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='levelDescription',
            field=models.TextField(),
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_title', models.CharField(max_length=100)),
                ('news_desc', models.TextField()),
                ('news_date', models.DateField(auto_now_add=True, null=True)),
                ('lessonsNum', models.IntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
            ],
        ),
    ]
