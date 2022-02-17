# Generated by Django 3.2 on 2021-09-29 03:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gymprofile', '0019_alter_gymprofile_gym_theme'),
        ('base', '0001_initial'),
        ('user', '0014_auto_20210929_0803'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.basemodel')),
                ('text', models.TextField()),
                ('n_gym', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gymprofile.gymprofile')),
                ('n_user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('base.basemodel',),
        ),
    ]
