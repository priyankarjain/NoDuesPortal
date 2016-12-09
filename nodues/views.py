from django.shortcuts import render,HttpResponse,redirect
from django.views import View
from django.contrib.auth import authenticate, login
from .models import Nodue,User,Administrative,Warden,Prof, Student,Caretaker,HeadOfDep,GrantClearance
# Create your views here.
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect("/stud/")


def hello(request):
    return HttpResponse("<h1>Welcome</h1>")

def sendClearence(request):
    u_id=request.user.id
    usr=Student.objects.filter(p_id=u_id)[0]
    department=usr.department
    hostel=usr.hostel

    profs=Prof.objects.filter(department__exact=department)
    ward=Warden.objects.filter(hostel__exact=hostel)[0]
    care=Caretaker.objects.filter(hostel__exact=hostel)[0]
    hod=HeadOfDep.objects.filter(department__exact=department)[0]
    lib=Administrative.objects.filter(department__exact='1')[0]
    cc=Administrative.objects.filter(department__exact='2')[0]
    occ=Administrative.objects.filter(department__exact='3')[0]
    st=Administrative.objects.filter(department__exact='4')[0]
    gk=Administrative.objects.filter(department__exact='5')[0]
    ar=Administrative.objects.filter(department__exact='6')[0]
    acc=Administrative.objects.filter(department__exact='7')[0]

    usr = User.objects.get(pk=u_id)

    a={}
    i=0

    a["profs"]={}
    b={}
    for p in profs:
        prf=User.objects.get(pk=p.p_id_id)
        cl=GrantClearance.objects.filter(b_id=usr,l_id=prf)
        if(cl.count()==0):
            GrantClearance(b_id=usr, l_id=prf, approved=False).save()
        else:
            b[str(i+1)]=cl.values()
            i+=1
            print("Hello")
    a["profs"]=b

    prf = User.objects.get(pk=ward.p_id_id)
    cl = GrantClearance.objects.filter(b_id=usr, l_id=prf)
    if (cl.count() == 0):
        GrantClearance(b_id=usr, l_id=prf, approved=False).save()
    else:
        a["ward"]=cl.values()
        print("Hello")

    prf = User.objects.get(pk=care.p_id_id)
    cl = GrantClearance.objects.filter(b_id=usr, l_id=prf)
    if (cl.count() == 0):
        GrantClearance(b_id=usr, l_id=prf, approved=False).save()
    else:
        a["care"]=cl.values()
        print("Hello")

    prf = User.objects.get(pk=hod.p_id_id)
    cl = GrantClearance.objects.filter(b_id=usr, l_id=prf)
    if (cl.count() == 0):
        GrantClearance(b_id=usr, l_id=prf, approved=False).save()
    else:
        a["hod"]=cl.values()
        print("Hello")

    prf = User.objects.get(pk=lib.p_id_id)
    cl = GrantClearance.objects.filter(b_id=usr, l_id=prf)
    if (cl.count() == 0):
        GrantClearance(b_id=usr, l_id=prf, approved=False).save()
    else:
        a["lib"]=cl.values()
        print("Hello")

    prf = User.objects.get(pk=cc.p_id_id)
    cl = GrantClearance.objects.filter(b_id=usr, l_id=prf)
    if (cl.count() == 0):
        GrantClearance(b_id=usr, l_id=prf, approved=False).save()
    else:
        a["cc"]=cl.values()
        print("Hello")

    prf = User.objects.get(pk=occ.p_id_id)
    cl = GrantClearance.objects.filter(b_id=usr, l_id=prf)
    if (cl.count() == 0):
        GrantClearance(b_id=usr, l_id=prf, approved=False).save()
    else:
        a["occ"]=cl.values()
        print("Hello")

    prf = User.objects.get(pk=st.p_id_id)
    cl = GrantClearance.objects.filter(b_id=usr, l_id=prf)
    if (cl.count() == 0):
        GrantClearance(b_id=usr, l_id=prf, approved=False).save()
    else:
        a["st"]=cl.values()
        print("Hello")

    prf = User.objects.get(pk=gk.p_id_id)
    cl = GrantClearance.objects.filter(b_id=usr, l_id=prf)
    if (cl.count() == 0):
        GrantClearance(b_id=usr, l_id=prf, approved=False).save()
    else:
        a["gk"]=cl.values()
        print("Hello")

    prf = User.objects.get(pk=ar.p_id_id)
    cl = GrantClearance.objects.filter(b_id=usr, l_id=prf)
    if (cl.count() == 0):
        GrantClearance(b_id=usr, l_id=prf, approved=False).save()
    else:
        a["ar"]=cl.values()
        print("Hello")

    prf = User.objects.get(pk=acc.p_id_id)
    cl = GrantClearance.objects.filter(b_id=usr, l_id=prf)
    if (cl.count() == 0):
        GrantClearance(b_id=usr, l_id=prf, approved=False).save()
    else:
        a["acc"]=cl.values()
        print("Hello")
    print(a)

    c={}
    return redirect(".",{'id':u_id})

