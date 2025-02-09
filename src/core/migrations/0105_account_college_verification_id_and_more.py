# Generated by Django 4.2.16 on 2024-12-19 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0104_account_osp_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='college_verification_id',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='College Verification ID'),
        ),
        migrations.AddField(
            model_name='account',
            name='is_knowledge_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='account',
            name='knowledge_approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='account',
            name='osp_royalty_score',
            field=models.IntegerField(default=0, verbose_name='OSP Royalty Score'),
        ),
    ]
