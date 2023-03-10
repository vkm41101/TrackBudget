# Generated by Django 4.1.5 on 2023-01-08 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friendship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friendshipId', models.CharField(max_length=200)),
                ('MobileNumber1', models.CharField(max_length=10)),
                ('MobileNumber2', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='pendingTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pendingTransactionId', models.CharField(max_length=200)),
                ('transactionFrom', models.CharField(max_length=10)),
                ('transactionTo', models.CharField(max_length=10)),
                ('transactionAmount', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transactionId', models.CharField(max_length=200)),
                ('transactionFrom', models.CharField(max_length=10)),
                ('transactionTo', models.CharField(max_length=10)),
                ('transactionAmount', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('walletTransac', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=200)),
                ('dob', models.DateField(verbose_name='Date of Birth')),
                ('MobileNumber', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('is_anonymous', models.BooleanField(default=False)),
                ('is_authenticated', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
