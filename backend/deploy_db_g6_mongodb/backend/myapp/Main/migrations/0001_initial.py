# Generated by Django 4.1.7 on 2023-03-18 16:51

import Main.storages
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Borrow_status',
            fields=[
                ('b_status_id', models.AutoField(primary_key=True, serialize=False)),
                ('b_status_name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'borrow_statuses',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('d_id', models.AutoField(primary_key=True, serialize=False)),
                ('d_name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'departments',
            },
        ),
        migrations.CreateModel(
            name='Id_type',
            fields=[
                ('t_id', models.AutoField(primary_key=True, serialize=False)),
                ('t_name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'id_types',
            },
        ),
        migrations.CreateModel(
            name='Item_category',
            fields=[
                ('item_cate_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_cate_name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'item_categories',
            },
        ),
        migrations.CreateModel(
            name='Item_status',
            fields=[
                ('item_status_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_status_name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'item_statuses',
            },
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('m_id', models.AutoField(primary_key=True, serialize=False)),
                ('m_name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'majors',
            },
        ),
        migrations.CreateModel(
            name='User_privilege',
            fields=[
                ('p_id', models.AutoField(primary_key=True, serialize=False)),
                ('p_name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'user_privileges',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('u_id', models.AutoField(primary_key=True, serialize=False)),
                ('u_name', models.CharField(max_length=100, unique=True)),
                ('u_password', models.CharField(max_length=100)),
                ('u_email', models.EmailField(max_length=100, unique=True)),
                ('u_tel', models.CharField(max_length=10)),
                ('u_created_at', models.DateTimeField(auto_now_add=True)),
                ('u_updated_at', models.DateTimeField(auto_now=True)),
                ('u_department', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='users', to='Main.department')),
                ('u_major', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='users', to='Main.major')),
                ('u_privilege', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='users', to='Main.user_privilege')),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('item_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=100)),
                ('item_description', models.TextField()),
                ('item_note', models.TextField()),
                ('item_img_url', models.FileField(blank=True, null=True, storage=Main.storages.MediaStorage, upload_to='media/')),
                ('item_created_at', models.DateTimeField(auto_now_add=True)),
                ('item_updated_at', models.DateTimeField(auto_now=True)),
                ('item_borrow_status', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Main.borrow_status')),
                ('item_category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Main.item_category')),
                ('item_department', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Main.department')),
                ('item_id_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Main.id_type')),
                ('item_major', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Main.major')),
                ('item_status', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Main.item_status')),
            ],
            options={
                'db_table': 'items',
            },
        ),
        migrations.CreateModel(
            name='Borrow_info',
            fields=[
                ('b_id', models.AutoField(primary_key=True, serialize=False)),
                ('b_location', models.TextField()),
                ('b_note', models.TextField()),
                ('b_borrow_time', models.DateTimeField()),
                ('b_return_time', models.DateTimeField()),
                ('b_created_at', models.DateTimeField(auto_now_add=True)),
                ('b_updated_at', models.DateTimeField(auto_now=True)),
                ('b_item', models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.DO_NOTHING, to='Main.item')),
                ('b_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Main.user')),
            ],
            options={
                'db_table': 'borrow_info',
            },
        ),
    ]
