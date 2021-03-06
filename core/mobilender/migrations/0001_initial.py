# Generated by Django 3.2.7 on 2021-09-06 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('on_request_date', models.DateTimeField(auto_now=True)),
                ('on_delivery_date', models.DateTimeField()),
                ('urgent', models.BooleanField(default=False)),
                ('quantity', models.IntegerField()),
                ('delivery_to', models.CharField(choices=[('DS', 'Distribution Center'), ('BF', 'Branch Office'), ('AF', 'Associated Firm')], max_length=2)),
                ('article_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mobilender.articles')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('code', models.CharField(max_length=100, unique=True)),
                ('photo', models.FileField(null=True, upload_to='./media')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('kind', models.CharField(choices=[('V', 'Vendor'), ('C', 'Client')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Sites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(choices=[('DS', 'Distribution Center'), ('BF', 'Branch Office'), ('AF', 'Associated Firm')], max_length=2)),
                ('name', models.CharField(max_length=50)),
                ('reference', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserRanks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ranks', models.CharField(choices=[('N', 'Normal'), ('S', 'Silver'), ('G', 'Gold'), ('P', 'Platinum')], max_length=1)),
                ('person_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ranks', to='mobilender.person')),
            ],
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('S', 'Sent'), ('OG', 'On Going'), ('R', 'Ready')], max_length=2)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mobilender.orders')),
            ],
        ),
        migrations.CreateModel(
            name='OrdersRecieved',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mobilender.orders')),
                ('person_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mobilender.person')),
            ],
        ),
        migrations.CreateModel(
            name='OrdersFullFilled',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mobilender.orders')),
            ],
        ),
        migrations.CreateModel(
            name='OrdersDelivered',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mobilender.orders')),
            ],
        ),
        migrations.AddField(
            model_name='orders',
            name='person_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mobilender.person'),
        ),
        migrations.AddField(
            model_name='orders',
            name='sites',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mobilender.sites'),
        ),
        migrations.AddField(
            model_name='articles',
            name='vendor_id',
            field=models.ManyToManyField(to='mobilender.Person'),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('person_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address', to='mobilender.person')),
            ],
        ),
    ]
