#!/usr/bin/env python3


class Matrix:
    """ Matrix """
    __data: dict

    def __init__(self, *elems, rows=1) -> None:

        # test split elems

        self.__data = {}

        if len(elems) % rows != 0:
            raise ValueError("Can't split len(elems) / rows")

        columns = len(elems) // rows

        if len(elems) > 0:
            self.__data["size"] = (rows, columns)

        for column in range(rows):
            for row in range(columns):
                self.__data[(row, column)] = elems[column + row * rows]

    def get_size(self) -> tuple:
        """ return size of matrix (rows, columns) """
        return self.__data.get("size", (0, 0))

    def get_elem(self, row_index, column_index):
        """ return elems of pos(row, column) """

        value = self.__data[(row_index, column_index)]

        if value is not None:
            return value

        raise ValueError(f"Unknow index {(row_index, column_index)}")

    def __arifm_func(self, func, other: 'Matrix') -> list:

        (rows, columns) = self.get_size()

        return [func(self.get_elem(x, y),  other.get_elem(x, y))
                for y in range(rows) for x in range(columns)]

    def __add__(self, other: 'Matrix') -> 'Matrix':
        """ operator + for matrix. return a new matrix """
        if self.get_size() != other.get_size():
            raise ValueError("Matrix's sizies must be eq")

        return Matrix(self.__arifm_func(lambda x, y: x + y, other), rows=self.get_size()[0])

    def __sub__(self, other: 'Matrix') -> 'Matrix':
        """ operator - for matrix. return a new matrix """

        if self.get_size() != other.get_size():
            raise ValueError("Matrix's sizies must be eq")

        return Matrix(self.__arifm_func(lambda x, y: x - y, other), rows=self.get_size()[0])

    def __str__(self) -> str:

        (rows, columns) = self.get_size()

        if rows * columns == 0:
            return "Empty Matrix"

        output = ""
        for j, row in enumerate(range(rows)):

            for i, column in enumerate(range(columns)):
                output += f"{self.get_elem(column, row)}"

                if i != columns - 1:
                    output += " "

            if j != rows - 1:
                output += "\n"

        return output