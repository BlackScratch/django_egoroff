from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.
def get_info_about_zodiac_sign(requests, sign_zodiac):
    if sign_zodiac == 'leo':
        return HttpResponse("Лев")
    elif sign_zodiac == 'Sagittarius':
        return HttpResponse("Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря)")
    elif sign_zodiac == 'Libra':
        return HttpResponse("Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).")
    elif sign_zodiac == 'Cancer':
        return HttpResponse("Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).")
    elif sign_zodiac == 'Capricorn':
        return HttpResponse("Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января.")
    elif sign_zodiac == 'Aquarius':
        return HttpResponse("Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля.)")
    elif sign_zodiac == 'Gemini':
        return HttpResponse("Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).")
    elif sign_zodiac == 'Taurus':
        return HttpResponse("Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).'")
    elif sign_zodiac == 'scorpion':
        return HttpResponse("Знак зодиака скорпион.'")
    else:
        return HttpResponse(f"Неизвестно чо такое {sign_zodiac}")


