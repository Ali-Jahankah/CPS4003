import csv

# Constants for each column used in this module
COLUMN_SURVIVED = 1
COLUMN_CLASS = 2
COLUMN_NAME = 3
COLUMN_SEX = 4
COLUMN_AGE = 5


def load_data(file_path):
   with open(file_path,mode='r',encoding='utf-8') as file:
       csv_file = csv.reader(file)
       next(csv_file,None)
       data = [row for row in csv_file]
   return data

def extract_passengers(records):
   names = []
   for person in records:
     names.append(person[3])
   return names


def count_survivors(records):
    count = 0 
    for person in records:
        if int(person[1]) == 1:
          count+=1
    return count


def count_per_sex(records):
    male = 0
    female = 0
    for person in records:
        if person[4] == 'male':
          male+=1
        elif person[4] == 'female':
            female+=1
    return {"Male":male,"Female":female}

def count_per_age_group(records):
    children= 0
    adults= 0
    elderies= 0
    for person in records:
        if person[5]:
            age = float(person[5])
            if age <=12 and age>0:
                children+=1
            elif age>=13 and age<60:
                adults+=1
            else:
                elderies +=1 
    return {"Children":children,"Adults":adults,"Elderies":elderies}

def per_class_count(records):
    class_1 = 0
    class_2 = 0
    class_3 = 0
    for person in records:
        print(int(person[2]))
        if int(person[2]) == 1:
            class_1 += 1
        if int(person[2]) == 2:
            class_2 += 1
        if int(person[2]) == 3:
            class_3 += 1
        else:
               return
    return {
        "first": class_1,
        "second": class_2,
        "third": class_3
        }