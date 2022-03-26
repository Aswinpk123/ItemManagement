import json
from Driver.models import *
from Item.models import *
from django.shortcuts import render
from ItemMangement.Constants import *
from .serializers import *
from .models import *
from  Settingsapp.models import *
from rest_framework.generics import ListAPIView
from rest_framework.response import Response


# Create your views here.
class StatusAPI(ListAPIView):
    def get(self,request):
        return Response({
            STATUS : True,
            MESSAGE : JOBSTATUS
        })

    def post(self,request):
        return Response({
            STATUS : True,
            MESSAGE : "k"
        })

# from django.contrib.admin.models import LogEntry

class JobsAPI(ListAPIView):
    serializer_class = JobSerializer

    def get_queryset(self):
        # data = LogEntry.objects.filter(id=5)
        # for x in data:
        #     print(x)
        data = JobModels.objects.all()
        print(JOBSTATUS[0]['status'])
        return data

    def post(self,request):

        alldata = self.request.data
        assigneddriver = self.request.POST.get("assigneddriver","")
        itemname = self.request.POST.get("itemname","")
        itemtype = self.request.POST.get("itemtype","")
        jobrefered = self.request.POST.get("jobrefered","")

        if assigneddriver:
            dri = DetailsModel.objects.filter(id=assigneddriver)
            if dri.count():
                dri = dri.first()
            else:
                return Response({STATUS:False,MESSAGE:"Driver Does Not exist"})
        else:
            return Response({STATUS:False,MESSAGE:"Enter VAlid Driver"})

        if itemname:
            iname = ItemModel.objects.filter(id=itemname)
            if iname.count():
                iname = iname.first()
            else:
                return Response({STATUS:False,MESSAGE:"Item name Does Not exist"})
        else:
            return Response({STATUS:False,MESSAGE:"Enter VAlid Item name"})

        if itemtype:
            itype = ItemTypeModel.objects.filter(id=itemtype)
            if itype.count():
                itype = itype.first()
            else:
                return Response({STATUS:False,MESSAGE:"Item Type Does Not exist"}) 
        else:
            return Response({STATUS:False,MESSAGE:"Enter VAlid item Type"})

        
        refcom = ChargesModel.objects.get(keyvalue=1)  
        # jbs = StatusModel.objects.get(id=1)
        if jobrefered:
            jobref = DetailsModel.objects.filter(id=jobrefered)
            if jobref.count():
                jobref = jobref.first()
                # Total =  int(alldata['transfercharge']) + int(alldata['extracharge']) + int(refcom.drivercommision) + int(refcom.referorcommision) +int(alldata['labourcharge'])
                data = JobSerializer(data=self.request.data)
                data.is_valid(raise_exception=True)
                data.save(assigneddriver=dri,itemname=iname,itemtype=itype,jobrefered=jobref,
                            referercommision=refcom.referorcommision,drivercommision=refcom.drivercommision)
                # jobref.referedcommision = int(jobref.referedcommision) + int(refcom.referorcommision)
                # jobref.save()
                # dri.drivercommision = int(dri.drivercommision) + int(refcom.drivercommision)
                # dri.save()
            else:
                return Response({STATUS:False,MESSAGE:"Driver Does Not exist"})
        else:

            # Total =  int(alldata['transfercharge']) + int(alldata['extracharge']) + int(refcom.drivercommision) + int(alldata['labourcharge'])
            data = JobSerializer(data=self.request.data)
            data.is_valid(raise_exception=True)
            data.save(assigneddriver=dri,itemname=iname,itemtype=itype,drivercommision=refcom.drivercommision)

            # dri.drivercommision = int(dri.drivercommision) + int(refcom.drivercommision)
            # dri.save()
    
        return Response({
            STATUS : True,
            MESSAGE : "Succesfully Job Created"
        })


    
    def put(self,request):
        id = self.request.POST.get("id","")
        jobstatus = self.request.POST.get("jobstatus","")
        itemtype = self.request.POST.get("itemtype","")
        itemname = self.request.POST.get("itemname","")
        assigneddriver = self.request.POST.get("assigneddriver","")
        jobrefered = self.request.POST.get("jobrefered","")
        alldata = self.request.data

        if id:
            if id.isdigit():
                jobdata = JobModels.objects.filter(id=id)
                if jobdata.count():
                    jobdata = jobdata.first()
                    if jobdata.jobstatus == "Completed":
                        return Response({
                            STATUS : False,
                            MESSAGE :"Order Completed,Update Option Will Not work in it"
                        })
                    else:
                        if itemtype:
                            itype = ItemTypeModel.objects.filter(id=itemtype)
                            if itype.count():
                                itype = itype.first()
                            else:
                                return Response({STATUS:False,MESSAGE:"Item Type Does Not exist"}) 
                        else:
                            itype = jobdata.itemtype

                        if itemname:
                            iname = ItemModel.objects.filter(id=itemname)
                            if iname.count():
                                iname = iname.first()
                            else:
                                return Response({STATUS:False,MESSAGE:"Item Name Does Not exist"}) 
                        else:
                            iname = jobdata.itemname

                        if assigneddriver:
                            assigndriver = DetailsModel.objects.filter(id=assigneddriver)
                            if assigndriver.count():
                                assigndriver = assigndriver.first()
                            else:
                                return Response({STATUS:False,MESSAGE:"Assigned Driver Does Not exist"}) 
                        else:
                            assigndriver = jobdata.assigneddriver



                        if jobrefered:
                            jbref = DetailsModel.objects.filter(id=jobrefered)
                            if jbref.count():
                                jbref = jbref.first()
                            else:
                                return Response({STATUS:False,MESSAGE:"Refered Driver Does Not exist"}) 
                        else:
                            jbref = jobdata.jobrefered
                        
                        
                        datas = JobSerializer(jobdata,data=self.request.data,partial=True)
                        datas.is_valid(raise_exception=True)
                        data = datas.save(itemtype=itype,itemname=iname,assigneddriver=assigndriver,jobrefered=jbref)
                        saved_data = JobSerializer(data).data
                        print(saved_data['jobstatus'])
                        if saved_data['jobstatus'] == "Completed":
                            refcom = ChargesModel.objects.get(keyvalue=1)
                            
                            if saved_data["jobrefered"] != None:
                                jobref = DetailsModel.objects.get(id=saved_data["jobrefered"])
                                jobref.referedcommision = int(jobref.referedcommision) + int(refcom.referorcommision)
                                jobref.save()
                               
                            else:
                                pass
                            

                            dri = DetailsModel.objects.get(id=saved_data["assigneddriver"][0]['id'])
                            dri.drivercommision = int(dri.drivercommision) + int(refcom.drivercommision)
                            dri.save()


                            Total = int(saved_data['transfercharge']) + int(saved_data['extracharge']) + int(saved_data['drivercommision']) + int(saved_data['referercommision']) + int(saved_data['labourcharge'])
                            # jobref.Total = 100
                            # jobref.save()
                            print(Total)
                            jb = JobModels.objects.get(id=id)
                            jb.Total = Total
                            jb.save()

                        else:
                            pass



                        return Response({
                            STATUS : True,
                            MESSAGE : "Updated Succesfully",
                            "DATA" : saved_data
                        })
                else:
                    return Response({STATUS:False,MESSAGE:"No Data Found With this ID"})
            else:
                return Response({STATUS:False,MESSAGE:"Invalid id"})

        else:
            return Response({STATUS:False,MESSAGE : "Credentials not given"})
       
    def delete(self,request):
        id = self.request.POST.get("id","")
        if id:
            if id.isdigit():
                jobdetails = JobModels.objects.filter(id=id)
                if jobdetails.count():
                    job = jobdetails.first()
                    job.delete()
                    return Response({
                        STATUS : True,
                        MESSAGE : "Succesfully Deleted"
                    })
                else:
                    return Response({
                        STATUS : False,
                        MESSAGE : "Job Not found with this id"
                    })
            else:
                return Response({
                    STATUS : False,
                    MESSAGE : "Invalid id"
                })

        else:

            return Response({
                STATUS : False,
                MESSAGE : "No Credentials provided"
            })


