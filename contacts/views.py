from contacts.models import Contact
from django.shortcuts import redirect, render

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

    
    return render(request, 'Contact.html')
    # return redirect('home')

# def contact(request):
#     return render(request, 'Contact.html')
    
