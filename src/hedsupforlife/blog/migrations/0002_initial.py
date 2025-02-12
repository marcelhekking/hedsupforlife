# Generated by Django 5.0.9 on 2025-02-11 09:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0001_initial'),
        ('images', '0001_initial'),
        ('utils', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlepage',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='utils.authorsnippet'),
        ),
        migrations.AddField(
            model_name='articlepage',
            name='listing_image',
            field=models.ForeignKey(blank=True, help_text='Choose the image you wish to be displayed when this page appears in listings', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='images.customimage'),
        ),
        migrations.AddField(
            model_name='articlepage',
            name='social_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='images.customimage'),
        ),
        migrations.AddField(
            model_name='articlepage',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='article_pages', to='utils.articletopic'),
        ),
        migrations.AddField(
            model_name='bloglistingpage',
            name='listing_image',
            field=models.ForeignKey(blank=True, help_text='Choose the image you wish to be displayed when this page appears in listings', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='images.customimage'),
        ),
        migrations.AddField(
            model_name='bloglistingpage',
            name='social_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='images.customimage'),
        ),
    ]
