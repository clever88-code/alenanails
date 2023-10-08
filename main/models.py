from django.db import models

class record(models.Model):
    name = models.CharField(max_length=150)
    number = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    
    class Meta:
        db_table = 'record'
        verbose_name = 'запись'
        verbose_name_plural = 'Записи'
        
    def __str__(self):
        return self.name

class completedrecord(models.Model):
    record = models.ForeignKey(record, on_delete=models.CASCADE, null=True, blank=True,verbose_name = 'Выберите клиента')
    completed_work = models.TextField('Выполненная работа', default="")
    price = models.IntegerField('Стоимость работы')

    class Meta:
        db_table = 'completedrecord'
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи Выполненые'
        
    def __str__(self):
        return self.completed_work
