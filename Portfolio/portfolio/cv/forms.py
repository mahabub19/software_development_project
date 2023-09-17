from django.forms import ModelForm
from .models import feedbacks
    
class feedbacksForm(ModelForm):
    class Meta:
        model = feedbacks
        fields = '__all__'
