
import django.db.models.deletion
import taggit.managers
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('genre', models.CharField(choices=[('pop', '팝'), ('dance', '댄스'), ('edm', 'EDM'), ('hiphop', '힙합'), ('rnb', 'R&B'), ('classic', '클래식'), ('newage', '뉴에이지'), ('rock', '락'), ('ballad', '발라드'), ('indie', '인디'), ('jazz', '재즈/스윙'), ('latin', '라틴'), ('korea', '국악'), ('world', '월드뮤직'), ('ambient', '앰비언트'), ('trot', '트로트'), ('etc', '기타')], default='etc', max_length=20)),
                ('tempo', models.CharField(choices=[('slower', '아주 느림'), ('slow', '느림'), ('normal', '보통빠름'), ('fast', '빠름'), ('faster', '아주 빠름')], default='normal', max_length=20)),
                ('thumbnail', models.ImageField(upload_to='thumbnail/')),
                ('price', models.PositiveIntegerField()),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
    ]
