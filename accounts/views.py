from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
        else:
            form = SignUpForm()
        return render(request, 'accounts/register.html', {'form': form})

class MyPasswordChangeView(PasswordChangeView):
    template_name = 'accounts/change_password.html'
    success_url = reverse_lazy('login')

@login_required
def dashboard_view(request):
    return render(request, 'accounts/dashboard.html')
