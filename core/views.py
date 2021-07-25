from django.shortcuts import render
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import pandas as pd
import json
import os

"""
    Column  0 : "Age",
    Column  1 : "Attrition",
    Column  2 : "BusinessTravel",
    Column  3 : "DailyRate",
    Column  4 : "Department",
    Column  5 : "DistanceFromHome",
    Column  6 : "Education",
    Column  7 : "EducationField",
    Column  8 : "EmployeeCount",
    Column  9 : "EmployeeNumber",
    Column 10 : "EnvironmentSatisfaction",
    Column 11 : "Gender",
    Column 12 : "HourlyRate",
    Column 13 : "JobInvolvement",
    Column 14 : "JobLevel",
    Column 15 : "JobRole",
    Column 16 : "JobSatisfaction",
    Column 17 : "MaritalStatus",
    Column 18 : "MonthlyIncome",
    Column 19 : "MonthlyRate",
    Column 20 : "NumCompaniesWorked",
    Column 21 : "Over18",
    Column 22 : "OverTime",
    Column 23 : "PercentSalaryHike",
    Column 24 : "PerformanceRating",
    Column 25 : "RelationshipSatisfaction",
    Column 26 : "StandardHours",
    Column 27 : "StockOptionLevel",
    Column 28 : "TotalWorkingYears",
    Column 29 : "TrainingTimesLastYear",
    Column 30 : "WorkLifeBalance",
    Column 31 : "YearsAtCompany",
    Column 32 : "YearsInCurrentRole",
    Column 33 : "YearsSinceLastPromotion",
    Column 34 : "YearsWithCurrManager"
"""

cfile = 'HR_Employee_Attrition.data'    
fContent = open(cfile,)
data = json.load(fContent)   
fContent.close()

def home(request):  

    if request.method == 'POST' and request.FILES['myfile']:

        fname = 'HR_Employee_Attrition.data'
        fullname = os.path.join(settings.MEDIA_ROOT, fname)
        if os.path.exists(fullname):            
            os.remove(fullname)

        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        #filename = fs.save(myfile.name, myfile)
        filename = fs.save(fname, myfile)        
        uploaded_file_url = fs.url(filename)
        
        return render(request, 'core/home.html', {
            'uploaded_file_url': uploaded_file_url
        })     

    return render(request, 'core/home.html')

def load_datatable_content(request):
    age_range = request.GET.get('age_range')          
    has_attrition = request.GET.get('has_attrition')     

    # filterlist is declared
    newlist = [] 

    #has_attrition values are:  None, Yes, No

    for i in data['data']:        

        if age_range == "0":
            if has_attrition == "Reg":                
                newlist.append(i)    
            elif has_attrition == "Yes":
                if i[1] == "Yes":
                    newlist.append(i)    
            elif has_attrition == "No":
                if i[1] == "No":
                    newlist.append(i)   

        if age_range == "1": #18 to 25            

            if i[0] >= 18 and i[0] <= 25:
                if has_attrition == "Reg":                
                    newlist.append(i)    
                elif has_attrition == "Yes":
                    if i[1] == "Yes":
                        newlist.append(i)    
                elif has_attrition == "No":
                    if i[1] == "No":
                        newlist.append(i)   

        if age_range == "2": #26 to 35            

            if i[0] >= 26 and i[0] <= 35:
                if has_attrition == "Reg":                
                    newlist.append(i)    
                elif has_attrition == "Yes":
                    if i[1] == "Yes":
                        newlist.append(i)    
                elif has_attrition == "No":
                    if i[1] == "No":
                        newlist.append(i)   

        if age_range == "3": #36 to 45

            if i[0] >= 36 and i[0] <= 45:
                if has_attrition == "Reg":                
                    newlist.append(i)    
                elif has_attrition == "Yes":
                    if i[1] == "Yes":
                        newlist.append(i)    
                elif has_attrition == "No":
                    if i[1] == "No":
                        newlist.append(i)   

        if age_range == "4": #46 to 55            

            if i[0] >= 46 and i[0] <= 55:
                if has_attrition == "Reg":                
                    newlist.append(i)    
                elif has_attrition == "Yes":
                    if i[1] == "Yes":
                        newlist.append(i)    
                elif has_attrition == "No":
                    if i[1] == "No":
                        newlist.append(i)   

        if age_range == "5": #Over 55

            if i[0] >= 56:
                if has_attrition == "Reg":                
                    newlist.append(i)    
                elif has_attrition == "Yes":
                    if i[1] == "Yes":
                        newlist.append(i)    
                elif has_attrition == "No":
                    if i[1] == "No":
                        newlist.append(i)   
    

    print("Number of items in new list: ", len(newlist))    

    return render(request, 'core/displays/datatable_content.html', {'newlist': newlist})   

