#!/usr/bin/python3
""" testing comments """
import json
import csv
import turtle
import random


class Base:
    """ coments of class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ class to create a rectangle object """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        class to create a rectangle object
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        class to create a rectangle object
        """
        ventana = turtle.Screen()
        lapiz = turtle.Turtle()

        lapiz.pensize(2)

        for info in list_rectangles:
            R = random.random()
            B = random.random()
            G = random.random()
            lapiz.color(R, G, B)
            print(info.x)
            lapiz.up()
            lapiz.setx(info.x)
            lapiz.sety(info.y)
            lapiz.down()
            lapiz.begin_fill()
            for i in range(2):
                lapiz.forward(info.width)
                lapiz.right(90)
                lapiz.forward(info.height)
                lapiz.right(90)
            lapiz.end_fill()

        for info in list_squares:
            R = random.random()
            B = random.random()
            G = random.random()
            lapiz.color(R, G, B)
            print(info.x)
            lapiz.up()
            lapiz.setx(info.x)
            lapiz.sety(info.y)
            lapiz.down()
            lapiz.begin_fill()
            for i in range(2):
                lapiz.forward(info.width)
                lapiz.right(90)
                lapiz.forward(info.height)
                lapiz.right(90)
            lapiz.end_fill()
        ventana.exitonclick()
        """
        t = turtle.Turtle()
        t.forward(100)
        turtle.done()
        """

    @staticmethod
    def from_json_string(json_string):
        """
        class to create a rectangle object
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        class to create a rectangle object
        """
        listm = []
        if list_objs is not None:
            for info in list_objs:
                listm.append(info.to_dictionary())

        filename = "{}.json".format(cls.__name__)
        with open(filename, "w") as write_file:
            write_file.write(cls.to_json_string(listm))

    @classmethod
    def create(cls, **dictionary):
        """
        class to create a rectangle object
        """
        if cls.__name__ == "Rectangle":
            text = cls(1, 1)
        elif cls.__name__ == "Square":
            text = cls(1)
        cls.update(text, **dictionary)
        return text

    @classmethod
    def load_from_file(cls):
        """
        class to create a rectangle object
        """
        listm = []
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, "r") as read_file:
                listm = cls.from_json_string(read_file.read())
            for i, j in enumerate(listm):
                listm[i] = cls.create(**listm[i])
        except:
            pass
        return listm

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        class to create a rectangle object
        """
        filename = "{}.csv".format(cls.__name__)
        if cls.__name__ == "Rectangle":
            text = ["width", "height", "x", "y", "id"]
        elif cls.__name__ == "Square":
            text = ["size", "x", "y", "id"]

        with open(filename, 'w') as csvFile:
            writer = csv.DictWriter(csvFile, fieldnames=text)
            if list_objs is not None:
                writer.writeheader()
                for text1 in list_objs:
                    writer.writerow(text1.to_dictionary())
            else:
                writer.writerow([[]])

    @classmethod
    def load_from_file_csv(cls):
        """
        class to create a rectangle object
        """
        filename = "{}.csv".format(cls.__name__)
        listm = []
        try:
            with open(filename, newline="") as csvFile:
                read = csv.DictReader(csvFile)
                for row in read:
                    for k, v in row.items():
                        row[k] = int(v)
                    listm.append(row)
            return [cls.create(**oj) for oj in listm]
        except FileNotFoundError:
            return [[]]
