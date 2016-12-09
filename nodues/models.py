from django.db import models
from django.contrib import admin
from django.contrib.auth.models import AbstractUser
from systemsoft import settings


# Create your models here.

class Choice(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type


class User(AbstractUser):
    designation = models.ForeignKey(Choice, null=True, blank=True)


class Prof(models.Model):
    p_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    dep_choices = (('1', 'CSE'),
                   ('2', 'MnC'),
                   ('3', 'ECE'),
                   ('4', 'EEE'),
                   ('5', 'CL'),
                   ('6', 'CE'),
                   ('7', 'EP'))
    department = models.CharField(max_length=1, choices=dep_choices)

class HeadOfDep(models.Model):
    p_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    dep_choices = (('1', 'CSE'),
                   ('2', 'MnC'),
                   ('3', 'ECE'),
                   ('4', 'EEE'),
                   ('5', 'CL'),
                   ('6', 'CE'),
                   ('7', 'EP'))
    department = models.CharField(max_length=1, choices=dep_choices)

class Warden(models.Model):
    p_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    hostel_choices = (('1', 'Manas'),
                      ('2', 'Siang'),
                      ('3', 'Subhansiri'),
                      ('4', 'Dhansiri'),
                      ('5', 'Dihing'),
                      ('6', 'Umiam'),
                      ('7', 'Barak'),
                      ('8', 'Kameng')
                      )
    hostel = models.CharField(max_length=1, choices=hostel_choices)

class Caretaker(models.Model):
    p_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    hostel_choices = (('1', 'Manas'),
                      ('2', 'Siang'),
                      ('3', 'Subhansiri'),
                      ('4', 'Dhansiri'),
                      ('5', 'Dihing'),
                      ('6', 'Umiam'),
                      ('7', 'Barak'),
                      ('8', 'Kameng')
                      )
    hostel = models.CharField(max_length=1, choices=hostel_choices)

class Student(models.Model):
    p_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    roll_num = models.CharField(max_length=9)
    dep_choices = (('1', 'CSE'),
                   ('2', 'MnC'),
                   ('3', 'ECE'),
                   ('4', 'EEE'),
                   ('5', 'CL'),
                   ('6', 'CE'),
                   ('7', 'EP'))
    department = models.CharField(max_length=1, choices=dep_choices)
    hostel_choices = (('1', 'Manas'),
                      ('2', 'Siang'),
                      ('3', 'Subhansiri'),
                      ('4', 'Dhansiri'),
                      ('5', 'Dihing'),
                      ('6', 'Umiam'),
                      ('7', 'Barak'),
                      ('8', 'Kameng'),
                      )
    prog_choices=(('1','B.Tech'),
                  ('2', 'M.Tech'),
                  ('3', 'P.hD'),
                  ('4','B.Des')
                  )
    program=models.CharField(max_length=1,choices=prog_choices)
    hostel = models.CharField(max_length=1, choices=hostel_choices)

class Administrative(models.Model):
    p_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    dep_choices = (('1', 'Library'),
                   ('2', 'CC'),
                   ('3', 'Online CC'),
                   ('4', 'Submit Thesis'),
                   ('5', 'Gymkhana'),
                   ('6', 'Assistant Registrar'),
                   ('7', 'Account'))
    department = models.CharField(max_length=1, choices=dep_choices)


class Nodue(models.Model):
    bor = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="borrower", on_delete=models.CASCADE)
    lend = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="lender", on_delete=models.CASCADE)
    remarks = models.CharField(max_length=100)

class GrantClearance(models.Model):
    b_id = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="Borrower", on_delete=models.CASCADE)
    l_id = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="Lender", on_delete=models.CASCADE)
    approved=models.BooleanField()

