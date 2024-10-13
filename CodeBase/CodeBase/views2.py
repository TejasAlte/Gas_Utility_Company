# support
from django.shortcuts import render
from service_requests.models import ServiceRequest
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_staff)
def manage_requests(request):
    requests = ServiceRequest.objects.filter(status='pending')
    return render(request, 'support/manage_requests.html', {'requests': requests})
