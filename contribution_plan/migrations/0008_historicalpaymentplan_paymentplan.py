# Generated by Django 3.0.14 on 2021-11-09 12:54

import contribution_plan.mixins
import core.fields
import datetime
import dirtyfields.dirtyfields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfallback.fields
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '__first__'),
        ('contribution_plan', '0007_auto_20210217_1302'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentPlan',
            fields=[
                ('id', models.UUIDField(db_column='UUID', default=None, editable=False, primary_key=True, serialize=False)),
                ('is_deleted', models.BooleanField(db_column='isDeleted', default=False)),
                ('json_ext', jsonfallback.fields.FallbackJSONField(blank=True, db_column='Json_ext', null=True)),
                ('date_created', core.fields.DateTimeField(db_column='DateCreated', null=True)),
                ('date_updated', core.fields.DateTimeField(db_column='DateUpdated', null=True)),
                ('version', models.IntegerField(default=1)),
                ('date_valid_from', core.fields.DateTimeField(db_column='DateValidFrom', default=datetime.datetime.now)),
                ('date_valid_to', core.fields.DateTimeField(blank=True, db_column='DateValidTo', null=True)),
                ('replacement_uuid', models.UUIDField(db_column='ReplacementUUID', null=True)),
                ('code', models.CharField(blank=True, db_column='Code', max_length=255, null=True)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=255, null=True)),
                ('calculation', models.UUIDField(db_column='calculationUUID')),
                ('periodicity', models.IntegerField(db_column='Periodicity')),
                ('benefit_plan', models.ForeignKey(db_column='BenefitPlanID', on_delete=django.db.models.deletion.DO_NOTHING, to='product.Product')),
                ('user_created', models.ForeignKey(db_column='UserCreatedUUID', on_delete=django.db.models.deletion.DO_NOTHING, related_name='paymentplan_user_created', to=settings.AUTH_USER_MODEL)),
                ('user_updated', models.ForeignKey(db_column='UserUpdatedUUID', on_delete=django.db.models.deletion.DO_NOTHING, related_name='paymentplan_user_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tblPaymentPlan',
            },
            bases=(contribution_plan.mixins.GenericPlanQuerysetMixin, dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalPaymentPlan',
            fields=[
                ('id', models.UUIDField(db_column='UUID', db_index=True, default=None, editable=False)),
                ('is_deleted', models.BooleanField(db_column='isDeleted', default=False)),
                ('json_ext', jsonfallback.fields.FallbackJSONField(blank=True, db_column='Json_ext', null=True)),
                ('date_created', core.fields.DateTimeField(db_column='DateCreated', null=True)),
                ('date_updated', core.fields.DateTimeField(db_column='DateUpdated', null=True)),
                ('version', models.IntegerField(default=1)),
                ('date_valid_from', core.fields.DateTimeField(db_column='DateValidFrom', default=datetime.datetime.now)),
                ('date_valid_to', core.fields.DateTimeField(blank=True, db_column='DateValidTo', null=True)),
                ('replacement_uuid', models.UUIDField(db_column='ReplacementUUID', null=True)),
                ('code', models.CharField(blank=True, db_column='Code', max_length=255, null=True)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=255, null=True)),
                ('calculation', models.UUIDField(db_column='calculationUUID')),
                ('periodicity', models.IntegerField(db_column='Periodicity')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('benefit_plan', models.ForeignKey(blank=True, db_column='BenefitPlanID', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='product.Product')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user_created', models.ForeignKey(blank=True, db_column='UserCreatedUUID', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user_updated', models.ForeignKey(blank=True, db_column='UserUpdatedUUID', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical payment plan',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
