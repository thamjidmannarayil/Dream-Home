from django.shortcuts import get_object_or_404, redirect

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from django.shortcuts import render

from registration.models import applicant_model, builder_model
from adminHome.models import office_model

from applicant.models import request_model, complaint_model
from builder.models import reqapply_model
from .editoffice import editoff_form
from .models import project_model, plot_model, quotenot_model, complrep_model, surveyreport_model
from .notiform import notif_form
from .plotform import plt_form
from .prjt_form import proj_form
from .surveyform import survey_form


# Create your views here.
def home(request):
    return render(request,"officerheader.html")
    # return HttpResponse("<a href='update_office'>UPDATE OFFICER</a>"
    #                     "<br><br><a href='insert_project'>PUBLISH NEW HOME PROJECT</a>"
    #                     "<br><br><a href='insert_plot'>PUBLISH PLOT DETAILS</a>"
    #                     "<br><br><a href='show_request'>HOME REQUESTS</a>"
    #                     "<br><br><a href = 'insert_notif' > PUBLISH QUOTATION NOTIFICATIONS </a>"
    #                     "<br><br><a href = 'show_complaint' >COMPLAINTS </a>"
    #                     "<br><br><a href = 'insert_survey' > PREPARE SURVEY REPORT </a>"
    #                     "<br><br><a href = 'notification_list' >SHOW REQUEST NOTIFICATION </a>"
    #                     "<br><br><a href = 'notification_list_approved' >SHOW APPROVED QUOTATION LIST </a>"
    #
    # # <a href='activate_builderQuote'>ACTIVATE BUILDER QUOTATION</a>"
    #
    #                     )





def update_office(request):
    context = {}
    id=request.session["office_id"]
    obj = get_object_or_404(office_model,id=id)
    frm = editoff_form(request.POST or None, instance=obj)
    if frm.is_valid():
        frm.save()
        return HttpResponseRedirect("/officer")
    context['off_data'] = frm
    return render(request, "updateoff.html", context)



# delete designation

def delete_office(request):
    context = {}
    obj = get_object_or_404(office_model)
    obj.delete()
    return HttpResponseRedirect("/adminHome/add_office", context)



def insert_project(request):
    context = {}
    frm = proj_form(request.POST or None,request.FILES or None)
    proj = request.POST.get('scheme')
    if project_model.objects.filter(scheme=proj).exists():
        messages.info(request,'project already exists')
        return redirect('/officer/insert_project')
    else:

        if frm.is_valid():
            frm.save()
            return redirect('/officer/insert_project')
    context['f'] = frm
    context['proj_list'] = project_model.objects.all()
    return render(request, "addproj.html", context)


def show_project(request):
    context = {}
    context['proj_list'] = project_model.objects.all()
    return render(request, "addproj.html", context)


def update_project(request, did):
    context = {}
    obj = get_object_or_404(project_model, id=did)
    frm = proj_form(request.POST or None, instance=obj)
    if frm.is_valid():
        frm.save()
        return HttpResponseRedirect("/officer/insert_project")
    context['proj_data'] = frm
    return render(request, "updateproj.html", context)


def delete_project(request, did):
    context = {}
    obj = get_object_or_404(project_model, id=did)
    obj.delete()
    return HttpResponseRedirect("/officer/insert_project", context)





def insert_plot(request):
    context = {}
    frm = plt_form(request.POST or None,request.FILES or None)
    plt = request.POST.get('plot')
    if plot_model.objects.filter(plot=plt).exists():
        messages.info(request,'plot already exists')
        return redirect('/officer/insert_plot')
    else:

        if frm.is_valid():
            frm.save()
            return redirect('/officer/insert_plot')
    context['f'] = frm
    context['plt_list'] = plot_model.objects.all()
    return render(request, "addplot.html", context)


def show_plot(request):
    context = {}
    context['plt_list'] = plot_model.objects.all()
    return render(request, "addplot.html", context)


def update_plot(request, did):
    context = {}
    obj = get_object_or_404(plot_model, id=did)
    frm = plt_form(request.POST or None, instance=obj)
    if frm.is_valid():
        frm.save()
        return HttpResponseRedirect("/officer/insert_plot")
    context['plt_data'] = frm
    return render(request, "updateplot.html", context)


def delete_plot(request, did):
    context = {}
    obj = get_object_or_404(plot_model, id=did)
    obj.delete()
    return HttpResponseRedirect("/officer/insert_plot", context)



