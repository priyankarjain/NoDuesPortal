from django.contrib.auth.models import Permission
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import View
from django.http import HttpResponse
from . import forms


# Create your views here.



class FormView(View):
    form_class = forms.Registration
    template_name = "registration/regform.html"

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            designation = form.cleaned_data['designation']

            user.username = username
            user.email = username + "@iitg.ernet.in"
            user.set_password(password)
            user.save()
            d = designation

            flag = 1

            if str(d.type) == "Student":
                flag = 0
            user.designation = d

            if int(flag) == 1:
                user.is_staff = True
            else:
                user.is_staff = False

            if user.is_staff:
                p1 = Permission.objects.get(name='Can add nodue')
                p2 = Permission.objects.get(name='Can delete nodue')
                p3 = Permission.objects.get(name='Can change nodue')
                p4 = Permission.objects.get(name='Can delete grant clearance')
                p5 = Permission.objects.get(name='Can change grant clearance')
                user.user_permissions.add(p1, p2, p3,p4,p5)
            else:
                p1 = Permission.objects.get(name='Can add grant clearance')
                user.user_permissions.add(p1)

            user.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if user.designation.type == 'Student':
                        print("Student")
                        return redirect('registration:stud')
                    elif user.designation.type == 'Professor':
                        print("Professor")
                        return redirect('registration:prof')
                    elif user.designation.type == 'HOD':
                        print("HOD")
                        return redirect('registration:hod')
                    elif user.designation.type == 'Caretaker':
                        print("CareTaker")
                        return redirect('registration:care')
                    elif user.designation.type == 'Warden':
                        print("Professor")
                        return redirect('registration:ward')
                    elif user.designation.type == 'Administrative':
                        print("Professor")
                        return redirect('registration:ad')
                    else:
                        print("Not")
                else:
                    print("Not active")
            else:
                print("None")
        return render(request, self.template_name, {'form': form})


def welcome(request):
    send = "<h1>" + request.user.designation + "</h1>"
    return HttpResponse(send)


class StudForm(View):
    form_class = forms.RegStud
    template_name = "registration/secform.html"

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form, 'URL': '.'})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']

            request.user.first_name = first_name
            request.user.last_name = last_name
            request.user.save()

            student = form.save(commit=False)
            student.p_id = request.user
            student.save()
            return redirect("registration:studProf")
        else:
            print("this aint working")
            return render(request, self.template_name, {'form': form, 'URL': '.'})


def studProf(request):
    return HttpResponse("<h1>Hi u Are logged in as Student</h1>")


class ProfForm(View):
    form_class = forms.RegProf
    template_name = "registration/secform.html"

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form, 'URL': '.'})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']

            request.user.first_name = first_name
            request.user.last_name = last_name
            request.user.save()

            professor = form.save(commit=False)
            professor.p_id = request.user
            professor.save()
            return redirect("registration:ProfWel")
        else:
            print("this aint working")
            return render(request, self.template_name, {'form': form, 'URL': '.'})


def ProfWel(request):
    return HttpResponse("<h1>Hi u Are logged in as Prof</h1>")

class HodForm(View):
    form_class = forms.RegHod
    template_name = "registration/secform.html"

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form, 'URL': '.'})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']

            request.user.first_name = first_name
            request.user.last_name = last_name
            request.user.save()

            professor = form.save(commit=False)
            professor.p_id = request.user
            professor.save()
            return redirect("registration:HodWel")
        else:
            print("this aint working")
            return render(request, self.template_name, {'form': form, 'URL': '.'})

def HodWel(request):
    return HttpResponse("<h1>Hi u Are logged in as HOD</h1>")

class WardForm(View):
    form_class = forms.RegWard
    template_name = "registration/secform.html"

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form, 'URL': '.'})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']

            request.user.first_name = first_name
            request.user.last_name = last_name
            request.user.save()

            warden = form.save(commit=False)
            warden.p_id = request.user
            warden.save()
            return redirect("registration:WardWel")
        else:
            print("this aint working")
            return render(request, self.template_name, {'form': form, 'URL': '.'})


def WardWel(request):
    return HttpResponse("<h1>Hi u Are logged in as Warden</h1>")

class CareForm(View):
    form_class = forms.RegCare
    template_name = "registration/secform.html"

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form, 'URL': '.'})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']

            request.user.first_name = first_name
            request.user.last_name = last_name
            request.user.save()

            warden = form.save(commit=False)
            warden.p_id = request.user
            warden.save()
            return redirect("registration:CareWel")
        else:
            print("this aint working")
            return render(request, self.template_name, {'form': form, 'URL': '.'})


def CareWel(request):
    return HttpResponse("<h1>Hi u Are logged in as CareTaker</h1>")

class AdminForm(View):
    form_class = forms.RegAdmin
    template_name = "registration/secform.html"

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form, 'URL': '.'})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']

            request.user.first_name = first_name
            request.user.last_name = last_name
            request.user.save()

            ad = form.save(commit=False)
            ad.p_id = request.user
            ad.save()
            return redirect("registration:AdminWel")
        else:
            print("this aint working")
            return render(request, self.template_name, {'form': form, 'URL': '.'})


def AdminWel(request):
    return HttpResponse("<h1>Hi u Are logged in as Admins</h1>")