from django.db import models
from django.urls import reverse


class Role(models.Model):
    # Роли
    name_role = models.CharField("Название роли", max_length=45)

    def __str__(self):
        return self.name_role

    class Meta:
        verbose_name = "Роль"
        verbose_name_plural = "Роли"


class Qualification(models.Model):
    # Квалификация
    qual_name = models.CharField("Название квалификации", max_length=50)

    def __str__(self):
        return self.qual_name

    class Meta:
        verbose_name = "Квалификация"
        verbose_name_plural = "Квалификации"


class Teacher(models.Model):
    # Класс преподавателей
    second_name = models.CharField("Фамилия", max_length=45)
    first_name = models.CharField("Имя", max_length=45)
    father_name = models.CharField("Отчество", max_length=45)
    image = models.ImageField('Фотография', upload_to='photos/', null=True)
    last_attest = models.DateField("Последняя аттестация", auto_now=False, auto_now_add=False)
    next_attest = models.DateField("Следующая аттестация", auto_now=False, auto_now_add=False)
    educ_place = models.CharField("Место обучения", max_length=120)
    rang = models.CharField("Ранг", max_length=45)
    qualification = models.ForeignKey(Qualification, verbose_name="Квалификация", on_delete=models.SET_NULL, null=True)
    roles = models.ForeignKey(Role, verbose_name="Роль", on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=130, unique=True, null=True)

    def __str__(self):
        return self.second_name + ' ' + self.first_name + ' ' + self.father_name

    def get_absolute_url(self):
        return reverse("teacher_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"


class Event(models.Model):
    # События
    date_start = models.DateField("Дата начала события", auto_now=False, auto_now_add=False)
    date_end = models.DateField("Дата конца события", auto_now=False, auto_now_add=False)
    event_name = models.CharField("Название события", max_length=60)
    players = models.CharField("Участники", max_length=90)
    reason = models.CharField("Повод", max_length=60)

    def __str__(self):
        return self.event_name

    class Meta:
        verbose_name = "Событие"
        verbose_name_plural = "События"


class Qualific_course(models.Model):
    # Курсы повышения квалификации
    date_start = models.DateField("Дата начала квалификации", auto_now=False, auto_now_add=False)
    date_end = models.DateField("Дата конца квалификации", auto_now=False, auto_now_add=False)
    place = models.CharField("Место квалификации", max_length=100)
    topic = models.CharField("Тема", max_length=200)
    document = models.FileField('Потдверждающий документ', upload_to='documents_qualific/')
    time = models.IntegerField("Время")

    def __str__(self):
        return self.topic

    class Meta:
        verbose_name = "Курс повышения квалификации"
        verbose_name_plural = "Курсы повышения квалификации"


class Category(models.Model):
    # Категории
    category_name = models.CharField("Название категории", max_length=45)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Criterie(models.Model):
    # Критерии
    categoryes_id = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    ball = models.IntegerField("Балл")

    def __str__(self):
        return self.ball

    class Meta:
        verbose_name = "Критерий"
        verbose_name_plural = "Критерии"


class Achievement(models.Model):
    # Достижения
    criterie_id = models.ForeignKey(Criterie, verbose_name="Критерий", on_delete=models.SET_NULL, null=True)
    reason = models.CharField("Повод", max_length=50)
    event_in_achievement = models.ForeignKey(Event, verbose_name="Событие", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.reason

    class Meta:
        verbose_name = "Критерий"
        verbose_name_plural = "Критерии"


class Type_educ(models.Model):
    # Тип образования
    educ_name = models.CharField("Образование", max_length=50)

    def __str__(self):
        return self.educ_name

    class Meta:
        verbose_name = "Образование"
        verbose_name_plural = "Образования"


class Staging_on_teacher(models.Model):
    # Постановки преподавателей
    date_start = models.DateField("Дата начала", auto_now=False, auto_now_add=False)
    date_end = models.DateField("Дата окончания", auto_now=False, auto_now_add=False)
    teacher_name = models.CharField("ФИО преподавателя", max_length=90)
    teacher_role = models.CharField("Роль преподавателя", max_length=60)
    teacher_id_stag = models.ForeignKey(Teacher, verbose_name="Преподаватель", on_delete=models.CASCADE)

    def __str__(self):
        return self.teacher_name

    class Meta:
        verbose_name = "Постановка"
        verbose_name_plural = "Постановки"


class Teachers_has_qualific_course(models.Model):
    # Преподаватели + квалификационный курс
    teacher_id_qualific = models.ForeignKey(Teacher, verbose_name="Преподаватель", on_delete=models.SET_NULL, null=True)
    qualific_course = models.ForeignKey(Qualific_course, verbose_name="Курс повышения квалификации",
                                        on_delete=models.SET_NULL, null=True)


class Teachers_has_type_educ(models.Model):
    # Преподаватели + образование
    teacher_id_educ = models.ForeignKey(Teacher, verbose_name="Преподаватель", on_delete=models.SET_NULL, null=True)
    type_educ = models.ForeignKey(Type_educ, verbose_name="Тип образования", on_delete=models.CASCADE)


class Achievements_has_teachers(models.Model):
    # Преподаватели + достижения
    achievements_id = models.ForeignKey(Achievement, verbose_name="Достижение", on_delete=models.CASCADE)
    teacher_id_achiev = models.ForeignKey(Teacher, verbose_name="Преподаватель", on_delete=models.SET_NULL, null=True)


class Teachers_has_event(models.Model):
    # Преподаватели + события
    event_id = models.ForeignKey(Event, verbose_name="Событие", on_delete=models.CASCADE)
    teacher_id_eve = models.ForeignKey(Teacher, verbose_name="Преподаватель", on_delete=models.SET_NULL, null=True)
