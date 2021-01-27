# Generated by Django 3.1.5 on 2021-01-26 22:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ano',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=4, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Banca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Nivel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Orgao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pergunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField()),
                ('respondida', models.BooleanField(default=False)),
                ('correta', models.BooleanField(default=False)),
                ('ano', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pergunta', to='questoes.ano')),
                ('banca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pergunta', to='questoes.banca')),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pergunta', to='questoes.disciplina')),
                ('nivel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pergunta', to='questoes.nivel')),
                ('orgao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pergunta', to='questoes.orgao')),
            ],
        ),
        migrations.CreateModel(
            name='Alternativa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correta', models.BooleanField(default=False)),
                ('selecionada', models.BooleanField(default=False)),
                ('pergunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alternativa', to='questoes.pergunta')),
            ],
        ),
    ]
