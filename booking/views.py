from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from accounts.models import Tourist, Package
# Create your views here.


class HomeView(TemplateView):
    template_name = 'booking/index1.html'
    #login_url = '/login/'
    # redirect_field_name = 'home_page'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        packages = Package.objects.all()[:2]
        context['packages']=packages
        return context


def BookingView(request):
    if not request.user.is_authenticated:
        return render(request, 'booking/index1.html',{'name': 'Home page','error':'Please login first!'})
    else:
        naam = request.user.username
        cur_user = User.objects.get(username=naam)
        packages = Package.objects.all()
        return render(request, 'booking/booking.html',{'name': 'Booking page', 'user': cur_user, 'places': packages})


def BookView(request):
    if not request.user.is_authenticated:
        return render(request, 'booking/index1.html',{'name': 'Home page','error':'Please login first!'})
    else:
        if request.method == "POST":
            id = request.POST['id']
            package = Package.objects.filter(pk=id).first()
            user = request.user
            tour = Tourist(user = user, package = package)
            tour.save()
            print("Shumo")
            return redirect('homepage')

        