class NoDueAdmin(admin.ModelAdmin):
    list_display = ('bor', 'lend', 'remarks')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):

        des = request.user.designation

        if str(des.type) == "Professor":
            dep = Prof.objects.filter(p_id=request.user.id)[0]
            if db_field.name == "bor":
                u = User.objects.filter(student__department=dep.department)
                print(u)
                kwargs["queryset"] = u
            if db_field.name == "lend":
                u = User.objects.filter(id=request.user.id)
                kwargs["queryset"] = u
        elif str(des.type) == "HOD":
            dep = HeadOfDep.objects.filter(p_id=request.user.id)[0]
            if db_field.name == "bor":
                u = User.objects.filter(student__department=dep.department)
                print(u)
                kwargs["queryset"] = u
            if db_field.name == "lend":
                u = User.objects.filter(id=request.user.id)
                kwargs["queryset"] = u
        elif str(des.type) == "Warden":
            dep = Warden.objects.filter(p_id=request.user.id)[0]
            if db_field.name == "bor":
                u = User.objects.filter(student__hostel=dep.hostel)
                print(u)
                kwargs["queryset"] = u
            if db_field.name == "lend":
                u = User.objects.filter(id=request.user.id)
                kwargs["queryset"] = u
        elif str(des.type) == "Caretaker":
            dep = Caretaker.objects.filter(p_id=request.user.id)[0]
            if db_field.name == "bor":
                u = User.objects.filter(student__hostel=dep.hostel)
                print(u)
                kwargs["queryset"] = u
            if db_field.name == "lend":
                u = User.objects.filter(id=request.user.id)
                kwargs["queryset"] = u
        elif str(des.type) == "Administrative":
            dep = Administrative.objects.filter(p_id=request.user.id)[0]
            if db_field.name == "lend":
                u = User.objects.filter(id=request.user.id)
                kwargs["queryset"] = u

        return super(NoDueAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = super(NoDueAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        elif request.user.is_staff:
            return qs.filter(lend__id=request.user.pk)
        else:
            return qs

def grant_clearance(modeladmin, request, queryset):
    des=request.user.designation

    flag=0

    if str(des.type)=="Warden":
        hostel=Warden.objects.get(p_id=request.user.id).hostel
        caretaker=Caretaker.objects.filter(hostel__exact=hostel)

        if caretaker.count()>0:
            for q in queryset:
                dues= Nodue.objects.filter(bor_id=q.b_id).filter(lend_id=request.user.id)
                cleared=GrantClearance.objects.filter(b_id=q.b_id).filter(l_id=caretaker[0].p_id)
                if dues.count()==0:
                    if cleared.count()>0 and cleared[0].approved==True:
                        q.approved = True
                        q.save()
    elif str(des.type)=="Caretaker":
        print("hello")
        for q in queryset:
            dues= Nodue.objects.filter(bor_id=q.b_id).filter(lend_id=request.user.id)
            if dues.count()==0:
                q.approved=True
                q.save()
    elif str(des.type)=="Administrative":
        ad=Administrative.objects.filter(p_id=request.user.id)[0]
        if ad.department=='5' or ad.department=='4' or ad.department=='3':
            for q in queryset:
                dues= Nodue.objects.filter(bor_id=q.b_id).filter(lend_id=request.user.id)
                if dues.count()==0:
                    q.approved=True
                    q.save()
        elif ad.department=='1':
            submitthesis=Administrative.objects.filter(department__exact='4')
            if submitthesis.count()>0:
                for q in queryset:
                    dues = Nodue.objects.filter(bor_id=q.b_id).filter(lend_id=request.user.id)
                    cleared = GrantClearance.objects.filter(b_id=q.b_id).filter(l_id=submitthesis[0].p_id)
                    if dues.count() == 0:
                        if cleared.count() > 0 and cleared[0].approved == True:
                            q.approved = True
                            q.save()
        elif ad.department=='2':
            onlinecc = Administrative.objects.filter(department__exact='3')
            if onlinecc.count() > 0:
                for q in queryset:
                    dues = Nodue.objects.filter(bor_id=q.b_id).filter(lend_id=request.user.id)
                    cleared = GrantClearance.objects.filter(b_id=q.b_id).filter(l_id=onlinecc[0].p_id)
                    if dues.count() == 0:
                        if cleared.count() > 0 and cleared[0].approved == True:
                            q.approved = True
                            q.save()
        elif ad.department=='6':
            gymkahana = Administrative.objects.filter(department__exact='5')
            if gymkahana.count() > 0:
                for q in queryset:
                    hos = str(Student.objects.filter(p_id=q.b_id)[0].hostel)
                    warden=Warden.objects.filter(hostel__exact=hos)
                    dues = Nodue.objects.filter(bor_id=q.b_id).filter(lend_id=request.user.id)
                    cleared = GrantClearance.objects.filter(b_id=q.b_id).filter(l_id=gymkahana[0].p_id)
                    cleared2 = GrantClearance.objects.filter(b_id=q.b_id).filter(l_id=warden[0].p_id)

                    if dues.count() == 0:
                        if cleared.count() > 0 and cleared2.count()>0 and cleared[0].approved == True \
                            and cleared2[0].approved == True:
                            q.approved = True
                            q.save()
        elif ad.department=='7':
            registrar=Administrative.objects.filter(department__exact='6')
            print(registrar)
            library=Administrative.objects.filter(department__exact='1')
            print(library)
            cc=Administrative.objects.filter(department__exact='2')

            for q in queryset:
                dep = Student.objects.get(p_id=q.b_id).department
                hod=HeadOfDep.objects.filter(department__exact=dep)
                dues= Nodue.objects.filter(bor_id=q.b_id).filter(lend_id=request.user.id)

                cleared1=GrantClearance.objects.filter(b_id=q.b_id).filter(l_id=registrar[0].p_id)
                cleared2=GrantClearance.objects.filter(b_id=q.b_id).filter(l_id=library[0].p_id)
                cleared3=GrantClearance.objects.filter(b_id=q.b_id).filter(l_id=cc[0].p_id)
                cleared4=GrantClearance.objects.filter(b_id=q.b_id).filter(l_id=hod[0].p_id)

                if dues.count() == 0:
                    if cleared1.count()>0 and cleared1[0].approved==True \
                        and cleared2.count()>0 and cleared2[0].approved==True \
                        and cleared3.count()>0 and cleared3[0].approved==True \
                        and cleared4.count()>0 and cleared4[0].approved==True:
                            q.approved = True
                            q.save()
    elif str(des.type)=="Professor":
        for q in queryset:
            dues= Nodue.objects.filter(bor_id=q.b_id).filter(lend_id=request.user.id)
            if dues.count()==0:
                q.approved=True
                q.save()
    elif str(des.type)=="HOD":
        department=str(HeadOfDep.objects.get(p_id=request.user.id).department)
        profs=Prof.objects.filter(department__exact=department)
        flag=0
        for q in queryset:
            flag=0
            dues = Nodue.objects.filter(bor_id=q.b_id).filter(lend_id=request.user.id)
            if dues.count() == 0:
                for p in profs:
                    cleared = GrantClearance.objects.filter(b_id=q.b_id).filter(l_id=p.p_id)
                    if cleared.count()==0 or (cleared.count()>0 and cleared[0].approved==False):
                        flag=1
            else:
                flag=1
            if not flag:
                q.approved=True
                q.save()

grant_clearance.short_desription="Approve clearance"

class ClearanceAdmin(admin.ModelAdmin):
    list_display = ('b_id', 'l_id', 'approved')
    actions = [grant_clearance]

    # def get_actions(self, request):
    #      actions = super(ClearanceAdmin, self).get_actions(request)
    #      if 'delete_selected' in actions:
    #          del actions['delete_selected']
    #      return actions

    def get_queryset(self, request):
        qs = super(ClearanceAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        elif request.user.is_staff:
            return qs.filter(l_id=request.user.pk).filter(approved=False)
        else:
            return qs