# Do you need to keep `directions` as a separate item? Could you not just us the keys to `movement`?
directions = ['N','E','S','W'] 
movement = {'N': (0,1), 'E': (1,0), 'S': (0,-1), 'W':(-1,0)}
commands = {'L': 'turn_left', 'R': 'turn_right', 'M': 'move'}

# Grouping the input-procssing lines together would make the program flow clearer
GRID_MAX_X, GRID_MAX_Y = map(int, raw_input().split())

# I don't think these variables do anything. If they do, consider the following comments:
# Why are second vehicle positions not initialized here or updated below? 
# Consider storing x and y locations as a tuple to keep them together.
# Do they need to be initialized with missing values? Why not just initialize with the input?
first_vehicle_x = None
first_vehicle_y = None

# Put class definitions near the top
class Vehicle():
    def __init__(self, x, y, face):
        self.x = x
        self.y = y
        self.dir = face

    # These turn functions are opaque to me. Can you clarify by simplifying
    # their operation or add a comment?
    # Also, write unit tests for each of these functions.
    def turn_left(self):
        self.dir = directions[(directions.index(self.dir)-1)%len(directions)]

    def turn_right(self):
        self.dir = directions[(directions.index(self.dir)+1)%len(directions)]

    def move(self):
        new_x = self.x + movement[self.dir][0]
        new_y = self.y + movement[self.dir][1]

        if new_x != first_vehicle_x or new_y != first_vehicle_y:
            if new_x in xrange(GRID_MAX_X+1):
                self.x = new_x
            if new_y in xrange(GRID_MAX_Y+1):  # This should be `yrange`
                self.y = new_y

# There's a lot of duplicate code for each vehicle here. Could you put it in a function?
# Better yet, is anything needed besides the intiialization, updating, and print lines for each vehicle?
vehicle_one_pos = raw_input().split()
vehicle_one_commands = raw_input()

vehicle_one = Vehicle(int(vehicle_one_pos[0]), int(vehicle_one_pos[1]), vehicle_one_pos[2])
for command in vehicle_one_commands:
    eval("vehicle_one.{0}()".format(commands[command]))

first_vehicle_x = vehicle_one.x
first_vehicle_y = vehicle_one.y


vehicle_two_pos = raw_input().split()
vehicle_two_commands = raw_input()

vehicle_two = Vehicle(int(vehicle_two_pos[0]), int(vehicle_two_pos[1]), vehicle_two_ps[2])
for command in vehicle_two_commands:
    eval("vehicle_two.{0}()".format(commands[command]))

print vehicle_one.x, vehicle_one.y, vehicle_one.dir
print vehicle_two.x, vehicle_two.y, vehicle_two.dir
