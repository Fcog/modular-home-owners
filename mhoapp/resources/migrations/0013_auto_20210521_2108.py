# Generated by Django 3.1.7 on 2021-05-21 21:08

from django.db import migrations
import mhoapp.theme.blocks.ResourcesCTA
import mhoapp.theme.blocks.ResourcesCards
import mhoapp.theme.blocks.Separator
import wagtail.admin.forms.choosers
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0012_auto_20210521_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resourcepage',
            name='body',
            field=wagtail.core.fields.StreamField([('Separator', mhoapp.theme.blocks.Separator()), ('headingH2', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock())])), ('ResourcesCTA', mhoapp.theme.blocks.ResourcesCTA()), ('PartnersCTA', wagtail.core.blocks.StructBlock([('style', wagtail.core.blocks.ChoiceBlock(choices=[('white', 'White'), ('gray', 'Gray')], icon='view'))])), ('PopularHomesGrid', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('button_text', wagtail.core.blocks.CharBlock()), ('button_link', wagtail.core.blocks.StructBlock([('link_to', wagtail.core.blocks.ChoiceBlock(choices=[('page', 'Page'), ('file', 'File'), ('custom_url', 'Custom URL')], classname='link_choice_type_selector', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(form_classname='page_link', required=False)), ('file', wagtail.documents.blocks.DocumentChooserBlock(form_classname='file_link', required=False)), ('custom_url', wagtail.core.blocks.CharBlock(form_classname='custom_url_link url_field', max_length=300, required=False, validators=[wagtail.admin.forms.choosers.URLOrAbsolutePathValidator()])), ('new_window', wagtail.core.blocks.BooleanBlock(form_classname='new_window_toggle', label='Open in new window', required=False))]))])), ('GetYourHouseCTA', wagtail.core.blocks.StructBlock([('style', wagtail.core.blocks.ChoiceBlock(choices=[('blue', 'Blue'), ('dark-blue', 'Dark Blue')], icon='view'))])), ('articlesCTA', wagtail.core.blocks.StructBlock([('style', wagtail.core.blocks.ChoiceBlock(choices=[('blue', 'Blue'), ('white', 'White')], icon='snippet')), ('add_border', wagtail.core.blocks.BooleanBlock(default=True)), ('introduction', wagtail.core.blocks.RichTextBlock(features=['bold'])), ('column_1_title', wagtail.core.blocks.CharBlock()), ('column_1_article_1', wagtail.core.blocks.PageChooserBlock(page_type=['articles.ArticlePage'])), ('column_1_article_2', wagtail.core.blocks.PageChooserBlock(page_type=['articles.ArticlePage'], required=False)), ('column_1_article_3', wagtail.core.blocks.PageChooserBlock(page_type=['articles.ArticlePage'], required=False)), ('column_1_article_4', wagtail.core.blocks.PageChooserBlock(page_type=['articles.ArticlePage'], required=False)), ('column_2_title', wagtail.core.blocks.CharBlock()), ('column_2_article_1', wagtail.core.blocks.PageChooserBlock(page_type=['articles.ArticlePage'], required=False)), ('column_2_article_2', wagtail.core.blocks.PageChooserBlock(page_type=['articles.ArticlePage'], required=False)), ('column_2_article_3', wagtail.core.blocks.PageChooserBlock(page_type=['articles.ArticlePage'], required=False)), ('column_2_article_4', wagtail.core.blocks.PageChooserBlock(page_type=['articles.ArticlePage'], required=False)), ('button_text', wagtail.core.blocks.CharBlock()), ('button_link', wagtail.core.blocks.StructBlock([('link_to', wagtail.core.blocks.ChoiceBlock(choices=[('page', 'Page'), ('file', 'File'), ('custom_url', 'Custom URL')], classname='link_choice_type_selector', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(form_classname='page_link', required=False)), ('file', wagtail.documents.blocks.DocumentChooserBlock(form_classname='file_link', required=False)), ('custom_url', wagtail.core.blocks.CharBlock(form_classname='custom_url_link url_field', max_length=300, required=False, validators=[wagtail.admin.forms.choosers.URLOrAbsolutePathValidator()])), ('new_window', wagtail.core.blocks.BooleanBlock(form_classname='new_window_toggle', label='Open in new window', required=False))]))])), ('ForumCTA', wagtail.core.blocks.StructBlock([('style', wagtail.core.blocks.ChoiceBlock(choices=[('white', 'White'), ('gray', 'Gray')], icon='view'))])), ('paragraph', wagtail.core.blocks.StructBlock([('text_size', wagtail.core.blocks.ChoiceBlock(choices=[('normal', 'Normal'), ('large', 'Large')], icon='title')), ('paragraph', wagtail.core.blocks.RichTextBlock())])), ('buttons', wagtail.core.blocks.StructBlock([('links', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock()), ('link', wagtail.core.blocks.StructBlock([('link_to', wagtail.core.blocks.ChoiceBlock(choices=[('page', 'Page'), ('file', 'File'), ('custom_url', 'Custom URL')], classname='link_choice_type_selector', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(form_classname='page_link', required=False)), ('file', wagtail.documents.blocks.DocumentChooserBlock(form_classname='file_link', required=False)), ('custom_url', wagtail.core.blocks.CharBlock(form_classname='custom_url_link url_field', max_length=300, required=False, validators=[wagtail.admin.forms.choosers.URLOrAbsolutePathValidator()])), ('new_window', wagtail.core.blocks.BooleanBlock(form_classname='new_window_toggle', label='Open in new window', required=False))]))])))])), ('quote', wagtail.core.blocks.BlockQuoteBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('embed', wagtail.embeds.blocks.EmbedBlock())], default=''),
        ),
        migrations.AlterField(
            model_name='resourcesindexpage',
            name='body',
            field=wagtail.core.fields.StreamField([('Separator', mhoapp.theme.blocks.Separator()), ('headingH2', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock())])), ('ResourcesCards', mhoapp.theme.blocks.ResourcesCards()), ('ResourcesCTA', mhoapp.theme.blocks.ResourcesCTA()), ('PartnersCTA', wagtail.core.blocks.StructBlock([('style', wagtail.core.blocks.ChoiceBlock(choices=[('white', 'White'), ('gray', 'Gray')], icon='view'))])), ('PopularHomesGrid', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('button_text', wagtail.core.blocks.CharBlock()), ('button_link', wagtail.core.blocks.StructBlock([('link_to', wagtail.core.blocks.ChoiceBlock(choices=[('page', 'Page'), ('file', 'File'), ('custom_url', 'Custom URL')], classname='link_choice_type_selector', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(form_classname='page_link', required=False)), ('file', wagtail.documents.blocks.DocumentChooserBlock(form_classname='file_link', required=False)), ('custom_url', wagtail.core.blocks.CharBlock(form_classname='custom_url_link url_field', max_length=300, required=False, validators=[wagtail.admin.forms.choosers.URLOrAbsolutePathValidator()])), ('new_window', wagtail.core.blocks.BooleanBlock(form_classname='new_window_toggle', label='Open in new window', required=False))]))])), ('GetYourHouseCTA', wagtail.core.blocks.StructBlock([('style', wagtail.core.blocks.ChoiceBlock(choices=[('blue', 'Blue'), ('dark-blue', 'Dark Blue')], icon='view'))])), ('articlesCTA', wagtail.core.blocks.StructBlock([('style', wagtail.core.blocks.ChoiceBlock(choices=[('blue', 'Blue'), ('white', 'White')], icon='snippet')), ('add_border', wagtail.core.blocks.BooleanBlock(default=True)), ('introduction', wagtail.core.blocks.RichTextBlock(features=['bold'])), ('column_1_title', wagtail.core.blocks.CharBlock()), ('column_1_article_1', wagtail.core.blocks.PageChooserBlock(page_type=['articles.ArticlePage'])), ('column_1_article_2', wagtail.core.blocks.PageChooserBlock(page_type=['articles.ArticlePage'], required=False)), ('column_1_article_3', wagtail.core.blocks.PageChooserBlock(page_type=['articles.ArticlePage'], required=False)), ('column_1_article_4', wagtail.core.blocks.PageChooserBlock(page_type=['articles.ArticlePage'], required=False)), ('column_2_title', wagtail.core.blocks.CharBlock()), ('column_2_article_1', wagtail.core.blocks.PageChooserBlock(page_type=['articles.ArticlePage'], required=False)), ('column_2_article_2', wagtail.core.blocks.PageChooserBlock(page_type=['articles.ArticlePage'], required=False)), ('column_2_article_3', wagtail.core.blocks.PageChooserBlock(page_type=['articles.ArticlePage'], required=False)), ('column_2_article_4', wagtail.core.blocks.PageChooserBlock(page_type=['articles.ArticlePage'], required=False)), ('button_text', wagtail.core.blocks.CharBlock()), ('button_link', wagtail.core.blocks.StructBlock([('link_to', wagtail.core.blocks.ChoiceBlock(choices=[('page', 'Page'), ('file', 'File'), ('custom_url', 'Custom URL')], classname='link_choice_type_selector', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(form_classname='page_link', required=False)), ('file', wagtail.documents.blocks.DocumentChooserBlock(form_classname='file_link', required=False)), ('custom_url', wagtail.core.blocks.CharBlock(form_classname='custom_url_link url_field', max_length=300, required=False, validators=[wagtail.admin.forms.choosers.URLOrAbsolutePathValidator()])), ('new_window', wagtail.core.blocks.BooleanBlock(form_classname='new_window_toggle', label='Open in new window', required=False))]))])), ('articlesCTAGlobal', wagtail.core.blocks.StructBlock([('style', wagtail.core.blocks.ChoiceBlock(choices=[('blue', 'Blue'), ('white', 'White')], icon='snippet')), ('add_border', wagtail.core.blocks.BooleanBlock(default=True))])), ('ForumCTA', wagtail.core.blocks.StructBlock([('style', wagtail.core.blocks.ChoiceBlock(choices=[('white', 'White'), ('gray', 'Gray')], icon='view'))])), ('paragraph', wagtail.core.blocks.StructBlock([('text_size', wagtail.core.blocks.ChoiceBlock(choices=[('normal', 'Normal'), ('large', 'Large')], icon='title')), ('paragraph', wagtail.core.blocks.RichTextBlock())])), ('buttons', wagtail.core.blocks.StructBlock([('links', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock()), ('link', wagtail.core.blocks.StructBlock([('link_to', wagtail.core.blocks.ChoiceBlock(choices=[('page', 'Page'), ('file', 'File'), ('custom_url', 'Custom URL')], classname='link_choice_type_selector', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(form_classname='page_link', required=False)), ('file', wagtail.documents.blocks.DocumentChooserBlock(form_classname='file_link', required=False)), ('custom_url', wagtail.core.blocks.CharBlock(form_classname='custom_url_link url_field', max_length=300, required=False, validators=[wagtail.admin.forms.choosers.URLOrAbsolutePathValidator()])), ('new_window', wagtail.core.blocks.BooleanBlock(form_classname='new_window_toggle', label='Open in new window', required=False))]))])))])), ('quote', wagtail.core.blocks.BlockQuoteBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('embed', wagtail.embeds.blocks.EmbedBlock())], default=''),
        ),
    ]
