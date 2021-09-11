from django.db import models
from datetime import date, datetime
import re

# Create your models here.
class UserManager(models.Manager):
    def validador_basico(self, postData):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        SOLO_LETRAS = re.compile(r'^[a-zA-Z. ]+$')

        errors = {}

        if len(postData['name']) < 2:
            errors['firstname_len'] = "El nombre debe tener al menos 2 caracteres de largo";

        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "correo invalido"

        if not SOLO_LETRAS.match(postData['name']):
            errors['solo_letras'] = "Solo letras en nombre, porfavor"

        if len(postData['password']) < 8:
            errors['password'] = "La contraseña debe tener al menos 8 caracteres";

        if postData['password'] != postData['password_confirm'] :
            errors['password_confirm'] = "La contraseñas no coinciden. "

        
        return errors

class TravelManager(models.Manager):
    def validador_basico(self, postData):
        today = date.today().strftime("%Y-%m-%d")
        start_date = postData['start_date']
        errors = {}
        
        if len(postData['destination']) == "":
            errors['destination'] = "El destino está vacío";
        if len(postData['description']) == "":
            errors['description'] = "La descripción está vacia";
        if (postData['start_date']) < today:
            errors["start_date"] = "La fecha no es correcta"
        if (postData['end_date']) < start_date :
            errors["end_date"] = "La fecha no es correcta"
        if (postData['start_date']) == "":
            errors["start_date"] = "La fecha no puede quedar vacía"
        if (postData['end_date']) == "":
            errors["end_date"] = "La fecha no puede quedar vacía"

        return errors

class User(models.Model):
    CHOICES = (
        ("user", 'User'),
        ("admin", 'Admin')
    )
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique=True)
    role = models.CharField(max_length=255, choices=CHOICES)
    password = models.CharField(max_length=70)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"

class Travel(models.Model):
    destination = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    start_date = models.DateField()
    end_date = models.DateField()
    creator = models.ForeignKey(User, related_name='my_trip', on_delete=models.CASCADE)
    travellers = models.ManyToManyField(User, related_name='other_trips')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TravelManager()
    
    def __str__(self):
        return f"{self.destination}"
    
    def __repr__(self):
        return f"{self.destination}"