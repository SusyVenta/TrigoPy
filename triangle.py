import math


class Triangle:
    def __init__(self):
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
                        print("\n------------------------------------------------------------------------------")
                        print(f"It's a right triangle. Applying sin equivalence. Getting side of opposite of "
                              f"{angle_name} ({angle_properties['opposite']}) as: sine of {angle_name} "
                              f"({angle_properties['sine']} * hypothenuse ({self.sides[hypotenuse]['value']})\n"
                              f"Side {angle_properties['opposite']} = {self.sides[angle_properties['opposite']]['value']}")
                if ((angle_properties["opposite"] is not None) and (angle_properties["sine"] is not None)
                        and (angle_properties["sine"] is not None) and
                        (self.sides[angle_properties["opposite"]]["value"] is not None) and
                        angle_properties["sine"] != 0):
                    self.sides[hypotenuse]["value"] = (
                            self.sides[angle_properties["opposite"]]["value"] / angle_properties["sine"])
                    print("\n------------------------------------------------------------------------------")
                    print(f"It's a right triangle. Applying sin equivalence. hypotenuse = opposite ({angle_name}) / "
                          f"sine({angle_name}) = {self.sides[angle_properties['opposite']]['value']} / "
                          f"{angle_properties['sine']} \n= {self.sides[hypotenuse]['value']}")
                """ Cosine equivalences """
                if (self.sides[hypotenuse]["value"] is not None and angle_properties["cosine"] is not None and
                    angle_properties["adjacent"] is not None):
                    adjacent_name = angle_properties["adjacent"]
                    self.sides[adjacent_name]["value"] = angle_properties["cosine"] * self.sides[hypotenuse]["value"]
                    print("\n------------------------------------------------------------------------------")
                    print(f"It's a right triangle. Applying sin equivalence. adjacent = cosine({angle_name}) * "
                          f"hypothenuse\n= {angle_properties['cosine']} * {self.sides[hypotenuse]['value']}\n"
                          f"= {self.sides[adjacent_name]['value']}")
                if angle_properties["adjacent"] is not None and (self.sides[angle_properties["adjacent"]]["value"] is not None) and (angle_properties["cosine"] is not None):
                    self.sides[hypotenuse]["value"] = (self.sides[angle_properties["adjacent"]]["value"] /
                                                        angle_properties["cosine"])
                    print("\n------------------------------------------------------------------------------")
                    print(f"It's a right triangle. Applying sin equivalence. hypotenuse = adjacent({angle_name}) / "
                          f"cosine({angle_name}) = {self.sides[hypotenuse]['value']}")
                """ Tangent equivalences """
                if angle_properties["adjacent"] is not None and angle_properties["tangent"] is not None and self.sides[angle_properties["adjacent"]]["value"] is not None:
                    self.sides[angle_properties["opposite"]]["value"] = (angle_properties["tangent"] *
                                                                         self.sides[angle_properties["adjacent"]]["value"])
                    print("\n------------------------------------------------------------------------------")
                    print(f"It's a right triangle. Applying tangent equivalence. opposite({angle_name}) = "
                          f"tangent({angle_name}) * adjacent ({angle_name}) = {angle_properties['tangent']} * "
                          f"{self.sides[angle_properties['adjacent']]['value']}")
                if ((angle_properties["opposite"] is not None) and
                        (self.sides[angle_properties["opposite"]]["value"] is not None)
                        and (angle_properties["tangent"] is not None) and (angle_properties["tangent"] != 0)
                        and (angle_properties["adjacent"] is not None)):
                    self.sides[angle_properties["adjacent"]]["value"] = (self.sides[angle_properties["opposite"]]["value"] /
                                                                         angle_properties["tangent"])
                    print("\n------------------------------------------------------------------------------")
                    print(f"It's a right triangle. Applying tangent equivalence. adjacent({angle_name}) = "
                          f"opposite({angle_name}) / tangent ({angle_name}) = "
                          f"{self.sides[angle_properties['opposite']]['value']} = "
                          f"{self.sides[angle_properties['adjacent']]['value']}")
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

                        print("\n------------------------------------------------------------------------------")
                        print(f"Generic triangle. Applying sin rule: (side_value / sin_of_opposite_angle) * self.angles[side_name.upper()]['sine']\n"
                              f"{side_name} = ({side_value} / {sin_of_opposite_angle}) * "
                              f"{self.angles[side_name.upper()]['sine']}\n={self.sides[side_name]['value']}")
            """generic triangle - cosine rule """
            known_sides_names = []
            known_sides_values = []
            missing_side = None
            for side_name, side_properties in self.sides.items():
                if side_properties["value"] is not None:
                    known_sides_names.append(side_name)
                    known_sides_values.append(side_properties["value"])
                else:
                    missing_side = side_name
            if len(known_sides_names) == 2 and self.angles[missing_side.upper()]["cosine"] is not None:
                missing_side_value = math.sqrt(((known_sides_values[0]**2) + (known_sides_values[1]**2)) -
                                               (2 * known_sides_values[0] * known_sides_values[1] *
                                                self.angles[missing_side.upper()]["cosine"]))
                self.sides[missing_side]["value"] = missing_side_value
                print("\n------------------------------------------------------------------------------")
                print(f"Generic triangle. Applying cosine rule: {missing_side} = (known_side_1 ^2) + "
                      f"(known_side_2 ^2)) - (2 * known_side_1 * known_side_2 * cosine({missing_side}) \n="
                      f"{missing_side_value}")

        return self.sides

    def get_angles_in_right_triangle(self):

        hypotenuse = None
        for side_name, side_properties in self.sides.items():
            if side_properties["is_hypotenuse"] == True:
                hypotenuse = side_name

        for angle_name, angle_properties in self.angles.items():
            if self.angles[angle_name]["value"] is None:
                if angle_properties["sine"] is not None:
                    """ When doing sin^-1 there are two solutions: x and 180 - x"""
                    angle = math.degrees(math.asin(angle_properties["sine"]))
                    required_solution = input("\nThere are two sin^-1 solutions. Do you want 1 (x) or 2 (180 - x)? Press 1 or 2")
                    print(required_solution)
                    if int(required_solution) == 2:
                        angle = 180 - angle
                    self.angles[angle_name]["value"] = angle
                    print("\n------------------------------------------------------------------------------")
                    print(f"{angle_name} = degrees(sin^-1(sin({angle_name}))) = sin^-1({angle_properties['sine']})\n"
                          f"= {angle}")

                elif angle_properties["cosine"] is not None:
                    angle = math.degrees(math.acos(angle_properties["cosine"]))
                    self.angles[angle_name]["value"] = angle
                    print("\n------------------------------------------------------------------------------")
                    print(f"{angle_name} = degrees(cos^-1(cos({angle_name}))) = cos^-1({angle_properties['cosine']})\n"
                          f"= {angle}")
                elif angle_properties["tangent"] is not None:
                    angle = math.degrees(math.atan(angle_properties["tangent"]))
                    self.angles[angle_name]["value"] = angle
                    print("\n------------------------------------------------------------------------------")
                    print(f"{angle_name} = degrees(tan^-1(tan({angle_name}))) = tan^-1({angle_properties['tangent']})\n"
                          f"= {angle}")

        return self.angles

    def get_tangent(self):
        """ For right triangles """
        hypotenuse = None
        for side_name, side_properties in self.sides.items():
            if side_properties["is_hypotenuse"] == True:
                hypotenuse = side_name

        if hypotenuse is not None:
            for angle_name, angle_properties in self.angles.items():
                if self.angles[angle_name]["tangent"] is None:
                    if angle_properties["cosine"] is not None and angle_properties["sine"] is not None:
                        try:
                            self.angles[angle_name]["tangent"] = angle_properties["sine"] / angle_properties["cosine"]
                            print("\n------------------------------------------------------------------------------")
                            print(f"tangent({angle_name}) = sine({angle_name}) / cosin({angle_name}) = "
                                  f"{self.angles[angle_name]['tangent']}")
                        except ZeroDivisionError:
                            pass
                    else:
                        if self.angles[angle_name]["opposite"] is not None and self.angles[angle_name]["adjacent"] is not None:
                            self.angles[angle_name]["tangent"] = (self.sides[self.angles[angle_name]["opposite"]]["value"] /
                                                                  self.sides[self.angles[angle_name]["adjacent"]]["value"])
                            print("\n------------------------------------------------------------------------------")
                            print(f"tangent({angle_name}) = opposite({angle_name}) / adjacent({angle_name}) = "
                                  f"{self.angles[angle_name]['opposite']} / {self.angles[angle_name]['adjacent']} = \n"
                                  f"{self.angles[angle_name]['tangent']}")
                        else:
                            if angle_properties["value"] is not None:
                                value = angle_properties["value"]
                                if angle_properties["unit"] == "deg":
                                    value = math.radians(value)
                                self.angles[angle_name]["tangent"] = math.tan(value)
                                print("\n------------------------------------------------------------------------------")
                                print(f"tangent({angle_name}) = tan({angle_name}) = tan({value}) = "
                                      f"{self.angles[angle_name]['tangent']}")
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
                    print("\n------------------------------------------------------------------------------")
                    print(f"Three sides are known: cosine({angle_name}) = (non_opposite_side_1 ^ 2 + "
                          f"non_opposite_side_2 ^ 2 - opposite_side ^ 2) / (2 * non_opposite_side_1 * "
                          f"non_opposite_side_2) = {self.sides[other_sides[opposite][0]]['value']} **2"
                          f"+ {self.sides[other_sides[opposite][1]]['value']} **2 - "
                          f"{self.sides[opposite]['value']} ^ 2) / (2 * "
                          f"{self.sides[other_sides[opposite][0]]['value']} * "
                          f"{self.sides[other_sides[opposite][1]]['value']})\n={cosine}")
        else:
            """ For right triangles """
            hypotenuse = None
            for side_name, side_properties in self.sides.items():
                if side_properties["is_hypotenuse"] == True:
                    hypotenuse = side_name

            for angle_name, angle_properties in self.angles.items():
                if angle_properties["value"] is not None and angle_properties["cosine"] is None:
                    self.angles[angle_name]["cosine"] = math.cos(math.radians(angle_properties["value"]))
                    print("\n------------------------------------------------------------------------------")
                    print(f"Deriving cosine directly from angle: Cos ({angle_name}) = cos({angle_properties['value']})"
                          f"= {self.angles[angle_name]['cosine']}")

                if angle_properties["cosine"] is None:
                    if hypotenuse is not None:
                        if angle_properties["adjacent"] is not None:
                            self.angles[angle_name]["cosine"] = (self.sides[angle_properties["adjacent"]]["value"] /
                                                                 self.sides[hypotenuse]["value"])
                            print("\n------------------------------------------------------------------------------")
                            print(f"It's a right triangle. Cosine({angle_name}) = adjacent ({angle_properties['adjacent']}) /"
                                  f"hypothenuse ({hypotenuse}) = {self.sides[angle_properties['adjacent']]['value']} /"
                                  f"{self.sides[hypotenuse]['value']} = \n{self.angles[angle_name]['cosine']}")
                        else:
                            if self.angles[angle_name]["sine"] is not None:
                                self.angles[angle_name]["cosine"] = math.sqrt(1 - self.angles[angle_name]["sine"] ** 2)
                                print("\n------------------------------------------------------------------------------")
                                print(f"It's a right triangle. Cosine({angle_name}) = sqrt(1 - sin({angle_name})^2 = "
                                    f"sqrt(1 - {self.angles[angle_name]['sine']}^2 = {self.angles[angle_name]['cosine']}")

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
            if hypotenuse_value is None and len(catheti_values) == 2:
                if catheti_values[0] is not None and catheti_values[1] is not None:
                    hypotenuse_value = math.sqrt(catheti_values[0] ** 2 + catheti_values[1] ** 2)
                    self.sides[hypotenuse_name]["value"] = hypotenuse_value
                    print("\n------------------------------------------------------------------------------")
                    print(f"Pytagora's for right triangle. hypotenuse = sqrt({catheti_values[0]}^2 + {catheti_values[1]}^2)")

            if hypotenuse_value is not None and len(catheti_values) == 2:
                if catheti_values[1] is not None and len(catheti_values) == 2:
                    self.sides[catheti_names[0]]["value"] = math.sqrt(hypotenuse_value ** 2 - catheti_values[1] ** 2)
                    print("\n------------------------------------------------------------------------------")
                    print(f"Pytagora's. catethi_1 ({catheti_names[0]})= sqrt({hypotenuse_value}^2 - {catheti_values[1]}^2) = "
                          f"{self.sides[catheti_names[0]]['value']}")
                elif catheti_values[0] is not None:
                    self.sides[catheti_names[1]]["value"] = math.sqrt(hypotenuse_value ** 2 - catheti_values[0] ** 2)
                    print("\n------------------------------------------------------------------------------")
                    print(f"Pytagora's. catethi_2 ({catheti_names[1]})= sqrt({hypotenuse_value}^2 - {catheti_values[0]}^2) = "
                          f"{self.sides[catheti_names[1]]['value']}")
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
                        print("\n------------------------------------------------------------------------------")
                        print(f"Applying Pytagora's extended theorem: opposite side of {angle_name} = "
                              f"sqrt(known_side_1 ** 2 + known_side_2 ** 2 - (2 * known_side_1 * known_side_2 * cosine))"
                              f"\n= sqrt({known_side_1} **2 + {known_side_2}**2) - (2 * {known_side_1} * "
                              f"{known_side_2} * {cosine})\n = {self.sides[opposite]['value']}")

        return self.sides

    def get_sines(self):
        is_right_triangle = False

        """ If the angle is available, get sin directly from angle """
        for angle_name, angle_properties in self.angles.items():
            if self.angles[angle_name]["sine"] is None:
                if angle_properties["value"] is not None:
                    angle_value = angle_properties["value"]
                    if angle_properties["unit"] == "deg":
                        angle_value = math.radians(angle_properties["value"])
                    sine = math.sin(angle_value)
                    print("\n------------------------------------------------------------------------------")
                    print(f"Getting sine directly from anlge: sin({angle_name}: {angle_value}) = {sine}")
                    self.angles[angle_name]["sine"] = sine
                if ((angle_properties["unit"] == "deg" and angle_properties["value"] == 90) or
                        (angle_properties["unit"] == "rad") and (angle_properties["value"] == math.pi / 2)):
                    is_right_triangle = True

        """ If sin not available and it's a right triangle: """
        if is_right_triangle:
            for angle_name, angle_properties in self.angles.items():
                if self.angles[angle_name]["sine"] is None:
                    opposite = angle_properties["opposite"]
                    hypotenuse = angle_properties["hypotenuse"]
                    if (hypotenuse is not None and self.sides[opposite]["value"] is not None
                            and self.sides[hypotenuse]["value"] is not None):
                        sine = self.sides[opposite]["value"] / self.sides[hypotenuse]["value"]
                        print("\n------------------------------------------------------------------------------")
                        print(f"It's a right triangle. So sine of {angle_name} = opposite "
                              f"({self.sides[opposite]['value']}) / hypothenuse: {self.sides[hypotenuse]['value']} \n"
                              f"= {sine}")
                        self.angles[angle_name]["sine"] = sine
                    else:
                        if self.angles[angle_name]["cosine"] is not None:
                            sine = math.sqrt(1 - (self.angles[angle_name]["cosine"] ** 2))
                            print("\n------------------------------------------------------------------------------")
                            print(f"It's a right triangle. Sine of {angle_name} = sqrt( sin^-1(1 - cos{angle_name}^2)): "
                                  f"sqrt( 1 - {self.angles[angle_name]['cosine']} ^2 )) "
                                  f"= {sine}")
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

                            print("\n------------------------------------------------------------------------------")
                            print(f"Applying sine rule. Sine ({other_angle}) = sine ({angle_name} * "
                                  f"value ({self.angles[other_angle]['opposite']}) / "
                                  f"value ({angle_properties['opposite']})"
                                  f"= {sine} * {self.sides[self.angles[other_angle]['opposite']]['value']} / "
                                  f"{self.sides[angle_properties['opposite']]['value']}\n="
                                  f"{self.angles[other_angle]['sine']}")
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
            print("\n------------------------------------------------------------------------------")
            print(f"Deriving missing angle from 2 known angles: {present_angles[0]} and {present_angles[1]}\n"
                  f"missing_angle = {self.angles[missing_angle]['value']}")
            print("\n------------------------------------------------------------------------------")

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
