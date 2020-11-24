import json

personal_data_file = open("personaldata.json", "r")
personal_data = json.loads(personal_data_file.read())

print(personal_data)
print(personal_data["age"])
print(personal_data["cars"][0]["model"])

academic_data_dict = {"Graduation": "B.E.Mechanical", "Post-Graduation": "M.Tech. Aircraft Production"}
academic_data = json.dumps(academic_data_dict)
academic_data_file = open("academic_data.json", "w")
academic_data_file.write(academic_data)
