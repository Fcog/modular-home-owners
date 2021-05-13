# Generated by Django 3.1.7 on 2021-05-13 02:32

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0060_fix_workflow_unique_constraint'),
        ('wagtailsvg', '0002_svg_edit_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeSearchPageSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('homes_ad_text', models.CharField(default='', max_length=254, null=True)),
                ('homes_ad_button_text', models.CharField(default='', max_length=255, null=True, verbose_name='Button text')),
                ('homes_ad_external_url', models.URLField(blank=True, default='', null=True, verbose_name='Button external URL')),
                ('filter_price_min', models.PositiveIntegerField(default='50000', null=True, verbose_name='Price range min value')),
                ('filter_price_max', models.PositiveIntegerField(default='1500000', null=True, verbose_name='Price range max value')),
                ('filter_price_step', models.PositiveIntegerField(default='10000', null=True, verbose_name='Price range widget values step')),
                ('filter_sqft_min', models.PositiveIntegerField(default='50', null=True, verbose_name='Square footage min value')),
                ('filter_sqft_max', models.PositiveIntegerField(default='600', null=True, verbose_name='Square footage max value')),
                ('filter_sqft_step', models.PositiveIntegerField(default='50', null=True, verbose_name='Square footage range widget values step')),
                ('homes_ad_button_link', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Button URL from a page')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HomePageSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_intro', models.TextField(default='', max_length=255, null=True, verbose_name='Home introduction')),
                ('home_button_text', models.CharField(default='', max_length=255, null=True, verbose_name='Button text')),
                ('home_small_text', models.TextField(default='', max_length=255, null=True, verbose_name='Small text')),
                ('home_verified_title', models.CharField(default='', max_length=255, null=True, verbose_name='Verified box title')),
                ('home_verified_text', models.CharField(default='', max_length=255, null=True, verbose_name='Verified box text')),
                ('home_similar_title', models.CharField(default='', max_length=255, null=True, verbose_name='Similar houses section title')),
                ('home_form', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Modal Form')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GeneralSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_email', models.EmailField(default='services@mho.com', max_length=255, null=True)),
                ('search_button_text', models.CharField(default='Find Your Home', max_length=254, null=True)),
                ('logo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailsvg.svg')),
                ('logo_white', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailsvg.svg')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BlocksSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forum_title', models.TextField(default='', max_length=255, null=True, verbose_name='Title')),
                ('forum_text', models.TextField(default='', max_length=255, null=True, verbose_name='Text')),
                ('forum_button_text', models.TextField(default='', max_length=255, null=True, verbose_name='Button Text')),
                ('forum_button_external_url', models.URLField(blank=True, default='', null=True, verbose_name='Button external URL')),
                ('gyh_title', models.TextField(default='', max_length=255, null=True, verbose_name='Title')),
                ('gyh_column_1_title', models.TextField(default='', max_length=255, null=True, verbose_name='Column 1 title')),
                ('gyh_column_1_text', models.TextField(default='', max_length=255, null=True, verbose_name='Column 1 text')),
                ('gyh_column_2_title', models.TextField(default='', max_length=255, null=True, verbose_name='Column 2 title')),
                ('gyh_column_2_text', models.TextField(default='', max_length=255, null=True, verbose_name='Column 2 text')),
                ('gyh_column_3_title', models.TextField(default='', max_length=255, null=True, verbose_name='Column 3 title')),
                ('gyh_column_3_text', models.TextField(default='', max_length=255, null=True, verbose_name='Column 3 text')),
                ('gyh_link_1_text', models.TextField(default='', max_length=255, null=True, verbose_name='Link 1 text')),
                ('gyh_link_2_text', models.TextField(default='', max_length=255, null=True, verbose_name='Link 2 text')),
                ('partner_1_title', wagtail.core.fields.RichTextField(blank=True, default='', null=True)),
                ('partner_1_text', models.TextField(default='', max_length=255, null=True, verbose_name='Column 1 text')),
                ('partner_1_button_text', models.TextField(default='', max_length=255, null=True, verbose_name='Column 1 button text')),
                ('partner_2_title', wagtail.core.fields.RichTextField(blank=True, default='', null=True)),
                ('partner_2_text', models.TextField(default='', max_length=255, null=True, verbose_name='Column 2 text')),
                ('partner_2_button_text', models.TextField(default='', max_length=255, null=True, verbose_name='Column 2 button text')),
                ('resources_text', wagtail.core.fields.RichTextField(blank=True, default='', null=True)),
                ('forum_button_page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Button URL from a page')),
                ('gyh_link_1_link', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Link 1 URL')),
                ('gyh_link_2_link', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Link 2 URL')),
                ('partner_1_button_link', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Column 1 link URL')),
                ('partner_2_button_link', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Column 2 link URL')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
