from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField



""" class Cliente(models.Model):
    doc = (
        ('D', 'DPI'),
        ('C', 'CEDULA'),
    )
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)
    nacimiento=models.DateField()
    documento=models.CharField(
        max_length=20,
        choices=doc,
        default='D')
    creacion=models.DateField(auto_now_add=True)
    actualizacion=models.DateField(auto_now_add=True)


    def __str__(self):
        return '%s %s' % (self.nombre, self.apellido)


class TipoCliente(models.Model):
    tipo = models.CharField(max_length=10)
    creacion= models.DateField(auto_now_add=True)
    actualizacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s' % (self.tipo)
 """

class Estudiantes(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)
    carne=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)
    creacion=models.DateField(auto_now_add=True)
    actualizacion=models.DateField(auto_now_add=True)


    def __str__(self):
        return '%s %s %s' % (self.nombre, self.apellido, self.carne)

class Administradores(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)
    carne=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)
    creacion=models.DateField(auto_now_add=True)
    actualizacion=models.DateField(auto_now_add=True)


    def __str__(self):
        return '%s %s %s' % (self.nombre, self.apellido, self.carne)


class Articulos(models.Model):
    titulo=models.CharField(max_length=100)
    contenido=models.CharField(max_length=250)
    fecha=models.DateField()
    hora=models.DateTimeField()
    estudiante=models.ForeignKey('Estudiantes',on_delete=CASCADE,default=1)
    admins=models.ForeignKey('Administradores',on_delete=CASCADE,default=1)
    creacion=models.DateField(auto_now_add=True)
    actualizacion=models.DateField(auto_now_add=True)


    def __str__(self):
        return '%s %s %s %s' % (self.titulo, self.contenido, self.fecha, self.hora)

class Comentarios(models.Model):
    titulo=models.CharField(max_length=100)
    contenido=models.CharField(max_length=250)
    fecha=models.DateField()
    hora=models.DateTimeField()
    estudiante=models.ForeignKey('Estudiantes',on_delete=CASCADE,default=1)
    articulosID=models.ForeignKey('Articulos',on_delete=CASCADE,default=1)
    creacion=models.DateField(auto_now_add=True)
    actualizacion=models.DateField(auto_now_add=True)


    def __str__(self):
        return '%s %s %s %s' % (self.titulo, self.contenido, self.fecha, self.hora)