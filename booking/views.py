from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .models import Turf, Booking
from .forms import BookingForm

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')


def index(request):
    turfs = Turf.objects.all()
    return render(request, 'booking/index.html', {'turfs': turfs})

@login_required
def book_turf(request, turf_id):
    turf = get_object_or_404(Turf, id=turf_id)
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.turf = turf
            booking.save()
            messages.success(request, "Turf booked successfully!")
            return redirect('booking_list')
    else:
        form = BookingForm(initial={'turf': turf})
    return render(request, 'booking/book_turf.html', {'form': form, 'turf': turf})

@login_required
def booking_list(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booking/booking_list.html', {'bookings': bookings})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully. Please log in.")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'booking/signup.html', {'form': form})
