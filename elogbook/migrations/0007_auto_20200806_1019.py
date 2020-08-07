# Generated by Django 3.0.8 on 2020-08-06 04:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elogbook', '0006_auto_20200805_0941'),
    ]

    operations = [
        migrations.CreateModel(
            name='log_sheet_pcc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('done_on', models.DateTimeField(default=datetime.datetime(2020, 8, 6, 10, 19, 37, 60060))),
                ('done_by', models.CharField(max_length=100)),
                ('time_hr', models.CharField(choices=[('00', '00'), ('01', '01'), ('02', '02'), ('03', '03'), ('04', '04'), ('05', '05'), ('06', '06'), ('07', '07'), ('08', '08'), ('09', '09'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23')], max_length=20)),
                ('shift', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=20)),
                ('icog_ph_voltage_l1', models.CharField(max_length=20)),
                ('icog_ph_voltage_l2', models.CharField(max_length=20)),
                ('icog_ph_voltage_l3', models.CharField(max_length=20)),
                ('icog_ph_curr_r', models.CharField(max_length=20)),
                ('icog_ph_curr_y', models.CharField(max_length=20)),
                ('icog_ph_curr_b', models.CharField(max_length=20)),
                ('icog_power_kwh', models.CharField(max_length=20)),
                ('dist_transformer', models.CharField(choices=[('1', 'D-TR1'), ('2', 'D-TR2')], max_length=20)),
                ('dt_winding_temp', models.CharField(max_length=20)),
                ('dt_oil_temp', models.CharField(max_length=20)),
                ('dt_oltc_counter', models.CharField(max_length=20)),
                ('rtcc_panel', models.CharField(choices=[('1', 'RTCC1'), ('2', 'RTCC2')], max_length=20)),
                ('rtcc_tap_position', models.CharField(max_length=100)),
                ('rtcc_winding_temp', models.CharField(max_length=20)),
                ('rtcc_oil_temp', models.CharField(max_length=20)),
                ('rtcc_volt_regulation_relay', models.CharField(max_length=20)),
                ('apfc_panel', models.CharField(choices=[('1', 'APFC1'), ('2', 'APFC2')], max_length=20)),
                ('apfc_power_factor', models.CharField(max_length=20)),
                ('apfc_current', models.CharField(max_length=20)),
                ('pcc_shift_operator', models.CharField(max_length=100)),
                ('pcc', models.CharField(choices=[('1', 'Trafo-1'), ('2', 'Trafo-2')], max_length=20)),
                ('pcc_volt_l1', models.CharField(max_length=20)),
                ('pcc_volt_l2', models.CharField(max_length=20)),
                ('pcc_volt_l3', models.CharField(max_length=20)),
                ('pcc_curr_r', models.CharField(max_length=20)),
                ('pcc_curr_y', models.CharField(max_length=20)),
                ('pcc_curr_b', models.CharField(max_length=20)),
                ('pcc_power_kwh', models.CharField(max_length=20)),
                ('remarks', models.CharField(max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='chlorinated_soft_water_tank',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 8, 6, 10, 19, 37, 60060)),
        ),
        migrations.AlterField(
            model_name='chlorinated_soft_water_tank',
            name='done_on',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 6, 10, 19, 37, 60060)),
        ),
        migrations.AlterField(
            model_name='chlorinated_soft_water_tank',
            name='next_due_on',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 6, 10, 19, 37, 60060)),
        ),
    ]
