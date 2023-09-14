from django.db import models

from onlineapp import constant



class enrolldata(models.Model):
    ename =  models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    ephone = models.CharField(max_length=100)
    ecourse = models.CharField(max_length=100)
    estatus = models.TextField(null=True,blank=True)
    eremark = models.TextField(null=True,blank=True)
    lead_in_source=models.CharField(max_length=100,null=True,blank=True)
    lead_assigned=models.CharField(max_length=100,null=True,blank=True)
    lead_status=models.CharField(max_length=100,null=True,blank=True)
    cell1=models.CharField(max_length=100,null=True,blank=True)
    cell2=models.CharField(max_length=100,null=True,blank=True)
    notes=models.CharField(max_length=1000,null=True,blank=True)
    date=models.CharField(max_length=1000,null=True,blank=True)
    created_at=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.ename


class contactUs(models.Model):
    cname = models.CharField(max_length=100)
    cmail = models.EmailField(max_length=200)
    cphone = models.CharField(max_length=100)
    cenquiry = models.CharField(max_length=100)
    cmessage = models.TextField()
    cstatus = models.TextField(null=True,blank=True)
    cremark = models.TextField(null=True,blank=True)
    lead_in_source=models.CharField(max_length=100,null=True,blank=True)
    lead_assigned=models.CharField(max_length=100,null=True,blank=True)
    lead_status=models.CharField(max_length=100,null=True,blank=True)
    cell1=models.CharField(max_length=100,null=True,blank=True)
    cell2=models.CharField(max_length=100,null=True,blank=True)
    notes=models.CharField(max_length=1000,null=True,blank=True)
    date=models.CharField(max_length=1000,null=True,blank=True)
    created_at=models.DateField(auto_now_add=True)


    def __str__(self):
        return self.cname
    

class subscribe_data(models.Model):
    sname =  models.CharField(max_length=200)
    semail = models.EmailField()
    sstatus = models.TextField(null=True,blank=True)
    sremark = models.TextField(null=True,blank=True)
    lead_in_source=models.CharField(max_length=100,null=True,blank=True)
    lead_assigned=models.CharField(max_length=100,null=True,blank=True)
    lead_status=models.CharField(max_length=100,null=True,blank=True)
    cell1=models.CharField(max_length=100,null=True,blank=True)
    cell2=models.CharField(max_length=100,null=True,blank=True)
    notes=models.CharField(max_length=1000,null=True,blank=True)
    date=models.CharField(max_length=1000,null=True,blank=True)
    created_at=models.DateField(auto_now_add=True)

    


    def __str__(self):
        return self.sname
    



class chatdata(models.Model):
    chatname = models.CharField(max_length=255)
    chatphone = models.IntegerField(null=True)
    chatemail= models.EmailField()
    chatstatus = models.TextField(null=True,blank=True)
    chatremark = models.TextField(null=True,blank=True)
    created_at=models.DateField(auto_now_add=True)

    def __str__(self):
        self.chatname


    
    

class phonedata(models.Model):
    phone= models.IntegerField()
    email=models.CharField(max_length=100,null=True,blank=True)
    name=models.CharField(max_length=100,blank=True,null=True)
    pstatus = models.TextField(null=True,blank=True)
    premark = models.TextField(null=True,blank=True)
    lead_in_source=models.CharField(max_length=100,null=True,blank=True)
    lead_assigned=models.CharField(max_length=100,null=True,blank=True)
    lead_status=models.CharField(max_length=100,null=True,blank=True)
    cell1=models.CharField(max_length=100,null=True,blank=True)
    cell2=models.CharField(max_length=100,null=True,blank=True)
    notes=models.CharField(max_length=1000,null=True,blank=True)
    date=models.CharField(max_length=1000,null=True,blank=True)
    created_at=models.DateField(auto_now_add=True)


    
    
class upcomingEvent(models.Model):
    date=models.DateField()
    description=models.TextField()
    time_from=models.TimeField()
    time_to=models.TimeField()

    title=models.CharField(max_length=100,null=True,blank=True)    
    presented_by=models.CharField(max_length=100,null=True,blank=True)
    venue=models.CharField(max_length=100,null=True,blank=True)
    day=models.CharField(max_length=50,null=True,blank=True)
    image = models.ImageField( upload_to='media/',blank=True,null=True)
    created_at=models.DateField(auto_now_add=True)


    def __str__(self):
        return self.title


class featuredEvent(models.Model):
    date=models.DateField()
    description=models.TextField()
    time_from=models.TimeField()
    time_to=models.TimeField()

    title=models.CharField(max_length=100,null=True,blank=True)
    presented_by=models.CharField(max_length=100,null=True,blank=True)
    venue=models.CharField(max_length=100,null=True,blank=True) 
    day=models.CharField(max_length=50,null=True,blank=True)
    image = models.ImageField( upload_to='media/',null=True,blank=True)
    created_at=models.DateField(auto_now_add=True)



    def __str__(self):
        return self.title



class upcoming_popup(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField()
    phone = models.IntegerField()
    created_at=models.DateField(auto_now_add=True)



    def __str__(self):
        return self.name

# class LeadInSource(models.Model):
#     lead_in_source=models.CharField(max_length=100,null=True,blank=True)
#     lead_assigned=models.CharField(max_length=100,null=True,blank=True)
#     lead_status=models.CharField(max_length=100,null=True,blank=True)

#     def __str__(self):
#         return self.lead_in_source
    


    