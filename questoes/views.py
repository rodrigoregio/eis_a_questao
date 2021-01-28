from django.shortcuts import render
from .forms import PerguntaForm,AlternativaForm
from .models import Pergunta,Alternativa

# Create your views here.
def index(request):
    return render(request, 'index.html')

def pergunta_inserir(request):
    form_pergunta=PerguntaForm(request.POST)
    form_alternativas=[AlternativaForm(
        request.POST,
        prefix=str(i)) for i in range(1,6)]
    if(form_pergunta.is_valid() and all(form_alternativa.is_valid() for form_alternativa in form_alternativas)):
        pergunta=form_pergunta.save()
        for form_alternativa in form_alternativas:
            alternativa = form_alternativa.save(commit=False)
            alternativa.pergunta=pergunta
            alternativa.save()
        redirect('index')
    return render(request,'pergunta_form.html',{'form_pergunta':form_pergunta,'form_alternativas':form_alternativas})