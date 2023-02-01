import pandas as pd #dependency
import numpy as np #dependency

df_teacher = pd.DataFrame({
"name": ["Pep Guardiola", "Jurgen Klopp", "Mikel Arteta", "Zinadine Zidane"],
"married": [True, True, False, True],
"school": ["Manchester High School", "Liverpool High School", "Arsenal High", np.nan]
})

df_student = pd.DataFrame({
    "teacher": ["Mikel Arteta", "Mikel Arteta", "Pep Guardiola", "Jurgen Klopp", "Jurg"
    +"en Klopp", "Jurgen Klopp", "Pep Guardiola","Pep Guardiola","Mikel Arteta"],
    "name": ["Bukayo Saka", "Gabriel Martinelli", "Jack Grealish", "Roberto Firmino",
    "Andrew Robertson", "Darwin Nunez", "Ederson Moraes", "Manuel Akanji", "Thomas Partey"],
    "age": [21, 21, 27, 31, 28, 23, 29, 27, 29],
    "height": ['2.1m','2.1m', '2.1m', '2.1m', '2.1m', '2.1m', '2.1m', '2.1m', '2.1m']
})

#This is a bit challenging and i don't have much time left to do this so
#I'm just going to write code and explain what I was going for


ds = pd.DataFrame(df_student)
dt = pd.DataFrame(df_teacher)

# This works and structures the teacher data frame like the first part of the desired part
for i in df_teacher:
    arr = [df_teacher[df_teacher.notnull().all(1)].to_json(orient="records")]
    

# Here i was trying to structure the student data in a way that when the column teacher from ds matches name column in dt
#all other columns are returned except for teacher and this would include the solution needed by Part B

for i in df_teacher:
    if df_student.index[df_student['teacher']] == arr.index['name']:
        s = ds.loc[:, ds.columns != 'teacher']

# So that when i append the student data to the arr it would look like the desired out come
arr['Students'] = [s]

print(arr)
