# Generated by Django 3.0.4 on 2020-04-01 05:12

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20200401_0429'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePageNavBarItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NavBarItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(blank=True, default='#', max_length=250)),
                ('text', models.CharField(blank=True, max_length=50)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='items', to='home.NavBarItem')),
            ],
        ),
        migrations.DeleteModel(
            name='HomePageGalleryImage',
        ),
        migrations.AddField(
            model_name='homepagenavbaritem',
            name='navbar_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='in_home_pages', to='home.NavBarItem'),
        ),
        migrations.AddField(
            model_name='homepagenavbaritem',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='navbar_items', to='home.HomePage'),
        ),
    ]
