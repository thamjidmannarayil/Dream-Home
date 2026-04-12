from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import context

from .applicant_form import applicant_form
from adminHome.models import Role_Model, district_model, office_model
from registration.build_form import build_form
from registration.models import builder_model, applicant_model


def home(request):
    return redirect(login)
    # return HttpResponse("<a href='insert_builder'>Builder's Registration</a>"
    #                     "<br><br><a href='insert_applicant'>Applicant's Registration</a>"
    #                     "<br><br><a href='login'> Login</a>"
    #                     )
def insert_builder(request, distid=None):
    context = {}
    try:

        frm = build_form(request.POST or None,request.FILES or None)
        if request.POST:
            builder_name = request.POST.get('builder_name')
            licenseno = request.POST.get('licenseno')
            licencedate = request.POST.get('licencedate')
            id_proof = request.FILES.get('id_proof')
            up_doc = request.FILES.get('up_doc')
            phone = request.POST.get('phone')
            email = request.POST.get('email')

            build_username = request.POST.get('username')
            build_password = request.POST.get('password')
            build_confpassword = request.POST.get('confirm_password')


            if   build_password  == build_confpassword :
                if frm.is_valid():
                    distid = frm.cleaned_data['District']
                    District = district_model.objects.get(district=distid)


                    login_id = User.objects.create_user(username=build_username, password=build_password)

                    role = Role_Model.objects.create(role_type='builder', login=login_id)
                    o = builder_model.objects.create(builder_name=builder_name, licenseno=licenseno, licencedate=licencedate, id_proof=id_proof,up_doc=up_doc,email=email,login=login_id,District=District,phone=phone)
                    return redirect(login)
            else:
                messages.info(request, ' password Does not match')
    except Exception as ex:
        err_msg=ex
        messages.info(request,ex)


    context['f'] = frm


    return render(request, "addbuilder.html", context)











def login(request):
    if request.POST:
        context={}
        Uname=request.POST.get('username')
        paswrd=request.POST.get('password')
        user=authenticate(username=Uname,password=paswrd)
        if user is not None:
            user_id=user.id
            sp=user.is_superuser
            if sp is True:
                return HttpResponseRedirect('/adminHome')
            roll_obj=Role_Model.objects.filter(login=user_id)
            for role_obj in roll_obj:
                type=role_obj.role_type
                print(type)

                if type=='builder':

                    builder_object=builder_model.objects.filter(login=user_id)
                    for obj in builder_object:
                        request.session["builder_id"]=obj.id
                        request.session["builder_name"]=obj.builder_name

                        return HttpResponseRedirect('/builder')
                elif type == 'applicant':

                    applicant_object = applicant_model.objects.filter(login=user_id)
                    for obj in applicant_object:
                        request.session["applicant_id"] = obj.id
                        request.session["applicant_name"] = obj.applicant_name

                        return HttpResponseRedirect('/applicant')
                elif type == 'office':

                    office_object = office_model.objects.filter(login=user_id)
                    for obj in office_object:
                        request.session["office_id"] = obj.id
                        request.session["office_name"] = obj.off_name

                        return HttpResponseRedirect('/officer')

        else:
            return HttpResponse("<script>alert('Invalid Credential !!!');window.location='/login';</script>")
    return render(request, "login.html")





# def login(request):
#     if request.POST:
#         context={}
#         Uname=request.POST.get('username')
#         paswrd=request.POST.get('password')
#         user=authenticate(username=Uname,password=paswrd)
#         if user is not None:
#             return HttpResponseRedirect('/Registration')
#         else:
#             return HttpResponse("<script>alert('Invalid Credential !!!');window.location='/login';</script>")
#     return render(request, "login1.html")

def insert_applicant(request):
    context = {}
    try:

        frm = applicant_form(request.POST or None)
        if request.POST:
            applicant_name = request.POST.get('applicant_name')
            address = request.POST.get('address')
            email = request.POST.get('email')
            mobile = request.POST.get('mobile')


            applicant_username = request.POST.get('username')
            applicant_password = request.POST.get('password')
            applicant_confpassword = request.POST.get('confirm_password')


            if   applicant_password  == applicant_confpassword :
                if frm.is_valid():
                    login_id = User.objects.create_user(username=applicant_username, password=applicant_password)

                    role = Role_Model.objects.create(role_type='applicant', login=login_id)
                    o = applicant_model.objects.create(applicant_name=applicant_name,address=address,login=login_id,email=email,mobile=mobile)
                    return redirect(login)
            else:
                messages.info(request, ' password Does not match')
    except Exception as ex:
        err_msg=ex
        messages.info(request,ex)


    context['f'] = frm


    return render(request, "addapplicant.html", context)





