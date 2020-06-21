from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class PCK(models.Model):
    pck_name = models.CharField("ПЦК, к которому относится сотрудник", max_length=100, null=True)

    def __str__(self):
        return self.pck_name

    class Meta:
        verbose_name = "Предметно-цикловая комиссия"
        verbose_name_plural = "Предметно-цикловые комиссии"


class Qualification_course(models.Model):
    # Курсы повышения квалификации
    date_start = models.DateField("Дата начала курса повышения квалификации", auto_now=False, auto_now_add=False)
    date_end = models.DateField("Дата конца курса повышения квалификации", auto_now=False, auto_now_add=False)
    topic = models.CharField("Тема курса", max_length=200)
    place = models.CharField("Место курса повышения квалификации", max_length=100)
    document = models.FileField('Потдверждающий документ', upload_to='documents_for_qualific/')
    time = models.IntegerField("Время")

    def __str__(self):
        return self.topic + self.place

    class Meta:
        verbose_name = "Курс повышения квалификации"
        verbose_name_plural = "Курсы повышения квалификации"


class Tag(models.Model):
    CATEGORY = (('1.Создание и развитие учебно-материальной базы техникума',
                 '1.Создание и развитие учебно-материальной базы техникума'),
                ('2.Образовательная деятельность', '2.Образовательная деятельность'),
                ('3.Методическая работа', '3.Методическая работа'),
                )

    SUBCATEGORY = (
        ('1.1.Создание и развитие учебно-материальной базы техникума',
         '1.1.Создание и развитие учебно-материальной базы техникума'),
        ('2.1.Динамика индивидуальных образовательных результатов (на 29 декабря и 5 июля)',
         '2.1.Динамика индивидуальных образовательных результатов (на 29 декабря и 5 июля)'),
        ('2.2.НСО (руководство студенческими исследовательскими проектами или работами)(не более20 баллов)',
         '2.2.НСО (руководство студенческими исследовательскими проектами или работами)(не более20 баллов)'),
        ('2.3.Реализация социальных и волонтерских программ областного или регионального уровней (не более 5 баллов)',
         '2.3.Реализация социальных и волонтерских программ областного или регионального уровней (не более 5 баллов)'),
        ('2.4.Профориентационная работа', '2.4.Профориентационная работа'),
        ('3.1.Участие в профессиональных и творческих конкурсах (не более 15 баллов)',
         '3.1.Участие в профессиональных и творческих конкурсах (не более 15 баллов)'),
        ('3.2.Выступление на внешних семинарах (не более 4,5 баллов)',
         '3.2.Выступление на внешних семинарах (не более 4,5 баллов)'),
        ('3.3.Выпуск публикаций, учебников (не более 16 баллов)',
         '3.3.Выпуск публикаций, учебников (не более 16 баллов)'),
        ('3.4.Участие в организации и проведении областных и региональных мероприятий (не более 6 баллов)',
         '3.4.Участие в организации и проведении областных и региональных мероприятий (не более 6 баллов)'),
        ('3.5.Работа в составе стажировочной, демонстрационной площадки (не более 5 баллов)',
         '3.5.Работа в составе стажировочной, демонстрационной площадки (не более 5 баллов)'),
    )

    CRITERION = (
        ('Создание макетов, действующих моделей (установок)', 'Создание макетов, действующих моделей (установок)'),
        ('Создание лабораторных стендов, специализированных рабочих мест',
         'Создание лабораторных стендов, специализированных рабочих мест'),
        ('Реконструкция существующих макетов, моделей, стендов, рабочих мест',
         'Реконструкция существующих макетов, моделей, стендов, рабочих мест'),
        ('Монтаж систем электро и теплоснабжения в техникуме со студентами старших курсов',
         'Монтаж систем электро и теплоснабжения в техникуме со студентами старших курсов'),
        ('Создание средств наглядной агитации, информационных и демонстрационных стендов',
         'Создание средств наглядной агитации, информационных и демонстрационных стендов'),
        ('Ремонтные работы по кабинету', 'Ремонтные работы по кабинету'),
        ('Положительная динамика качества обучения', 'Положительная динамика качества обучения'),
        ('Участие студентов в очном региональном, межрегиональном, всероссийском, международном конкурсе/конференции',
         'Участие студентов в очном региональном, межрегиональном, всероссийском, международном конкурсе/конференции'),
        ('Победа в очном конкурсе областного или регионального уровня',
         'Победа в очном конкурсе областного или регионального уровня'),
        ('Победа в очном конкурсе всероссийского и международного уровня',
         'Победа в очном конкурсе всероссийского и международного уровня'),
        ('Победа в заочном конкурсе регионального, межрегионального  всероссийского уровня',
         'Победа в заочном конкурсе регионального, межрегионального  всероссийского уровня'),
        ('Руководство коллективом студентов свыше 5 человек (только командная форма)',
         'Руководство коллективом студентов свыше 5 человек (только командная форма)'),
        ('Руководство студенческой работой технической направленности',
         'Руководство студенческой работой технической направленности'),
        ('Оформление статьи в сборники по работам студентов (ББК, ISBN)',
         'Оформление статьи в сборники по работам студентов (ББК, ISBN)'),
        ('Разработка образовательной программы, курса до 72 часов',
         'Разработка образовательной программы, курса до 72 часов'),
        ('Разработка образовательной программы, курса свыше 72 часов',
         'Разработка образовательной программы, курса свыше 72 часов'),
        ('Реализация образовательной программы до 72 часов', 'Реализация образовательной программы до 72 часов'),
        ('Реализация образовательной программы свыше 72 часов', 'Реализация образовательной программы свыше 72 часов'),
        (
            'Организация и участие в реализации профессиональных проб для школьников, днях открытых дверей, профессиональных субботах, др. мероприятиях',
            'Организация и участие в реализации профессиональных проб для школьников, днях открытых дверей, профессиональных субботах, др. мероприятиях'),
        (
            'Участие в реализации профессиональных проб для школьников, днях открытых дверей, профессиональных субботах, др. мероприятиях',
            'Участие в реализации профессиональных проб для школьников, днях открытых дверей, профессиональных субботах, др. мероприятиях'),
        ('Участие в заочных региональных  конкурсах профессионального мастерства',
         'Участие в заочных региональных  конкурсах профессионального мастерства'),
        ('Очное участие в областных или региональных конкурсах профессионального мастерства',
         'Очное участие в областных или региональных конкурсах профессионального мастерства'),
        ('Победа в заочных региональных конкурсах профессионального мастерства',
         'Победа в заочных региональных конкурсах профессионального мастерства'),
        ('Победа в очных региональных конкурсах профессионального мастерства',
         'Победа в очных региональных конкурсах профессионального мастерства'),
        ('Результативное участие в конкурсе методических работ техникума',
         'Результативное участие в конкурсе методических работ техникума'),
        ('Участие в творческих очных конкурсах регионального и уровня и выше',
         'Участие в творческих очных конкурсах регионального и уровня и выше'),
        ('Победа в творческих очных конкурсах регионального уровня и межрегионального уровня и выше',
         'Победа в творческих очных конкурсах регионального уровня и межрегионального уровня и выше'),
        ('Выступление по заявленной теме на конференциях, семинарах, форумах городского уровня',
         'Выступление по заявленной теме на конференциях, семинарах, форумах городского уровня'),
        (
            'Выступление по заявленной теме на конференциях, семинарах, форумах областного (регионального)  и Всероссийского уровней',
            'Выступление по заявленной теме на конференциях, семинарах, форумах областного (регионального)  и Всероссийского уровней'),

        ('Публикация в журнале, сборнике (ББК, ISBN)', 'Публикация в журнале, сборнике (ББК, ISBN)'),

        ('Организация и проведение областных (региональных) мероприятий (конкурсов, олимпиад, конференций)',
         'Организация и проведение областных (региональных) мероприятий (конкурсов, олимпиад, конференций)'),
        ('Проведение областных (региональных) мероприятий (конкурсов, олимпиад, конференций) в составе рабочих групп',
         'Проведение областных (региональных) мероприятий (конкурсов, олимпиад, конференций) в составе рабочих групп'),
        ##############################    ПОДКАТЕГОРИЯ 3.5    ##########################################################
        (
            'Работа в стажировочной или демонстрационной площадке КЭТ и инновационных проектах (РЦ, МФЦ ПК, кластер «Энергетика», демонстрационная площадка)',
            'Работа в стажировочной или демонстрационной площадке КЭТ и инновационных проектах (РЦ, МФЦ ПК, кластер «Энергетика», демонстрационная площадка)'),
        ('Мастер-класс стажировочной и демонстрационной  площадок для педагогов других ОУ',
         'Мастер-класс стажировочной и демонстрационной  площадок для педагогов других ОУ'),
        ('Открытый урок для педагогов других ОУ', 'Открытый урок для педагогов других ОУ'),
        ('Представление результатов работы на внешней аудитории',
         'Представление результатов работы на внешней аудитории'),
    )

    category_name = models.CharField("Название категории мероприятия", max_length=200, null=True, choices=CATEGORY)
    subcategory_name = models.CharField("Название подкатегории мероприятия", max_length=200, null=True,
                                        choices=SUBCATEGORY)
    criterion_name = models.CharField("Название критерия мероприятия", max_length=200, null=True, choices=CRITERION)

    ball = models.FloatField("Балл", null=True)

    def __str__(self):
        return self.criterion_name + ' Балл: ' + str(self.ball)


