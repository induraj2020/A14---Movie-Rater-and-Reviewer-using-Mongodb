from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template


# Create your views here.
def home(request):
    #return HttpResponse('<h1> Blog Home <h1>')
    return render(request, 'homescreen/home.html')

def contact(request):
    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('homescreen/contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
                }
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" +'',
                ['induraj2020@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return redirect('homescreen-home-1')

    return render(request, 'homescreen/contact.html', {
        'form': form_class,
    })

