#!/usr/bin/env python3

class Cell:
    __cells: int

    def __init__(self, cells: int) -> None:
        self.__cells = cells

    def __add__(self, other: 'Cell'):
        return Cell(self._get_size() + other._get_size())

    def __sub__(self, other: 'Cell'):
        if self._get_size() < other._get_size():
            raise ValueError("cells can't be < 0")

        return Cell(self._get_size() - other._get_size())

    def __mul__(self, other: 'Cell'):
        return Cell(self._get_size() * other._get_size())

    def __floordiv__(self, other: 'Cell'):
        return Cell(self._get_size() // other._get_size())

    def _get_cells(self) -> str:
        return str(self).replace("Cell(", "").replace(")", "")

    def _get_size(self) -> int:
        return self._get_cells().count("*")

    def __str__(self) -> str:
        return f"Cell({'*'*self.__cells})"

    def make_order(self, split_cell) -> str:
        """ ordering cells to cube the size eq split_cell*split_cell """

        if split_cell == 0:
            raise ValueError("can't split cells by 0")

        if split_cell >= self._get_size():
            return self._get_cells()

        size = self._get_size()

        return "".join([f"{x}\n" if i % split_cell == 0 and i != size  else x
                        for i, x in enumerate(self._get_cells(), start=1)])