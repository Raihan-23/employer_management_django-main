from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Employees
from .forms import EmployeeForm, UpdateEmployeeForm

# Create your views here.


def home(request):
    # return HttpResponse("Welcome to the Home Page!")
    return render(
        request,
        "employees/create_employee.html",
    )


# create employears
def create_employer(request):
    # create_form = EmployeeForm(request.POST)
    if request.method == "POST":
        create_form = EmployeeForm(request.POST)
        if create_form.is_valid():
            create_form.save()
            return redirect("get_employers")
            # context = {
            #     "create_form": EmployeeForm(),
            # }
            # return render(request, "employees/create_employee.html", context=context)
        else:
            context = {
                "create_form": create_form,
            }
            return render(request, "employees/create_employee.html", context=context)
    else:
        create_form = EmployeeForm()
        context = {
            "create_form": create_form,
        }
        return render(request, "employees/create_employee.html", context=context)
    

# get employers

def get_employers(request):
    employers = Employees.objects.all()
    context = {
        "employers": employers,
    }
    return render(request, "employees/get_employees.html", context=context)


def get_employers_forudateanddelete(request):
    employers = Employees.objects.all()
    context = {
        "employers": employers,
    }
    return render(request, "employees/get_employers_forudateanddelete.html", context=context)



# employers details 
def employer_details(request, pk):
    employer = Employees.objects.get(pk=pk)
    context = {
        "employer": employer,
    }
    return render(request, "employees/employer_details.html", context=context)



# update employer
def update_employer(request, pk):
    try:
        employers = Employees.objects.get(pk = pk)
        if request.method == "POST":
            update_form = UpdateEmployeeForm(request.POST, instance = employers)
            if update_form.is_valid():
                update_form.save()
                return redirect("get_employers")
            else:
                context = {
                    "update_form": update_form,
                }
                return render(request, "employees/update_employee.html", context=context)
        else:
            update_form = UpdateEmployeeForm(instance = employers)
            context = {
                "update_form": update_form,
            }
            return render(request, "employees/update_employee.html", context=context)
    except Employees.DoesNotExist:
        # return redirect("get_employers")
        return HttpResponse("Employee not found.")


#  delete employers
def delete_employer(request, pk):
    try:
        employers = Employees.objects.get(pk = pk)
        employers.delete()
        return redirect("employers_for_date_and_delete")
    except Employees.DoesNotExist:
        return HttpResponse("Employee not found.")