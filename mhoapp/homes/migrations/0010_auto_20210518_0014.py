# Generated by Django 3.1.7 on 2021-05-18 00:14

from django.db import migrations
import wagtail.admin.forms.choosers
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('homes', '0009_auto_20210514_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homesindexpage',
            name='two_cols_content',
            field=wagtail.core.fields.StreamField([('two_columns', wagtail.core.blocks.StructBlock([('column_0', wagtail.core.blocks.StreamBlock([('headingH1', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock())])), ('paragraph', wagtail.core.blocks.StructBlock([('text_size', wagtail.core.blocks.ChoiceBlock(choices=[('normal', 'Normal'), ('large', 'Large')], icon='title')), ('paragraph', wagtail.core.blocks.RichTextBlock())])), ('readMoreText', wagtail.core.blocks.StructBlock([('text_size', wagtail.core.blocks.ChoiceBlock(choices=[('small', 'Small'), ('normal', 'Normal')], icon='title')), ('paragraph', wagtail.core.blocks.RichTextBlock(default=''))])), ('blueBoxCTA', wagtail.core.blocks.StructBlock([('layout', wagtail.core.blocks.ChoiceBlock(choices=[('horizontal', 'Horizontal'), ('vertical', 'Vertical')], icon='title')), ('title', wagtail.core.blocks.RichTextBlock(features=['bold'])), ('text', wagtail.core.blocks.TextBlock()), ('button_text', wagtail.core.blocks.CharBlock()), ('button_link', wagtail.core.blocks.StructBlock([('link_to', wagtail.core.blocks.ChoiceBlock(choices=[('page', 'Page'), ('file', 'File'), ('custom_url', 'Custom URL')], classname='link_choice_type_selector', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(form_classname='page_link', required=False)), ('file', wagtail.documents.blocks.DocumentChooserBlock(form_classname='file_link', required=False)), ('custom_url', wagtail.core.blocks.CharBlock(form_classname='custom_url_link url_field', max_length=300, required=False, validators=[wagtail.admin.forms.choosers.URLOrAbsolutePathValidator()])), ('new_window', wagtail.core.blocks.BooleanBlock(form_classname='new_window_toggle', label='Open in new window', required=False))]))])), ('ArticlesLinksBox', wagtail.core.blocks.StructBlock([('button_text', wagtail.core.blocks.CharBlock(default='Helpful Articles')), ('links', wagtail.core.blocks.ListBlock(wagtail.core.blocks.PageChooserBlock(page_type=['articles.ArticlePage'])))])), ('quote', wagtail.core.blocks.BlockQuoteBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('embed', wagtail.embeds.blocks.EmbedBlock())])), ('column_1', wagtail.core.blocks.StreamBlock([('headingH1', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock())])), ('paragraph', wagtail.core.blocks.StructBlock([('text_size', wagtail.core.blocks.ChoiceBlock(choices=[('normal', 'Normal'), ('large', 'Large')], icon='title')), ('paragraph', wagtail.core.blocks.RichTextBlock())])), ('readMoreText', wagtail.core.blocks.StructBlock([('text_size', wagtail.core.blocks.ChoiceBlock(choices=[('small', 'Small'), ('normal', 'Normal')], icon='title')), ('paragraph', wagtail.core.blocks.RichTextBlock(default=''))])), ('blueBoxCTA', wagtail.core.blocks.StructBlock([('layout', wagtail.core.blocks.ChoiceBlock(choices=[('horizontal', 'Horizontal'), ('vertical', 'Vertical')], icon='title')), ('title', wagtail.core.blocks.RichTextBlock(features=['bold'])), ('text', wagtail.core.blocks.TextBlock()), ('button_text', wagtail.core.blocks.CharBlock()), ('button_link', wagtail.core.blocks.StructBlock([('link_to', wagtail.core.blocks.ChoiceBlock(choices=[('page', 'Page'), ('file', 'File'), ('custom_url', 'Custom URL')], classname='link_choice_type_selector', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(form_classname='page_link', required=False)), ('file', wagtail.documents.blocks.DocumentChooserBlock(form_classname='file_link', required=False)), ('custom_url', wagtail.core.blocks.CharBlock(form_classname='custom_url_link url_field', max_length=300, required=False, validators=[wagtail.admin.forms.choosers.URLOrAbsolutePathValidator()])), ('new_window', wagtail.core.blocks.BooleanBlock(form_classname='new_window_toggle', label='Open in new window', required=False))]))])), ('ArticlesLinksBox', wagtail.core.blocks.StructBlock([('button_text', wagtail.core.blocks.CharBlock(default='Helpful Articles')), ('links', wagtail.core.blocks.ListBlock(wagtail.core.blocks.PageChooserBlock(page_type=['articles.ArticlePage'])))])), ('quote', wagtail.core.blocks.BlockQuoteBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('embed', wagtail.embeds.blocks.EmbedBlock())]))], grid_width=12, group='Columns', template='patterns/organisms/sections/two-cols-equal-width.html'))], blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='homesindexpage',
            name='two_cols_content_shorter',
            field=wagtail.core.fields.StreamField([('two_columns', wagtail.core.blocks.StructBlock([('column_0', wagtail.core.blocks.StreamBlock([('headingH1', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock())])), ('paragraph', wagtail.core.blocks.StructBlock([('text_size', wagtail.core.blocks.ChoiceBlock(choices=[('normal', 'Normal'), ('large', 'Large')], icon='title')), ('paragraph', wagtail.core.blocks.RichTextBlock())])), ('readMoreText', wagtail.core.blocks.StructBlock([('text_size', wagtail.core.blocks.ChoiceBlock(choices=[('small', 'Small'), ('normal', 'Normal')], icon='title')), ('paragraph', wagtail.core.blocks.RichTextBlock(default=''))])), ('blueBoxCTA', wagtail.core.blocks.StructBlock([('layout', wagtail.core.blocks.ChoiceBlock(choices=[('horizontal', 'Horizontal'), ('vertical', 'Vertical')], icon='title')), ('title', wagtail.core.blocks.RichTextBlock(features=['bold'])), ('text', wagtail.core.blocks.TextBlock()), ('button_text', wagtail.core.blocks.CharBlock()), ('button_link', wagtail.core.blocks.StructBlock([('link_to', wagtail.core.blocks.ChoiceBlock(choices=[('page', 'Page'), ('file', 'File'), ('custom_url', 'Custom URL')], classname='link_choice_type_selector', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(form_classname='page_link', required=False)), ('file', wagtail.documents.blocks.DocumentChooserBlock(form_classname='file_link', required=False)), ('custom_url', wagtail.core.blocks.CharBlock(form_classname='custom_url_link url_field', max_length=300, required=False, validators=[wagtail.admin.forms.choosers.URLOrAbsolutePathValidator()])), ('new_window', wagtail.core.blocks.BooleanBlock(form_classname='new_window_toggle', label='Open in new window', required=False))]))])), ('ArticlesLinksBox', wagtail.core.blocks.StructBlock([('button_text', wagtail.core.blocks.CharBlock(default='Helpful Articles')), ('links', wagtail.core.blocks.ListBlock(wagtail.core.blocks.PageChooserBlock(page_type=['articles.ArticlePage'])))])), ('quote', wagtail.core.blocks.BlockQuoteBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('embed', wagtail.embeds.blocks.EmbedBlock())])), ('column_1', wagtail.core.blocks.StreamBlock([('headingH1', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock())])), ('paragraph', wagtail.core.blocks.StructBlock([('text_size', wagtail.core.blocks.ChoiceBlock(choices=[('normal', 'Normal'), ('large', 'Large')], icon='title')), ('paragraph', wagtail.core.blocks.RichTextBlock())])), ('readMoreText', wagtail.core.blocks.StructBlock([('text_size', wagtail.core.blocks.ChoiceBlock(choices=[('small', 'Small'), ('normal', 'Normal')], icon='title')), ('paragraph', wagtail.core.blocks.RichTextBlock(default=''))])), ('blueBoxCTA', wagtail.core.blocks.StructBlock([('layout', wagtail.core.blocks.ChoiceBlock(choices=[('horizontal', 'Horizontal'), ('vertical', 'Vertical')], icon='title')), ('title', wagtail.core.blocks.RichTextBlock(features=['bold'])), ('text', wagtail.core.blocks.TextBlock()), ('button_text', wagtail.core.blocks.CharBlock()), ('button_link', wagtail.core.blocks.StructBlock([('link_to', wagtail.core.blocks.ChoiceBlock(choices=[('page', 'Page'), ('file', 'File'), ('custom_url', 'Custom URL')], classname='link_choice_type_selector', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(form_classname='page_link', required=False)), ('file', wagtail.documents.blocks.DocumentChooserBlock(form_classname='file_link', required=False)), ('custom_url', wagtail.core.blocks.CharBlock(form_classname='custom_url_link url_field', max_length=300, required=False, validators=[wagtail.admin.forms.choosers.URLOrAbsolutePathValidator()])), ('new_window', wagtail.core.blocks.BooleanBlock(form_classname='new_window_toggle', label='Open in new window', required=False))]))])), ('ArticlesLinksBox', wagtail.core.blocks.StructBlock([('button_text', wagtail.core.blocks.CharBlock(default='Helpful Articles')), ('links', wagtail.core.blocks.ListBlock(wagtail.core.blocks.PageChooserBlock(page_type=['articles.ArticlePage'])))])), ('quote', wagtail.core.blocks.BlockQuoteBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('embed', wagtail.embeds.blocks.EmbedBlock())]))], grid_width=12, group='Columns', template='patterns/organisms/sections/two-cols-left-shorter.html'))], blank=True, default=''),
        ),
    ]