def load_total_employees(request):
    age_range = request.GET.get('age_range')    
    has_attrition = request.GET.get('has_attrition')               

    total_employees = 0

    if age_range == "0":

        for i in data['data']: 
            if has_attrition == "Reg":                
                total_employees = total_employees + 1
            elif has_attrition == "Yes":
                if i[1] == "Yes":
                    total_employees = total_employees + 1
            elif has_attrition == "No":
                if i[1] == "No":
                    total_employees = total_employees + 1               
        
    else:

        for i in data['data']:                

            if age_range == "1": #18 to 25            

                if i[0] >= 18 and i[0] <= 25:                    
                    if has_attrition == "Reg":                
                        total_employees = total_employees + 1
                    elif has_attrition == "Yes":
                        if i[1] == "Yes":
                            total_employees = total_employees + 1
                    elif has_attrition == "No":
                        if i[1] == "No":
                            total_employees = total_employees + 1
                    

            if age_range == "2": #26 to 35            

                if i[0] >= 26 and i[0] <= 35:
                    if has_attrition == "Reg":                
                        total_employees = total_employees + 1
                    elif has_attrition == "Yes":
                        if i[1] == "Yes":
                            total_employees = total_employees + 1
                    elif has_attrition == "No":
                        if i[1] == "No":
                            total_employees = total_employees + 1

            if age_range == "3": #36 to 45

                if i[0] >= 36 and i[0] <= 45:
                    if has_attrition == "Reg":                
                        total_employees = total_employees + 1
                    elif has_attrition == "Yes":
                        if i[1] == "Yes":
                            total_employees = total_employees + 1
                    elif has_attrition == "No":
                        if i[1] == "No":
                            total_employees = total_employees + 1

            if age_range == "4": #46 to 55            

                if i[0] >= 46 and i[0] <= 55:
                    if has_attrition == "Reg":                
                        total_employees = total_employees + 1
                    elif has_attrition == "Yes":
                        if i[1] == "Yes":
                            total_employees = total_employees + 1
                    elif has_attrition == "No":
                        if i[1] == "No":
                            total_employees = total_employees + 1

            if age_range == "5": #Over 55

                if i[0] >= 56:
                    if has_attrition == "Reg":                
                        total_employees = total_employees + 1
                    elif has_attrition == "Yes":
                        if i[1] == "Yes":
                            total_employees = total_employees + 1
                    elif has_attrition == "No":
                        if i[1] == "No":
                            total_employees = total_employees + 1

    to_json = {
        "total_employees": total_employees
    }    

    return JsonResponse(to_json, safe=False)

