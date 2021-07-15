from django.http import HttpResponse
from django.shortcuts import render
from django import forms
import pickle
import numpy as np
import wikipediaapi
import requests


# Create your views here.
def index(request):
    return render(request,"index.html")


def predict(request):

    symptoms=['itching','skin_rash','nodal_skin_eruptions','continuous_sneezing','shivering','chills','joint_pain',
    'stomach_pain','acidity','ulcers_on_tongue','muscle_wasting','vomiting','burning_micturition','spotting_ urination',
    'fatigue','weight_gain','anxiety','cold_hands_and_feets','mood_swings','weight_loss','restlessness','lethargy',
    'patches_in_throat','irregular_sugar_level','cough','high_fever','sunken_eyes','breathlessness','sweating',
    'dehydration','indigestion','headache','yellowish_skin','dark_urine','nausea','loss_of_appetite','pain_behind_the_eyes',
    'back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',
    'yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach',
    'swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
    'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs',
    'fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool',
    'irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs',
    'swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
    'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips',
    'slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints',
    'movement_stiffness','spinning_movements','loss_of_balance','unsteadiness',
    'weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine',
    'continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
    'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain',
    'abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum',
    'rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion',
    'receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen',
    'history_of_alcohol_consumption','fluid_overload','blood_in_sputum','prominent_veins_on_calf',
    'palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
    'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose',
    'yellow_crust_ooze']

    disease = ['Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction',
    'Peptic ulcer diseae','AIDS','Diabetes','Gastroenteritis','Bronchial Asthma','Hypertension',
    ' Migraine','Cervical spondylosis',
    'Paralysis (brain hemorrhage)','Jaundice','Malaria','Chicken pox','Dengue','Typhoid','hepatitis A',
    'Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E','Alcoholic hepatitis','Tuberculosis',
    'Common Cold','Pneumonia','Dimorphic hemmorhoids(piles)',
    'Heartattack','Varicoseveins','Hypothyroidism','Hyperthyroidism','Hypoglycemia','Osteoarthristis',
    'Arthritis','(vertigo) Paroymsal  Positional Vertigo','Acne','Urinary tract infection','Psoriasis',
    'Impetigo']

    dic = {}
    val = 0

    for i in range(len(disease)):
        if disease[i] in dic.keys():
            disease[i] = dic[disease[i]]
        else:
            dic[disease[i]] = disease[i] = val
            val += 1


    data = []
    a = request.POST.get("sym1")
    b = request.POST.get("sym2")
    c = request.POST.get("sym3")
    d = request.POST.get("sym4")
    e = request.POST.get("sym5")
    data.append(a)
    data.append(b)
    data.append(c)
    data.append(d)
    data.append(e)


    features = []
    for i in symptoms:
        if i in data:
            features.append(1)
        else:
            features.append(0)

    features = np.reshape(features, (1,-1))


    with open('Classifier1.pkl', 'rb') as file:      
        decisionTree = pickle.load(file)

    pred1 = decisionTree.predict(features)
    prediction1 = "" 
    for i in dic.keys():
        if dic[i] == pred1:
            prediction1 = i
            break

    result = []
    
    result.append(prediction1)

    return render(request, 'result.html', {'form': result})

def details(request):
    wiki_wiki = wikipediaapi.Wikipedia('en')
    val = request.GET.get('val')
    page_py = wiki_wiki.page(val)
    
    return render(request, "details.html", {'content' : page_py.text, 'head' : val })

def location(request):
    URL = "https://discover.search.hereapi.com/v1/discover"
    coordinates = request.GET.get('val')
    index = coordinates.find(",")
    latitude = float(coordinates[:index-1])
    longitude = float(coordinates[index+1:])
    # latitude = 28.715569801497598
    # longitude = 77.26764160851835
    api_key = 'zuUMa9gijqbsVTdaCE4xbmvferkdQgb8BdmHB4lgAWQ'
    query = 'hospitals'
    limit = 10

    PARAMS = {
                'apikey':api_key,
                'q':query,
                'limit': limit,
                'at':'{},{}'.format(latitude,longitude)
            } 

    # sending get request and saving the response as response object 
    r = requests.get(url = URL, params = PARAMS) 
    data = r.json()


    hospitalOne = data['items'][0]['title']
    hospitalOne_address =  data['items'][0]['address']['label']
    # hospitalOne_latitude = data['items'][0]['position']['lat']
    # hospitalOne_longitude = data['items'][0]['position']['lng']

    hospitalTwo = data['items'][1]['title']
    hospitalTwo_address =  data['items'][1]['address']['label']

    hospitalThree = data['items'][2]['title']
    hospitalThree_address =  data['items'][2]['address']['label']

    hospitalFour = data['items'][3]['title']
    hospitalFour_address =  data['items'][3]['address']['label']

    hospitalFive = data['items'][4]['title']
    hospitalFive_address =  data['items'][4]['address']['label']

    hospitalSix = data['items'][5]['title']
    hospitalSix_address =  data['items'][5]['address']['label']

    hospitalSeven = data['items'][6]['title']
    hospitalSeven_address =  data['items'][6]['address']['label']

    hospitalEight = data['items'][7]['title']
    hospitalEight_address =  data['items'][7]['address']['label']

    hospitalNine = data['items'][8]['title']
    hospitalNine_address =  data['items'][8]['address']['label']

    hospitalTen = data['items'][9]['title']
    hospitalTen_address =  data['items'][9]['address']['label']

    result = []
    result.append(hospitalOne)
    result.append(hospitalOne_address)
    result.append(hospitalTwo)
    result.append(hospitalTwo_address)
    result.append(hospitalThree)
    result.append(hospitalThree_address)
    result.append(hospitalFour)
    result.append(hospitalFour_address)
    result.append(hospitalFive)
    result.append(hospitalFive_address)
    result.append(hospitalSix)
    result.append(hospitalSix_address)
    result.append(hospitalSeven)
    result.append(hospitalSeven_address)
    result.append(hospitalEight)
    result.append(hospitalEight_address)
    result.append(hospitalNine)
    result.append(hospitalNine_address)
    result.append(hospitalTen)
    result.append(hospitalTen_address)

    return render(request, "hospital.html", {'result' : result })

