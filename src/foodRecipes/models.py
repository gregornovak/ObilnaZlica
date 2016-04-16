from django.db import models

class Recept(models.Model):
    ime_recepta = models.CharField(max_length=120)
    postopek_recepta = models.TextField()
    sestavine_recepta = models.TextField()
    datum_objave = models.DateTimeField(auto_now=False, auto_now_add=True)
    slika_recepta = models.ImageField(upload_to="images", height_field=None,
    width_field=None, max_length=100)
    #SESTAVINE = (
    #    ("meso", "Meso"),
    #    ("morska", "Morski sadeži"),
    #    ("testenine", "Testenine"),
    #    ("riž", "Riž"),
    #    ("sadje", "Sadje"),
    #    ("zelenjava", "Zelenjava"),
    #    ("sir", "Sir")
    #)
    #glavna_sestavina = models.CharField(max_length=80,
    #                                    choices=SESTAVINE,
    #                                    default="Meso")

    def __str__(self):
        return self.ime_recepta
