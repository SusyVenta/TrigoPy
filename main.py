from triangle import Triangle
import json
import math

sides = {
    "a": {"value": 1,
          "is_hypotenuse": False},
    "b": {"value": 1,
          "is_hypotenuse": False},
    "c": {"value": math.sqrt(2),
          "is_hypotenuse": True}
}

angles = {
    "A": {"value": None,
          "unit": "deg",
          "sine": None,
          "cosine": None,
          "tangent": None,
          "opposite": "a",
          "hypotenuse": None,
          "adjacent": None},
    "B": {"value": None,
          "unit": "deg",
          "sine": None,
          "cosine": None,
          "tangent": None,
          "opposite": "b",
          "hypotenuse": None,
          "adjacent": None},
    "C": {"value": None,
          "unit": "deg",
          "sine": None,
          "cosine": None,
          "tangent": None,
          "opposite": "c",
          "hypotenuse": None,
          "adjacent": None}
}


def main(sides, angles):
    triangle = Triangle(known_sides=sides, known_angles=angles)

    tried_n = 0
    while tried_n < 1000:
        triangle.sides = triangle.assign_known_sides(known_sides=sides, known_angles=angles)
        triangle.angles = triangle.assign_known_angles(known_angles=angles, known_sides=sides)
        triangle.sides = triangle.assign_known_sides(known_sides=sides, known_angles=angles)
        triangle.angles = triangle.assign_known_angles(known_angles=angles, known_sides=sides)
        triangle.angles = triangle.derive_missing_angles_given_two_known_angles()
        triangle.angles = triangle.find_adjacent_sides()
        triangle.angles = triangle.get_sines()
        triangle.sides = triangle.get_missing_sides_pitagora()
        triangle.angles = triangle.get_cosines()
        triangle.angles = triangle.get_tangent()
        triangle.angles = triangle.get_angles_in_right_triangle()
        triangle.sides = triangle.get_missing_sides()

        if angles["B"]["tangent"] is not None:
            break
        tried_n += 1


    print(json.dumps(triangle.angles, indent=4))
    print(json.dumps(triangle.sides, indent=4))


main(sides, angles)
