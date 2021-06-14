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
        Phone_no = request.POST['Phone_no']

        # Contact.objects.create(first_name=first_name, last_name=last_name, email=email, subject=subject, message=message)
        contact = Contact(first_name=first_name, last_name=last_name, email=email, subject=subject, message=message)
        # contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id)
        # Contact.save()
        contact.save()

        send_mail( 
            subject,
            # 'Subject',
            'A user has sent us a message:' + message + ' from ' + first_name + last_name + ' his contact details ' + email +' ' + Phone_no,
            EMAIL_HOST_USER, # from email
            [EMAIL_HOST_USER], # to email
            fail_silently = False,
        )

        send_mail (
            'Email Sent to the admin Team', # Subject
            # message 
            'Hello Mr/Mrs, ' + first_name +' ' + last_name + '\n\nHope you are having fantastic day your message with the subject "' + subject +'" has been sent to our admin team. \n\nWe will get back to you shortly. \n\nThank you for contacting us. \n\nRegards, /n/nAdmin Team',  
            EMAIL_HOST_USER, # from email
            [email], # to email
            fail_silently=False,
        )
        
        return redirect('home')
    else:
        return render(request, 'Contact.html')

# def contact(request):
#     return render(request, 'Contact.html')
    
