# Generated by Django 3.0.5 on 2020-04-15 00:56

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="GuacamoleConnection",
            fields=[
                ("connection_id", models.AutoField(primary_key=True, serialize=False)),
                ("connection_name", models.CharField(max_length=128)),
                ("protocol", models.CharField(max_length=32)),
                ("proxy_port", models.IntegerField(blank=True, null=True)),
                (
                    "proxy_hostname",
                    models.CharField(blank=True, max_length=512, null=True),
                ),
                (
                    "proxy_encryption_method",
                    models.CharField(blank=True, max_length=4, null=True),
                ),
                ("max_connections", models.IntegerField(blank=True, null=True)),
                (
                    "max_connections_per_user",
                    models.IntegerField(blank=True, null=True),
                ),
                ("connection_weight", models.IntegerField(blank=True, null=True)),
                ("failover_only", models.IntegerField()),
            ],
            options={"db_table": "guacamole_connection", "managed": False,},
        ),
        migrations.CreateModel(
            name="GuacamoleConnectionGroup",
            fields=[
                (
                    "connection_group_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("connection_group_name", models.CharField(max_length=128)),
                ("type", models.CharField(max_length=14)),
                ("max_connections", models.IntegerField(blank=True, null=True)),
                (
                    "max_connections_per_user",
                    models.IntegerField(blank=True, null=True),
                ),
                ("enable_session_affinity", models.IntegerField()),
            ],
            options={"db_table": "guacamole_connection_group", "managed": False,},
        ),
        migrations.CreateModel(
            name="GuacamoleConnectionHistory",
            fields=[
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("username", models.CharField(max_length=128)),
                (
                    "remote_host",
                    models.CharField(blank=True, max_length=256, null=True),
                ),
                ("connection_name", models.CharField(max_length=128)),
                (
                    "sharing_profile_name",
                    models.CharField(blank=True, max_length=128, null=True),
                ),
                ("start_date", models.DateTimeField()),
                ("end_date", models.DateTimeField(blank=True, null=True)),
            ],
            options={"db_table": "guacamole_connection_history", "managed": False,},
        ),
        migrations.CreateModel(
            name="GuacamoleEntity",
            fields=[
                ("entity_id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=128)),
                ("type", models.CharField(max_length=10)),
            ],
            options={"db_table": "guacamole_entity", "managed": False,},
        ),
        migrations.CreateModel(
            name="GuacamoleSharingProfile",
            fields=[
                (
                    "sharing_profile_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("sharing_profile_name", models.CharField(max_length=128)),
            ],
            options={"db_table": "guacamole_sharing_profile", "managed": False,},
        ),
        migrations.CreateModel(
            name="GuacamoleUserGroup",
            fields=[
                ("user_group_id", models.AutoField(primary_key=True, serialize=False)),
                ("disabled", models.IntegerField()),
            ],
            options={"db_table": "guacamole_user_group", "managed": False,},
        ),
        migrations.CreateModel(
            name="GuacamoleUserHistory",
            fields=[
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("username", models.CharField(max_length=128)),
                (
                    "remote_host",
                    models.CharField(blank=True, max_length=256, null=True),
                ),
                ("start_date", models.DateTimeField()),
                ("end_date", models.DateTimeField(blank=True, null=True)),
            ],
            options={"db_table": "guacamole_user_history", "managed": False,},
        ),
        migrations.CreateModel(
            name="GuacamoleUserPasswordHistory",
            fields=[
                (
                    "password_history_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("password_hash", models.CharField(max_length=32)),
                (
                    "password_salt",
                    models.CharField(blank=True, max_length=32, null=True),
                ),
                ("password_date", models.DateTimeField()),
            ],
            options={"db_table": "guacamole_user_password_history", "managed": False,},
        ),
        migrations.CreateModel(
            name="GuacamoleUser",
            fields=[
                ("user_id", models.AutoField(primary_key=True, serialize=False)),
                ("password_hash", models.BinaryField(max_length=32)),
                (
                    "password_salt",
                    models.BinaryField(blank=True, max_length=32, null=True),
                ),
                (
                    "password_date",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("disabled", models.IntegerField(default=0)),
                ("expired", models.IntegerField(default=0)),
                ("access_window_start", models.TimeField(blank=True, null=True)),
                ("access_window_end", models.TimeField(blank=True, null=True)),
                ("valid_from", models.DateField(blank=True, null=True)),
                ("valid_until", models.DateField(blank=True, null=True)),
                ("timezone", models.CharField(blank=True, max_length=64, null=True)),
                ("full_name", models.CharField(blank=True, max_length=256, null=True)),
                (
                    "email_address",
                    models.CharField(blank=True, max_length=256, null=True),
                ),
                (
                    "organization",
                    models.CharField(blank=True, max_length=256, null=True),
                ),
                (
                    "organizational_role",
                    models.CharField(blank=True, max_length=256, null=True),
                ),
                (
                    "entity",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="guacamole.GuacamoleEntity",
                    ),
                ),
            ],
            options={"db_table": "guacamole_user", "managed": True,},
        ),
        migrations.CreateModel(
            name="GuacamoleConnectionAttribute",
            fields=[
                (
                    "connection",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        primary_key=True,
                        serialize=False,
                        to="guacamole.GuacamoleConnection",
                    ),
                ),
                ("attribute_name", models.CharField(max_length=128)),
                ("attribute_value", models.CharField(max_length=4096)),
            ],
            options={"db_table": "guacamole_connection_attribute", "managed": False,},
        ),
        migrations.CreateModel(
            name="GuacamoleConnectionGroupAttribute",
            fields=[
                (
                    "connection_group",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        primary_key=True,
                        serialize=False,
                        to="guacamole.GuacamoleConnectionGroup",
                    ),
                ),
                ("attribute_name", models.CharField(max_length=128)),
                ("attribute_value", models.CharField(max_length=4096)),
            ],
            options={
                "db_table": "guacamole_connection_group_attribute",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="GuacamoleConnectionGroupPermission",
            fields=[
                (
                    "entity",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        primary_key=True,
                        serialize=False,
                        to="guacamole.GuacamoleEntity",
                    ),
                ),
                ("permission", models.CharField(max_length=10)),
            ],
            options={
                "db_table": "guacamole_connection_group_permission",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="GuacamoleConnectionParameter",
            fields=[
                (
                    "connection",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        primary_key=True,
                        serialize=False,
                        to="guacamole.GuacamoleConnection",
                    ),
                ),
                ("parameter_name", models.CharField(max_length=128)),
                ("parameter_value", models.CharField(max_length=4096)),
            ],
            options={"db_table": "guacamole_connection_parameter", "managed": False,},
        ),
        migrations.CreateModel(
            name="GuacamoleSharingProfileAttribute",
            fields=[
                (
                    "sharing_profile",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        primary_key=True,
                        serialize=False,
                        to="guacamole.GuacamoleSharingProfile",
                    ),
                ),
                ("attribute_name", models.CharField(max_length=128)),
                ("attribute_value", models.CharField(max_length=4096)),
            ],
            options={
                "db_table": "guacamole_sharing_profile_attribute",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="GuacamoleSharingProfileParameter",
            fields=[
                (
                    "sharing_profile",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        primary_key=True,
                        serialize=False,
                        to="guacamole.GuacamoleSharingProfile",
                    ),
                ),
                ("parameter_name", models.CharField(max_length=128)),
                ("parameter_value", models.CharField(max_length=4096)),
            ],
            options={
                "db_table": "guacamole_sharing_profile_parameter",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="GuacamoleSharingProfilePermission",
            fields=[
                (
                    "entity",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        primary_key=True,
                        serialize=False,
                        to="guacamole.GuacamoleEntity",
                    ),
                ),
                ("permission", models.CharField(max_length=10)),
            ],
            options={
                "db_table": "guacamole_sharing_profile_permission",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="GuacamoleSystemPermission",
            fields=[
                (
                    "entity",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        primary_key=True,
                        serialize=False,
                        to="guacamole.GuacamoleEntity",
                    ),
                ),
                ("permission", models.CharField(max_length=23)),
            ],
            options={"db_table": "guacamole_system_permission", "managed": False,},
        ),
        migrations.CreateModel(
            name="GuacamoleUserAttribute",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        primary_key=True,
                        serialize=False,
                        to="guacamole.GuacamoleUser",
                    ),
                ),
                ("attribute_name", models.CharField(max_length=128)),
                ("attribute_value", models.CharField(max_length=4096)),
            ],
            options={"db_table": "guacamole_user_attribute", "managed": False,},
        ),
        migrations.CreateModel(
            name="GuacamoleUserGroupAttribute",
            fields=[
                (
                    "user_group",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        primary_key=True,
                        serialize=False,
                        to="guacamole.GuacamoleUserGroup",
                    ),
                ),
                ("attribute_name", models.CharField(max_length=128)),
                ("attribute_value", models.CharField(max_length=4096)),
            ],
            options={"db_table": "guacamole_user_group_attribute", "managed": False,},
        ),
        migrations.CreateModel(
            name="GuacamoleUserGroupMember",
            fields=[
                (
                    "user_group",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        primary_key=True,
                        serialize=False,
                        to="guacamole.GuacamoleUserGroup",
                    ),
                ),
            ],
            options={"db_table": "guacamole_user_group_member", "managed": False,},
        ),
        migrations.CreateModel(
            name="GuacamoleUserGroupPermission",
            fields=[
                (
                    "entity",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        primary_key=True,
                        serialize=False,
                        to="guacamole.GuacamoleEntity",
                    ),
                ),
                ("permission", models.CharField(max_length=10)),
            ],
            options={"db_table": "guacamole_user_group_permission", "managed": False,},
        ),
        migrations.CreateModel(
            name="GuacamoleUserPermission",
            fields=[
                (
                    "entity",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        primary_key=True,
                        serialize=False,
                        to="guacamole.GuacamoleEntity",
                    ),
                ),
                ("permission", models.CharField(max_length=10)),
            ],
            options={"db_table": "guacamole_user_permission", "managed": False,},
        ),
        migrations.CreateModel(
            name="GuacamoleConnectionPermission",
            fields=[
                (
                    "entity",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        primary_key=True,
                        serialize=False,
                        to="guacamole.GuacamoleEntity",
                    ),
                ),
                ("permission", models.CharField(max_length=10)),
                (
                    "connection",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="guacamole.GuacamoleConnection",
                    ),
                ),
            ],
            options={
                "db_table": "guacamole_connection_permission",
                "managed": True,
                "unique_together": {("entity", "connection", "permission")},
            },
        ),
    ]