from django.db import models

# Create your models here.

class Income(models.Model):

    class IncomeTypes(models.IntegerChoices):
        SALARY = 1, "SALARY"
        BONUS = 2, "BONUS"
        GIFT = 3, "GIFT"
        OTHER = 4, "OTHER"

    class RepetitionInterval(models.IntegerChoices):
        NON = 1, "NONE"
        DAY = 2, 'DAILY'
        WEK = 3, 'WEEKLY'
        FNT = 4, 'FORNIGHTLY'
        MTH = 5, 'MONTHLY'
        SEM = 6, 'BIANNUALLY'
        YEA = 7, 'YEARLY'

    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='incomes')
    name = models.CharField(max_length=64)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(null=True)
    category = models.PositiveSmallIntegerField(choices = IncomeTypes.choices)
    repetitive = models.BooleanField(default=False)
    repetition_interval = models.PositiveSmallIntegerField(choices = RepetitionInterval.choices, default=1)
    repetition_time = models.PositiveSmallIntegerField(default =0)
    details = models.CharField(max_length=64)
    comment_char = models.TextField(max_length=255, blank=True, null=True)
    comment_text = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Income {self.id} {self.date.strftime("%d/%m/%Y")}'
    class Meta:
        verbose_name_plural = "incomes"

class Outcome(models.Model):

    class OutcomeTypes(models.IntegerChoices):
        RENT = 1, "SALARY"
        UTI = 2, "BONUS"
        INS = 3, "INSURANCE"
        TRA = 4, 'TRANSPORTATION'
        ENT= 5, 'ENTERTAINMENT'
        GIF= 6, 'GIFTS'
        TAX = 7, 'TAXES'
        SAV = 8, 'SAVINGS'
        INV = 9, 'INVESMENT'

    class RepetitionInterval(models.IntegerChoices):
       
        NON = 1, "NONE"
        DAY = 2, 'DAILY'
        WEK = 3, 'WEEKLY'
        FNT = 4, 'FORNIGHTLY'
        MTH = 5, 'MONTHLY'
        SEM = 6, 'BIANNUALLY'
        YEA = 7, 'YEARLY'


    
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='outcomes')
    name = models.CharField(max_length=64)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    category = models.CharField(max_length=64)
    category = models.PositiveSmallIntegerField(choices =  OutcomeTypes.choices)
    repetition_interval = models.PositiveSmallIntegerField(choices = RepetitionInterval.choices, default=1)
    repetition_time = models.PositiveSmallIntegerField(default =0)
    details = models.CharField(max_length=64)

    def __str__(self):
        return f'Outcome {self.id} {self.date.strftime("%m-%d-%Y")}'
    class Meta:
        verbose_name_plural = "outcomes"


class Balance(models.Model):
    class BalanceTypes(models.IntegerChoices):
        CUR = 1, 'CURRENT'
        SAV = 2, 'SAVINGS'
        CAS = 3, 'CASH'
        INV = 4, 'INVESTMENT'

    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='balances')
    name = models.CharField(max_length=64)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    category = models.PositiveSmallIntegerField(choices =  BalanceTypes.choices)
    update_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    details = models.CharField(max_length=64)

    def __str__(self):
        return f'Balance {self.id} {self.date.strftime("%/d/%m/%Y")}'

    class Meta:
        verbose_name_plural = "balances"

