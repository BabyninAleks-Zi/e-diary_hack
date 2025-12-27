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


def get_schoolkid(schoolkid):
    if not schoolkid or schoolkid.strip() == '':
        print('Ошибка: Не указано имя ученика или указано некорректно')
    try:
        return Schoolkid.objects.get(full_name__contains=schoolkid)
    except Schoolkid.DoesNotExist:
        print(f'Ошибка: Ученик {schoolkid} не найден!')
    except Schoolkid.MultipleObjectsReturned:
        print(f'Ошибка: Найдено несколько учеников с именем {schoolkid}')


def fix_marks(schoolkid):
    schoolkid_name = get_schoolkid(schoolkid)
    schoolkid_marks = Mark.objects.filter(schoolkid=schoolkid_name)
    bad_marks = schoolkid_marks.filter(points__in=[2, 3])
    return bad_marks.update(points=5)


def remove_chastisements(schoolkid):
    schoolkid_name = get_schoolkid(schoolkid)
    schoolkid_chast = Chastisement.objects.filter(schoolkid=schoolkid_name)
    return schoolkid_chast.delete()


def create_commendation(schoolkid, subject, teacher):
    schoolkid_name = get_schoolkid(schoolkid)
    if not subject or subject.strip() == '':
        print('Ошибка: Не указан предмет или указано некорректно!')
    commendation_date = date.today()
    commendation_text = random.choice(commendations)
    try:
        school_subject = Subject.objects.get(
            title=subject,
            year_of_study=schoolkid_name.year_of_study
        )
        school_teacher = Teacher.objects.get(full_name__contains=teacher)
        created_commendation = Commendation.objects.create(
            text=commendation_text,
            schoolkid=schoolkid_name,
            subject=school_subject,
            teacher=school_teacher,
            created=commendation_date
        )
        return created_commendation
    except Subject.DoesNotExist:
        print(f'Ошибка: Предмет {subject} не найден!')
    except Teacher.DoesNotExist:
        print(f'Ошибка: Учитель {teacher} не найден!')
