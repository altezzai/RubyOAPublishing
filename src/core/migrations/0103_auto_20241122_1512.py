# Generated by Django 4.2.16 on 2024-11-22 09:35

from django.db import migrations, models


def populate_osp_username(apps, schema_editor):
    Account = apps.get_model("core", "Account")
    for account in Account.objects.all():
        account.osp_username = account.email
        account.save()

class Migration(migrations.Migration):

    dependencies = [
        ("core", "0102_account_ban_duration_account_is_user_author"),
    ]

    operations = [
        migrations.AddField(
            model_name="account",
            name="osp_username",
            field=models.CharField(
                max_length=254,
                unique=True,
                verbose_name="OSP username",
                null=True,
            ),
        ),
        migrations.RunPython(populate_osp_username),
        migrations.AlterField(
            model_name="account",
            name="osp_username",
            field=models.CharField(
                max_length=254,
                unique=True,
                verbose_name="OSP username",
                null=False,
            ),
        ),
    ]

