from django.shortcuts import render

# Create your views here.


# Create your views here.
from django.shortcuts import render, redirect
from provider.models import ProviderList
from customer.models import CustomerList


def dashboard(request):
   
    

 
    return render(request, 'dashboard.html')

def provider_table(request):
    providers = ProviderList.objects.all().order_by('-created_at')
    context = {
        'providers': providers
    }
    return render(request, 'provider.html', context)

def customer_table(request):
    customers = CustomerList.objects.all().order_by('-created_at')
    providers = ProviderList.objects.all()
    context = {
        'customers': customers,
        'providers': providers
    }
    return render(request, 'customer.html', context)

def create_customer(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        url = request.POST['url']
        status = request.POST.get('status', False)
        code = request.POST['code']
        provider_id = request.POST['provider']

        provider = ProviderList.objects.get(pk=provider_id)

        CustomerList.objects.create(
            name=name,
            description=description,
            url=url,
            status=status,
            code=code,
            provider=provider
        )

        return redirect('customer_table')  
    
    
    return render(request, 'customer.html')




def edit_customer(request, customer_id):
    customer = CustomerList.objects.get(pk=customer_id)

    if request.method == 'POST':
        customer.name = request.POST['name']
        customer.description = request.POST['description']
        customer.url = request.POST['url']
        customer.status = request.POST.get('status', False)
        customer.code = request.POST['code']
       
        
        provider_id = request.POST['provider']
        provider = ProviderList.objects.get(pk=provider_id)
        customer.provider = provider
        
        customer.save()

        return redirect('customer_table')  

    
    
    return render(request, 'customer.html')




def create_provider(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        url = request.POST['url']
        status = request.POST.get('status', False)
        code = request.POST['code']

        ProviderList.objects.create(
            name=name,
            description=description,
            url=url,
            status=status,
            code=code
        )

        return redirect('provider_table')
    return render(request,'provider.html')



def edit_provider(request, provider_id):
    provider = ProviderList.objects.get(pk=provider_id)

    if request.method == 'POST':
        provider.name = request.POST['name']
        provider.description = request.POST['description']
        provider.url = request.POST['url']
        provider.status = request.POST.get('status', False)
        provider.code = request.POST['code']
        provider.save()

        return redirect('provider_table')  

    context = {
        'provider': provider
    }
    return render(request, 'provider.html', context)
