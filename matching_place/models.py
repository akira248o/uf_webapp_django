from django.db import models

# Job
class Job(models.Model):
    name = models.CharField(max_length=100)
    # Prefix
    vno = models.IntegerField(default=1)
    insdate = models.DateTimeField(auto_now_add=True)
    upddate = models.DateTimeField(auto_now_add=False, null=True,blank=True)
    insuser = models.CharField(max_length=100, null=True,blank=True)
    upduser = models.CharField(max_length=100, null=True,blank=True)
    # __str__
    def __str__(self):
        return "Job:id=" + str(self.id) + "," + str(self.name)

    class Meta:
        ordering = ('name',)

class Junle(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    # Prefix
    vno = models.IntegerField(default=1)
    insdate = models.DateTimeField(auto_now_add=True)
    upddate = models.DateTimeField(auto_now_add=False, null=True,blank=True)
    insuser = models.CharField(max_length=100, null=True,blank=True)
    upduser = models.CharField(max_length=100, null=True,blank=True)
    # __str__
    def __str__(self):
        return "Junle:id=" + str(self.id) + ",[" + str(self.job) + "]," + str(self.name)
    class Meta:
        ordering = ('name',)


class Area(models.Model):
    name = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=8, null=True,blank=True)
    # Prefix
    vno = models.IntegerField(default=1)
    insdate = models.DateTimeField(auto_now_add=True)
    upddate = models.DateTimeField(auto_now_add=False, null=True,blank=True)
    insuser = models.CharField(max_length=100, null=True,blank=True)
    upduser = models.CharField(max_length=100, null=True,blank=True)
    # __str__
    def __str__(self):
        return "Area:id=" + str(self.id) + "," + str(self.name)
    class Meta:
        ordering = ('name',)

# Member
class Member(models.Model):
    loginid = models.CharField(max_length=200)
    mail_address = models.EmailField(max_length=200, null=True,blank=True)
    first_name = models.CharField(max_length=50, null=True,blank=True)
    middle_name = models.CharField(max_length=50, null=True,blank=True)
    last_name = models.CharField(max_length=50, null=True,blank=True)
    nick_name = models.CharField(max_length=100, null=True,blank=True)
    password = models.CharField(max_length=16, null=True,blank=True)
    tel = models.CharField(max_length=12, null=True,blank=True)
    birthday = models.DateField(null=True,blank=True)
    gender = models.CharField(max_length=1, null=True,blank=True)
    zip_code = models.CharField(max_length=8, null=True,blank=True)
    address1 = models.CharField(max_length=200, null=True,blank=True)
    address2 = models.CharField(max_length=200, null=True,blank=True)
    address3 = models.CharField(max_length=200, null=True,blank=True)
    # Matching Data
    area = models.ForeignKey(Area, on_delete=models.CASCADE, null=True,blank=True)
    # dancer,yoga-master,fitness instructor
    job =  models.ForeignKey(Job, on_delete=models.CASCADE, null=True,blank=True)
    # dancer - pop,jazz,lock,break
    junle = models.ForeignKey(Junle, on_delete=models.CASCADE, null=True,blank=True)
    #
    # weekdate(0-6),hh:mm:dd => 7
    # ex) monday,20:30:00 - 21:30:00 = 1203000213000
    time_range = models.CharField(max_length=14, null=True,blank=True)
    # Prefix
    vno = models.IntegerField(default=1)
    insdate = models.DateTimeField(auto_now_add=True,blank=True)
    upddate = models.DateTimeField(auto_now_add=False, null=True,blank=True)
    insuser = models.CharField(max_length=100, null=True,blank=True)
    upduser = models.CharField(max_length=100, null=True,blank=True)
    # __str__
    def __str__(self):
        return "Member:id=" + str(self.mail_address)
#        return "Member:id=" + str(self.id)  \
#            + "," + str(self.loginid)  \
#            + "," + str(self.mail_address)  \
#            + "," + str(self.last_name)  \
#            + "," + str(self.first_name) \
#            + "," + str(self.last_name) \
#            + "," + str(self.nick_name) \
#            + "," + str(self.tel) \
#            + "," + str(self.birthday) \
#            + "," + str(self.gender) \
#            + "," + str(self.zip_code) \
#            + "," + str(self.address1) \
#            + "," + str(self.address2) \
#            + "," + str(self.address3) \
#            + ",[" + str(self.area) \
#            + "],[" + str(self.job) \
#            + "],[" + str(self.junle) \
#            + "]"
            
    class Meta:
        ordering = ('insdate',)



