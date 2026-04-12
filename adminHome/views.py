from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

from registration.models import builder_model, applicant_model
from applicant.models import request_model
from builder.models import reqapply_model
from .design_form import des_form
from .dist_form import dist_form
from .faq_form import fq_form
from .models import designation_model, district_model, village_model, quote_model, office_model, Role_Model, \
    faqQuest_model
from .off import off_form
from .qtform import qt_form
from .vlg_form import vlg_form


# Create your views here.
def home(request):
    return render(request, "adminheader.html")
    # return HttpResponse("<a href='insert_designation'>Designation</a>"
    #                     "<br><br><a href='insert_district'>District</a>"
    #                     "<br><br><a href='insert_vlg'>Village</a>"
    #                     "<br><br><a href='insert_qt'>Quotation</a>"
    #                     "<br><br><a href='add_office'>Office Registration</a>"
    #                     "<br><br><a href='login'>Office Login</a>"
    #                     "<br><br><a href='insert_notif'>Add Notification</a>"
    #                     "<br><br><a href='index'>Add index</a>"
    #                     "<br><br><a href='insert_FAQ'>Provide Frequently Asked Questions</a>"
    #                     )




def insert_designation(request):
    context = {}
    frm = des_form(request.POST or None)
    design = request.POST.get('designation')
    if designation_model.objects.filter(designation=design).exists():
        messages.info(request, 'designation already exists')
        return redirect('/adminHome/insert_designation')
    else:
        if frm.is_valid():
            frm.save()
            return redirect('/adminHome/insert_designation')
    context['f'] = frm
    context['desi_list'] = designation_model.objects.all()
    return render(request, "adddesign.html", context)


def show_designation(request):
    context = {}
    context['desi_list'] = designation_model.objects.all()
    return render(request, "adddesign.html", context)


# update designation

def update_designation(request, did):
    context = {}
    obj = get_object_or_404(designation_model, id=did)
    frm = des_form(request.POST or None, instance=obj)
    if frm.is_valid():
        frm.save()
        return HttpResponseRedirect("/adminHome/insert_designation")
    context['desi_data'] = frm
    return render(request, "updatedesi.html", context)


# delete designation


def delete_designation(request, did):
    context = {}
    obj = get_object_or_404(designation_model, id=did)
    obj.delete()
    return HttpResponseRedirect("/adminHome/insert_designation", context)


def insert_district(request):
    context = {}
    frm = dist_form(request.POST or None)
    dist = request.POST.get('district')
    if district_model.objects.filter(district=dist).exists():
        messages.info(request, 'district already exists')
        return redirect('/adminHome/insert_district')
    else:

        if frm.is_valid():
            frm.save()
            return redirect('/adminHome/insert_district')
    context['f'] = frm
    context['dist_list'] = district_model.objects.all()
    return render(request, "adddist.html", context)


def show_district(request):
    context = {}
    context['dist_list'] = district_model.objects.all()
    return render(request, "adddist.html", context)


def update_district(request, did):
    context = {}
    obj = get_object_or_404(district_model, id=did)
    frm = dist_form(request.POST or None, instance=obj)
    if frm.is_valid():
        frm.save()
        return HttpResponseRedirect("/adminHome/insert_district")
    context['dist_data'] = frm
    return render(request, "updatedist.html", context)


def delete_district(request, did):
    context = {}
    obj = get_object_or_404(district_model, id=did)
    obj.delete()
    return HttpResponseRedirect("/adminHome/insert_district", context)


def insert_vlg(request):
    context = {}
    frm = vlg_form(request.POST or None)
    vlg = request.POST.get('village')
    if village_model.objects.filter(village=vlg).exists():
        messages.info(request, 'village already exists')
        return redirect('/adminHome/insert_vlg')
    else:

        if frm.is_valid():
            frm.save()
            return redirect('/adminHome/insert_vlg')
    context['f'] = frm
    context['vlg_list'] = village_model.objects.all()
    return render(request, "addvlg.html", context)


def show_vlg(request):
    context = {}
    context['vlg_list'] = village_model.objects.all()
    return render(request, "addvlg.html", context)


def update_vlg(request, did):
    context = {}
    obj = get_object_or_404(village_model, id=did)
    frm = vlg_form(request.POST or None, instance=obj)
    if frm.is_valid():
        frm.save()
        return HttpResponseRedirect("/adminHome/insert_vlg")
    context['vlg_data'] = frm
    return render(request, "updatevlg.html", context)


def delete_vlg(request, did):
    context = {}
    obj = get_object_or_404(village_model, id=did)
    obj.delete()
    return HttpResponseRedirect("/adminHome/insert_vlg", context)


