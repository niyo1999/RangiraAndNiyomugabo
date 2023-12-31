from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from core.models import Speaker
from core.forms import ContactForm
from core.models import Contact


def home(request):
    return render(request, 'core/home.html')


@login_required
def contact(request):
    form = ContactForm()
    # Ensures that submit button has been clicked!
    if request.method == 'POST':
        # form with data
        form = ContactForm(request.POST)
        # checking if form validation is correct
        if form.is_valid():
            # getting input data
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            # storing the data in Contact Model
            Contact.objects.create(name=name, email=email, message=message)
    else:
        form = ContactForm()
    return render(request, 'core/contact.html', {'form': form})


def viewSpeaker(request, id):
    speaker = Speaker.objects.get(id=id)

    return render(request, 'core/viewspeaker.html', {'speaker': speaker})