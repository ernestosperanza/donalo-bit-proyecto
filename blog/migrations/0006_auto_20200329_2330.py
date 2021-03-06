# Generated by Django 3.0.3 on 2020-03-29 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200327_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cantidad',
            field=models.IntegerField(verbose_name='Cantidad'),
        ),
        migrations.AlterField(
            model_name='post',
            name='categoria',
            field=models.CharField(choices=[('Alimentos y Bebidas', 'Alimentos y Bebidas'), ('Animales y Mascotas', 'Animales y Mascotas'), ('Arte, Librería y Mercería', 'Arte, Librería y Mercería'), ('Autos, Motos y Otros', 'Autos, Motos y Otros'), ('Belleza y Cuidado Personal', 'Belleza y Cuidado Personal'), ('Celulares y Telefonía', 'Celulares y Telefonía'), ('Computación', 'Computación'), ('Deportes y Fitness', 'Deportes y Fitness'), ('Electrodomésticos', 'Electrodomésticos'), ('Electrónica', 'Electrónica'), ('Herramientas y Construcción', 'Herramientas y Construcción'), ('Hogar, Muebles y Jardín', 'Hogar, Muebles y Jardín'), ('Industrias y Oficinas', 'Industrias y Oficinas'), ('Inmuebles', 'Inmuebles'), ('Instrumentos Musicales', 'Instrumentos Musicales'), ('Joyas y Relojes', 'Joyas y Relojes'), ('Juegos y Juguetes', 'Juegos y Juguetes'), ('Libros y Revistas', 'Libros y Revistas'), ('Música y Películas', 'Música y Películas'), ('Ropa, Calzados y Accesorios', 'Ropa, Calzados y Accesorios'), ('Salud y Equipamiento Médico', 'Salud y Equipamiento Médico'), ('Servicios', 'Servicios'), ('Otras categorías', 'Otras categorías')], default='otras categorias', max_length=100, verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='post',
            name='contenido',
            field=models.TextField(max_length=300, verbose_name='Que uso pensas darle?'),
        ),
        migrations.AlterField(
            model_name='post',
            name='producto',
            field=models.CharField(max_length=100, verbose_name='Descripción'),
        ),
    ]
