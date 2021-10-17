import pandas as pd

BMI_df = pd.read_json("Source_file.json")
# print(cars)
cm_to_m = BMI_df['HeightCm']/100
BMI_df["BMI"] = BMI_df['WeightKg'] / (cm_to_m ** 2)
print(BMI_df)
