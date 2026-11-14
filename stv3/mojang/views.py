from django.shortcuts import render

def churn_calculator(request):
    customerlost = float(request.POST.get('custLost', '0') or '0')
    initialcustomer = float(request.POST.get('initCust', '0') or '0')

    churn_rate = (customerlost / initialcustomer) * 100 if request.method == 'POST' else 0

    print("Customer Lost =", customerlost)
    print("Initial Customer =", initialcustomer)
    print("Churn Rate =", churn_rate)

    return render(
        request,
        'mojang/area.html',
        {
            'customerlost': customerlost, 
            'initialcustomer': initialcustomer, 
            'churn_rate': churn_rate
        }
    )