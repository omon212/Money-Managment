from django.db import models

class User(models.Model):
    username = models.CharField(max_length=30,unique=True)
    password = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    recover_password = models.IntegerField(null=True)

    def __str__(self):
        return self.username


class PayMoney(models.Model):
    total = models.IntegerField(default=0)
    where = models.CharField(max_length=100)
    who = models.ForeignKey(User,on_delete=models.CASCADE)
    CHOISE_PAY = (
        ("kirim","kirim"),
        ("chiqim","chiqim")
    )
    status_money = models.CharField(choices=CHOISE_PAY,max_length=20)
    CHOISE2 = (
        ("Oziq-ovqat", "Oziq-ovqat"),
        ("Transport", "Transport"),
        ("Kiyim-kechak", "Kiyim-kechak"),
        ("Komunal", "Komunal"),
        ("Axborot-vositalari", "Axborot-vositalari"),
        ("Kafe-restoran", "Kafe-restoran"),
        ("Taksi", "Taksi"),
        ("Xizmatlar", "Xizmatlar"),

    )
    method_plase = models.CharField(choices=CHOISE2,max_length=32)
    comment = models.TextField(blank=True)

    def __str__(self):
        return f"{self.who}"


