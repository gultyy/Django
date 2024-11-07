from django.shortcuts import render

def main(request):
    return render(request, 'third_task/main.html')

def phones(request):
    _phones = {
        'iPhone 666 UltraMegaSuperPro': 'Забыть и не вспоминать этот peace of shit',
        'Samsung A52': 'Продолжить использовать',
        "Nokia 3310": 'Отправить этот экспонат в музей'
    }
    return render(request, 'third_task/phones.html', {'phones': _phones})

def amnezia(request):
    return render(request, 'third_task/amnezia.html')