import pickle
students = []

with open("data.csv", "r") as data:
 next(data)
 for row in data:
     students.append([int(i) if i.isnumeric() else i for i in row[:-1].split(", ")])

stud_dict = {}

for student in students:
    if student[3] in stud_dict:
        if student[5] in stud_dict[student[3]]:
            stud_dict[student[3]][student[5]].append(student)
        else:
         stud_dict[student[3]][student[5]]=[student]
    else:
        stud_dict[student[3]] = {}
        stud_dict[student[3]][student[5]] = [student]
with open("stud_dict.pkl", "wb") as file:
 pickle.dump(stud_dict, file)
 file.close()