def insert_survey(request):
    context = {}
    frm = survey_form(request.POST or None,request.FILES or None)
    surv = request.POST.get('survey')
    if surveyreport_model.objects.filter(verifyby=surv).exists():
        messages.info(request,'survey already exists')
        return redirect('/officer/insert_survey')
    else:

        if frm.is_valid():
            frm.save()
            return redirect('/officer/insert_survey')
    context['f'] = frm
    context['surv_list'] = surveyreport_model.objects.all()
    return render(request, "addsurvey.html", context)





def show_request(request):
    context = {}
    context['req_list'] = request_model.objects.filter(status='New')
    return render(request, "addreq.html", context)

def verify(request,did):
    context = {}
    request_model_obj = get_object_or_404(request_model, id=did)

    # Assuming 'status' is the field to be updated
    new_status = 'Active'
    request_model_obj.status = new_status
    request_model_obj.save()
    return HttpResponseRedirect('/officer/show_request',context)



def insert_notif(request):
    context = {}
    frm = notif_form(request.POST or None,request.FILES or None)
    ntf = request.POST.get('notification')
    if quotenot_model.objects.filter(quote_name=ntf).exists():
        messages.info(request,'notification already exists')
        return redirect('/officer/insert_notif')
    else:

        if frm.is_valid():
            frm.save()
            return redirect('/officer/insert_notif')
    context['f'] = frm
    context['notif_list'] = quotenot_model.objects.all()
    return render(request, "addnotif.html", context)




def show_notif(request):
    context = {}
    context['notif_list'] = quotenot_model.objects.all()
    return render(request, "addnotif.html", context)


def apply_notif(request, did):
    context = {}
    obj = get_object_or_404(quotenot_model, id=did)
    frm = notif_form(request.POST or None, instance=obj)
    if frm.is_valid():
        frm.save()
        return HttpResponseRedirect("/builder/insert_reqapply")
    context['notif_data'] = frm
    return render(request, "addreqapply.html", context)


def show_complaint(request):
    context = {}
    context['com_list'] = complaint_model.objects.filter(status='INACTIVE')
    return render(request, "showcompl.html", context)


def show_notification(request):
    context = {}
    context['quo_list'] = quotenot_model.objects.filter(status='NEW')
    return render(request, "notiflist.html", context)





def insert_reply(request,cid):

    if request.POST:
        reply = request.POST.get('reply')
        cid = request.POST.get('cid')
        com_id=complaint_model.objects.get(pk=cid)


        role = complrep_model.objects.create(complaint=com_id,reply=reply)
        return HttpResponse("<script>alert('SUCCESSFULLY SEND YOUR REPLY!!!');window.location='/show_complaint';</script>")


    return render(request, "addcomplrep.html", {'cid':cid})





def show_builder(request):
    context = {}
    context['build_list'] = builder_model.objects.filter(status='INACTIVE')
    return render(request, "view_builder.html", context)



def activate_builder(request,sid):
    context = {}
    builder_obj = get_object_or_404(builder_model, id=sid)

    # Assuming 'status' is the field to be updated
    new_status = 'Active'
    builder_obj.status = new_status
    builder_obj.save()
    return HttpResponseRedirect('/officer/notification_list')


def show_reapply(request,id):
    context = {}
    context['reqapply_list'] = reqapply_model.objects.filter(quote_code=id,bid_status='New')
    return render(request, "showreqapply.html", context)

def activate_builderQuote(request,sid):
    context = {}
    builder_obj = get_object_or_404(reqapply_model, id=sid)

    # Assuming 'status' is the field to be updated
    bid_status = 'Approved'
    builder_obj.bid_status = bid_status
    builder_obj.save()
    return HttpResponseRedirect('/officer/notification_list')


def notification_list(request):
    context = {}
    context['notif_list'] = quotenot_model.objects.all()
    return render(request, "notiflist.html", context)

def notification_list_approved(request):
    context = {}
    context['notif_list'] = quotenot_model.objects.all()
    return render(request, "approvedQt.html", context)
def approved_quotationlist(request,id):
    context = {}
    context['reqapply_list'] = reqapply_model.objects.filter(quote_code=id,bid_status='Approve')
    return render(request, "showreqapply.html", context)

def view_project1(request):
    context = {}
    context['project_list'] = request_model.objects.all()
    return render(request, "viewproject_officer.html", context)
def more_request1(request,id):
    context = {}
    context['project_list'] = request_model.objects.filter(pk=id)
    return render(request, "moreproject_officer.html", context)

def approve_projectlist(request,sid):
    context = {}
    request_obj = get_object_or_404(request_model, id=sid)

    # Assuming 'status' is the field to be updated
    new_status = 'Active'
    request_obj.status = new_status
    request_obj.save()
    return render(request, "moreproject_officer.html", context)