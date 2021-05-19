# Generated by Django 3.1.7 on 2021-05-19 15:30

from django.db import migrations
import mhoapp.theme.blocks.Separator
import wagtail.admin.forms.choosers
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_auto_20210518_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepage',
            name='body',
            field=wagtail.core.fields.StreamField([('separator', mhoapp.theme.blocks.Separator()), ('headingH2', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock())])), ('paragraph', wagtail.core.blocks.StructBlock([('text_size', wagtail.core.blocks.ChoiceBlock(choices=[('normal', 'Normal'), ('large', 'Large')], icon='title')), ('paragraph', wagtail.core.blocks.RichTextBlock())])), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.core.blocks.TextBlock(default=''))])), ('buttons', wagtail.core.blocks.StructBlock([('links', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock()), ('link', wagtail.core.blocks.StructBlock([('link_to', wagtail.core.blocks.ChoiceBlock(choices=[('page', 'Page'), ('file', 'File'), ('custom_url', 'Custom URL')], classname='link_choice_type_selector', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(form_classname='page_link', required=False)), ('file', wagtail.documents.blocks.DocumentChooserBlock(form_classname='file_link', required=False)), ('custom_url', wagtail.core.blocks.CharBlock(form_classname='custom_url_link url_field', max_length=300, required=False, validators=[wagtail.admin.forms.choosers.URLOrAbsolutePathValidator()])), ('new_window', wagtail.core.blocks.BooleanBlock(form_classname='new_window_toggle', label='Open in new window', required=False))]))])))])), ('quote', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.RichTextBlock(required=True))])), ('quote2', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=True)), ('text', wagtail.core.blocks.RichTextBlock(required=True))])), ('embed', wagtail.embeds.blocks.EmbedBlock())], default=''),
        ),
    ]
