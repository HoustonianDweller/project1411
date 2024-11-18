#<<<<<<< Jeremy
def name_input():
    name = input('Enter the name: ')
    while name not name.isalpha():
        name = input('The name needs to contain letters only')
    return name
def c_name():
    c_name = input('Enter the class name and number: ')
    return c_name
def class_start():
    start = int(input('Enter the time the class starts in 24 hour format: '))
    while start not >= 0900 and start not <= 1500:
        start = int(input('The start of the class must be after 0900 and before 1500: '))
    return start
def class_end():
    end = int(input('Enter the time the class ends in 24 hour format: '))
    while end not >= 1000 and end not <= 1600:
        end = int(input('The end of the class must be after 1000 and before 1600: '))
    return end
def room_number():
    room = int(input('Enter the room number to the classroom: '))
    while room not >= 101 and room not <= 110 and room not >= 201 and room not <= 210:
        room = int(input('The room number must be in between 101 and 110 or between 201 and 210: '))
#=======
import floor
#>>>>>>> main

def main():
    data_file = 'project_data_file.csv'
    input_name = name_input()
    input_class = c_name()
    input_s_time = class_start()
    input_e_time = class_end()
    input_room_number = room_number()

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


    ## find name in file

    ## compare time to class start/stop times

#<<<<<<< Jeremy
## ??seperate course list and schedules??
#=======
    ## display map based on class and time records

    ## ??seperate course list and schedules??

if __name__ == '__main__':
    
    floor.display_path(107,108)
#>>>>>>> main
