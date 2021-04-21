'''
PROGRAM TO CALCULATE BMI , BMI category and Health Risk given a JSON Data

ADD the results as 3 New Columns 

Calculate total persons in OverWeight Category

'''
input_json=[{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }, { "Gender": "Male", "HeightCm": 161, "WeightKg":
85 }, { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 }, { "Gender": "Female", "HeightCm": 166,
"WeightKg": 62}, {"Gender": "Female", "HeightCm": 150, "WeightKg": 70}, {"Gender": "Female", 
"HeightCm": 167, "WeightKg": 82}]

import pandas as pd
df = pd.DataFrame(input_json)

bmi_list=[]
bmi_category_list=[]
health_risk_list=[]


def get_bmi_category_health_risk(bmi):
    if bmi<18.4:
        bmi_category="Underweight"
        health_risk='Malnutrition'
    elif (bmi>=18.5 and bmi<=24.9):
        bmi_category="Normal weight"
        health_risk='Low risk'
    elif (bmi>=25 and bmi<=29.9):
        bmi_category="Overweight"
        health_risk='Enhanced risk'
    elif (bmi>=30 and bmi<=34.9):
        bmi_category="Moderately obese"
        health_risk='Medium risk'
    elif (bmi>=35 and bmi<=39.9):
        bmi_category="Severely obese"
        health_risk='High risk'
    else:
        bmi_category="Very severely obese"
        health_risk='Very high risk'
    return bmi_category,health_risk






def calculate_bmi(ht,wt):
    bmi=round(wt/(ht/100)**2,2)
    return(bmi)

for i in range(len(df)) :
    bmi_calc=calculate_bmi(df.loc[i, "HeightCm"], df.loc[i, "WeightKg"])
    bmi_list.append(bmi_calc)
    bmi_category_calc,health_risk_calc=get_bmi_category_health_risk(bmi_calc)
    bmi_category_list.append(bmi_category_calc)
    health_risk_list.append(health_risk_calc)
final_df=df.assign(**{'BMI' : bmi_list, 'BmiCategoryList' : bmi_category_list,'HealthRisk':health_risk_list})


json = final_df.to_json(orient="records")
print("Final JSON WHICH CONTAINS 3 ADDED COLUMNS >>>\n")
print(json)

    

def total_overweight_people(final_df):
    rslt_df = list(final_df['BmiCategoryList'] =='Overweight')
    return(rslt_df.count(True))
total_overweight_people_calc=total_overweight_people(final_df)
print("\nTotal Overweight People >> ")
print(total_overweight_people_calc)
