# Generated by Django 3.1.7 on 2021-05-14 17:27

from django.db import migrations
import wagtail.admin.forms.choosers
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('homes', '0005_auto_20210514_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homesindexpage',
            name='full_content',
            field=wagtail.core.fields.StreamField([('partnersButtons', wagtail.core.blocks.ChoiceBlock(choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District Of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming'), ('AB', 'Alberta'), ('BC', 'British Columbia'), ('MB', 'Manitoba'), ('NB', 'New Brunswick'), ('NL', 'Newfoundland and Labrador'), ('NS', 'Nova Scotia'), ('NT', 'Northwest Territories'), ('NU', 'Nunavut'), ('ON', 'Ontario'), ('PE', 'Prince Edward Island'), ('QC', 'Quebec'), ('SK', 'Saskatchewan'), ('YT', 'Yukon Territory')])), ('readMoreText', wagtail.core.blocks.StructBlock([('text_size', wagtail.core.blocks.ChoiceBlock(choices=[('small', 'Small'), ('normal', 'Normal')], icon='title')), ('paragraph', wagtail.core.blocks.RichTextBlock(default=''))])), ('blueBoxCTA', wagtail.core.blocks.StructBlock([('layout', wagtail.core.blocks.ChoiceBlock(choices=[('horizontal', 'Horizontal'), ('vertical', 'Vertical')], icon='title')), ('title', wagtail.core.blocks.RichTextBlock(features=['bold'])), ('text', wagtail.core.blocks.TextBlock()), ('button_text', wagtail.core.blocks.CharBlock()), ('button_link', wagtail.core.blocks.StructBlock([('link_to', wagtail.core.blocks.ChoiceBlock(choices=[('page', 'Page'), ('file', 'File'), ('custom_url', 'Custom URL')], classname='link_choice_type_selector', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(form_classname='page_link', required=False)), ('file', wagtail.documents.blocks.DocumentChooserBlock(form_classname='file_link', required=False)), ('custom_url', wagtail.core.blocks.CharBlock(form_classname='custom_url_link url_field', max_length=300, required=False, validators=[wagtail.admin.forms.choosers.URLOrAbsolutePathValidator()])), ('new_window', wagtail.core.blocks.BooleanBlock(form_classname='new_window_toggle', label='Open in new window', required=False))]))])), ('paragraph', wagtail.core.blocks.StructBlock([('text_size', wagtail.core.blocks.ChoiceBlock(choices=[('normal', 'Normal'), ('large', 'Large')], icon='title')), ('paragraph', wagtail.core.blocks.RichTextBlock())])), ('quote', wagtail.core.blocks.BlockQuoteBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('embed', wagtail.embeds.blocks.EmbedBlock())], blank=True, default=''),
        ),
    ]
