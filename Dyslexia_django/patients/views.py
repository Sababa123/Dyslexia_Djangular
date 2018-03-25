from django.shortcuts import render, get_object_or_404
import random
from django.http import HttpResponse,HttpResponseRedirect, Http404
from django.views import View
from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from .models import Patient
from .forms import Patient_classCreateForm,UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q


class RegisterView(CreateView):
	form_class=UserCreationForm
	template_name = 'registration/register.html'
	success_url = '/'

@login_required()
def patients_view(request):

	template_name = 'patients/patients_list.html'
	#queryset = Patient.objects.filter(p_name__iexact='tahir')
	query = request.GET.get('q')
	queryset = Patient.objects.filter(owner=request.user)
	if query:
		query = query.strip()
		queryset=queryset.filter(Q(p_name__icontains=query)|Q(p_dob__icontains=query)).distinct()
	context = { 'obj_list' : queryset}
	return render(request, template_name, context)

@login_required()
def patients_name(request):

	template_name = 'patients/patients_name.html'
	queryset = Patient.objects.filter(owner=request.user)
	context = { 'names_list' : queryset}
	return render(request, template_name, context)


# def contact(request):
	 
# 	 context = {
		 	
# 				}
# 	 return render(request, 'patientsHTML/contact.html', context )

# def about(request):
	 
# 	 context = {
		 	
# 				}
# 	 return render(request, 'patientsHTML/about.html', context )

#class contactview(View):
	#def get(self,request, *args, **kwargs):
	 
	 #context = {}
	 #return render(request, 'patientsHTML/contact.html', context )

class contactview(TemplateView):
	
	 template_name ='patientsHTML/contact.html'

class aboutview(TemplateView):
	
	 template_name ='patientsHTML/about.html'



@login_required()
def patients_detailview(request, p_id):
	
	template_name = 'patients/patients_list.html'
	queryset = Patient.objects.filter(pk = p_id).values()
	context = { 'obj_list' : queryset}
	return render(request, template_name, context)


class patients_listview(ListView):
	model = Patient
	template_name = 'patients/patients_list.html'
	context_object_name = 'obj_list' 



@login_required()
def patients_createform(request):
	form = Patient_classCreateForm(request.POST or None)
	 	#if request.method == "POST":
		#p_name = request.POST.get("p_name")
		#p_dob = request.POST.get("p_dob")
		#form = PatientCreateForm(request.POST)
                #abcd
	if form.is_valid():
		if request.user.is_authenticated:
			instance = form.save(commit=False)

			instance.owner = request.user
			instance.save()

			# obj = Patient.objects.create(

			# p_name=form.cleaned_data.get('p_name'),
			# p_dob=form.cleaned_data.get('p_dob')

			# 	)
			return HttpResponseRedirect("/patients/name")
		else:
			return HttpResponseRedirect("/login/")




	template_name = 'patients/form.html'
	context = { 'form':form }
	return render(request, template_name, context)


class patients_classcreateform(LoginRequiredMixin, CreateView ):
	form_class = Patient_classCreateForm
	template_name = 'patientsHTML/forms.html'
	#login_url = '/login/'
	success_url = "/"

	def get_context_data(self, *args, **kwargs):
		context = super(patients_classcreateform, self).get_context_data(*args, **kwargs)
		context['title'] = 'Add Patient'
		return context

	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.owner = self.request.user
		return super(patients_classcreateform, self).form_valid(form)

class patient_UpdateView(LoginRequiredMixin,UpdateView):
    model = Patient
    form_class = Patient_classCreateForm
    template_name = 'patientsHTML/forms.html'
    success_url = "/patients/name"








