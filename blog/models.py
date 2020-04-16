from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
import django_filters


CATEGORIAS_OPCIONES = (
                    ('Alimentos y Bebidas', 'Alimentos y Bebidas'),
                    ('Animales y Mascotas', 'Animales y Mascotas'),
                    ('Arte, Librería y Mercería', 'Arte, Librería y Mercería'),
                    ('Autos, Motos y Otros', 'Autos, Motos y Otros'),
                    ('Belleza y Cuidado Personal', 'Belleza y Cuidado Personal'),
                    ('Celulares y Telefonía', 'Celulares y Telefonía'),
                    ('Computación', 'Computación'),
                    ('Deportes y Fitness', 'Deportes y Fitness'),
                    ('Electrodomésticos', 'Electrodomésticos'),
                    ('Electrónica', 'Electrónica'),
                    ('Herramientas y Construcción', 'Herramientas y Construcción'),
                    ('Hogar, Muebles y Jardín', 'Hogar, Muebles y Jardín'),
                    ('Industrias y Oficinas', 'Industrias y Oficinas'),
                    ('Inmuebles', 'Inmuebles'),
                    ('Instrumentos Musicales', 'Instrumentos Musicales'),
                    ('Joyas y Relojes', 'Joyas y Relojes'),
                    ('Juegos y Juguetes', 'Juegos y Juguetes'),
                    ('Libros y Revistas', 'Libros y Revistas'),
                    ('Música y Películas', 'Música y Películas'),
                    ('Ropa, Calzados y Accesorios', 'Ropa, Calzados y Accesorios'),
                    ('Salud y Equipamiento Médico','Salud y Equipamiento Médico'),
                    ('Servicios', 'Servicios'),
                    ('Otras categorías', 'Otras categorías')
                    )


class Post(models.Model):
    categoria = models.CharField(max_length=100, choices=CATEGORIAS_OPCIONES,
    default='otras categorias',verbose_name = "Categoria")
    title = ''
    producto = models.CharField(max_length=100,verbose_name = "Descripción")
    cantidad = models.IntegerField(verbose_name = "Cantidad")
    contenido = models.TextField(max_length=300,verbose_name = "Que uso pensas darle?")
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class PostFilter(django_filters.FilterSet):
    producto = django_filters.CharFilter(lookup_expr='icontains', label='Buscar')
    #categoria = django_filters.ChoiceFilter(choices=CATEGORIAS_OPCIONES)

class Meta:
    model = Post
    fields = ['categoria', 'producto']