class Event(models.Model):
    TEACHER_ROLE_IN_EVENT = (
        ("Организатор", "Организатор"),
        ("Участник", "Участник"),
    )

    event_name = models.CharField("Название события", max_length=200, null=True)
    date_start = models.DateField("Дата начала события", auto_now=False, auto_now_add=False, null=True)
    date_end = models.DateField("Дата конца события", auto_now=False, auto_now_add=False, null=True)
    teacher_role = models.CharField("Роль преподавателя в мероприятии", max_length=60, null=True,
                                    choices=TEACHER_ROLE_IN_EVENT)
    document_for_event = models.FileField('Потдверждающий документ', upload_to='document_for_event/', null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.event_name

    class Meta:
        verbose_name = "событие"
        verbose_name_plural = "события"


class Teacher(models.Model):
    NAME_ROLE = (
        ('Преподаватель', 'Преподаватель'),
        ('Методист', 'Методист'),
        ('Председатель ПЦК', 'Председатель ПЦК'),
    )

    # Класс преподавателей
    user = models.OneToOneField(User, verbose_name="Имя профиля", null=True, max_length=100, on_delete=models.CASCADE)
    second_name = models.CharField("Фамилия", max_length=45)
    first_name = models.CharField("Имя", max_length=45)
    father_name = models.CharField("Отчество", max_length=45)
    photo = models.ImageField('Фотография', upload_to='photos/', null=True)
    last_attest = models.DateField("Последняя аттестация", auto_now=False, auto_now_add=False)
    next_attest = models.DateField("Следующая аттестация", auto_now=False, auto_now_add=False)
    educ_name = models.CharField("Образование", max_length=200, null=True)
    position = models.CharField("Занимаемая должность", max_length=130, null=True)
    subjects = models.CharField("Преподаваемые дисциплины", max_length=130, null=True)
    qualification = models.CharField("Квалификация", max_length=60, null=True)
    rang = models.CharField("Разряд/соответсвие ПС", max_length=45, null=True)
    role = models.CharField("Роль сотрудника в системе", max_length=100, null=True, choices=NAME_ROLE)
    pck = models.ForeignKey(PCK, verbose_name="ПЦК", null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.second_name + ' ' + self.first_name + ' ' + self.father_name

    class Meta:
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"


class Activity(models.Model):
    teachers = models.ForeignKey(Teacher, null=True, on_delete=models.SET_NULL)
    events = models.ForeignKey(Event, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.teachers.second_name + " " + self.teachers.first_name + " / " + self.events.event_name




class Qualific_course_for_Teachers(models.Model):
    teachers = models.ForeignKey(Teacher, null=True, on_delete=models.SET_NULL)
    qual_course = models.ForeignKey(Qualification_course, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.teachers.second_name + " " + self.teachers.first_name + ' / ' + self.qual_course.topic
