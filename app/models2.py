from django.db import models
from .models import CustomUser
from datetime import datetime

class Medication(models.Model):
    disease_id = models.AutoField(primary_key=True, unique=True)
    disease = models.CharField(max_length=255, unique =True)
    medicine = models.CharField(max_length=255, null=True)
    supportive_care = models.TextField(max_length=1000, null=True)

    def __str__(self):
        return f'{self.disease} can be treated with {self.medicine}'
    
class MachineLearningModelData(models.Model):
    item_id = models.AutoField(primary_key=True, unique=True)
    itching = models.BooleanField()
    skin_rash = models.BooleanField()
    nodal_skin_eruptions= models.BooleanField()
    continuous_sneezing = models.BooleanField()
    shivering = models.BooleanField()
    chills = models.BooleanField()
    joint_pain = models.BooleanField()
    acidity = models.BooleanField()
    vomiting = models.BooleanField()
    fatigue = models.BooleanField()
    weight_loss = models.BooleanField()
    restlessness =  models.BooleanField()
    cough = models.BooleanField()
    high_fever = models.BooleanField()
    breathlessness = models.BooleanField()
    sweating = models.BooleanField()
    indigestion = models.BooleanField()
    headache = models.BooleanField()
    yellowish_skin = models.BooleanField()
    dark_urine = models.BooleanField()
    nausea = models.BooleanField()
    loss_of_appetite = models.BooleanField(default=False)
    pain_behind_the_eyes = models.BooleanField()
    back_pain = models.BooleanField()
    constipation = models.BooleanField()
    abdominal_pain = models.BooleanField()
    diarrhea = models.BooleanField()
    mild_fever = models.BooleanField()
    yellow_urine = models.BooleanField()
    yellowing_of_eyes = models.BooleanField()
    swelled_lymph_nodes = models.BooleanField()
    malaise = models.BooleanField()
    blurred_vision = models.BooleanField()
    throat_irritation = models.BooleanField()
    redness_of_eyes = models.BooleanField()
    sinus_pressure = models.BooleanField()
    congestion = models.BooleanField()
    runny_nose = models.BooleanField()
    chest_pain = models.BooleanField()
    fast_heart_rate = models.BooleanField()
    cramps = models.BooleanField()
    bruising = models.BooleanField()
    obesity = models.BooleanField()
    swollen_legs = models.BooleanField()
    swollen_blood_vessels = models.BooleanField()
    excessive_hunger = models.BooleanField()
    muscle_weakness = models.BooleanField()
    stiff_neck = models.BooleanField()
    swelling_joints = models.BooleanField()
    movement_stiffness = models.BooleanField()
    loss_of_smell = models.BooleanField()
    passage_of_gases = models.BooleanField()
    internal_itching = models.BooleanField()
    depression = models.BooleanField()
    irritability = models.BooleanField()
    muscle_pain = models.BooleanField()
    red_spots_over_body = models.BooleanField()
    belly_pain = models.BooleanField()
    dischromic_patches = models.BooleanField()
    watering_from_eyes = models.BooleanField()
    increased_appetite = models.BooleanField()
    polyuria = models.BooleanField()
    mucoid_sputum = models.BooleanField()
    rusty_sputum = models.BooleanField()
    visual_disturbances = models.BooleanField()
    blood_transfusion = models.BooleanField()
    unsterile_injections = models.BooleanField()
    blood_in_sputum = models.BooleanField()
    prominent_veins_on_calf = models.BooleanField()
    painful_walking = models.BooleanField()
    irregular_sugar_level = models.BooleanField()
    phlegm = models.BooleanField()
    lethargy = models.BooleanField()
    toxic_look= models.BooleanField()
    disease = models.CharField(max_length=255)

class Records(models.Model):
    record_id = models.AutoField(primary_key=True, unique=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    disease = models.CharField(max_length=100)
    medicine = models.CharField(max_length = 100)
    supportive_care = models.CharField(max_length = 100)
    date_created = models.DateTimeField(auto_now_add=True)

class Doctor(models.Model):
    doctorID = models.AutoField(unique= True , primary_key=True )
    doctor_name = models.CharField(max_length=255)
    health_institution = models.CharField(max_length=255)
    disease_of_specialization = models.CharField(max_length=255)
    doctor_email = models.EmailField(max_length=255, unique=True)
    contact = models.BigIntegerField()
    latitude = models.DecimalField(max_digits=20, decimal_places=17)   
    longitude = models.DecimalField(max_digits=20, decimal_places=17) 

    def __str__(self):
        return self.doctor_name      

class InputField(models.Model):
    inputID = models.AutoField(unique=True, primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    input = models.TextField(max_length=300, null=True)


class NLPLookUpTable(models.Model):
    sign_id = models.AutoField(unique=True, primary_key=True)
    sign = models.CharField(max_length=255)
    synonym_1= models.CharField(max_length=255)
    synonym_2 = models.CharField(max_length=255)
    synonym_3 = models.CharField(max_length=255)
    synonym_4 = models.CharField(max_length=255)
    synonym_5 = models.CharField(max_length=255)

class DoctorsViewed(models.Model):
    doctorsViewed_id = models.AutoField(unique=True, primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

class Feedback(models.Model):
    feedback_id = models.AutoField(unique=True, primary_key = True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    feedback = models.TextField(max_length=2000)
    classification = models.CharField(max_length=20, default='Positive')
    date_added = models.DateTimeField(auto_now_add=True)


class DiseaseInformation(models.Model):
    disease_id = models.AutoField(unique=True, primary_key=True)
    disease = models.CharField(max_length=255)
    description = models.CharField(max_length = 2000, default = '')
    causes = models.CharField(max_length = 2000)
    symptoms = models.CharField(max_length = 2000)
    preventive_measures = models.CharField(max_length = 2000)
