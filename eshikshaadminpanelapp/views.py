from django.shortcuts import render
from onlineapp.models import *
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect
from .form import LoginForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
# Create your views here.

STATUS_OPTIONS = [
    ('Not contacted','Not Contacted'),
    ('Contacted','Contacted')
]

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

@login_required
def home(request):
    response = render(request, 'adminpanel/index.html')
    response['Cache-Control'] = 'no-store'
    return response

@login_required
def contact_us(request):
    print('view start')
    contact = contactUs.objects.all()
    # LeadSource=LeadInSource.objects.all()
    context ={
        'contactUs':contact,
        # 'LeadSource':LeadSource,
        'statuses':STATUS_OPTIONS,
    }
    return render(request,'adminpanel/contactus.html', context)

@login_required
def update_contact_status(request):
    if request.method == "POST":
        contact_id = request.POST.get("contact_id")
        selected_status = request.POST.get("status")
        selected_remark = request.POST.get("remark")
        lead_source = request.POST.get('leadsrc')
        lead_assigned=request.POST.get('lead_assigned')
        lead_status=request.POST.get('leadstatus')
        cell_1=request.POST.get('cell1')
        cell_2=request.POST.get('cell2')
        note=request.POST.get('notes')
        Date=request.POST.get('lead_close_date')


        try:
            contact = contactUs.objects.get(id=contact_id)
            contact.cstatus = selected_status
            contact.cremark = selected_remark
            contact.lead_in_source=lead_source
            contact.lead_assigned=lead_assigned
            contact.lead_status=lead_status
            contact.cell1=cell_1
            contact.cell2=cell_2
            contact.notes=note
            contact.date=Date

            contact.save()
            print(contact.lead_in_source)
            # Redirect back to the contact_us page after successful update
            return redirect('eshikshaadminpanelapp:contact_us')
        except contactUs.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Contact not found"})
    return JsonResponse({"status": "error", "message": "Invalid request"})


@login_required
def news_letters(request):
    subscribe = subscribe_data.objects.all()
    context ={
        'subscribe_data':subscribe,
        'statuses':STATUS_OPTIONS,
    }
    return render(request,'adminpanel/newsletters.html', context)

@login_required
def update_newsletters_status(request):
    if request.method == "POST":
        newsletters_id = request.POST.get("newsletters_id")
        selected_status = request.POST.get("status")
        selected_remark = request.POST.get("remark")

        lead_source = request.POST.get('leadsrc')
        lead_assigned=request.POST.get('lead_assigned')
        lead_status=request.POST.get('leadstatus')
        cell_1=request.POST.get('cell1')
        cell_2=request.POST.get('cell2')
        note=request.POST.get('notes')
        Date=request.POST.get('lead_close_date')

        try:
            newsletters = subscribe_data.objects.get(id=newsletters_id)
            newsletters.sstatus = selected_status
            newsletters.sremark = selected_remark
            newsletters.lead_in_source=lead_source
            newsletters.lead_assigned=lead_assigned
            newsletters.lead_status=lead_status
            newsletters.cell1=cell_1
            newsletters.cell2=cell_2
            newsletters.notes=note
            newsletters.date=Date
            newsletters.save()
            return redirect('eshikshaadminpanelapp:news_letters')
        except contactUs.DoesNotExist:
            return JsonResponse({"status":"error","message":"Contact not found"})
    return JsonResponse({"status":"error","message":"Invalid request"})

@login_required
def brouchers(request):
    broucher = enrolldata.objects.all()
    context= {
        'enrolldata':broucher,
        'statuses':STATUS_OPTIONS
    }
    return render(request,'adminpanel/brouchers.html',context)

@login_required
def update_brouchers_status(request):
    if request.method == "POST":
        brouchers_id = request.POST.get("brouchers_id")
        selected_status = request.POST.get("status")
        selected_remark = request.POST.get("remark")
        lead_source = request.POST.get('leadsrc')
        lead_assigned=request.POST.get('lead_assigned')
        lead_status=request.POST.get('leadstatus')
        cell_1=request.POST.get('cell1')
        cell_2=request.POST.get('cell2')
        note=request.POST.get('notes')
        Date=request.POST.get('lead_close_date')
        try:
            brouchers = enrolldata.objects.get(id=brouchers_id)
            brouchers.estatus = selected_status
            brouchers.eremark = selected_remark
            brouchers.lead_in_source=lead_source
            brouchers.lead_assigned=lead_assigned
            brouchers.lead_status=lead_status
            brouchers.cell1=cell_1
            brouchers.cell2=cell_2
            brouchers.notes=note
            brouchers.date=Date
            brouchers.save()
            return redirect('eshikshaadminpanelapp:brouchers')
        except contactUs.DoesNotExist:
            return JsonResponse({"status":"error","message":"Contact not found"})
    return JsonResponse({"status":"error","message":"Invalid request"})


    
        

@login_required
def enquiries(request):
    enquiry = phonedata.objects.all()
    context ={
        'phonedata':enquiry,
        'statuses':STATUS_OPTIONS
    }
    return render(request, 'adminpanel/enquiry.html',context)

@login_required
def update_enquiry_status(request):
    if request.method == "POST":
        enquiry_id = request.POST.get("enquiry_id")
        selected_status = request.POST.get("status")
        selected_remark = request.POST.get("remark")
        lead_source = request.POST.get('leadsrc')
        lead_assigned=request.POST.get('lead_assigned')
        lead_status=request.POST.get('leadstatus')
        cell_1=request.POST.get('cell1')
        cell_2=request.POST.get('cell2')
        note=request.POST.get('notes')
        Date=request.POST.get('lead_close_date')

        try:
            enquiries = phonedata.objects.get(id=enquiry_id)
            enquiries.pstatus = selected_status
            enquiries.premark = selected_remark
            enquiries.lead_in_source=lead_source
            enquiries.lead_assigned=lead_assigned
            enquiries.lead_status=lead_status
            enquiries.cell1=cell_1
            enquiries.cell2=cell_2
            enquiries.notes=note
            enquiries.date=Date
            enquiries.save()
            return redirect('eshikshaadminpanelapp:enquiries')
        except contactUs.DoesNotExist:
            return JsonResponse({"status":"error","message":"Contact not found"})
    return JsonResponse({"status":"error","message":"Invalid request"})

def user_login(request):
    if request.user.is_authenticated:
        return redirect(reverse_lazy("eshikshaadminpanelapp:index"))
    
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        print(username, password)
        user = authenticate(username=username,password=password)
        
        if user is None:
            request.session['login_error']="*Invalid credentials."
            return redirect(reverse_lazy("eshikshaadminpanelapp:user_login"))
        
        if 'login_error' in request.session:
            del request.session['login_error']
            
        if user is not None:
            login(request,user)
            messages.success(request,"Logged In successfully")
            return redirect(reverse_lazy("eshikshaadminpanelapp:index"))
        
    return render(request, "adminpanel/login.html")


@login_required
def user_logout(request):
    logout(request)
    messages.success(request,"Logged out successfully")
    return render(request,'adminpanel/login.html')













