from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render, get_object_or_404, redirect

from registration.models import builder_model
from builder.models import reqapply_model
from builder.reqapply import reqapply_form
from officer.models import quotenot_model
from officer.notiform import notif_form


# Create your views here.
def home(request):
    return HttpResponse("<a href='show_notif'>Show Notifications</a>"
                        )






def show_notif(request):
    context = {}
    context['notif_list'] = quotenot_model.objects.all()
    return render(request, "shownotif.html", context)






# def insert_req(request, did):
#     context = {}
#     obj = get_object_or_404(reqapply_model, id=did)
#     frm = reqapply_form(request.POST or None, instance=obj)
#     if frm.is_valid():
#         frm.save()
#         return HttpResponseRedirect("/builder/reqapply_model")
#     context['reqapply_data'] = frm
#     return render(request, "addreqapply.html", context)

def insert_reqapply(request,nid):
    context = {}
    frm = reqapply_form(request.POST or None, request.FILES or None)
    if request.POST:
        builderid = request.session["builder_id"]
        bid=builder_model.objects.get(pk=builderid)
        notid=quotenot_model.objects.get(pk=nid)
        bid_amt = request.POST.get('bid_amt')
        doc1 = request.FILES.get('doc1')
        doc2 = request.FILES.get('doc2')
        if frm.is_valid():
            reqapply_model.objects.create(builderid=bid, quote_code=notid, bid_amt=bid_amt,
                                         doc1=doc1, doc2=doc2)
            return redirect('/builder')
    context['f'] = frm
    # context['reqapply_list'] = reqapply_model.objects.all()
    return render(request, "addreqapply.html", context)

def show_reqapply(request):
    context = {}
    context['reqapply_list'] = reqapply_model.objects.all()
    return render(request, "addreqapply.html", context)
def update_req(request, did):
    context = {}
    obj = get_object_or_404(reqapply_model, id=did)
    frm = reqapply_form(request.POST or None, instance=obj)
    if frm.is_valid():
        frm.save()
        return HttpResponseRedirect("/builder/insert_reqapply")
    context['reqapply_data'] = frm
    return render(request, "updatereq.html", context)
