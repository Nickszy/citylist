# Generated by Django 3.0.4 on 2020-04-04 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=20)),
                ('user_id', models.IntegerField()),
                ('time', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'user_status',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='usex',
            field=models.CharField(choices=[('male', '男'), ('female', '女')], default='male', max_length=6),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='user',
            table='user',
        ),
    ]