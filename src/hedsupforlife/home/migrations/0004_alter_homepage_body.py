# Generated by Django 5.0.9 on 2025-03-20 13:14

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_homepage_team_member_alter_homepage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.fields.StreamField([('section', 3), ('cta', 13), ('statistics', 17), ('members', 20)], block_lookup={0: ('wagtail.blocks.CharBlock', (), {'form_classname': 'title', 'icon': 'title', 'template': 'components/streamfield/blocks/heading2_block.html'}), 1: ('wagtail.blocks.RichTextBlock', (), {'features': ['bold', 'italic', 'link', 'ol', 'ul', 'h3'], 'template': 'components/streamfield/blocks/paragraph_block.html'}), 2: ('wagtail.blocks.StreamBlock', [[('paragraph', 1)]], {}), 3: ('wagtail.blocks.StructBlock', [[('heading', 0), ('content', 2)]], {}), 4: ('wagtail.blocks.CharBlock', (), {'form_classname': 'title', 'icon': 'title', 'required': True}), 5: ('wagtail.blocks.PageChooserBlock', (), {}), 6: ('wagtail.blocks.CharBlock', (), {'help_text': "Leave blank to use page's listing title.", 'required': False}), 7: ('wagtail.blocks.StructBlock', [[('page', 5), ('title', 6)]], {}), 8: ('wagtail.blocks.URLBlock', (), {}), 9: ('wagtail.blocks.CharBlock', (), {}), 10: ('wagtail.blocks.StructBlock', [[('link', 8), ('title', 9)]], {}), 11: ('wagtail.blocks.StreamBlock', [[('internal', 7), ('external', 10)]], {}), 12: ('wagtail.blocks.TextBlock', (), {'required': False}), 13: ('wagtail.blocks.StructBlock', [[('heading', 4), ('link', 11), ('description', 12)]], {}), 14: ('wagtail.blocks.BooleanBlock', (), {'help_text': 'If checked, the heading will be hidden from view', 'label': 'Screen reader only label', 'required': False}), 15: ('wagtail.snippets.blocks.SnippetChooserBlock', ('utils.Statistic',), {}), 16: ('wagtail.blocks.ListBlock', (15,), {'max_num': 3, 'min_num': 3}), 17: ('wagtail.blocks.StructBlock', [[('heading', 4), ('sr_only_label', 14), ('statistics', 16)]], {}), 18: ('wagtail.snippets.blocks.SnippetChooserBlock', ('utils.MemberSnippet',), {}), 19: ('wagtail.blocks.ListBlock', (18,), {'max_num': 5, 'min_num': 5}), 20: ('wagtail.blocks.StructBlock', [[('heading', 4), ('sr_only_label', 14), ('members', 19)]], {})}),
        ),
    ]
