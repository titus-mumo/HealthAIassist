from django.contrib import admin
from . import models
from . import models2
from .  import models_3

# Register your models here.
@admin.register(models.UserSymptoms)
class UserSymptomsAdmin(admin.ModelAdmin):
    list_display = ('symptom_id', 'user','date_diagonised','predicted_disease', 'itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing', 'shivering', 'chills', 'joint_pain', 'acidity', 'vomiting', 'fatigue', 'weight_loss',
                  	'restlessness',	'cough', 'high_fever', 'breathlessness', 'sweating', 'indigestion', 'headache', 'yellowish_skin', 'dark_urine',	'nausea', 'loss_of_appetite',
                    'pain_behind_the_eyes',	'back_pain', 'constipation','abdominal_pain', 'diarrhea', 'mild_fever', 'yellow_urine', 'yellowing_of_eyes', 'swelled_lymph_nodes',
                    'malaise', 'blurred_vision', 'throat_irritation', 'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion', 'chest_pain', 'fast_heart_rate', 'cramps', 'bruising','obesity' ,'swollen_legs', 
                    'swollen_blood_vessels', 'excessive_hunger', 'muscle_weakness', 'stiff_neck', 'swelling_joints',
                  'movement_stiffness', 'loss_of_smell', 'passage_of_gases', 'internal_itching', 'depression', 'irritability', 'muscle_pain', 
                  'red_spots_over_body', 'belly_pain','dischromic_patches','watering_from_eyes','increased_appetite', 'polyuria','mucoid_sputum','rusty_sputum', 'visual_disturbances', 'blood_transfusion', 'unsterile_injections', 
                  'blood_in_sputum', 'prominent_veins_on_calf', 'painful_walking', 'irregular_sugar_level', 'phlegm', 'lethargy', 'toxic_look')
    search_fields=('predicted_disease','user')
    list_filter = ('predicted_disease', 'user', 'date_diagonised', )


@admin.register(models2.MachineLearningModelData)
class MachineLearningModelDataAdmin(admin.ModelAdmin):
    list_display = ('item_id','disease', 'itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing', 'shivering', 'chills', 'joint_pain', 'acidity', 'vomiting', 'fatigue', 'weight_loss',
                  	'restlessness',	'cough', 'high_fever', 'breathlessness', 'sweating', 'indigestion', 'headache', 'yellowish_skin', 'dark_urine',	'nausea', 'loss_of_appetite',
                    'pain_behind_the_eyes',	'back_pain', 'constipation','abdominal_pain', 'diarrhea', 'mild_fever', 'yellow_urine', 'yellowing_of_eyes', 'swelled_lymph_nodes',
                    'malaise', 'blurred_vision', 'throat_irritation', 'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion', 'chest_pain', 'fast_heart_rate', 'cramps', 'bruising','obesity' ,'swollen_legs', 
                    'swollen_blood_vessels', 'excessive_hunger', 'muscle_weakness', 'stiff_neck', 'swelling_joints',
                  'movement_stiffness', 'loss_of_smell', 'passage_of_gases', 'internal_itching', 'depression', 'irritability', 'muscle_pain', 
                  'red_spots_over_body', 'belly_pain','dischromic_patches','watering_from_eyes','increased_appetite', 'polyuria','mucoid_sputum','rusty_sputum', 'visual_disturbances', 'blood_transfusion', 'unsterile_injections', 
                  'blood_in_sputum', 'prominent_veins_on_calf', 'painful_walking', 'irregular_sugar_level', 'phlegm', 'lethargy', 'toxic_look')  
    search_fields = ('disease', )
    list_filter =('disease', )  

@admin.register(models.CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('patient_id', 'first_name', 'last_name', 'user_email', 'contact', 'date_created', 'is_active', 'is_admin')
    search_fields = ('first_name', 'last_name', 'patient_email')
    list_filter = ('first_name', 'last_name', 'date_created')


@admin.register(models2.Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('doctorID', 'doctor_name', 'health_institution', 'disease_of_specialization', 'doctor_email', 'contact', 'latitude', 'longitude')
    search_fields = ('doctor_name', 'health_institution', 'disease_of_specialization')
    list_filter = ('doctor_name', 'health_institution', 'disease_of_specialization')

@admin.register(models2.InputField)
class InputFieldAdmin(admin.ModelAdmin):
    list_display = ('inputID', 'user', 'input')
    search_fields = ('user',)
    list_filter = ('user', )

@admin.register(models2.Records)
class RecordsAdmin(admin.ModelAdmin):
    list_display = ('record_id','user', 'disease', 'medicine', 'supportive_care', 'date_created')
    search_fields = ('disease',)
    list_filter = ('user', 'disease', )

@admin.register(models2.Medication)
class MedicationsAdmin(admin.ModelAdmin):
    list_display = ('disease_id', 'disease', 'medicine', 'supportive_care')
    search_fields = ('disease', )
    list_filter = ('disease', )

@admin.register(models2.Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('feedback_id', 'user', 'feedback', 'classification', 'date_added')
    search_fields = ('user', 'feedback', 'classiication', )
    list_filter = ('date_added', 'classification', )

@admin.register(models2.DiseaseInformation)
class DiseaseInformationAdmin(admin.ModelAdmin):
    list_display = ('disease_id', 'disease', 'causes', 'symptoms', 'preventive_measures')
    search_fields = ('disease',)
    list_filter = ('disease', )

@admin.register(models2.NLPLookUpTable)
class NLPLookUpTableAdmin(admin.ModelAdmin):
    list_display = ('sign_id', 'sign', 'synonym_1', 'synonym_2', 'synonym_3', 'synonym_4', 'synonym_5')
    search_fields = ('sign',)
    list_filter = ('sign',)

@admin.register(models_3.TransactionApproval)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('process_id', 'user','merchant_request_id', 'checkout_request_id', 'response_code', 'response_description', 'amount', 'mpesa_receipt_number', 'transaction_date', 'phone_number', 'payment_status')
    list_filter= ('transaction_date', )

@admin.register(models_3.LocationsViewed)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('location_id', 'user', 'doctor', 'date_viewed')
    list_filter = ('user', 'doctor', 'date_viewed', )