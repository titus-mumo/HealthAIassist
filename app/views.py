
from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .models import UserSymptoms
from.models2 import MachineLearningModelData, Medication, Records, Doctor, NLPLookUpTable, DiseaseInformation, Feedback
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
# from joblib import dump
import numpy as np
from django.utils.safestring import mark_safe
from reportlab.pdfgen import canvas
from django.http import FileResponse
import io
import re
from .nlp import check_similarity, classify_feedback
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from  django_daraja.mpesa.core import MpesaClient
from .models_3 import TransactionApproval, LocationsViewed
import json
import matplotlib.pyplot as plt

from collections import Counter
from io import BytesIO
import warnings
warnings.simplefilter("ignore", UserWarning)

# Download the "punkt" resource
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')

# Create your views here.
def home(request):
    return render(request, 'app/home.html')

@csrf_exempt
def login_view(request):
    if request.method == 'GET':
        form = forms.LoginForm()
        return render(request, "app/login.html", {"form": form})
    else:
        form = forms.LoginForm(request.POST)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        if email and password:
            user = authenticate(request, user_email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You have successfully logged in.')
                return redirect(get_started) 
        else:
            form = forms.LoginForm()
            messages.error(request, 'Invalid email or password.')
            return render(request, 'app/login.html', {"form":form})

@csrf_exempt
def register(request):
    if request.method == "POST":
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect(login_view)
        else:
            messages.error(request, "Unsuccessful registration. Invalid Information.")
    else:       
        form = forms.SignUpForm()
    return render (request, "app/register.html", context={"form":form})



@login_required
def get_started(request):
    all_diseases = UserSymptoms.objects.values_list('predicted_disease', flat=True)
    disease_counter = Counter(all_diseases)
    disease_names = list(disease_counter.keys())
    occurence_counts = list(disease_counter.values())
    return render(request, 'app/get_started.html', {'disease_names':disease_names, 'occurence_counts':occurence_counts})

@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('home')

@csrf_exempt
@login_required
def symptoms_encoding(request):
    if request.method == 'POST':
        form = forms.PatientSignsForm(request.POST)
        if form.is_valid():
            raw_data = []
            for field in form.fields:
                button_value = request.POST.get(f'response_{field}')
                #setattr(signs, field, True if button_value =='yes' else False)
                raw_data.append(button_value)
            request.session['raw_data'] = raw_data
            request.session['fields'] = list(form.fields.keys())
            #print(f'{raw_data} {list(form.fields.keys())}')
            return redirect(record_user_input)
    else:
        form = forms.PatientSignsForm()
        first_name = request.user.first_name
    return render(request, 'app/symptoms_encoding.html', {'form': form, 'first_name': first_name})

@login_required
def record_user_input(request):
    if request.method == 'POST':
        form = forms.InputForm(request.POST)
        if form.is_valid():
            input = form.save(commit=False)
            input.user = request.user
            input.save()
            request.session['input'] = input.input
            return redirect(processing)
    else:
        form = forms.InputForm()
    return render(request, 'app/user_input.html', {'form': form})        

def loading_page(request):
    return render(request, 'app/loading_page.html')

def processing(request):
    fields = request.session.get('fields')
    raw_data = request.session.get('raw_data')
    input = request.session.get('input')
    signs = UserSymptoms()
    signs.user = request.user
    processed_raw_data = []
    for i in raw_data:
        if i == 'yes':
            processed_raw_data.append(True)
        else:
            processed_raw_data.append(False)
    print(processed_raw_data)
    for i, field in enumerate(fields):
        setattr(signs, field, processed_raw_data[i])
    input = str(input)
    actual_signs = re.split(r"[.,]", input)
    data = NLPLookUpTable.objects.values('sign', 'synonym_1', 'synonym_2', 'synonym_3', 'synonym_4', 'synonym_5')
    for row in data:
        for column, synonym in row.items():
            if column == 'sign':
                continue
            for sign in actual_signs:
                similarity = check_similarity(sign, synonym)
                if similarity is None:
                    continue
                if similarity > 0.7:
                    associated_signs = row['sign']
                    setattr(signs, associated_signs, True)
    signs.save()

    fields = signs._meta.get_fields()

    for field in fields:
        if field.name =='predicted_disease':
            continue
        field_value = getattr(signs, field.name)
        if field_value is None:
            setattr(signs, field.name, False)
    signs.save()
    input_data = MachineLearningModelData.objects.values('itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing', 'shivering', 'chills', 'joint_pain', 'acidity', 'vomiting', 'fatigue', 'weight_loss',
            'restlessness',	'cough', 'high_fever', 'breathlessness', 'sweating', 'indigestion', 'headache', 'yellowish_skin', 'dark_urine',	'nausea', 'loss_of_appetite',
            'pain_behind_the_eyes',	'back_pain', 'constipation','abdominal_pain', 'diarrhea', 'mild_fever', 'yellow_urine', 'yellowing_of_eyes', 'swelled_lymph_nodes',
            'malaise', 'blurred_vision', 'throat_irritation', 'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion', 'chest_pain', 'fast_heart_rate', 'cramps', 'bruising','obesity' ,'swollen_legs', 
            'swollen_blood_vessels', 'excessive_hunger', 'muscle_weakness', 'stiff_neck', 'swelling_joints',
            'movement_stiffness', 'loss_of_smell', 'passage_of_gases', 'internal_itching', 'depression', 'irritability', 'muscle_pain', 
            'red_spots_over_body', 'belly_pain','dischromic_patches','watering_from_eyes','increased_appetite', 'polyuria','mucoid_sputum','rusty_sputum', 'visual_disturbances', 'blood_transfusion', 'unsterile_injections', 
            'blood_in_sputum', 'prominent_veins_on_calf', 'painful_walking', 'irregular_sugar_level', 'phlegm', 'lethargy', 'toxic_look')
    output_data = MachineLearningModelData.objects.values('disease')
    x = np.array([list(item.values()) for item in input_data])
    x = x.reshape(len(x), -1)  # Reshape to 2D array
    y = np.array([item['disease'] for item in output_data])
    y = y.reshape(-1)  # Reshape to 1D array
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    model = DecisionTreeClassifier()
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)
    # dump(model, 'C:/Users/USER/Desktop/HealthApp/model.joblib')
    accuracy = accuracy_score(y_test, predictions)
    print("Accuracy:", accuracy)
    patient_data = [[signs.itching, signs.skin_rash, signs.nodal_skin_eruptions,signs.continuous_sneezing, signs.shivering, signs.chills, signs.joint_pain, signs.acidity, 
                        signs.vomiting, signs.fatigue, signs.weight_loss, signs.restlessness, signs.cough, signs.high_fever,signs.breathlessness,signs.sweating, signs.indigestion, signs.headache, 
                        signs.yellowish_skin, signs.dark_urine, signs.nausea, signs.loss_of_appetite, signs.pain_behind_the_eyes, signs.back_pain, 
                        signs.constipation, signs.abdominal_pain, signs.diarrhea, signs.mild_fever, signs.yellow_urine, signs.yellowing_of_eyes, signs.swelled_lymph_nodes,
                        signs.malaise, signs.blurred_vision, signs.throat_irritation, signs.redness_of_eyes, signs.sinus_pressure, signs.runny_nose, signs.congestion, signs.chest_pain,
                        signs.fast_heart_rate, signs.cramps, signs.bruising, signs.obesity, signs.swollen_legs, signs.swollen_blood_vessels, 
                        signs.excessive_hunger, signs.muscle_weakness, signs.stiff_neck, signs.swelling_joints, signs.movement_stiffness, signs.loss_of_smell,
                        signs.passage_of_gases, signs.internal_itching, signs.depression, signs.irritability, signs.muscle_pain, 
                    signs.red_spots_over_body,signs.belly_pain,signs.dischromic_patches,signs.watering_from_eyes, signs.increased_appetite, signs.polyuria, signs.mucoid_sputum, signs.rusty_sputum, 
                    signs.visual_disturbances, signs.blood_transfusion, signs.unsterile_injections, signs.blood_in_sputum, 
                    signs.prominent_veins_on_calf, signs.painful_walking, signs.irregular_sugar_level, signs.phlegm, signs.lethargy, signs.toxic_look
                ]]
                        
    predicted_disease = model.predict(patient_data)
    predicted_disease = ''.join(predicted_disease)
    signs.predicted_disease = predicted_disease
    signs.save()
    request.session['predicted_disease'] = predicted_disease
    return redirect(initialize_stk_push)

