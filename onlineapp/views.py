from django.shortcuts import render, redirect
from .models import featuredEvent, phonedata, upcomingEvent , upcoming_popup
from django.shortcuts import render, redirect, HttpResponse
from .models import contactUs, enrolldata, subscribe_data, chatdata, phonedata
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

from django.utils.html import strip_tags

from django.conf import settings

from django.core.mail import EmailMultiAlternatives
from django.http import JsonResponse
from .models import chatdata
from django.views.decorators.csrf import csrf_exempt
import re


# Create your views here.

def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def the_future_of_education(request):
    return render(request, 'blog-single.html')


def building_a_growth_mindset(request):
    return render(request, 'blog-single1.html')


def work_education_balance(request):
    return render(request, 'blog-single2.html')


def blog(request):
    return render(request, 'blog.html')


def contact(request):
    return render(request, 'contact.html')


def enrollnow(request):
    return render(request, 'enrollnow.html')


def courses(request):
    return render(request, 'course.html')


def coursedataanalytics(request):
    return render(request, 'coursedataanalytics.html')


def coursecybersecurity(request):
    return render(request, 'coursecybersecurity.html')


def coursecloudcomputing(request):
    return render(request, 'coursecloudcomputing.html')


def instructordetails(request):
    return render(request, 'instructor-details.html')


def instructor(request):
    return render(request, 'instructor.html')


def privacy(request):
    return render(request, 'privacy.html')


def terms(request):
    return render(request, 'terms.html')

def robots(request):
    return render(request, 'robots.txt')

def eroll_data(request):
    if request.method == 'POST':
        fullname = request.POST.get('ename', '')
        emailaddress = request.POST.get('eemail', '')
        mobileno = request.POST.get('ephone', '')
        coures = request.POST.get('eexampleRadios', '')
        email = emailaddress

        html_content = render_to_string('enrolling.html', {'name': fullname})
        text_content = strip_tags(html_content)
        email = EmailMultiAlternatives(
            "Welcome To Eshiksha",
            text_content,
            settings.EMAIL_HOST_USER,
            [emailaddress, settings.EMAIL_HOST_USER]
        )
        print(email, emailaddress)
        email.attach_alternative(html_content, "text/html")
        email.send()

        data = enrolldata(ename=fullname,
            email=emailaddress,
            ephone=mobileno,
            ecourse=coures)
        data.save()
        return redirect('onlineapp:index')
    return redirect('onlineapp:index')


def contact_us(request):
    if request.method == "POST":
        name = request.POST.get('cname', '')
        print(name)
        cemail = request.POST.get('cemail', '')
        mobileno = request.POST.get('cphone', '')
        enquiry = request.POST.get('csubject', '')
        message = request.POST.get('cmessage', '')
        email = cemail

        html_content = render_to_string('contacttemplate.html', {'name': name})
        text_content = strip_tags(html_content)
        email = EmailMultiAlternatives(
            "Welcome To Eshiksha",
            text_content,
            settings.EMAIL_HOST_USER,
            [cemail, settings.EMAIL_HOST_USER]
        )
        print(email, cemail)
        email.attach_alternative(html_content, "text/html")
        email.send()

        data = contactUs(cname=name, cmail=cemail,
                cphone=mobileno, cenquiry=enquiry, cmessage=message)
        data.save()
        return redirect('onlineapp:index')
    return redirect('onlineapp:index')


def maildata(request):
    if request.method == "POST":
        emaildata = request.POST.get('email', '')
        name = request.POST.get('sname', '')
        email = emaildata

        html_content = render_to_string('emailtemplate.html', {'name': name})
        text_content = strip_tags(html_content)
        email = EmailMultiAlternatives(
            "Welcome To Eshiksha",
            text_content,
            settings.EMAIL_HOST_USER,
            [emaildata, settings.EMAIL_HOST_USER]
        )
        print(email, emaildata)
        email.attach_alternative(html_content, "text/html")
        email.send()
        data = subscribe_data(sname=name,
                semail=emaildata)
        data.save()
        print("send")
        return redirect('onlineapp:index')
    return redirect('onlineapp:index')


# def phonedata1(request):
#     if request.method == "POST":
#         phone = request.POST.get('phonedata', '')
#         email=request.POST.get('emailphone')


