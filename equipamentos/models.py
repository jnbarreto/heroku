from django.db import models

class Equipamento(models.Model):
    tipo = models.CharField(verbose_name ="Tipo", max_length=50)
    marca = models.CharField(verbose_name ="Marca", max_length=50)
    modelo = models.CharField(verbose_name ="Modelo", max_length=50)
    num_controle = models.IntegerField(verbose_name ="Número de controle")
    img_equip = models.ImageField(verbose_name = "Imagem do equipamento", upload_to='equipamentos', null=True, blank=True)

    def __str__(self):
        return self.tipo + " " + self.marca+ " " + str(self.num_controle)