def initialize_stk_push(request):
    predicted_disease = request.session.get('predicted_disease')
    cl = MpesaClient()
    phone_number = request.user.contact
    amount = 1
    account_reference = 'Titus'
    transaction_desc = 'Description'
    callback_url = 'https://3ec6-102-140-207-36.ngrok-free.app/'
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    if response.status_code == 200:
        try:
            response_data = response.json()
            print(response_data)
            print('Hello')
            merchant_request_id = response_data['MerchantRequestID']
            checkout_request_id = response_data['CheckoutRequestID']
            request.session['merchant_request_id'] = merchant_request_id
            request.session['checkout_request_id'] = checkout_request_id
        except json.JSONDecodeError:
            pass
    else:
        pass
    return redirect(results, predicted_disease=predicted_disease)
        
# def stk_push_callback(request):  
#     merchant_request_id = request.session.get('merchant_request_id')
#     checkout_request_id = request.session.get('checkout_request_id')

#     decoded_info = decode_information(request)
#     result_code = decoded_info.get('ResultCode')
#     result_desc = decoded_info.get('ResultDesc')
#     amount = decoded_info.get('Amount')
#     mpesa_receipt_number = decoded_info.get('MpesaReceiptNumber')
#     transaction_date = decoded_info.get('TransactionDate')
#     phone_number = decoded_info.get('PhoneNumber')

