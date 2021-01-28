from django.forms import ModelForm,ModelChoiceField,TextInput,Select, Textarea
from questoes.models import Pergunta, Disciplina,Ano,Banca,Orgao,Nivel,Alternativa
class PerguntaForm(ModelForm):
    disciplina = ModelChoiceField(queryset = Disciplina.objects.all(), empty_label = "Disciplina...",required=True,widget=Select(attrs={'class':'selecting'}))
    ano = ModelChoiceField(queryset = Ano.objects.all(), empty_label = "Ano...",required=True,widget=Select(attrs={'class':'selecting'}))
    banca = ModelChoiceField(queryset = Banca.objects.all(), empty_label = "Banca...",required=True,widget=Select(attrs={'class':'selecting'}))
    orgao = ModelChoiceField(queryset = Orgao.objects.all(), empty_label = "Orgao...",required=True,widget=Select(attrs={'class':'selecting'}))
    nivel = ModelChoiceField(queryset = Nivel.objects.all(), empty_label = "Nivel...",required=True,widget=Select(attrs={'class':'selecting'}))
    class Meta:
        model=Pergunta
        fields=['texto', 'disciplina', 'ano', 'banca', 'orgao', 'nivel']
        widgets = {'texto':Textarea(attrs={'class':'entrada','placeholder':'Pergunta'})}


class AlternativaForm(ModelForm):
    class Meta:
        model=Alternativa
        fields = ['texto', 'correta']
        widgets = {'texto':Textarea(attrs={'class':'entrada','placeholder':'Alternativa'})}
