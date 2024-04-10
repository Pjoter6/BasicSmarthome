from django.shortcuts import render
from django.http import HttpResponseRedirect

# Słownik symulujący stan urządzeń
device_status = {
    'light': False,
    'camera': False,
    'temperature': 22.5,  # Symulacja odczytu temperatury
}


def home(request):
    if request.method == 'POST':
        device = request.POST.get('device')
        if device in ['light', 'camera']:
            device_status[device] = not device_status[device]
        return HttpResponseRedirect('/')

    return render(request, 'home.html', {'device_status': device_status})