class ReportAPI(ListAPIView):    
    def get_queryset(self):
        driverid = self.request.POST.get("driverid","[]")
        drivername = self.request.POST.get("drivername","")
        fromdate = self.request.POST.get("fromdate","")
        enddate = self.request.POST.get("enddate","")
        fromkm = self.request.POST.get("fromkm","")
        endkm = self.request.POST.get("endkm","")
        itemname = self.request.POST.get("itemname","")

        if driverid:
            self.serializer_class = DetailsSerializer
            alldata = DetailsModel.objects.all()            
            id = json.loads(driverid)
            alldata = alldata.filter(id__in = id)
        
        if drivername:
            self.serializer_class = DetailsSerializer
            alldata = DetailsModel.objects.all()                       
            alldata = alldata.filter(name__icontains = drivername)


        if fromdate and enddate:
            self.serializer_class=JobSerializer
            alldata = JobModels.objects.all()
            alldata = alldata.filter(created_date__range =(fromdate,enddate))

        if fromkm and endkm:
            self.serializer_class=JobSerializer
            alldata = JobModels.objects.all()
            alldata = alldata.filter(totalkm__range = (fromkm,endkm))

        if itemname:
            self.serializer_class=JobSerializer
            alldata = JobModels.objects.all()
            alldata = alldata.filter(itemname__Itemname__icontains = itemname)
         
        
        return alldata





