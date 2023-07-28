from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, UserSymptoms
from. models2 import InputField, Feedback
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'autocomplete': 'off','data-toggle': 'password'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'user_email', 'contact', 'password1', 'password2']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'user_email': 'Email',
            'contact': 'Contact Number',
            'password1': 'Password',
            'password2': 'Confirm PassWord',
        }

    def clean_patient_email(self):
        user_email = self.cleaned_data.get('user_email')
        if CustomUser.objects.filter(user_email=user_email).exists():
            raise forms.ValidationError('This email address is already registered.')
        return user_email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords do not match.')
        return password2

class LoginForm(forms.Form):
    email = forms.EmailField(
        max_length=255,
        label='Email',
        widget=forms.EmailInput(attrs={'placeholder': 'Email', 'autocomplete':'on'})
    )
    password = forms.CharField(
        max_length=10,
        label='Password',
        widget=forms.PasswordInput(attrs={'placeholder': '********', 'autocomplete': 'off', 'data-toggle': 'password'})
    )

    def confirm_validiity(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        user = authenticate(user_email=email, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
        return self.cleaned_data

class PatientSignsForm(forms.ModelForm):
    class Meta:
        model = UserSymptoms
        fields = ['itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing', 'shivering', 'chills', 'joint_pain', 'acidity', 'vomiting', 'fatigue', 'weight_loss',
                  	'restlessness',	'cough', 'high_fever', 'breathlessness', 'sweating', 'indigestion', 'headache', 'yellowish_skin', 'dark_urine',	'nausea', 'loss_of_appetite',
                    'pain_behind_the_eyes',	'back_pain', 'constipation','abdominal_pain', 'diarrhea', 'mild_fever', 'yellow_urine', 'yellowing_of_eyes', 'swelled_lymph_nodes',
                    'malaise', 'blurred_vision', 'throat_irritation', 'redness_of_eyes']
        labels = {
            'itching':"Do you have itching?", 
            'skin_rash':"Do you have a skin rash?", 
            'nodal_skin_eruptions':'Do you have nodal skin eruption?',
            'continuous_sneezing': 'Are you experiencing continuous sneezing?', 
            'shivering':'Are you shivering?', 
            'chills': 'Do you have chills?', 
            'joint_pain': 'Do you have joint pain?', 
            'acidity':'Do you have stomach acidity?', 
            'vomiting': 'Are you vomiting?', 
            'fatigue': 'Do you feel fatigue?', 
            'weight_loss': 'Are you experincing weight loss?', 
            'restlessness':'Do you experience restlessness?',
            'cough': 'Are you coughing?', 
            'high_fever':'Do you have high fever?',
            'breathlessness':'Do you experience breathlessness?',
            'sweating':'Are you experiencing excessive sweating?', 
            'indigestion':'Any instances of indigestion?', 
            'headache': 'Do you have headache?',
            'yellowish_skin':'Do you have a yellowish skin?',
            'dark_urine':'Do you have dark urine?',
            'nausea': 'Do you have nausea?', 
            'loss_of_appetite': 'Do you have reduced appetite?', 
            'pain_behind_the_eyes': 'Do you have pain behind the eyes?', 
            'back_pain': 'Do you have back pain?', 
            'constipation': 'Are you experiencing constipation?', 
            'abdominal_pain': 'Do you have abdominal pain?', 
            'diarrhea': 'Do you have diarrhea?', 
            'mild_fever': 'Do you have mild fever?', 
            'yellow_urine': 'Do you have yellow urine?',
            'yellowing_of_eyes':'Are your eyes yellowing?',
            'swelled_lymph_nodes':'Do you have swelled lymph nodes?',
            'malaise':'Do you have malaise?', 
            'blurred_vision': 'Are you experiencing blurred vision?',  
            'throat_irritation': 'Do you have throat irritation?', 
            'redness_of_eyes': 'Do you have redness of the eyes?', 
        }

class InputForm(forms.ModelForm):
    input = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Enhanced craving for food, lack of muscle strength'}), label='Enter textual input about any other signs or symptoms',
    )

    class Meta:
        model = InputField
        fields = ['input']

class FeedbackForm(forms.ModelForm):
    feedback = forms.CharField(label="We value your feedback as it helps us improve the quality of services we offer", widget=forms.Textarea(attrs={'placeholder': 'Your feedback here'}))

    class Meta:
        model = Feedback
        fields = ['feedback']

'''itching	skin_rash	nodal_skin_eruptions	continuous_sneezing	shivering	chills	joint_pain	acidity	vomiting	fatigue	weight_loss	restlessness	
cough	high_fever	breathlessness	sweating	indigestion	headache	yellowish_skin	dark_urine	nausea	loss_of_appetite	pain_behind_the_eyes	back_pain	
constipation	abdominal_pain	diarrhoea	mild_fever	yellow_urine	yellowing_of_eyes	swelled_lymph_nodes	malaise	blurred_vision	throat_irritation	redness_of_eyes	
sinus_pressure	runny_nose	congestion	chest_pain	fast_heart_rate	cramps	bruising	obesity	swollen_legs	swollen_blood_vessels	excessive_hunger	muscle_weakness	
stiff_neck	swelling_joints	movement_stiffness	loss_of_smell	passage_of_gases	internal_itching	depression	irritability	muscle_pain	red_spots_over_body	belly_pain	
dischromic_patches	watering_from_eyes	increased_appetite	polyuria	mucoid_sputum	rusty_sputum	visual_disturbances	blood_transfusion	unsterile_injections	
blood_in_sputum	prominent_veins_on_calf	painful_walking	irregular_sugar_level	phlegm	lethargy	toxic_look_(typhos)	disease'''


class SettingForm(forms.Form):
    contact = forms.IntegerField(
        label='Contact',
        widget=forms.TextInput(attrs={'autocomplete':'off'})
    )
    first_name = forms.CharField(
        max_length=255,
        label='First name',
        widget=forms.TextInput(attrs={'autocomplete':'off'})
    )
    last_name = forms.CharField(
        max_length=255,
        label='Last name',
        widget=forms.TextInput(attrs={'autocomplete':'off'})
    )

    def __init__(self, user, *args, **kwargs):
            super(SettingForm, self).__init__(*args, **kwargs)
            self.fields['first_name'].widget.attrs['placeholder'] = user.first_name
            self.fields['last_name'].widget.attrs['placeholder'] = user.last_name
            self.fields['contact'].widget.attrs['placeholder'] = user.contact