from django.shortcuts import render
from myApp.models import*

def mainpage(request):
        Depertment_selection = studentModel.objects.values_list("Depertment", flat=True).distinct()
        student_dept_data = request.GET.get("Dept_select")
        if student_dept_data:
          students= studentModel.objects.filter(Depertment = student_dept_data)
        else:
          students= studentModel.objects.all()
        context = {
          "students" : students,
          "dept_selection" : Depertment_selection,
          "teacherdata": teacherModel.objects.all(),          
    }
  
        return render(request,"mainpage.html",context)

def studentPage(request):
        Depertment_selection = studentModel.objects.values_list("Depertment", flat=True).distinct()
        student_dept_data = request.GET.get("Dept_select")
        if student_dept_data:
          students= studentModel.objects.filter(Depertment = student_dept_data)
        else:
          students= studentModel.objects.all()
        context={
        # "studentdata" : studentModel.objects.all(),
        "students" : students,
        "dept_selection" : Depertment_selection,    
    }
    
        return render(request,"studentPage.html",context)

def teacherPage(request):
    
    context = {
      "teacherdata": teacherModel.objects.all(),
      
      
    } 
  
    
    return render(request,"teacherPage.html",context)