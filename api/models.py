from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    website = models.CharField(max_length=100)
    company = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Todo(models.Model):
    uerId = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    completed = models.BooleanField()

    def __str__(self):
        return self.nome

class Comment(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    completed = models.BooleanField()

    def __str__(self):
        return self.nome

class Post(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