#     payment_status = "Completed" if result_code == 0 else "Failed"

#     transaction = TransactionApproval()
#     transaction.user = request.user
#     transaction.merchant_request_id = merchant_request_id
#     transaction.checkout_request_id = checkout_request_id
#     transaction.response_code = result_code
#     transaction.response_description = result_desc
#     transaction.amount = amount
#     transaction.mpesa_receipt_number = mpesa_receipt_number
#     transaction.transaction_date = transaction_date
#     transaction.phone_number = phone_number
#     transaction.payment_status = payment_status
#     transaction.save()

#     return redirect(results, predicted_disease=request.session.get('predicted_disease'))





@login_required
def results(request, predicted_disease):
    medical_data = Medication.objects.filter(disease=predicted_disease)
    medicines = medical_data.values_list('medicine', flat=True)
    medicines = ', '.join(str(m) for m in medicines if m) if medicines else 'N/A'
    
    supportive_care = medical_data.values_list('supportive_care', flat=True) 
    supportive_care = ', '.join(str(sc) for sc in supportive_care if sc) if supportive_care else 'N/A'
    object = Records()
    object.user = request.user
    object.disease = predicted_disease
    object.medicine = medicines
    object.supportive_care = supportive_care
    object.save()
    doctor_data = Doctor.objects.filter(disease_of_specialization__regex=predicted_disease)
    doctor_name = doctor_data.values('doctor_name').first()['doctor_name']
    institution = doctor_data.values('health_institution').first()['health_institution']
    disease_of_specialization = doctor_data.values('disease_of_specialization').first()['disease_of_specialization']
    doctor_email = doctor_data.values('doctor_email').first()['doctor_email']
    doctor_contact = doctor_data.values('contact').first()['contact']
    doctor_latitude = doctor_data.values('latitude').first()['latitude']
    doctor_latitude = str(doctor_latitude)
    doctor_longitude = doctor_data.values('longitude').first()['longitude']
    doctor_longitude = str(doctor_longitude)
    
    return render(request, 'app/results.html', {'predicted_disease': predicted_disease, 'medicines': medicines, 'supportive_care': supportive_care, 'doctor_name':doctor_name,
                  'institution': institution, 'disease_of_specialization':disease_of_specialization, 'doctor_email': doctor_email, 'doctor_contact':doctor_contact,
                  'latitude': doctor_latitude, 'longitude' : doctor_longitude})

@login_required
def get_doctor_profiles(request):
    doctors = Doctor.objects.all()
    doctor_profiles = []
    for doctor in doctors:
        doctor_profiles.append({
            'id':doctor.doctorID,
            'name':doctor.doctor_name,
            'health_institution': doctor.health_institution,
            'disease_of_specialization':doctor.disease_of_specialization,
            'doctor_email': doctor.doctor_email,
            'doctor_contact': doctor.contact,
            'location':(str(doctor.latitude), str(doctor.longitude))

        })
    return render(request, 'app/doctor_profiles.html', {'doctor_profiles':doctor_profiles})

