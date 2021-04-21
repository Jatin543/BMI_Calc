'''
To write test cases i m using pytest Framework

'''
input_json=[{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }, { "Gender": "Male", "HeightCm": 161, "WeightKg":
85 }, { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 }, { "Gender": "Female", "HeightCm": 166,
"WeightKg": 62}, {"Gender": "Female", "HeightCm": 150, "WeightKg": 70}, {"Gender": "Female", 
"HeightCm": 167, "WeightKg": 82}]


final_result='[{"Gender":"Male","HeightCm":171,"WeightKg":96,"BMI":32.83,"BmiCategoryList":"Moderately obese","HealthRisk":"Medium risk"},{"Gender":"Male","HeightCm":161,"WeightKg":85,"BMI":32.79,"BmiCategoryList":"Moderately obese","HealthRisk":"Medium risk"},{"Gender":"Male","HeightCm":180,"WeightKg":77,"BMI":23.77,"BmiCategoryList":"Normal weight","HealthRisk":"Low risk"},{"Gender":"Female","HeightCm":166,"WeightKg":62,"BMI":22.5,"BmiCategoryList":"Normal weight","HealthRisk":"Low risk"},{"Gender":"Female","HeightCm":150,"WeightKg":70,"BMI":31.11,"BmiCategoryList":"Moderately obese","HealthRisk":"Medium risk"},{"Gender":"Female","HeightCm":167,"WeightKg":82,"BMI":29.4,"BmiCategoryList":"Overweight","HealthRisk":"Enhanced risk"}]'


from BMI_python import get_bmi_category_health_risk,calculate_bmi,total_overweight_people
import pandas as pd
df = pd.DataFrame(input_json)

bmi_list=[]
bmi_category_list=[]
health_risk_list=[]


for i in range(len(df)) :
    bmi_calc=calculate_bmi(df.loc[i, "HeightCm"], df.loc[i, "WeightKg"])
    bmi_list.append(bmi_calc)
    bmi_category_calc,health_risk_calc=get_bmi_category_health_risk(bmi_calc)
    bmi_category_list.append(bmi_category_calc)
    health_risk_list.append(health_risk_calc)
final_df=df.assign(**{'BMI' : bmi_list, 'BmiCategoryList' : bmi_category_list,'HealthRisk':health_risk_list})


json = final_df.to_json(orient="records")
print(json)
import pytest
def test_final_json():
	assert json == final_result

def test_total_overweight_people():
    x=1
    assert x == total_overweight_people(final_df)

