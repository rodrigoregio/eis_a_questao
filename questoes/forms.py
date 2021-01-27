from django.forms import ModelForm
from questoes.models import Pergunta, Disciplina,Ano,Banca,Orgao,Nivel,Alternativa
class PerguntaForm(ModelForm):
    disciplina=forms.ModelChoiceField(queryset=Disciplina.objects.all(), empty_Label='Disciplina...')
    ano=forms.ModelChoiceField(queryset=Ano.objects.all(), empty_Label='Ano...')
    banca=forms.ModelChoiceField(queryset=Banca.objects.all(), empty_Label='Banca...')
    orgao=forms.ModelChoiceField(queryset=Orgao.objects.all(), empty_Label='Orgao...')
    nivel=forms.ModelChoiceField(queryset=Nivel.objects.all(), empty_Label='Nivel...')
    class Meta:
        model=Pergunta
        fields=['texto', 'respondida', 'correta', 'disciplina', 'ano', 'banca', 'orgao', 'nivel']

class AlternativaForm(ModelForm):
    class Meta:
        model=Alternativa
        fields=['texto', 'correta', 'selecionada']
