# Generated by Django 3.1.7 on 2021-05-13 00:52

from django.db import migrations, models
import django.db.models.deletion
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
    ]

    operations = [
        migrations.CreateModel(
            name='ElevationGalleryImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('caption', models.CharField(blank=True, max_length=250)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FloorplanGalleryImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('caption', models.CharField(blank=True, max_length=250)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('code', models.TextField(max_length=255)),
                ('verified', models.BooleanField(default=False)),
                ('sqft', models.PositiveSmallIntegerField()),
                ('bedrooms', models.PositiveSmallIntegerField()),
                ('baths', models.FloatField()),
                ('stories', models.FloatField()),
                ('cost', models.PositiveIntegerField()),
                ('estimated_cost', models.PositiveIntegerField()),
                ('link', models.URLField(blank=True)),
                ('floorplans_link', models.URLField(blank=True)),
                ('info', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='HomesIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('layout', models.CharField(choices=[('FW', '1 Column - Full width'), ('LS', '2 Columns - Left side smaller'), ('EW', '2 Columns - Equal width')], default='FW', max_length=2, verbose_name='Heading layout')),
                ('left_content', wagtail.core.fields.StreamField([('partnersButtons', wagtail.core.blocks.ChoiceBlock(choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District Of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming'), ('AB', 'Alberta'), ('BC', 'British Columbia'), ('MB', 'Manitoba'), ('NB', 'New Brunswick'), ('NL', 'Newfoundland and Labrador'), ('NS', 'Nova Scotia'), ('NT', 'Northwest Territories'), ('NU', 'Nunavut'), ('ON', 'Ontario'), ('PE', 'Prince Edward Island'), ('QC', 'Quebec'), ('SK', 'Saskatchewan'), ('YT', 'Yukon Territory')])), ('readMoreText', wagtail.core.blocks.StructBlock([('text_size', wagtail.core.blocks.ChoiceBlock(choices=[('small', 'Small'), ('normal', 'Normal')], icon='title')), ('paragraph', wagtail.core.blocks.RichTextBlock(default=''))])), ('blueBoxCTA', wagtail.core.blocks.StructBlock([('layout', wagtail.core.blocks.ChoiceBlock(choices=[('horizontal', 'Horizontal'), ('vertical', 'Vertical')], icon='title')), ('title', wagtail.core.blocks.RichTextBlock(features=['bold'])), ('text', wagtail.core.blocks.TextBlock()), ('button_text', wagtail.core.blocks.CharBlock()), ('button_link', wagtail.core.blocks.StructBlock([('link_to', wagtail.core.blocks.ChoiceBlock(choices=[('page', 'Page'), ('file', 'File'), ('custom_url', 'Custom URL')], classname='link_choice_type_selector', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(form_classname='page_link', required=False)), ('file', wagtail.documents.blocks.DocumentChooserBlock(form_classname='file_link', required=False)), ('custom_url', wagtail.core.blocks.CharBlock(form_classname='custom_url_link url_field', max_length=300, required=False, validators=[wagtail.admin.forms.choosers.URLOrAbsolutePathValidator()])), ('new_window', wagtail.core.blocks.BooleanBlock(form_classname='new_window_toggle', label='Open in new window', required=False))]))])), ('paragraph', wagtail.core.blocks.StructBlock([('text_size', wagtail.core.blocks.ChoiceBlock(choices=[('small', 'Small'), ('normal', 'Normal')], icon='title')), ('paragraph', wagtail.core.blocks.RichTextBlock())])), ('quote', wagtail.core.blocks.BlockQuoteBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('embed', wagtail.embeds.blocks.EmbedBlock())], default='', verbose_name='Heading Left Content')),
                ('right_content', wagtail.core.fields.StreamField([('partnersButtons', wagtail.core.blocks.ChoiceBlock(choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District Of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming'), ('AB', 'Alberta'), ('BC', 'British Columbia'), ('MB', 'Manitoba'), ('NB', 'New Brunswick'), ('NL', 'Newfoundland and Labrador'), ('NS', 'Nova Scotia'), ('NT', 'Northwest Territories'), ('NU', 'Nunavut'), ('ON', 'Ontario'), ('PE', 'Prince Edward Island'), ('QC', 'Quebec'), ('SK', 'Saskatchewan'), ('YT', 'Yukon Territory')])), ('readMoreText', wagtail.core.blocks.StructBlock([('text_size', wagtail.core.blocks.ChoiceBlock(choices=[('small', 'Small'), ('normal', 'Normal')], icon='title')), ('paragraph', wagtail.core.blocks.RichTextBlock(default=''))])), ('blueBoxCTA', wagtail.core.blocks.StructBlock([('layout', wagtail.core.blocks.ChoiceBlock(choices=[('horizontal', 'Horizontal'), ('vertical', 'Vertical')], icon='title')), ('title', wagtail.core.blocks.RichTextBlock(features=['bold'])), ('text', wagtail.core.blocks.TextBlock()), ('button_text', wagtail.core.blocks.CharBlock()), ('button_link', wagtail.core.blocks.StructBlock([('link_to', wagtail.core.blocks.ChoiceBlock(choices=[('page', 'Page'), ('file', 'File'), ('custom_url', 'Custom URL')], classname='link_choice_type_selector', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(form_classname='page_link', required=False)), ('file', wagtail.documents.blocks.DocumentChooserBlock(form_classname='file_link', required=False)), ('custom_url', wagtail.core.blocks.CharBlock(form_classname='custom_url_link url_field', max_length=300, required=False, validators=[wagtail.admin.forms.choosers.URLOrAbsolutePathValidator()])), ('new_window', wagtail.core.blocks.BooleanBlock(form_classname='new_window_toggle', label='Open in new window', required=False))]))])), ('paragraph', wagtail.core.blocks.StructBlock([('text_size', wagtail.core.blocks.ChoiceBlock(choices=[('small', 'Small'), ('normal', 'Normal')], icon='title')), ('paragraph', wagtail.core.blocks.RichTextBlock())])), ('quote', wagtail.core.blocks.BlockQuoteBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('embed', wagtail.embeds.blocks.EmbedBlock())], blank=True, default='', verbose_name='Heading Right Content')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='StyleCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'styles of homes',
            },
        ),
        migrations.CreateModel(
            name='PriceRanges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('UN', 'Under'), ('OV', 'Over')], default='UN', max_length=2)),
                ('price', models.PositiveIntegerField(default=0)),
                ('homes_search_page', modelcluster.fields.ParentalKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='homes_search_page', to='wagtailcore.page')),
            ],
            options={
                'verbose_name_plural': 'price ranges',
            },
        ),
    ]
