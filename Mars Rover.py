# Define the Grid and Obstacles classes
class Grid:
    def __init__(self, size_x, size_y):
        self.size_x = size_x
        self.size_y = size_y

    def is_within_bounds(self, x, y):
        return 0 <= x < self.size_x and 0 <= y < self.size_y

class Obstacles:
    def __init__(self):
        self.obstacles = set()

    def add_obstacle(self, x, y):
        self.obstacles.add((x, y))

    def has_obstacle(self, x, y):
        return (x, y) in self.obstacles

# Define command classes
class MoveCommand:
    def execute(self, rover):
        rover.move()

class LeftCommand:
    def execute(self, rover):
        rover.turn_left()

class RightCommand:
    def execute(self, rover):
        rover.turn_right()

# Define the Rover class
class Rover:
    def __init__(self, x, y, direction, obstacles):
        self.x = x
        self.y = y
        self.direction = direction
        self.obstacles = obstacles

    def move(self):
        new_x, new_y = self.x, self.y

        if self.direction == 'N':
            new_y += 1
        elif self.direction == 'S':
            new_y -= 1
        elif self.direction == 'E':
            new_x += 1
        elif self.direction == 'W':
            new_x -= 1

        if (new_x, new_y) not in self.obstacles:
            self.x, self.y = new_x, new_y

    def turn_left(self):
        if self.direction == 'N':
            self.direction = 'W'
        elif self.direction == 'S':
            self.direction = 'E'
        elif self.direction == 'E':
            self.direction = 'N'
        elif self.direction == 'W':
            self.direction = 'S'

    def turn_right(self):
        if self.direction == 'N':
            self.direction = 'E'
        elif self.direction == 'S':
            self.direction = 'W'
        elif self.direction == 'E':
            self.direction = 'S'
        elif self.direction == 'W':
            self.direction = 'N'

    def execute_commands(self, commands):
        for command in commands:
            command.execute(self)

    def status_report(self):
        obstacle_detected = (self.x, self.y) in self.obstacles
        report = f"Rover is at ({self.x}, {self.y}) facing {self.direction}."

        if obstacle_detected:
            report += " Obstacle detected!"

        return report

if __name__ == "__main__":
    # Example usage:
    obstacles = [(2, 2), (3, 5)]
    grid = Grid(10, 10)
    obstacles_obj = Obstacles()
    for obstacle in obstacles:
        obstacles_obj.add_obstacle(*obstacle)
    
    rover = Rover(0, 0, 'N', obstacles_obj.obstacles)
    commands = [MoveCommand(), MoveCommand(), RightCommand(), MoveCommand(), LeftCommand(), MoveCommand()]
    rover.execute_commands(commands)

    # Generate and print the status report
    print(rover.status_report())