@login_required
def doctor_location(request, doctor_id):
    doctor = Doctor.objects.get(doctorID = doctor_id)
    latitude = doctor.latitude
    longitude = doctor.longitude
    doctor_name = doctor.doctor_name
    return render(request, 'app/location.html', {'latitude':latitude, 'longitude':longitude, 'doctor_name':doctor_name})

@login_required
def all_doctors_location(request):
    doctors = Doctor.objects.all()
    doctor_locations = []
    
    for doctor in doctors:
        doctor_locations.append({
            'latitude': str(doctor.latitude),
            'longitude': str(doctor.longitude)
        })
    
    return render(request, 'app/doctors_map.html', {'doctors': doctor_locations})

@login_required
def recent_activity(request):
    return render(request, 'app/recent_activity.html')

@login_required
def disease_records(request):
    user = request.user
    user_records = Records.objects.filter(user = user)
    user_records_array = []
    for record in user_records:
        user_records_array.append({
            'date_diagonised': record.date_created,
            'record_id': record.record_id,
            'name':f'{record.user.first_name} {record.user.last_name}',
            'disease': record.disease,
            'medicine':record.medicine,
            'supportive_care':record.supportive_care,
        })
    return render(request, 'app/disease_records.html', {'user_records_array':user_records_array})


@login_required
@csrf_exempt
def feedback(request):
    if request.method == 'GET':
        feedback = forms.FeedbackForm()
        return render(request, 'app/feedback.html', {'form':feedback})
    else:
        feedback = forms.FeedbackForm(request.POST)
        if feedback.is_valid():
            feedback_instance = feedback.save(commit=False)
            feedback_instance.user = request.user
            classification_score = classify_feedback(str(feedback_instance.feedback))
            if classification_score >= 0.5:
                feedback_instance.classification = 'Positive'
            elif classification_score <= -0.5:
                feedback_instance.classification = 'Negative'
            else:
                feedback_instance.classification = 'Neutral'
            feedback_instance.save()
            return redirect(symptoms_encoding)

@login_required
def disease_information(request):
    diseases = DiseaseInformation.objects.all()
    disease_array = []
    for disease in diseases:
        disease_array.append({
            'disease_id':disease.disease_id,
            'disease': disease.disease,
            'causes':disease.causes,
            'symptoms':disease.symptoms,
            'measures':disease.preventive_measures,
        })
    return render(request, 'app/disease_information.html', {'disease_array':disease_array})

@login_required
def print_records(request):
    buffer = io.BytesIO()
    user = request.user
    record = Records.objects.filter(user = user).latest('date_created')
    p= canvas.Canvas(buffer)
    #formatted_record = f"User ID: {record.user}, Disease: {record.disease}, Medication: {record.medicine}, Supportice care: {record.supportive_care}"
    p.drawString(100, 700, f'Patient_id:{record.user}')
    p.drawString(100, 680, f'Predicted disease: {record.disease}')
    if record.medicine is not None:
        p.drawString(100, 660, f'Suggested medication: {record.medicine}')
    if record.supportive_care is not None:
        p.drawString(100, 640, f'Suggested supported care: {record.supportive_care}')
    p.drawString(100, 620, f'Date of assessement: {record.date_created}')
    # Draw a rectangle
    p.rect(50, 50, 500, 700, fill=0)
    # Draw a line
    p.line(50, 750, 550, 750)
    # Save and close the PDF document
    p.showPage()
    p.save()
    file_path = f'record{user.patient_id}.pdf'
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename=file_path)

def settings(request):
    if request.method == 'POST':
        user = request.user
        contact = request.POST['contact']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user.first_name = first_name
        user.last_name = last_name
        user.contact = contact
        user.save()
        form = forms.SettingForm(user = request.user)
        return render(request, 'app/settings.html', {'form': form})
    else:
        form = forms.SettingForm(user = request.user)
        return render(request, 'app/settings.html', {'form': form})

def search_doctor(request):
    doctor_profiles = Doctor.objects.all()
    doctor_names = [profile.doctor_name for profile in doctor_profiles]
    return JsonResponse(doctor_names, safe=False)

@csrf_exempt
def locations_viewed(request, doctor_id):
    if request.method == 'POST':
        doctor = Doctor.objects.get(doctorID=doctor_id)
        # Create a new Location object and associate it with the doctor
        location = LocationsViewed()
        location.user = request.user
        location.doctor = doctor
        location.save()
        print(location)
        # Perform any other necessary operations or validations
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method.'})







