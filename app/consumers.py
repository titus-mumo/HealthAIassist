from channels.generic.websocket import AsyncWebsocketConsumer
import re
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from .models import UserSymptoms
from .models2 import NLPLookUpTable, MachineLearningModelData
from .nlp import check_similarity

class ProcessingConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        
    async def process_input(self, event):
        # Receive the input data from the WebSocket message and perform the processing logic
        input_data = event.get('input_data', None)
        #fields = request.session.get('fields')
        raw_data = event.get('fields', None)
        input = event.get('raw_data', None)
        signs = UserSymptoms()
        signs.user = self.scope['user']
        processed_raw_data = []
        for i in raw_data:
            if i == 'yes':
                processed_raw_data.append(True)
            else:
                processed_raw_data.append(False)
        print(processed_raw_data)
        for i, field in enumerate(fields):
            setattr(signs, field, processed_raw_data[i])
        input = str(input.input)
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
        self.scope['session']['predicted_disease'] = predicted_disease
        # Send the result back to the client
        await self.send(text_data=predicted_disease)