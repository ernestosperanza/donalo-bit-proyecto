# Generated by Django 3.0.3 on 2020-03-27 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_tipo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tipo',
        ),
        migrations.AlterField(
            model_name='post',
            name='categoria',
            field=models.CharField(choices=[('Alimentos y Bebidas', 'Alimentos y Bebidas'), ('Animales y Mascotas', 'Animales y Mascotas'), ('Arte, Librería y Mercería', 'Arte, Librería y Mercería'), ('Autos, Motos y Otros', 'Autos, Motos y Otros'), ('Belleza y Cuidado Personal', 'Belleza y Cuidado Personal'), ('Celulares y Telefonía', 'Celulares y Telefonía'), ('Computación', 'Computación'), ('Deportes y Fitness', 'Deportes y Fitness'), ('Electrodomésticos', 'Electrodomésticos'), ('Electrónica', 'Electrónica'), ('Herramientas y Construcción', 'Herramientas y Construcción'), ('Hogar, Muebles y Jardín', 'Hogar, Muebles y Jardín'), ('Industrias y Oficinas', 'Industrias y Oficinas'), ('Inmuebles', 'Inmuebles'), ('Instrumentos Musicales', 'Instrumentos Musicales'), ('Joyas y Relojes', 'Joyas y Relojes'), ('Juegos y Juguetes', 'Juegos y Juguetes'), ('libros y revistas', 'Libros y Revistas'), ('música y películas', 'Música y Películas'), ('ropa, calzados y accesorios', 'Ropa, Calzados y Accesorios'), ('salud y equipamiento médico', 'Salud y Equipamiento Médico'), ('servicios', 'Servicios'), ('otras categorías', 'Otras categorías')], default='otras categorias', max_length=100),
        ),
    ]
