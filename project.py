import floor

def main():
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


    ## find name in file

    ## compare time to class start/stop times

    ## display map based on class and time records

    ## ??seperate course list and schedules??

if __name__ == '__main__':
    
    floor.display_path(107,108)