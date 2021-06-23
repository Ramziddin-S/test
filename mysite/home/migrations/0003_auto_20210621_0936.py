# Generated by Django 3.2.3 on 2021-06-21 04:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uz', models.CharField(max_length=128)),
                ('en', models.CharField(max_length=128)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameField(
            model_name='follower',
            old_name='comment',
            new_name='en_comment',
        ),
        migrations.RenameField(
            model_name='follower',
            old_name='full_name',
            new_name='en_full_name',
        ),
        migrations.RenameField(
            model_name='icon',
            old_name='comment',
            new_name='en_comment',
        ),
        migrations.RenameField(
            model_name='icon',
            old_name='title',
            new_name='uz_title',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='description',
            new_name='en_description',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='en_title',
        ),
        migrations.AddField(
            model_name='follower',
            name='uz_comment',
            field=models.TextField(default=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='follower',
            name='uz_full_name',
            field=models.CharField(default=11, max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='icon',
            name='en_title',
            field=models.CharField(default=11, max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='icon',
            name='uz_comment',
            field=models.TextField(default=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='uz_description',
            field=models.TextField(default=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='uz_title',
            field=models.CharField(default=11, max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='follower',
            name='language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.language'),
        ),
        migrations.AddField(
            model_name='icon',
            name='language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.language'),
        ),
        migrations.AddField(
            model_name='post',
            name='language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.language'),
        ),
    ]