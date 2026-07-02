class Rhombus:
    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a

    def __setattr__(self, name, value):
        if name == "side_a" and value <= 0:
            raise ValueError("Сторона повинна бути більшою за 0")

        if name == "angle_a":
            object.__setattr__(self, "angle_b", 180 - value)

        object.__setattr__(self, name, value)
        