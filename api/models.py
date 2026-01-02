from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()



class Profile(models.Model):
    name = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='avatars/')  # media/avatars/ ichiga saqlanadi


class Talaba(models.Model):
    full_name = models.CharField(max_length=255)
    ism = models.CharField(max_length=100)
    telefon = models.CharField(max_length=20)
    balans = models.IntegerField(default=0)
    phone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.full_name



class Tolov(models.Model):
    TURI = (
        ('tolov', 'To‘lov'),
        ('yechib', 'Yechib olish'),
    )

    talaba = models.ForeignKey(
        Talaba,
        on_delete=models.CASCADE,
        related_name='tolovlar'
    )
    summa = models.PositiveIntegerField()
    turi = models.CharField(max_length=10, choices=TURI)
    izoh = models.TextField(blank=True, null=True)
    xodim = models.CharField(max_length=255)
    sana = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.talaba} - {self.summa}"



class ExpenseCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Expense(models.Model):
    PAYMENT_CHOICES = (
        ('cash', 'Naqd pul'),
        ('card', 'Plastik karta'),
        ('click', 'Click'),
        ('payme', 'Payme'),
        ('bank', 'Bank hisobi'),
        ('uzum', 'Uzum'),
        ('humo', 'Humo'),
    )

    date = models.DateField()
    category = models.ForeignKey(
        ExpenseCategory,
        on_delete=models.SET_NULL,
        null=True,
        related_name='expenses'
    )
    name = models.CharField(max_length=255)
    receiver = models.CharField(max_length=255)
    payment_type = models.CharField(max_length=20, choices=PAYMENT_CHOICES)
    amount = models.PositiveIntegerField()
    employee = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='expenses'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class IshHaqqi(models.Model):
    MAOSH_TURI = (
        ('oylik', 'Oylik'),
        ('soatlik', 'Soatlik'),
        ('bonus', 'Bonus'),
    )

    maosh_turi = models.CharField(max_length=20, choices=MAOSH_TURI)
    miqdori = models.DecimalField(max_digits=12, decimal_places=2)
    kurs = models.CharField(max_length=100)
    guruh = models.CharField(max_length=100)      # hozircha TEXT
    oqituvchi = models.CharField(max_length=255) # hozircha TEXT
    talaba = models.ForeignKey(
        Talaba,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.maosh_turi} - {self.miqdori}"




class Qarzdor(models.Model):
    HOLAT = (
        ('faol', 'Faol'),
        ('arxiv', 'Arxivlangan'),
    )

    ism = models.CharField(max_length=255)
    telefon = models.CharField(max_length=20)
    balans = models.DecimalField(max_digits=12, decimal_places=2)
    davr_jami = models.DecimalField(max_digits=12, decimal_places=2)
    jami_qarz = models.DecimalField(max_digits=12, decimal_places=2)
    guruh = models.CharField(max_length=100)
    izoh = models.TextField(blank=True, null=True)
    holati = models.CharField(max_length=10, choices=HOLAT, default='faol')

    def __str__(self):
        return self.ism


class QarzMiqdori(models.Model):
    qarzdor = models.ForeignKey(
        Qarzdor,
        related_name='qarzlar',
        on_delete=models.CASCADE
    )
    miqdor = models.DecimalField(max_digits=12, decimal_places=2)
    sana = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.qarzdor.ism} - {self.miqdor}"