def formReceipt(request):
    if(request.user.is_authenticated):
        id = request.user.id
        name = str(User.objects.get(pk = id).first_name) + " " + str(User.objects.get(pk = id).last_name)
        temp={}
        temp["name"] = name
        usr=Student.objects.get(p_id=id)
        dep=usr.department
        hos=usr.hostel;
        dept = Student.dep_choices[int(Student.objects.get(p_id=id).department)-1][1]
        print(dept)
        temp["dept"] = dept
        temp["rollNo"] = usr.roll_num
        a = {}
        a["student"] = temp

        prof = Prof.objects.filter(department = str(dep))
        care=Caretaker.objects.filter(hostel=str(hos))[0]
        ward=Warden.objects.filter(hostel=str(hos))[0]
        hod = HeadOfDep.objects.filter(department=dep)[0]
        adm = Administrative.objects.filter()

        j=0

        for p in prof:
            temp = {}
            temp["type"] = "Professor"
            temp["designation"] = "Professor"
            temp["name"] = str(User.objects.get(pk=p.p_id_id).first_name) + " " + str(
                User.objects.get(pk=p.p_id_id).last_name)
            temp["approved"] = GrantClearance.objects.filter(l_id=p.p_id_id).filter(b_id=id)[0].approved
            a[j] = temp
            j += 1

        temp = {}
        temp["type"] = "HOD"
        temp["name"] = str(User.objects.get(pk=hod.p_id_id).first_name) + " " + str(
            User.objects.get(pk=hod.p_id_id).last_name)
        temp["approved"] = GrantClearance.objects.filter(l_id=hod.p_id_id).filter(b_id=id)[0].approved
        temp["designation"] = "HOD"
        a[j] = temp
        j += 1

        temp = {}
        temp["type"] = "Caretaker"
        temp["name"] = str(User.objects.get(pk=care.p_id_id).first_name) + " " + str(
            User.objects.get(pk=care.p_id_id).last_name)
        temp["approved"] = GrantClearance.objects.filter(l_id=care.p_id_id).filter(b_id=id)[0].approved
        temp["designation"] = "Caretaker"
        a[j] = temp
        j += 1

        temp = {}
        temp["type"] = "Warden"
        temp["name"] = str(User.objects.get(pk=ward.p_id_id).first_name) + " " + str(
            User.objects.get(pk=ward.p_id_id).last_name)
        temp["approved"] = GrantClearance.objects.filter(l_id=ward.p_id_id).filter(b_id=id)[0].approved
        temp["designation"] = "Warden"
        a[j] = temp
        j += 1

        for p in adm:
            temp = {}
            temp["type"] = "Administrative"
            temp["name"] = str(User.objects.get(pk=p.p_id_id).first_name) + " " + str(
                User.objects.get(pk=p.p_id_id).last_name)
            temp["approved"] = GrantClearance.objects.filter(l_id=p.p_id_id).filter(b_id=id)[0].approved
            # temp["designation"] = Administrative.dep_choices(int(p.department))
            # temp["approved"] = st.get(l_id=p.p_id_id).approved
            temp2 = p.department
            temp2 = int(temp2)
            if (temp2 == 1):
                temp["designation"] = "Libraray"
            if (temp2 == 2):
                temp["designation"] = "CC Admin"
            if (temp2 == 3):
                temp["designation"] = "Online CC"
            if (temp2 == 4):
                temp["designation"] = "Submit thesis"
            if (temp2 == 5):
                temp["designation"] = "Gymkhana"
            if (temp2 == 6):
                temp["designation"] = "Assistant registrar"
            if (temp2 == 7):
                temp["designation"] = "Account"

            a[j] = temp
            j += 1

        print(a)

    return render(request,"templateForPdf.html", {'a':a})

