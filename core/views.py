from django.shortcuts import render, get_object_or_404

def home(request):
    members = MemberProfile.objects.all()
    return render(request, 'home.html', {'members': members})

def profile_detail(request, slug):
    member = get_object_or_404(MemberProfile, slug=slug)
    return render(request, 'portfolio_detail.html', {'member': member})