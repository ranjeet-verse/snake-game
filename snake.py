from turtle import Turtle, Screen


STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):

        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
                segment = Turtle(shape="square")
                segment.color("sky blue")
                segment.penup()
                segment.goto(position)
                self.segments.append(segment)

                self.head = self.segments[0]

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        # Add a new segment at the position of the last segment
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:  # Can't go up if going down
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:  # Can't go down if going up
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:  # Can't go left if going right
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:  # Can't go right if going left
            self.head.setheading(0)



