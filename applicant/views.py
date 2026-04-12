from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from django.shortcuts import render, redirect

from registration.models import applicant_model
from adminHome.models import quote_model, district_model, Role_Model, village_model
from adminHome.off import off_form
from adminHome.qtform import qt_form
from applicant.comform import com_form
from applicant.models import request_model, complaint_model
from applicant.reqform import req_form
from officer.models import complrep_model


# Create your views here.
def home(request):
    return render(request,'applicantheader.html')
    # return HttpResponse(
    #                     "<br><br><a href='req_home'>Request for Home</a>"
    #                     "<br><br><a href='insert_complaint'>complaints</a>"
    #                     "<br><br><a href='show_reply'>Comlaint Reply </a>"
    #
    # )



# def req_home(request):
#     context = {}
#     frm = req_form(request.POST or None,request.FILES or None)
#     req = request.POST.get('request')
#     if request_model.objects.filter(appln_no=req).exists():
#         messages.info(request,'req already exists')
#         return redirect('/officer/request_model')
#     else:
#
#         if frm.is_valid():
#             frm.save()
#             return redirect('/officer/request_model')
#     context['f'] = frm
#     context['req_list'] = request_model.objects.all()
#     return render(request, "addreq.html", context)



def req_home(request):
    context = {}
    try:

        frm = req_form(request.POST or None,request.FILES or None)
        if request.POST:

            applicantid = request.session["applicant_id"]
            appid=applicant_model.objects.get(pk=applicantid)
            adhar_no = request.POST.get('adhar_no')
            gender = request.POST.get('gender')
            age = request.POST.get('age')
            photo = request.FILES.get('photo')
            app_job = request.POST.get('app_job')
            idproof = request.FILES.get('idproof')
            plot_available = request.POST.get('plot_available')
            cent = request.POST.get('cent')
            survey_no = request.POST.get('survey_no')
            location = request.POST.get('location')
            loc_type = request.POST.get('loc_type')
            rationcard_no = request.POST.get('rationcard_no')

            if frm.is_valid():
                distid = frm.cleaned_data['plot_distid']
                District = district_model.objects.get(district=distid)
                villageid = frm.cleaned_data['plot_villageid']
                village = village_model.objects.get(village=villageid)

                o = request_model.objects.create(applicantid=appid,  adhar_no=adhar_no, gender=gender,age=age,photo=photo,app_job=app_job,plot_distid=District,plot_villageid=village,idproof=idproof,plot_available=plot_available,cent=cent,survey_no=survey_no,location=location,loc_type=loc_type,rationcard_no=rationcard_no)
                return redirect('/applicant')
    except Exception as ex:
        err_msg = ex
        messages.info(request, ex)

    context['f'] = frm
    return render(request, "addreq.html", context)



def insert_complaint(request):
    context = {}
    frm = com_form(request.POST or None)
    if request.POST:
        complaints = request.POST.get('complaints')
        appid= request.session["applicant_id"]
        appln_no=applicant_model.objects.get(pk=appid)
        role = complaint_model.objects.create(complaints=complaints,appln_no=appln_no)
        return HttpResponse("<script>alert('SUCCESSFULLY SEND YOUR COMPLAINT!!!');window.location='/home';</script>")

    context['f'] = frm
    return render(request, "addcomplaint.html", context)



def show_reply(request):
    context = {}
    context['rep_list'] = complrep_model.objects.all()
    return render(request, "showreply.html", context)
