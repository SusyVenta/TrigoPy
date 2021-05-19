from triangle import Triangle
import json
import math

sides = {
    "a": {"value": None,
          "is_hypotenuse": False},
    "b": {"value": 105,
          "is_hypotenuse": False},
    "c": {"value": 76,
          "is_hypotenuse": False}
}

angles = {
    "A": {"value": 29,
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
    print("### START")
    triangle = Triangle()

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

        # if (angles["B"]["value"] is not None) and (
        #     sides["a"]["value"] is not None) and (angles["B"]["value"] is not None):
        #     break
        tried_n += 1


    print(json.dumps(triangle.angles, indent=4))
    print(json.dumps(triangle.sides, indent=4))


main(sides, angles)
