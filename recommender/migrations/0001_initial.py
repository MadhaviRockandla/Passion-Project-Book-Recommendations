from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BRS_Dataset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserID', models.CharField(max_length=200)),
                ('BookTitle', models.CharField(max_length=200)),
                ('BookRating', models.CharField(max_length=200)),
            ],
        ),
    ]