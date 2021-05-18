import math


class Triangle:
    def __init__(self, known_angles={}, known_sides={}):
        self.sides = {
            "a": {"value": None,
                  "is_hypotenuse": False},
            "b": {"value": None,
                  "is_hypotenuse": False},
            "c": {"value": None,
                  "is_hypotenuse": False}
        }

        self.angles = {
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

    def get_missing_sides(self):
        missing_sides = False
        for side_name, side_properties in self.sides.items():
            if side_properties["value"] is None:
                missing_sides = True
        if missing_sides == False:
            return self.sides

        hypotenuse = None
        for side_name, side_properties in self.sides.items():
            if side_properties["is_hypotenuse"] == True:
                hypotenuse = side_name

        """ Right triangles """
        if hypotenuse is not None:
            for angle_name, angle_properties in self.angles.items():
                """ Sin equivalences """
                if angle_properties["sine"] is not None and self.sides[hypotenuse]["value"] is not None:
                    if self.sides[angle_properties["opposite"]]["value"] is None:
                        self.sides[angle_properties["opposite"]]["value"] = (
                                angle_properties["sine"] * self.sides[hypotenuse]["value"])
                if angle_properties["sine"] is not None and self.sides[angle_properties["opposite"]]["value"] is not None:
                    self.sides[angle_properties[hypotenuse]]["value"] = (
                            self.sides[angle_properties["opposite"]]["value"] / angle_properties["sine"])
                """ Cosine equivalences """
                if self.sides[hypotenuse]["value"] is not None and angle_properties["cosine"] is not None:
                    adjacent_name = angle_properties["adjacent"]
                    self.sides[adjacent_name]["value"] = angle_properties["cosine"] * self.sides[hypotenuse]["value"]
                if self.sides[angle_properties["adjacent"]]["value"] is not None and angle_properties["cosine"] is not None:
                    self.sides[hypotenuse]["value"] = (self.sides[angle_properties["adjacent"]]["value"] /
                                                        angle_properties["cosine"])
                """ Tangent equivalences """
                if angle_properties["tangent"] is not None and self.sides[angle_properties["adjacent"]]["value"] is not None:
                    self.sides[angle_properties["opposite"]]["value"] = (angle_properties["tangent"] *
                                                                         self.sides[angle_properties["adjacent"]]["value"])
                if self.sides[angle_properties["opposite"]]["value"] is not None and angle_properties["tangent"] is not None:
                    self.sides[angle_properties["adjacent"]]["value"] = (self.sides[angle_properties["opposite"]]["value"] /
                                                                         angle_properties["tangent"])
        else:
            """ Generic triangles - sine rule """
            side = None
            side_value = None
            sin_of_opposite_angle = None
            for angle_name, angle_properties in self.angles.items():
                if angle_properties["sine"] is not None and self.sides[angle_name.lower()]["value"] is not None:
                    side = angle_name.lower()
                    side_value = self.sides[angle_name.lower()]["value"]
                    sin_of_opposite_angle = angle_properties["sine"]

            if side is not None and sin_of_opposite_angle is not None:
                for side_name, side_properties in self.sides.items():
                    if side_properties["value"] is None and self.angles[side_name.upper()]["sine"] is not None:
                        self.sides[side_name]["value"] = ((side_value / sin_of_opposite_angle) *
                                                          self.angles[side_name.upper()]["sine"])
            """generic triangle - cosine rule """
            known_sides_names = []
            known_sides_values = []
            missing_side = None
            for side_name, side_properties in self.sides.items():
                if side_properties["cosine"] is not None:
                    known_sides_names.append(side_name)
                    known_sides_values.append(side_properties["value"])
                else:
                    missing_side = side_name

            if len(known_sides_names) == 2 and self.angles[missing_side.upper()]["cosine"] is not None:
                missing_side_value = math.sqrt(((known_sides_values[0]**2) + (known_sides_values[1]**2)) -
                                               (2 * known_sides_values[0] * known_sides_values[1] *
                                                self.angles[missing_side.upper()]["cosine"]))
                self.sides[missing_side]["value"] = missing_side_value

        return self.sides

    def get_angles_in_right_triangle(self):
        hypotenuse = None
        for side_name, side_properties in self.sides.items():
            if side_properties["is_hypotenuse"] == True:
                hypotenuse = side_name

        if hypotenuse is not None:
            for angle_name, angle_properties in self.angles.items():
                if angle_properties["cosine"] is not None:
                    angle = math.degrees(math.acos(angle_properties["cosine"]))
                    self.angles[angle_name]["value"] = angle
                elif angle_properties["sine"] is not None:
                    angle = math.degrees(math.asin(angle_properties["sine"]))
                    self.angles[angle_name]["value"] = angle
                elif angle_properties["tangent"] is not None:
                    angle = math.degrees(math.atan(angle_properties["tangent"]))
                    self.angles[angle_name]["value"] = angle

        return self.angles

    def get_tangent(self):
        """ For right triangles """
        hypotenuse = None
        for side_name, side_properties in self.sides.items():
            if side_properties["is_hypotenuse"] == True:
                hypotenuse = side_name

        if hypotenuse is not None:
            for angle_name, angle_properties in self.angles.items():
                if angle_properties["cosine"] is not None and angle_properties["sine"] is not None:
                    self.angles[angle_name]["tangent"] = angle_properties["sine"] / angle_properties["cosine"]
                else:
                    if self.angles[angle_name]["opposite"] is not None and self.angles[angle_name]["adjacent"] is not None:
                        self.angles[angle_name]["tangent"] = (self.angles[angle_name]["opposite"] /
                                                              self.angles[angle_name]["adjacent"])
                    else:
                        if angle_properties["value"] is not None:
                            value = angle_properties["value"]
                            if angle_properties["unit"] == "deg":
                                value = math.radians(value)
                            self.angles[angle_name]["tangent"] = math.tan(value)
        return self.angles


    def get_cosines(self):
        """ if I have all sides - cosine rule / generalized Pythagora """
        known_sides = 0
        for side_name, side_properties in self.sides.items():
            if side_properties["value"] is not None:
                known_sides += 1

        if known_sides == 3:
            for angle_name, angle_properties in self.angles.items():
                if angle_properties["cosine"] is None:
                    opposite = angle_properties["opposite"]
                    other_sides = {"a": ["b", "c"], "b": ["a", "c"], "c": ["a", "b"]}

                    cosine = ((self.sides[other_sides[opposite][0]]["value"] ** 2 +
                               self.sides[other_sides[opposite][1]]["value"] ** 2 -
                               (self.sides[opposite]["value"] ** 2)) /

                              (2 * self.sides[other_sides[opposite][0]]["value"] *
                              self.sides[other_sides[opposite][1]]["value"]))

                    self.angles[angle_name]["cosine"] = cosine
        else:
            """ For right triangles """
            hypotenuse = None
            for side_name, side_properties in self.sides.items():
                if side_properties["is_hypotenuse"] == True:
                    hypotenuse = side_name

            for angle_name, angle_properties in self.angles.items():
                if angle_properties["adjacent"] is not None and hypotenuse is not None:
                    self.angles[angle_name]["cosine"] = (self.sides[angle_properties["adjacent"]]["value"] /
                                                         self.sides[hypotenuse]["value"])
                else:
                    if self.angles[angle_name]["sine"] is not None:
                        self.angles[angle_name]["cosine"] = math.sqrt(1 - self.angles[angle_name]["sine"] ** 2)

        return self.angles


    def get_missing_sides_pitagora(self):
        """ Pitagora's theorem """
        there_are_missing_sides = False
        for side_name, side_properties in self.sides.items():
            if side_properties["value"] is None:
                there_are_missing_sides = True

        if not there_are_missing_sides:
            return self.sides

        is_right_triangle = False
        for side_name, side_properties in self.sides.items():
            if side_properties["is_hypotenuse"]:
                is_right_triangle = True

        if is_right_triangle:
            hypotenuse_name = ""
            hypotenuse_value = None
            catheti_names = []
            catheti_values = []
            for side_name, details in self.sides.items():
                if self.sides[side_name]["is_hypotenuse"]:
                    hypotenuse_name = side_name
                    hypotenuse_value = self.sides[side_name]["value"]
                else:
                    catheti_names.append(side_name)
                    catheti_values.append(self.sides[side_name]["value"])

            if hypotenuse_value is not None and len(catheti_names) == 2:
                if catheti_values[0] is not None and catheti_values[1] is not None:
                    hypotenuse_value = math.sqrt(catheti_values[0] ** 2 + catheti_values[1] ** 2)
                    self.sides[hypotenuse_name]["value"] = hypotenuse_value

            if hypotenuse_value is not None:
                if catheti_values[1] is not None:
                    self.sides[catheti_names[0]]["value"] = math.sqrt(hypotenuse_value ** 2 - catheti_values[1] ** 2)
                elif catheti_values[0] is not None:
                    self.sides[catheti_names[0]]["value"] = math.sqrt(hypotenuse_value ** 2 - catheti_values[0] ** 2)
        else:
            """ Apply extended Pythagora's theorem / cosine rule  - I have cosine of A and sides b and c"""
            for angle_name, angle_properties in self.angles.items():
                if angle_properties["cosine"] is not None:
                    cosine = angle_properties["cosine"]
                    opposite = angle_properties["opposite"]
                    other_sides = {"a": ["b", "c"], "b": ["a", "c"], "c": ["a", "b"]}
                    if (self.sides[other_sides[angle_name.lower()][0]]["value"] is not None and
                            self.sides[other_sides[angle_name.lower()][1]]["value"] is not None):
                        known_side_1 = self.sides[other_sides[angle_name.lower()][0]]["value"]
                        known_side_2 = self.sides[other_sides[angle_name.lower()][1]]["value"]
                        self.sides[opposite]["value"] = (math.sqrt(known_side_1 ** 2 + known_side_2 ** 2 -
                                                                   (2 * known_side_1 * known_side_2 * cosine)))

        return self.sides

    def get_sines(self):
        is_right_triangle = False

        """ If the angle is available, get sin directly from angle """
        for angle_name, angle_properties in self.angles.items():
            if angle_properties["value"] is not None:
                angle_value = angle_properties["value"]
                if angle_properties["unit"] == "deg":
                    angle_value = math.radians(angle_properties["value"])
                sine = math.sin(angle_value)
                self.angles[angle_name]["sine"] = sine
            if ((angle_properties["unit"] == "deg" and angle_properties["value"] == 90) or
                    (angle_properties["unit"] == "rad") and (angle_properties["value"] == math.pi / 2)):
                is_right_triangle = True

        """ If sin not available and it's a right triangle: """
        if is_right_triangle:
            for angle_name, angle_properties in self.angles.items():
                opposite = angle_properties["opposite"]
                hypotenuse = angle_properties["hypotenuse"]
                if (hypotenuse is not None and self.sides[opposite]["value"] is not None
                        and self.sides[hypotenuse]["value"] is not None):
                    sine = self.sides[opposite]["value"] / self.sides[hypotenuse]["value"]
                    self.angles[angle_name]["sine"] = sine
                else:
                    if self.angles[angle_name]["cosine"] is not None:
                        sine = math.sqrt(1 - (self.angles[angle_name]["cosine"] ** 2))
                        self.angles[angle_name]["sine"] = sine

        """ sine rule """
        for angle_name, angle_properties in self.angles.items():
            other_angles = {"A": ["B", "C"], "B": ["A", "C"], "C": ["A", "B"]}
            sine = self.angles[angle_name]["sine"]
            if sine is not None and angle_properties["opposite"] is not None:
                if self.sides[angle_properties["opposite"]]["value"] is not None:

                    for other_angle in other_angles[angle_name]:
                        if (self.angles[other_angle]["sine"] is None and
                                self.sides[self.angles[other_angle]["opposite"]]["value"] is not None):
                            self.angles[other_angle]["sine"] = ((sine *
                                                                 self.sides[self.angles[other_angle]["opposite"]][
                                                                     "value"]) /
                                                                self.sides[angle_properties["opposite"]]["value"])
        return self.angles

    def assign_known_angles(self, known_angles, known_sides):
        for angle_name in known_angles.keys():
            for angle_propery, property_value in known_angles[angle_name].items():
                if self.angles[angle_name][angle_propery] is None:
                    self.angles[angle_name][angle_propery] = known_angles[angle_name][angle_propery]

        for side_name in known_sides.keys():
            if known_sides[side_name]["is_hypotenuse"]:
                self.angles[side_name.upper()]["value"] = 90

        return self.angles

    def assign_known_sides(self, known_sides, known_angles):
        right_angle = None
        for angle_name, values_dict in known_angles.items():
            if known_angles[angle_name]["value"] == 90:
                right_angle = angle_name

        for side_name in known_sides.keys():
            if self.sides[side_name]["value"] is None:
                self.sides[side_name]["value"] = known_sides[side_name]["value"]
            self.sides[side_name]["is_hypotenuse"] = known_sides[side_name]["is_hypotenuse"]
            if right_angle is not None and side_name == right_angle.lower():
                self.sides[side_name]["is_hypotenuse"] = True

        return self.sides

    def derive_missing_angles_given_two_known_angles(self):
        missing_angle = ""
        number_of_present_angles = 0
        present_angles = []
        for angle_name, angle_properties in self.angles.items():
            if angle_properties["value"] is not None:
                number_of_present_angles += 1
                present_angles.append(angle_properties["value"])
            else:
                missing_angle = angle_name

        if number_of_present_angles == 2:
            self.angles[missing_angle]["value"] = 180 - (int(present_angles[0]) + int(present_angles[1]))

        return self.angles

    def find_adjacent_sides(self):
        """ Adjacent side is the smallest side next to an angle """
        sides_angles_map = {
            "A": [[self.sides["b"], "b"], [self.sides["c"], "c"]],
            "B": [[self.sides["a"], "a"], [self.sides["c"], "c"]],
            "C": [[self.sides["a"], "a"], [self.sides["b"], "b"]]
        }
        for angle_name in self.angles.keys():
            if sides_angles_map[angle_name][0][0]["value"] is None or sides_angles_map[angle_name][1][0][
                "value"] is None:
                return self.angles
            if sides_angles_map[angle_name][0][0]["value"] < sides_angles_map[angle_name][1][0]["value"]:
                self.angles[angle_name]["adjacent"] = sides_angles_map[angle_name][0][1]
            else:
                self.angles[angle_name]["adjacent"] = sides_angles_map[angle_name][1][1]

        return self.angles