def insert_qt(request):
    context = {}
    frm = qt_form(request.POST or None)
    quote = request.POST.get('quotetype')
    if quote_model.objects.filter(quotetype=quote).exists():
        messages.info(request, 'quotation  already exists')
        return redirect('/adminHome/insert_qt')
    else:
        if frm.is_valid():
            frm.save()
            return redirect('/adminHome/insert_qt')
    context['f'] = frm
    context['qt_list'] = quote_model.objects.all()
    return render(request, "addqt.html", context)


def show_quote(request):
    context = {}
    context['qt_list'] = quote_model.objects.all()
    return render(request, "addqt.html", context)


# update designation

def update_quote(request, did):
    context = {}
    obj = get_object_or_404(quote_model, id=did)
    frm = qt_form(request.POST or None, instance=obj)
    if frm.is_valid():
        frm.save()
        return HttpResponseRedirect("/adminHome/insert_qt")
    context['qt_data'] = frm
    return render(request, "updateqt.html", context)


# delete designation


def delete_quote(request, did):
    context = {}
    obj = get_object_or_404(quote_model, id=did)
    obj.delete()
    return HttpResponseRedirect("/adminHome/insert_qt", context)







def office1(request):
    return HttpResponse("<a href='insert_reg'>Sign up</a>")


def add_office(request):
    context = {}
    frm = off_form(request.POST or None)
    if request.POST:
        off_name = request.POST.get('off_name')
        off_address = request.POST.get('address')
        off_mob = request.POST.get('mob')
        off_username = request.POST.get('username')
        off_password = request.POST.get('password')
        off_confpassword = request.POST.get('confirm_password')

        if off_password == off_confpassword:

            if frm.is_valid():
                desigid = frm.cleaned_data['desig']
                off_desig = designation_model.objects.get(designation=desigid)
                distid = frm.cleaned_data['dist']
                off_dist = district_model.objects.get(district=distid)
                villageid = frm.cleaned_data['village']
                off_vlg = village_model.objects.get(village=villageid)

                login_id = User.objects.create_user(username=off_username, password=off_password)

                role = Role_Model.objects.create(role_type='office', login=login_id)
                o = office_model.objects.create(off_name=off_name, desig=off_desig, dist=off_dist, village=off_vlg,
                                                address=off_address, mob=off_mob, login=login_id)
                return redirect('/adminHome')
        else:
            messages.info(request, 'Invalid password')

    context['f'] = frm

    # context["prod_freq_data"] = Agents_Model.objects.all()
    return render(request, "addoff.html", context)



def insert_FAQ(request):
    context = {}
    frm = fq_form(request.POST or None)
    faq = request.POST.get('faqQuest')
    if faqQuest_model.objects.filter(faqQuest=faq).exists():
        messages.info(request, 'Question already exists')
        return redirect('/adminHome/insert_FAQ')
    else:
        if frm.is_valid():
            frm.save()
            return redirect('/adminHome/insert_FAQ')
    context['f'] = frm
    context['fq_list'] = faqQuest_model.objects.all()
    return render(request, "addfaq.html", context)


def show_FAQ(request):
    context = {}
    context['fq_list'] = faqQuest_model.objects.all()
    return render(request, "addfaq.html", context)


# update FAQ

def update_FAQ(request, did):
    context = {}
    obj = get_object_or_404(faqQuest_model, id=did)
    frm = fq_form(request.POST or None, instance=obj)
    if frm.is_valid():
        frm.save()
        return HttpResponseRedirect("/adminHome/insert_FAQ")
    context['fq_data'] = frm
    return render(request, "updatefaq.html", context)


# delete FAQ


def delete_FAQ(request, did):
    context = {}
    obj = get_object_or_404(faqQuest_model, id=did)
    obj.delete()
    return HttpResponseRedirect("/adminHome/insert_FAQ", context)

def view_applicant(request):
    context = {}
    context['applicant_list'] = applicant_model.objects.all()
    return render(request, "viewapplicant.html", context)

def view_project(request):
    context = {}
    context['project_list'] = request_model.objects.all()
    return render(request, "viewproject.html", context)
def more_request(request,id):
    context = {}
    context['project_list'] = request_model.objects.filter(pk=id)
    return render(request, "moreproject.html", context)

# def survey(request):
#     context = {}
#     frm = fq_form(request.POST or None)
#     survy = request.POST.get('survey')
#     if survey_model.objects.filter(survey=survy).exists():
#         messages.info(request, ' already exists')
#         return redirect('/adminHome/survey')
#     else:
#         if frm.is_valid():
#             frm.save()
#             return redirect('/adminHome/survey')
#     context['f'] = frm
#     context['fq_list'] = survey_model.objects.all()
#     return render(request, "survey.html", context)