def load_monthly_income_avg(request):
    age_range = request.GET.get('age_range')   
    has_attrition = request.GET.get('has_attrition')                          

    monthly_income = 0
    monthly_income_avg = 0      
    male_monthly_income = 0
    female_monthly_income = 0
    total_employees = 0    

    if has_attrition == None:
        has_attrition = "Reg"

    for i in data['data']:  

        if age_range == "0":           

            if has_attrition == "Reg":                
                monthly_income = monthly_income + i[18]            
                total_employees = total_employees + 1

                if i[11] == 'Male':
                    male_monthly_income = male_monthly_income + i[18] 

                if i[11] == 'Female':
                    female_monthly_income = female_monthly_income + i[18] 
            elif has_attrition == "Yes":
                if i[1] == "Yes":
                    monthly_income = monthly_income + i[18]            
                    total_employees = total_employees + 1

                    if i[11] == 'Male':
                        male_monthly_income = male_monthly_income + i[18] 

                    if i[11] == 'Female':
                        female_monthly_income = female_monthly_income + i[18] 
            elif has_attrition == "No":
                if i[1] == "No":
                    monthly_income = monthly_income + i[18]            
                    total_employees = total_employees + 1

                    if i[11] == 'Male':
                        male_monthly_income = male_monthly_income + i[18] 

                    if i[11] == 'Female':
                        female_monthly_income = female_monthly_income + i[18]         
            

        if age_range == "1": #18 to 25            

            if i[0] >= 18 and i[0] <= 25:
                if has_attrition == "Reg":                
                    monthly_income = monthly_income + i[18]            
                    total_employees = total_employees + 1

                    if i[11] == 'Male':
                        male_monthly_income = male_monthly_income + i[18] 

                    if i[11] == 'Female':
                        female_monthly_income = female_monthly_income + i[18] 
                elif has_attrition == "Yes":
                    if i[1] == "Yes":
                        monthly_income = monthly_income + i[18]            
                        total_employees = total_employees + 1

                        if i[11] == 'Male':
                            male_monthly_income = male_monthly_income + i[18] 

                        if i[11] == 'Female':
                            female_monthly_income = female_monthly_income + i[18] 
                elif has_attrition == "No":
                    if i[1] == "No":
                        monthly_income = monthly_income + i[18]            
                        total_employees = total_employees + 1

                        if i[11] == 'Male':
                            male_monthly_income = male_monthly_income + i[18] 

                        if i[11] == 'Female':
                            female_monthly_income = female_monthly_income + i[18]  

        if age_range == "2": #26 to 35            

            if i[0] >= 26 and i[0] <= 35:
                if has_attrition == "Reg":                
                    monthly_income = monthly_income + i[18]            
                    total_employees = total_employees + 1

                    if i[11] == 'Male':
                        male_monthly_income = male_monthly_income + i[18] 

                    if i[11] == 'Female':
                        female_monthly_income = female_monthly_income + i[18] 
                elif has_attrition == "Yes":
                    if i[1] == "Yes":
                        monthly_income = monthly_income + i[18]            
                        total_employees = total_employees + 1

                        if i[11] == 'Male':
                            male_monthly_income = male_monthly_income + i[18] 

                        if i[11] == 'Female':
                            female_monthly_income = female_monthly_income + i[18] 
                elif has_attrition == "No":
                    if i[1] == "No":
                        monthly_income = monthly_income + i[18]            
                        total_employees = total_employees + 1

                        if i[11] == 'Male':
                            male_monthly_income = male_monthly_income + i[18] 

                        if i[11] == 'Female':
                            female_monthly_income = female_monthly_income + i[18]  

        if age_range == "3": #36 to 45

            if i[0] >= 36 and i[0] <= 45:
                if has_attrition == "Reg":                
                    monthly_income = monthly_income + i[18]            
                    total_employees = total_employees + 1

                    if i[11] == 'Male':
                        male_monthly_income = male_monthly_income + i[18] 

                    if i[11] == 'Female':
                        female_monthly_income = female_monthly_income + i[18] 
                elif has_attrition == "Yes":
                    if i[1] == "Yes":
                        monthly_income = monthly_income + i[18]            
                        total_employees = total_employees + 1

                        if i[11] == 'Male':
                            male_monthly_income = male_monthly_income + i[18] 

                        if i[11] == 'Female':
                            female_monthly_income = female_monthly_income + i[18] 
                elif has_attrition == "No":
                    if i[1] == "No":
                        monthly_income = monthly_income + i[18]            
                        total_employees = total_employees + 1

                        if i[11] == 'Male':
                            male_monthly_income = male_monthly_income + i[18] 

                        if i[11] == 'Female':
                            female_monthly_income = female_monthly_income + i[18]  

        if age_range == "4": #46 to 55            

            if i[0] >= 46 and i[0] <= 55:
                if has_attrition == "Reg":                
                    monthly_income = monthly_income + i[18]            
                    total_employees = total_employees + 1

                    if i[11] == 'Male':
                        male_monthly_income = male_monthly_income + i[18] 

                    if i[11] == 'Female':
                        female_monthly_income = female_monthly_income + i[18] 
                elif has_attrition == "Yes":
                    if i[1] == "Yes":
                        monthly_income = monthly_income + i[18]            
                        total_employees = total_employees + 1

                        if i[11] == 'Male':
                            male_monthly_income = male_monthly_income + i[18] 

                        if i[11] == 'Female':
                            female_monthly_income = female_monthly_income + i[18] 
                elif has_attrition == "No":
                    if i[1] == "No":
                        monthly_income = monthly_income + i[18]            
                        total_employees = total_employees + 1

                        if i[11] == 'Male':
                            male_monthly_income = male_monthly_income + i[18] 

                        if i[11] == 'Female':
                            female_monthly_income = female_monthly_income + i[18]       

        if age_range == "5": #Over 55

            if i[0] >= 56:
                if has_attrition == "Reg":                
                    monthly_income = monthly_income + i[18]            
                    total_employees = total_employees + 1

                    if i[11] == 'Male':
                        male_monthly_income = male_monthly_income + i[18] 

                    if i[11] == 'Female':
                        female_monthly_income = female_monthly_income + i[18] 
                elif has_attrition == "Yes":
                    if i[1] == "Yes":
                        monthly_income = monthly_income + i[18]            
                        total_employees = total_employees + 1

                        if i[11] == 'Male':
                            male_monthly_income = male_monthly_income + i[18] 

                        if i[11] == 'Female':
                            female_monthly_income = female_monthly_income + i[18] 
                elif has_attrition == "No":
                    if i[1] == "No":
                        monthly_income = monthly_income + i[18]            
                        total_employees = total_employees + 1

                        if i[11] == 'Male':
                            male_monthly_income = male_monthly_income + i[18] 

                        if i[11] == 'Female':
                            female_monthly_income = female_monthly_income + i[18]  

    monthly_income_avg = monthly_income / total_employees
    male_monthly_income_avg = male_monthly_income / total_employees
    female_monthly_income_avg = female_monthly_income / total_employees
    
    to_json = {
        "total_employees": total_employees,
        "monthly_income_avg": monthly_income_avg,
        "male_monthly_income_avg": male_monthly_income_avg,
        "female_monthly_income_avg": female_monthly_income_avg,
    }    

    return JsonResponse(to_json, safe=False)

