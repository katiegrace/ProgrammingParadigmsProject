from .models import Profile #import Profile from models.py

# Create your forms here.
class NewUserForm(UserCreationForm):
    ...

class CandidateUserForm(forms.ModelForm):
    model = User
    fields = ('username','first_name', 'last_name', 'email')

class RecruiterUserForm(forms.ModelForm):
    model = User
    fields = ('username','first_name', 'last_name', 'email')