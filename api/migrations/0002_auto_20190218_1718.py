# Generated by Django 2.1.7 on 2019-02-18 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThreeInner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('children', models.CharField(max_length=500, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='twoinner',
            name='children',
            field=models.ForeignKey(null=True, on_delete=True, to='api.ThreeInner'),
        ),
    ]
