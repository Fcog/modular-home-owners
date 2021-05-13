# Generated by Django 3.1.7 on 2021-05-13 00:52

from django.db import migrations, models
import django.db.models.deletion
import mhoapp.partners.models.PartnerTypePage
import mhoapp.theme.blocks.ForumCTA
import mhoapp.theme.blocks.GetYourHouseCTA
import mhoapp.theme.blocks.PartnersCTA
import mhoapp.theme.blocks.ResourcesCTA
import mhoapp.theme.blocks.Separator
import modelcluster.fields
import wagtail.admin.forms.choosers
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0060_fix_workflow_unique_constraint'),
        ('wagtailimages', '0023_add_choose_permissions'),
        ('wagtailsvg', '0002_svg_edit_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocationCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(default='', max_length=2)),
            ],
            options={
                'verbose_name_plural': 'locations of partners',
            },
        ),
        migrations.CreateModel(
            name='PartnersIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='PartnerTypePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('heading', wagtail.core.fields.StreamField([('two_columns', wagtail.core.blocks.StructBlock([('column_0', wagtail.core.blocks.StreamBlock([('headingH1', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock())])), ('paragraph', wagtail.core.blocks.StructBlock([('text_size', wagtail.core.blocks.ChoiceBlock(choices=[('small', 'Small'), ('normal', 'Normal')], icon='title')), ('paragraph', wagtail.core.blocks.RichTextBlock())])), ('readMoreText', wagtail.core.blocks.StructBlock([('text_size', wagtail.core.blocks.ChoiceBlock(choices=[('small', 'Small'), ('normal', 'Normal')], icon='title')), ('paragraph', wagtail.core.blocks.RichTextBlock(default=''))])), ('blueBoxCTA', wagtail.core.blocks.StructBlock([('layout', wagtail.core.blocks.ChoiceBlock(choices=[('horizontal', 'Horizontal'), ('vertical', 'Vertical')], icon='title')), ('title', wagtail.core.blocks.RichTextBlock(features=['bold'])), ('text', wagtail.core.blocks.TextBlock()), ('button_text', wagtail.core.blocks.CharBlock()), ('button_link', wagtail.core.blocks.StructBlock([('link_to', wagtail.core.blocks.ChoiceBlock(choices=[('page', 'Page'), ('file', 'File'), ('custom_url', 'Custom URL')], classname='link_choice_type_selector', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(form_classname='page_link', required=False)), ('file', wagtail.documents.blocks.DocumentChooserBlock(form_classname='file_link', required=False)), ('custom_url', wagtail.core.blocks.CharBlock(form_classname='custom_url_link url_field', max_length=300, required=False, validators=[wagtail.admin.forms.choosers.URLOrAbsolutePathValidator()])), ('new_window', wagtail.core.blocks.BooleanBlock(form_classname='new_window_toggle', label='Open in new window', required=False))]))])), ('quote', wagtail.core.blocks.BlockQuoteBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('embed', wagtail.embeds.blocks.EmbedBlock())])), ('column_1', wagtail.core.blocks.StreamBlock([('headingH1', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock())])), ('paragraph', wagtail.core.blocks.StructBlock([('text_size', wagtail.core.blocks.ChoiceBlock(choices=[('small', 'Small'), ('normal', 'Normal')], icon='title')), ('paragraph', wagtail.core.blocks.RichTextBlock())])), ('readMoreText', wagtail.core.blocks.StructBlock([('text_size', wagtail.core.blocks.ChoiceBlock(choices=[('small', 'Small'), ('normal', 'Normal')], icon='title')), ('paragraph', wagtail.core.blocks.RichTextBlock(default=''))])), ('blueBoxCTA', wagtail.core.blocks.StructBlock([('layout', wagtail.core.blocks.ChoiceBlock(choices=[('horizontal', 'Horizontal'), ('vertical', 'Vertical')], icon='title')), ('title', wagtail.core.blocks.RichTextBlock(features=['bold'])), ('text', wagtail.core.blocks.TextBlock()), ('button_text', wagtail.core.blocks.CharBlock()), ('button_link', wagtail.core.blocks.StructBlock([('link_to', wagtail.core.blocks.ChoiceBlock(choices=[('page', 'Page'), ('file', 'File'), ('custom_url', 'Custom URL')], classname='link_choice_type_selector', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(form_classname='page_link', required=False)), ('file', wagtail.documents.blocks.DocumentChooserBlock(form_classname='file_link', required=False)), ('custom_url', wagtail.core.blocks.CharBlock(form_classname='custom_url_link url_field', max_length=300, required=False, validators=[wagtail.admin.forms.choosers.URLOrAbsolutePathValidator()])), ('new_window', wagtail.core.blocks.BooleanBlock(form_classname='new_window_toggle', label='Open in new window', required=False))]))])), ('quote', wagtail.core.blocks.BlockQuoteBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('embed', wagtail.embeds.blocks.EmbedBlock())]))], grid_width=12, group='Columns', template='patterns/organisms/sections/two-cols.html'))], default='')),
                ('body', wagtail.core.fields.StreamField([('Separator', mhoapp.theme.blocks.Separator()), ('headingH1', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock())])), ('headingH2', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.RichTextBlock())])), ('PartnerTypeGrid', wagtail.core.blocks.ChoiceBlock(choices=mhoapp.partners.models.get_partner_types)), ('ResourcesCTA', mhoapp.theme.blocks.ResourcesCTA()), ('PartnersCTA', mhoapp.theme.blocks.PartnersCTA()), ('PopularHomesGrid', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('button_text', wagtail.core.blocks.CharBlock()), ('button_link', wagtail.core.blocks.StructBlock([('link_to', wagtail.core.blocks.ChoiceBlock(choices=[('page', 'Page'), ('file', 'File'), ('custom_url', 'Custom URL')], classname='link_choice_type_selector', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(form_classname='page_link', required=False)), ('file', wagtail.documents.blocks.DocumentChooserBlock(form_classname='file_link', required=False)), ('custom_url', wagtail.core.blocks.CharBlock(form_classname='custom_url_link url_field', max_length=300, required=False, validators=[wagtail.admin.forms.choosers.URLOrAbsolutePathValidator()])), ('new_window', wagtail.core.blocks.BooleanBlock(form_classname='new_window_toggle', label='Open in new window', required=False))]))])), ('GetYourHouseCTA', mhoapp.theme.blocks.GetYourHouseCTA()), ('articlesCTA', wagtail.core.blocks.StructBlock([('introduction', wagtail.core.blocks.RichTextBlock(features=['bold'])), ('column_1_title', wagtail.core.blocks.CharBlock()), ('column_1_article_1', wagtail.core.blocks.PageChooserBlock(page_type=['articles.ArticlePage'])), ('column_1_article_2', wagtail.core.blocks.PageChooserBlock(page_type=['articles.ArticlePage'], required=False)), ('column_1_article_3', wagtail.core.blocks.PageChooserBlock(page_type=['articles.ArticlePage'], required=False)), ('column_1_article_4', wagtail.core.blocks.PageChooserBlock(page_type=['articles.ArticlePage'], required=False)), ('column_2_title', wagtail.core.blocks.CharBlock()), ('column_2_article_1', wagtail.core.blocks.PageChooserBlock(page_type=['articles.ArticlePage'], required=False)), ('column_2_article_2', wagtail.core.blocks.PageChooserBlock(page_type=['articles.ArticlePage'], required=False)), ('column_2_article_3', wagtail.core.blocks.PageChooserBlock(page_type=['articles.ArticlePage'], required=False)), ('column_2_article_4', wagtail.core.blocks.PageChooserBlock(page_type=['articles.ArticlePage'], required=False)), ('button_text', wagtail.core.blocks.CharBlock()), ('button_link', wagtail.core.blocks.StructBlock([('link_to', wagtail.core.blocks.ChoiceBlock(choices=[('page', 'Page'), ('file', 'File'), ('custom_url', 'Custom URL')], classname='link_choice_type_selector', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(form_classname='page_link', required=False)), ('file', wagtail.documents.blocks.DocumentChooserBlock(form_classname='file_link', required=False)), ('custom_url', wagtail.core.blocks.CharBlock(form_classname='custom_url_link url_field', max_length=300, required=False, validators=[wagtail.admin.forms.choosers.URLOrAbsolutePathValidator()])), ('new_window', wagtail.core.blocks.BooleanBlock(form_classname='new_window_toggle', label='Open in new window', required=False))]))])), ('ForumCTA', mhoapp.theme.blocks.ForumCTA()), ('hero', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock()), ('introduction', wagtail.core.blocks.CharBlock()), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('search_button_text', wagtail.core.blocks.CharBlock(default='Search Homes')), ('filter_bar_text', wagtail.core.blocks.CharBlock(default=''))])), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('text', wagtail.core.blocks.TextBlock()), ('quote', wagtail.core.blocks.BlockQuoteBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('embed', wagtail.embeds.blocks.EmbedBlock())], default='')),
                ('icon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailsvg.svg')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='PartnerPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('phone', models.TextField(max_length=25)),
                ('website', models.URLField()),
                ('locations', modelcluster.fields.ParentalManyToManyField(to='partners.LocationCategory')),
                ('logo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('main_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='PartnerGalleryImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('caption', models.CharField(blank=True, max_length=250)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailimages.image')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery_images', to='partners.partnerpage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
