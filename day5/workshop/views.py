from django.shortcuts import render
from .models import Workshop,Member

# Create your views here.
def workshop_list(request):
    """
    this returns workshop list
    """
    template_name =  "workshop/workshop_list.html"
    context ={
        "title":"Workshop list",
        "workshops":Workshop.objects.all(),
        "members":Member.objects.all()
        #SELECT * FROM WORKSHOP
    }
    return render(request,template_name,context)

def workshop_detail(request, id):
        template_name = "workshop/workshop_detail.html"
         #SELECT * FROM WORKSHOP WHERE ID=ID
         #.get()--->returns single object
         #.filter()---> multiple objects
         #select * from workshop where name_icontains="abcd"
         #.all()--->returns all
        workshop = Workshop.objects.get(id=id)
        members = Member.objects.filter(workshops=workshop)
        # filtered_obj = Workshop.objects.filter(id=id).first()
        context={
            "workshop":workshop,
            "members": members
            # "filtered_obj": filtered_obj
        }
        return render (request, template_name, context)
        
#     def member_list(request):
#     """
#     this returns workshop list
#     """
#     template_name =  "workshop/workshop_list.html"
#     context ={
#         "title":"Workshop list",
#         "workshops":Workshop.objects.all(),
#         "members":Member.objects.all()
#         #SELECT * FROM WORKSHOP
#     }
#     return render(request,template_name,context)

# def member_detail(request, id):
#         template_name = "workshop/workshop_detail.html"
#          #SELECT * FROM WORKSHOP WHERE ID=ID
#          #.get()--->returns single object
#          #.filter()---> multiple objects
#          #select * from workshop where name_icontains="abcd"
#          #.all()--->returns all
#         workshop = Workshop.objects.get(id=id)
#         filtered_obj = Workshop.objects.filter(id=id).first()
#         context={
#             "workshop":workshop,
#             # "filtered_obj": filtered_obj
#         }
#         return render (request, template_name)
