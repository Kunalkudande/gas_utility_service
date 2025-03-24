from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest
from .forms import ServiceRequestForm
from django.utils import timezone

@login_required
def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.user = request.user
            service_request.save()
            return redirect('track_requests')
    else:
        form = ServiceRequestForm()
    return render(request, 'customer_service/submit_request.html', {'form': form})

@login_required
def track_requests(request):
    requests = ServiceRequest.objects.filter(user=request.user).order_by('-submitted_at')
    return render(request, 'customer_service/track_requests.html', {'requests': requests})

@login_required
def manage_requests(request):
    if not request.user.is_staff:
        return redirect('track_requests')
    requests = ServiceRequest.objects.all().order_by('-submitted_at')
    return render(request, 'customer_service/manage_requests.html', {'requests': requests})

@login_required
def update_request_status(request, request_id):
    if not request.user.is_staff:
        return redirect('track_requests')
    service_request = get_object_or_404(ServiceRequest, id=request_id)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        service_request.status = new_status
        if new_status == 'resolved':
            service_request.resolved_at = timezone.now()
        service_request.save()
        return redirect('manage_requests')
    return render(request, 'customer_service/update_status.html', {'service_request': service_request})