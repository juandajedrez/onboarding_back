from django.db import models

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    othername = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    segundoapellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)

    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=10)

    cargo = models.CharField(max_length=100)
    area = models.CharField(max_length=100)

    numero_identificacion = models.CharField(
        max_length=10,
        unique=True
    )

 # ===== GETTERS =====
    def get_nombre(self):
        return self.nombre
    
    def get_othername(self):
        return self.othername

    def get_apellido(self):
        return self.apellido
    
    def getsegundoapellido(self):
        return self.segundoapellido

    def get_telefono(self):
        return self.telefono

    def get_direccion(self):
        return self.direccion

    def get_ciudad(self):
        return self.ciudad

    def get_codigo_postal(self):
        return self.codigo_postal

    def get_cargo(self):
        return self.cargo

    def get_area(self):
        return self.area

    def get_numero_identificacion(self):
        return self.numero_identificacion

    # ===== SETTERS =====
    def set_nombre(self, nombre):
        self.nombre = nombre

    def setothername(self,othername):
        self.othername = othername

    def set_apellido(self, apellido):
        self.apellido = apellido

    def set_segundoapellido(self,segundoapellido):
        self.segundoapellido = segundoapellido

    def set_telefono(self, telefono):
        self.telefono = telefono

    def set_direccion(self, direccion):
        self.direccion = direccion

    def set_ciudad(self, ciudad):
        self.ciudad = ciudad

    def set_codigo_postal(self, codigo_postal):
        self.codigo_postal = codigo_postal

    def set_cargo(self, cargo):
        self.cargo = cargo

    def set_area(self, area):
        self.area = area

    def set_numero_identificacion(self, numero_identificacion):
        self.numero_identificacion = numero_identificacion

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.cargo}"

