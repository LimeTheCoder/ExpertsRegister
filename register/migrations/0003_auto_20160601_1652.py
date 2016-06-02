# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_auto_20160601_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expert',
            name='organ',
            field=models.ForeignKey(to='register.DergOrgan'),
        ),
    ]