def load_hourly_rate_avg(request):
    age_range = request.GET.get('age_range')      
    has_attrition = request.GET.get('has_attrition')                                  

    hourly_rate = 0
    hourly_rate_avg = 0      
    total_employees = 0

    if has_attrition == None:
        has_attrition = "Reg"

    for i in data['data']:  

        if age_range == "0":

            if has_attrition == "Reg":    
                hourly_rate = hourly_rate + i[12]            
                total_employees = total_employees + 1                    
                
            elif has_attrition == "Yes":
                if i[1] == "Yes":
                    hourly_rate = hourly_rate + i[12]            
                    total_employees = total_employees + 1        
                    
            elif has_attrition == "No":
                if i[1] == "No":
                    hourly_rate = hourly_rate + i[12]            
                    total_employees = total_employees + 1               
            

        if age_range == "1": #18 to 25            

            if i[0] >= 18 and i[0] <= 25:
                if has_attrition == "Reg":    
                    hourly_rate = hourly_rate + i[12]            
                    total_employees = total_employees + 1                    
                    
                elif has_attrition == "Yes":
                    if i[1] == "Yes":
                        hourly_rate = hourly_rate + i[12]            
                        total_employees = total_employees + 1        
                        
                elif has_attrition == "No":
                    if i[1] == "No":
                        hourly_rate = hourly_rate + i[12]            
                        total_employees = total_employees + 1           

        if age_range == "2": #26 to 35            

            if i[0] >= 26 and i[0] <= 35:
                if has_attrition == "Reg":    
                    hourly_rate = hourly_rate + i[12]            
                    total_employees = total_employees + 1                    
                    
                elif has_attrition == "Yes":
                    if i[1] == "Yes":
                        hourly_rate = hourly_rate + i[12]            
                        total_employees = total_employees + 1        
                        
                elif has_attrition == "No":
                    if i[1] == "No":
                        hourly_rate = hourly_rate + i[12]            
                        total_employees = total_employees + 1   

        if age_range == "3": #36 to 45

            if i[0] >= 36 and i[0] <= 45:
                if has_attrition == "Reg":    
                    hourly_rate = hourly_rate + i[12]            
                    total_employees = total_employees + 1                    
                    
                elif has_attrition == "Yes":
                    if i[1] == "Yes":
                        hourly_rate = hourly_rate + i[12]            
                        total_employees = total_employees + 1        
                        
                elif has_attrition == "No":
                    if i[1] == "No":
                        hourly_rate = hourly_rate + i[12]            
                        total_employees = total_employees + 1  

        if age_range == "4": #46 to 55            

            if i[0] >= 46 and i[0] <= 55:
                if has_attrition == "Reg":    
                    hourly_rate = hourly_rate + i[12]            
                    total_employees = total_employees + 1                    
                    
                elif has_attrition == "Yes":
                    if i[1] == "Yes":
                        hourly_rate = hourly_rate + i[12]            
                        total_employees = total_employees + 1        
                        
                elif has_attrition == "No":
                    if i[1] == "No":
                        hourly_rate = hourly_rate + i[12]            
                        total_employees = total_employees + 1      

        if age_range == "5": #Over 55

            if i[0] >= 56:
                if has_attrition == "Reg":    
                    hourly_rate = hourly_rate + i[12]            
                    total_employees = total_employees + 1                    
                    
                elif has_attrition == "Yes":
                    if i[1] == "Yes":
                        hourly_rate = hourly_rate + i[12]            
                        total_employees = total_employees + 1        
                        
                elif has_attrition == "No":
                    if i[1] == "No":
                        hourly_rate = hourly_rate + i[12]            
                        total_employees = total_employees + 1  

    hourly_rate_avg = hourly_rate / total_employees
    
    to_json = {
        "total_employees": total_employees,
        "hourly_rate_avg": hourly_rate_avg
    }    

    return JsonResponse(to_json, safe=False)
    
