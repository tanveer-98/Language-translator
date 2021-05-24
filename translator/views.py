from django.shortcuts import render,redirect
from translate import Translator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def index(request):

    if request.method == 'POST':
        data = request.POST
        input_text = data["in_text"]
        convert_lan=  data["t_to"]
        translator = Translator(to_lang= convert_lan)
        translated_text = translator.translate(input_text)
        return render(request,'index.html',context = {'translated_text':translated_text})
    return render(request,'index.html')
