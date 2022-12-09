# Generated by Django 4.1.2 on 2022-10-19 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='additalians',
            fields=[
                ('iid', models.AutoField(primary_key=True, serialize=False)),
                ('iname', models.CharField(max_length=50)),
                ('iprize', models.IntegerField(default=0)),
                ('itemimage', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='addpanjabis',
            fields=[
                ('pid', models.AutoField(primary_key=True, serialize=False)),
                ('pname', models.CharField(max_length=50)),
                ('pprize', models.IntegerField(default=0)),
                ('pimage', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='addsouths',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('sname', models.CharField(max_length=50)),
                ('sprize', models.IntegerField(default=0)),
                ('southimage', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='addtocart',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('uid', models.CharField(max_length=50, null=True)),
                ('atcid', models.CharField(max_length=50)),
                ('atcname', models.CharField(max_length=50)),
                ('atcprize', models.IntegerField(default=0)),
                ('atcimage', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('desc', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='paydetails',
            fields=[
                ('payid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('address1', models.CharField(max_length=50)),
                ('address2', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=40)),
                ('state', models.CharField(max_length=50)),
                ('pincode', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='registration',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=20)),
                ('phonenum', models.CharField(max_length=20)),
                ('type', models.CharField(max_length=20)),
            ],
        ),
    ]