#         # Assuming you have a model named 'PhoneData' to save the phone number
#         data = phonedata(phone=phone,email=email)
#         data.save()

#         # Return a JSON response indicating success
#         return HttpResponse(status=204)

#     # Render the template if it's a GET request or not submitted through the form
#     return render(request, 'index.html')



import smtplib
from email.message import EmailMessage

def send_email(subject, plain_body, html_body, from_email, to_email):
    msg = EmailMessage()
    msg.set_content(plain_body)
    msg.add_alternative(html_body, subtype='html')
    msg['Subject'] = subject
    msg['From'] = 'learn@eshiksha.ai'
    msg['To'] = to_email

    try:
        # Set up your email server and send the email
        with smtplib.SMTP('smtp-mail.outlook.com', 587) as server:
            server.starttls()
            server.login('learn@eshiksha.ai', 'Cloud@136')  # Update with your email credentials
            server.send_message(msg)
    except Exception as e:
        # Log the exception for debugging purposes
        print(f"Email sending failed: {str(e)}")


def phonedata1(request):
    if request.method == "POST":
        phone = request.POST.get('phonedata', '')
        email = request.POST.get('emailphone')
        name = request.POST.get('phonename')

        # Assuming you have a model named 'PhoneData' to save the phone number
        data = phonedata(phone=phone, email=email, name=name)
        data.save()

        # Send email notification with template
        subject = "eShiksha"
        plain_body = f'A new phone number has been submitted: {phone}'
        html_body = render_to_string('phonedata.html', {'phone': phone, 'name': name})

        # Specify different sender and recipient email addresses
        from_email = settings.EMAIL_HOST_USER
        to_email = email
        send_email(subject, plain_body, html_body, from_email, (to_email , from_email))

        # Return a JSON response indicating success
        return HttpResponse(status=204)

    # Render the template if it's a GET request or not submitted through the form
    return render(request, 'index.html')




def events(request):
    event=upcomingEvent.objects.all()
    fevent=featuredEvent.objects.all()
    return render(request, 'event.html',{'event':event,'fevent':fevent})


# def subcribe_now(request):
#     if request.method == "POST":
#         name = request.POST.get('cname', '')
#         print(name)
#         email = request.POST.get('cemail', '')
#         mobileno = request.POST.get('cphone', '')
#         enquiry = request.POST.get('csubject', '')
#         message = request.POST.get('cmessage', '')
#         data = contactUs(cname=name, cmail=email, cphone=mobileno, cenquiry=enquiry, cmessage=message)
#         data.save()
#         return redirect('onlineapp:index')
#     return redirect('onlineapp:index')


@csrf_exempt
def chatview(request):
    if request.method == "POST" and request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        name = request.POST.get('chatname', '')
        phone = request.POST.get('chatphone', '')
        email = request.POST.get('chatmail', '')

        name_regex = r'^[a-zA-Z\s]+$'
        email_regex = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'
        phone_regex = r'^[0-9]{10}$'

        if not (re.match(name_regex, name) and re.match(email_regex, email) and re.match(phone_regex, phone)):
            return JsonResponse({'success': False, 'message': 'Invalid input'})

        # Save data to chatdata model
        chat_data_instance = chatdata(
            chatname=name, chatphone=phone, chatemail=email)
        chat_data_instance.save()

        return JsonResponse({'success': True})

    return JsonResponse({'success': False, 'message': 'Invalid request'})
    


def popdata(request):
    if request.method == "POST":
        pop_data=upcoming_popup()
        pop_data.name = request.POST.get('popname')
        pop_data.email = request.POST.get('popemail')
        pop_data.phone = request.POST.get('popphone')

        # Assuming 'PopData' is the name of your model
        # data = popdata(name=name1, email=email1, phone=phone1)
        pop_data.save()
        # data.save() is not needed because 'create' already saves the instance

        return redirect("onlineapp:index")  # Redirect to the appropriate view
    else:
        return redirect("onlineapp:index") 
    
def blogs(request):
    return render(request,'blogger.html')
# def popupPhoneData(request):
#     data=phonedata.objects.all()
#     print('data',data)
#     return render(request,'phonedata.html',{'data':data})
