data_file = 'project_data_file.csv'
input_name = input('Enter a name: ')
input_class = input('Enter the class name: ')
input_s_time = input('Enter class start time: ')
input_e_time = input('Enter class end time: ')
input_room_number = int(input('Enter room number: '))

room_number_digits = [int(i) for i in str(input_room_number)]

with open(data_file, '+at') as f:
    f.write(f"{input_name},{input_class},{input_s_time},{input_e_time},{input_room_number}\n")

with open(data_file, 'r') as f:
    # current/last place
    # next place
    for line in f.readlines():
        print(line.rstrip('\n').split(','))

        # if time > input_s_time:
        #     current_last = input_class
        # if time < input_e_time:
        #     next_place = input_class
        ## ?? multiple time < and time > ??

#imports
import csv
from collections import Counter
## find name in file
def duplicate_names(csv_file_path, name_column):
    name_count = Counter()
    with open(csv_file_path, newline ='', encoding ='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row.get(name_column)
            if name:
                name_count[name] += 1
    duplicates = {name: count for name, count in name_count.items() if count > 1}
    return duplicates

## compare time to class start/stop times
def query_time_range(query_time, start_time, end_time):
    return start_time <= query_time <= end_time
def get_student_location(csv_file_path, query_time):
    student_location = {}
    with open(csv_file_path, newline ='', encoding ='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            student_name = row['StudentName']
            course_start_time = row['StartTime']
            course_end_time = row['EndTime']
            classroom = row['Classroom']
            if query_time_range(query_time, course_start_time, course_end_time):
                student_location[student_name] = classroom
            return student_location

locations = get_student_location(csv_file_path, query_time)
if locations:
    print(f"Student locations at {query_time}:")
    for student, classrooms in locations.items():
        print(f"{student} is in classroom {classrooms}")
else:
    print(f"No students are in class at {query_time}")


## display map based on class and time records

## ??seperate course list and schedules??