from datacenter.models import Schoolkid, Commendation, Chastisement
from datacenter.models import Subject, Teacher, Mark
from datetime import date
import random

commendations = [
    'Молодец!',
    'Отлично!',
    'Хорошо!',
    'Гораздо лучше, чем я ожидал!',
    'Ты меня приятно удивил!',
    'Великолепно!',
    'Прекрасно!',
    'Ты меня очень обрадовал!',
    'Именно этого я давно ждал от тебя!',
    'Сказано здорово – просто и ясно!',
    'Ты, как всегда, точен!',
    'Очень хороший ответ!',
    'Талантливо!',
    'Ты сегодня прыгнул выше головы!',
    'Я поражен!',
    'Уже существенно лучше!',
    'Потрясающе!',
    'Замечательно!',
    'Прекрасное начало!',
    'Так держать!',
    'Ты на верном пути!',
    'Здорово!',
    'Это как раз то, что нужно!',
    'Я тобой горжусь!',
    'С каждым разом у тебя получается всё лучше!',
    'Мы с тобой не зря поработали!',
    'Я вижу, как ты стараешься!',
    'Ты растешь над собой!',
    'Ты многое сделал, я это вижу!',
    'Теперь у тебя точно все получится!',
]


def fix_marks(schoolkid):
    try:
        if not schoolkid or schoolkid.strip() == '':
            print('Ошибка: Не указано имя ученика или указано некорректно')
        schoolkid_name = Schoolkid.objects.get(full_name__contains=schoolkid)
        schoolkid_marks = Mark.objects.filter(schoolkid=schoolkid_name)
        bad_marks = schoolkid_marks.filter(points__in=[2, 3])
        return bad_marks.update(points=5)
    except Schoolkid.DoesNotExist:
        print(f'Ошибка: Ученик {schoolkid} не найден!')
    except Schoolkid.MultipleObjectsReturned:
        print(f'Ошибка: Найдено несколько учеников с именем {schoolkid}')


def remove_chastisements(schoolkid):
    try:
        if not schoolkid or schoolkid.strip() == '':
            print('Ошибка: Не указано имя ученика или указано некорректно')
        schoolkid_name = Schoolkid.objects.get(full_name__contains=schoolkid)
        schoolkid_chast = Chastisement.objects.filter(schoolkid=schoolkid_name)
        return schoolkid_chast.delete()
    except Schoolkid.DoesNotExist:
        print(f'Ошибка: Ученик {schoolkid} не найден!')
    except Schoolkid.MultipleObjectsReturned:
        print(f'Ошибка: Найдено несколько учеников с именем {schoolkid}')


def create_commendation(schoolkid, subject):
    try:
        if not schoolkid or schoolkid.strip() == '':
            print('Ошибка: Не указано имя ученика или указано некорректно')
        if not subject or subject.strip() == '':
            print('Ошибка: Не указан предмет или указано некорректно!')
        schoolkid_name = Schoolkid.objects.get(full_name__contains=schoolkid)
        any_subject = Subject.objects.get(
            title=subject,
            year_of_study=schoolkid_name.year_of_study
        )
        teacher_m = Teacher.objects.get(full_name__contains='Селезнева Майя')
        date_с = date.today()
        text_c = random.choice(commendations)
        create_commendation_obj = Commendation.objects.create(
            text=text_c,
            schoolkid=schoolkid_name,
            subject=any_subject,
            teacher=teacher_m,
            created=date_с
        )
        return create_commendation_obj
    except Schoolkid.DoesNotExist:
        print(f'Ошибка: Ученик {schoolkid} не найден!')
    except Subject.DoesNotExist:
        print(f'Ошибка: Предмет {subject} не найден!')
    except Schoolkid.MultipleObjectsReturned:
        print(f'Ошибка: Найдено несколько учеников с именем {schoolkid}')
