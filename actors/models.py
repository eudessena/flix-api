from django.db import models


NATIONALITY_CHOICE = (
   ( "BRAZIL", "Brasil"),
   ("USA", "Estados Unidos") # na direita valor que usuario ver, na esquerda o valor que sera salvo em banco
)

class Actor(models.Model):
    name = models.CharField(max_length=200) # charfield texto livre
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField( max_length=100, 
                                   choices=NATIONALITY_CHOICE, 
                                   blank=True, 
                                   null=True )  # choices define opcoes de textos para o usuario preencher o campo 


    def __str__(self):
        return self.name   