def load_age_avg(request):
    age_range = request.GET.get('age_range')  
    has_attrition = request.GET.get('has_attrition')                                  

    if has_attrition == None:
        has_attrition = "Reg"            

    age = 0
    age_avg = 0      
    total_employees = 0

    for i in data['data']:  

        if age_range == "0":

            if has_attrition == "Reg":    
                age = age + i[0]            
                total_employees = total_employees + 1
                
            elif has_attrition == "Yes":
                if i[1] == "Yes":
                    age = age + i[0]            
                    total_employees = total_employees + 1
                    
            elif has_attrition == "No":
                if i[1] == "No":
                    age = age + i[0]            
                    total_employees = total_employees + 1

        if age_range == "1": #18 to 25            

            if i[0] >= 18 and i[0] <= 25:
                if has_attrition == "Reg":    
                    age = age + i[0]            
                    total_employees = total_employees + 1
                    
                elif has_attrition == "Yes":
                    if i[1] == "Yes":
                        age = age + i[0]            
                        total_employees = total_employees + 1
                        
                elif has_attrition == "No":
                    if i[1] == "No":
                        age = age + i[0]            
                        total_employees = total_employees + 1

        if age_range == "2": #26 to 35            

            if i[0] >= 26 and i[0] <= 35:
                if has_attrition == "Reg":    
                    age = age + i[0]            
                    total_employees = total_employees + 1
                    
                elif has_attrition == "Yes":
                    if i[1] == "Yes":
                        age = age + i[0]            
                        total_employees = total_employees + 1
                        
                elif has_attrition == "No":
                    if i[1] == "No":
                        age = age + i[0]            
                        total_employees = total_employees + 1     

        if age_range == "3": #36 to 45

            if i[0] >= 36 and i[0] <= 45:
                if has_attrition == "Reg":    
                    age = age + i[0]            
                    total_employees = total_employees + 1
                    
                elif has_attrition == "Yes":
                    if i[1] == "Yes":
                        age = age + i[0]            
                        total_employees = total_employees + 1
                        
                elif has_attrition == "No":
                    if i[1] == "No":
                        age = age + i[0]            
                        total_employees = total_employees + 1
        if age_range == "4": #46 to 55            

            if i[0] >= 46 and i[0] <= 55:
                if has_attrition == "Reg":    
                    age = age + i[0]            
                    total_employees = total_employees + 1
                    
                elif has_attrition == "Yes":
                    if i[1] == "Yes":
                        age = age + i[0]            
                        total_employees = total_employees + 1
                        
                elif has_attrition == "No":
                    if i[1] == "No":
                        age = age + i[0]            
                        total_employees = total_employees + 1
        if age_range == "5": #Over 55

            if i[0] >= 56:
                if has_attrition == "Reg":    
                    age = age + i[0]            
                    total_employees = total_employees + 1
                    
                elif has_attrition == "Yes":
                    if i[1] == "Yes":
                        age = age + i[0]            
                        total_employees = total_employees + 1
                        
                elif has_attrition == "No":
                    if i[1] == "No":
                        age = age + i[0]            
                        total_employees = total_employees + 1         

    age_avg = age / total_employees
    
    to_json = {
        "total_employees": total_employees,
        "age_avg": age_avg
    }    

    return JsonResponse(to_json, safe=False)