from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float
    z: float

# Creating an instance of the data class
p = Point(1.0, 2.0, 3.0)

# Accessing the data fields
print(p.x, p.y, p.z)  # Output: 1.0 2.0 3.0
