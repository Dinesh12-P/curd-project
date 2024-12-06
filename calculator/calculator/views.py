from django.shortcuts import render

def calculator_view(request):
    result = None
    if request.method == 'POST':
        expression = request.POST.get('expression')
        try:
            result = eval(expression)  # Evaluates the mathematical expression
        except Exception as e:
            result = "Error"  # Handle any exceptions

    return render(request, 'calculator/home.html', {'result': result})

