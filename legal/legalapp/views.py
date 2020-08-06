from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import *
class UserViewSet(viewsets.ViewSet):
    def list(self,request):
        userlist = User.objects.all()
        data=[]
        for userlists in userlist:
            data.append({
                'name':userlists.name,
                'email':userlists.email,
                'mobile':userlists.mobile,
                'plans':userlists.plans
            })
        return Response({'data list':data})
    def retrieve(self, request, pk=None):
        data=User.objects.get(id=pk) 
        datad=[{
            'name':data.name,
            'email':data.email,
            'mobile':data.mobile,
            'plans':data.plans
        }]
        return Response({'user retrieve':datad})
    def destroy(self, request, pk=None):
        userset=User.objects.filter(id=pk).delete()
        return Response({'Successfully data delete'})
    def update(self, request, pk=None):
        name=request.data.get('name')
        if not name:
            return Response({'name':'enter your name'})
        email=request.data.get('email')
        if not email:
            return Response({'email':'enter your email'})
        mobile=request.data.get('mobile')    
        if not mobile:
            return Response({'mobile':'enter your mobile'})
        plans=request.data.get('plans')    
        if not plans:
            return Response({'plans':'enter your plans'})        
        user=User.objects.get(id=pk)
        user.name=name
        user.email=email
        user.mobile=mobile
        user.plans=plans
        user.save()
        return Response({'data update':'data save'})      
    def create(self,request):
        usercreate = User()
        usercreate.name = request.data.get('name')
        usercreate.email = request.data.get('email')
        usercreate.mobile = request.data.get('mobile')
        usercreate.plans = request.data.get('plans')
        usercreate.save()
        return Response({'Create Data'})
class PlanViewSet(viewsets.ViewSet):        
    def list(self,request):
        planlist = Plan.objects.all()
        data = []
        for planlists in planlist:
            data.append({
                'plan_name':planlists.plan_name,
                'plans':planlists.userfor.plans,
                'amount':planlists.amount,
                'discount':planlists.discount
            })
        return Response({'data list':data})
    def create(self,request):
        plancreate = User.objects.get(id=request.data.get('user_id'))
        plancreate.userfor= plancreate
        plancreate = Plan()
        plancreate.plan_name = request.data.get('plan_name')
        plancreate.amount = request.data.get('amount')
        plancreate.discount = request.data.get('discount')
        plancreate.save()
        return Response({'Create Data'})            
class Previous_PlansViewSet(viewsets.ViewSet):
    def list(self,request):
        previouslist = Previous_Plans.objects.all()
        data =[]
        for previouslists in previouslist:
            data.append({
                'plan_name':previouslists.planfor.plan_name,
                'plans':previouslists.uerfors.plans,
                'date':previouslists.date,
                'amount':previouslists.planfor.amount,
                'discount':previouslists.planfor.discount,
                'transection_id':previouslists.transection_id,
                'staus':previouslists.staus
            })
        return Response({'data list':data})
    def create(self,request):
        previouscreate = Plan.objects.get(id=request.data.get('plan_id'))
        previouscreate = User.objects.get(id=request.data.get('user_ids'))
        previouscreate.planfor = previouscreate
        previouscreate = Previous_Plans()
        previouscreate.date = request.data.get('date')
        previouscreate.transection_id = request.data.get('transection_id')
        previouscreate.staus = request.data.get('staus')
        previouscreate.save()
        return Response({'Create Data'})
