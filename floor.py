import turtle as t

# floor (x)560 x (y)640
# center (280,320)
# room 80 x 80
# room number:
#   fist digit: floor
#   2/3 digit: number (odd on top)

# 1: gotto start_rm
# 2: enter hall (left:even/right:odd 90 fw 80)
# 3: hall turn **TBD (from even: left:going lower/right:going higher)(from odd: right:going lower/left going higher) (no turn: rm +/- 1)
# 4: hall move **TBD (in front of room or into strairwell) rm difference/2 *80(rm width)
# 5: to_rm_turn (left/right 90 fw 80) @ end_room
#     or
# 5: jump to floor
# 6: hall move **TBD
# 7: to_rm_turn (left/right 90 fw 80) @ end_room

Y_START = 160
ROOM_X ={
    1: -160,
    2: -160,
    3: -80,
    4: -80,
    5: 0,
    6: 0,
    7: 80,
    8: 80,
    9: 160,
    10: 160,
    11: 240
}

floor_start:int = 0
room_start:int = 0
floor_end:int = 0
room_end:int = 0

# t.bgpic('floors_1.png')
# t.penup()

def split_floor_room(room_number:int) ->tuple[int, int]:
    """
    Split room_number integer into floor integer and room integer.
    Args:
        room_number (str): 3 digit room number.
    Returns: (floor, room)
    """
    room_number = [int(i) for i in str(room_number)]
    return (room_number[0], room_number[1] * 10 + room_number[2])

def go_to_start(start_room:int, end_room:int=None) -> t.Vec2D:
    """
    Moves cursor to start room.
        1) Determines if room number is even or odd.
        2) Moves cursor to starting room.
        3) Draws a circle in room if end_room is None.
    Args:
        start_room: room number for cursor move
        end_room: indicates if line or corcle will be drawn.
    Returns:
        cursor location
    """
    movement = -80 if room_start % 2 == 0 else 80
    t.setposition(ROOM_X[room_start], Y_START + movement)

    if end_room is None:
        t.pendown()
        t.circle(10)
    t.penup()
    
def leave_classroom():
    """
    Draw line from room into hallway.
        1) Set heading based on current position.
        2) Draw line into hallway.
    Args:
        class_pos: current cursor position
    Returns:
        cursor location
    """
    t.pendown()
    t.goto(t.xcor(), Y_START)

def hall_move():
    """
    Set cursor heading before moving down the hallway.
        1) .
        2) Draw line into hallway.
    Args:
        class_pos: current cursor position
    Returns:
        cursor location
    """
    floor_y = Y_START
    if floor_start != floor_end:
        t.goto(ROOM_X[11], 180)
        t.penup()
        floor_y = -160
        t.goto(ROOM_X[11], -180)
        t.pendown()
    
    t.goto(ROOM_X[room_end], floor_y)

def enter_classroom():
    """
    Enter classroom from the hallway.
        1) Determine if room number is odd or even.
        2) Draw line into classroom.
    Args:
        class_pos: current cursor position
    Returns:
        cursor location
    """
    movement = -80 if room_end % 2 == 0 else 80
    t.goto(t.xcor(), t.ycor() + movement)

def display_path(friend_start:int, friend_end:int=None, you_start:int=None, you_end:int=None):
    global floor_start, room_start, floor_end, room_end
    floor_start, room_start = split_floor_room(friend_start)
    floor_end, room_end = split_floor_room(friend_end) # if friend_end else (floor_start)

    if floor_start == floor_end: 
        t.bgpic('floors_1.png') 
    else:
        t.bgpic('floors_2.png')

    t.penup()
    t.goto(-240, Y_START)
    t.write(f'{friend_start},{friend_end}')
    go_to_start(friend_start, friend_end)
    t.pendown()
    leave_classroom()
    hall_move()
    enter_classroom()
    t.penup()
    if __name__ != '__main__':
        t.mainloop()

    # t.mainloop()

if __name__ == '__main__':
    t.speed(10)
    for i in range(101, 111):
        for j in range(101, 111):
            display_path(i, j)
            t.clear()
        for j in range(201, 211):
            display_path(i, j)
            t.clear()
    t.speed(6)