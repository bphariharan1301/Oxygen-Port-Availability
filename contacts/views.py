from Covid_Support.settings import EMAIL_HOST_USER
from contacts.models import Contact
from django.shortcuts import redirect, render
from django.core.mail import send_mail

# Create your views here.

def contact(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        # Contact.objects.create(first_name=first_name, last_name=last_name, email=email, subject=subject, message=message)
        contact = Contact(first_name=first_name, last_name=last_name, email=email, subject=subject, message=message)
        # contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id)
        # Contact.save()
        contact.save()

        send_mail( 
            subject,
            # 'Subject',
            'A user has sent us a message:' + message + ' from ' + first_name + last_name + ' his contact details /n' + email,
            email, # from email
            # ['tiwariashu@pm.me', EMAIL_HOST_USER], # to email
            [EMAIL_HOST_USER], # to email
            fail_silently = False,
        )
        print(email)
        
        return redirect('contact-us')
    else:
        return render(request, 'Contact.html')

# def contact(request):
#     return render(request, 'Contact.html')
    
