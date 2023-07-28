from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from datetime import datetime
class CustomUserManager(BaseUserManager):
    def create_user(self, first_name, last_name, user_email, contact, password):
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            user_email=self.normalize_email(user_email),
            contact=contact,
        )
        user.patient_id = models.AutoField(unique=True, primary_key=True)
        user.date_created = datetime.now
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, user_email, contact, password):
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            User_email=user_email,
            contact=contact,
            password=password,
        )
        user.patient_id = models.AutoField(unique=True, primary_key=True)
        user.is_admin = True
        user.is_staff = True
        user.date_created = datetime.now
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser):
    patient_id = models.AutoField(unique=True, primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user_email = models.EmailField(max_length=30, unique=True)
    contact = models.CharField(max_length=15)
    date_created = models.DateTimeField(auto_now_add=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'user_email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'contact']

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    def __str__(self):
        return f'{self.user_email}'
    
class UserSymptoms(models.Model):
    symptom_id = models.AutoField(primary_key=True, unique=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    itching = models.BooleanField(null=True)
    skin_rash = models.BooleanField(null=True)
    nodal_skin_eruptions= models.BooleanField(null=True)
    continuous_sneezing = models.BooleanField(null=True)
    shivering = models.BooleanField(null=True)
    chills = models.BooleanField(null=True)
    joint_pain = models.BooleanField(null=True)
    acidity = models.BooleanField(null=True)
    vomiting = models.BooleanField(null=True)
    fatigue = models.BooleanField(null=True)
    weight_loss = models.BooleanField(null=True)
    restlessness =  models.BooleanField(null=True)
    cough = models.BooleanField(null=True)
    high_fever = models.BooleanField(null=True)
    breathlessness = models.BooleanField(null=True)
    sweating = models.BooleanField(null=True)
    indigestion = models.BooleanField(null=True)
    headache = models.BooleanField(null=True)
    yellowish_skin = models.BooleanField(null=True)
    dark_urine = models.BooleanField(null=True)
    nausea = models.BooleanField(null=True)
    loss_of_appetite = models.BooleanField(null=True, default=False)
    pain_behind_the_eyes = models.BooleanField(null=True)
    back_pain = models.BooleanField(null=True)
    constipation = models.BooleanField(null=True)
    abdominal_pain = models.BooleanField(null=True)
    diarrhea = models.BooleanField(null=True)
    mild_fever = models.BooleanField(null=True)
    yellow_urine = models.BooleanField(null=True)
    yellowing_of_eyes = models.BooleanField(null=True)
    swelled_lymph_nodes = models.BooleanField(null=True)
    malaise = models.BooleanField(null=True)
    blurred_vision = models.BooleanField(null=True)
    throat_irritation = models.BooleanField(null=True)
    redness_of_eyes = models.BooleanField(null=True)
    sinus_pressure = models.BooleanField(null=True)
    congestion = models.BooleanField(null=True)
    runny_nose = models.BooleanField(null=True)
    chest_pain = models.BooleanField(null=True)
    fast_heart_rate = models.BooleanField(null=True)
    cramps = models.BooleanField(null=True)
    bruising = models.BooleanField(null=True)
    obesity = models.BooleanField(null=True)
    swollen_legs = models.BooleanField(null=True)
    swollen_blood_vessels = models.BooleanField(null=True)
    excessive_hunger = models.BooleanField(null=True)
    muscle_weakness = models.BooleanField(null=True)
    stiff_neck = models.BooleanField(null=True)
    swelling_joints = models.BooleanField(null=True)
    movement_stiffness = models.BooleanField(null=True)
    loss_of_smell = models.BooleanField(null=True)
    passage_of_gases = models.BooleanField(null=True)
    internal_itching = models.BooleanField(null=True)
    depression = models.BooleanField(null=True)
    irritability = models.BooleanField(null=True)
    muscle_pain = models.BooleanField(null=True)
    red_spots_over_body = models.BooleanField(null=True)
    belly_pain = models.BooleanField(null=True)
    dischromic_patches = models.BooleanField(null=True)
    watering_from_eyes = models.BooleanField(null=True)
    increased_appetite = models.BooleanField(null=True)
    polyuria = models.BooleanField(null=True)
    mucoid_sputum = models.BooleanField(null=True)
    rusty_sputum = models.BooleanField(null=True)
    visual_disturbances = models.BooleanField(null=True)
    blood_transfusion = models.BooleanField(null=True)
    unsterile_injections = models.BooleanField(null=True)
    blood_in_sputum = models.BooleanField(null=True)
    prominent_veins_on_calf = models.BooleanField(null=True)
    painful_walking = models.BooleanField(null=True)
    irregular_sugar_level = models.BooleanField(null=True)
    phlegm = models.BooleanField(null=True)
    lethargy = models.BooleanField(null=True)
    toxic_look= models.BooleanField(null=True)
    predicted_disease = models.CharField(null=False, default='', max_length=255)
    date_diagonised= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'