def statusView(request):
    if request.user.is_authenticated:

        st=GrantClearance.objects.filter(b_id=request.user.pk)
        a= {}
        i = 1
        flag1 = 0
        flag2 = 0
        flag3 = 0
        id = request.user.id

        s = Student.objects.get(p_id= id)
        dep = str(s.department)
        hostel = str(s.hostel)


        prof = Prof.objects.filter(department = dep)
        warden = Warden.objects.filter(hostel = hostel)[0]
        adm = Administrative.objects.filter()
        care = Caretaker.objects.filter(hostel = hostel)[0]
        hod = HeadOfDep.objects.filter(department = dep)[0]

        print (prof)

        j = 0
        for p in prof:
            temp = {}
            temp["type"]="Professor"
            temp["deisgnation"]= "Professor"
            temp["name"] = str(User.objects.get(pk=p.p_id_id).first_name)+ " "+ str(User.objects.get(pk=p.p_id_id).last_name)
            temp["approved"] = GrantClearance.objects.filter(l_id = warden.p_id_id).filter(b_id = id)[0].approved
            a[j] = temp
            j+=1


        temp = {}
        temp["type"]="HOD"
        temp["name"] = str(User.objects.get(pk=hod.p_id_id).first_name)+ " "+ str(User.objects.get(pk=hod.p_id_id).last_name)
        temp["approved"] = GrantClearance.objects.filter(l_id = hod.p_id_id).filter(b_id = id)[0].approved
        temp["deisgnation"]= "HOD"

        a[j] = temp
        j+=1



        temp = {}
        temp["type"]="Caretaker"
        temp["name"] = str(User.objects.get(pk=care.p_id_id).first_name)+ " "+ str(User.objects.get(pk=care.p_id_id).last_name)
        temp["approved"] = GrantClearance.objects.filter(l_id = care.p_id_id).filter(b_id = id)[0].approved
        temp["designation"]="Caretaker"
        a[j] = temp
        j+=1

        temp = {}
        temp["type"]="Warden"
        temp["name"] = str(User.objects.get(pk=warden.p_id_id).first_name)+ " "+ str(User.objects.get(pk=warden.p_id_id).last_name)
        temp["approved"] = GrantClearance.objects.filter(l_id = warden.p_id_id).filter(b_id = id)[0].approved
        temp["designation"]="Warden"
        a[j] = temp
        j=+1



        for p in adm:
            temp = {}
            temp["type"]="Administrative"
            temp["name"] = str(User.objects.get(pk=p.p_id_id).first_name)+ " "+ str(User.objects.get(pk=p.p_id_id).last_name)
            temp["approved"] = GrantClearance.objects.filter(l_id = p.p_id_id).filter(b_id = id)[0].approved
            # temp["designation"] = Administrative.dep_choices(int(p.department))
            # temp["approved"] = st.get(l_id=p.p_id_id).approved
            temp2 = p.department
            temp2 = int(temp2)
            if(temp2 == 1):
                temp["designation"] = "Libraray"
            if(temp2 == 2):
                temp["designation"] = "CC Admin"
            if(temp2 == 3):
                temp["designation"] = "Online CC"
            if(temp2 == 4):
                temp["designation"] = "Submit thesis"
            if(temp2 == 5):
                temp["designation"] = "Gymkhana"
            if(temp2 == 6):
                temp["designation"] = "Assistant registrar"
            if(temp2 == 7):
                temp["designation"] = "Account"


            a[j] = temp
            j+=1




        print (a)
        return render(request,"statusView.html",{'a':a})
    else:
        return HttpResponse("Login first")

def stu(request):
    if request.user.is_authenticated:
        st=Nodue.objects.filter(bor_id=request.user.pk)
        a= {}
        i = 0


        for s in st:
            name = str(User.objects.get(pk=s.lend_id).first_name)+ " "+ str(User.objects.get(pk=s.lend_id).last_name)
            des = str(User.objects.get(pk=s.lend_id).designation)

            if(des == "Professor"):
                p = {}
                p["des"] = "Professor " + str(Prof.dep_choices[int(Prof.objects.get(p_id=s.lend_id).department)-1][1])
                p["type"] = "Professor"
                p["lender"] = s.lend_id
                p["remarks"] = s.remarks
                p["name"] = name
            elif (des == "HOD"):
                p = {}
                p["des"] = "HOD " + str(HeadOfDep.dep_choices[int(HeadOfDep.objects.get(p_id=s.lend_id).department)-1][1])
                p["type"] = "HOD"
                p["lender"] = s.lend_id
                p["remarks"] = s.remarks
                p["name"] = name
            elif (des == "Caretaker"):
                p = {}
                p["des"] = "Caretaker " + str(Caretaker.hostel_choices[int(Caretaker.objects.get(p_id=s.lend_id).hostel)-1][1])
                p["type"] = "Caretaker"
                p["lender"] = s.lend_id
                p["remarks"] = s.remarks
                p["name"]=name
            elif (des == "Warden"):
                p = {}
                p["des"] = "Warden " + str(Warden.hostel_choices[int(Warden.objects.get(p_id=s.lend_id).hostel)-1][1])
                p["type"] = "Warden"
                p["lender"] = s.lend_id
                p["remarks"] = s.remarks
                p["name"]=name
            elif (des == "Administrative"):
                p = {}
                p["type"] = "Administrative"
                p["des"] = str(Administrative.dep_choices[int(Administrative.objects.get(p_id=s.lend_id).department)-1][1])
                p["lender"] = s.lend_id
                p["remarks"] = s.remarks
                p["name"] = name

            a[i] = p
            i = i+1
        print (a)


        return render(request,"studentView.html",{'a':a})
    else:
        return HttpResponse("Login first")

class loginHandler(View):
    template_name = "registration/studLogin.html"

    def get(self,request):
        return render(request, self.template_name)

    def post(self,request):
            username=request.POST['username']
            password=request.POST['password']

            user = authenticate(username=username, password=password)
            login(request,user)
            if user is not None:
                return redirect("login/",{'id',user.id})
            else:
                return render(request, self.template_name)
