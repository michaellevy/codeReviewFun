VEHICLE_COUNT = 2
DIRECTIONS = ['N', 'E', 'S', 'W']
MOVEMENT = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
COMMANDS = {'L': 'turn_left', 'R': 'turn_right', 'U': 'turn_around', 'M': 'move'}


class Vehicle:
    def __init__(self, x, y, max_x, max_y, face, occupied_cells):
        self.x = x
        self.y = y
        self.max_x = max_x
        self.max_y = max_y
        self.face = face
        self.occupied_cells = set(occupied_cells)

    # When turning, set face to one position off curent direction, mod 4 in case moving N<->W
    def turn_left(self):
        self.face = DIRECTIONS[(DIRECTIONS.index(self.face) - 1) % len(DIRECTIONS)]

    def turn_right(self):
        self.face = DIRECTIONS[(DIRECTIONS.index(self.face) + 1) % len(DIRECTIONS)]

    def turn_around(self):
        self.face = DIRECTIONS[(DIRECTIONS.index(self.face) + 2) % len(DIRECTIONS)]

    def move(self):
        new_x = self.x + MOVEMENT[self.face][0]
        new_y = self.y + MOVEMENT[self.face][1]

        if (new_x, new_y) not in self.occupied_cells:
            if new_x <= self.max_x:
                self.x = new_x
            if new_y <= self.max_y:
                self.y = new_y


if __name__ == '__main__':
    max_x, max_y = map(int, raw_input().split())

    occupied_cells = set([])
    results = []
    for _ in range(VEHICLE_COUNT):
        x, y, face = raw_input().split()

        vehicle = Vehicle(int(x), int(y), max_x, max_y, face, occupied_cells)
        for command in raw_input():
            getattr(vehicle, COMMANDS[command])()
        occupied_cells.add((vehicle.x, vehicle.y))

        results.append((vehicle.x, vehicle.y, vehicle.face))

    for result in results:
        print(' '.join(str(result)))
