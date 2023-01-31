'''
Use __new__ when you need to control the creation of a new instance. Use __init__ when you need to control initialization of a new instance.

__new__ is the first step of instance creation. It's called first, and is responsible for returning a new instance of your class. 
In contrast, __init__ doesn't return anything; it's only responsible for initializing the instance after it's been created.

In general, you shouldn't need to override __new__ unless you're subclassing an immutable type like str, int, unicode or tuple.
Interning should only be used for immutable value types
'''
class ChessCoordinate:

    _interned = {}

    def __new__(cls, file, rank):

        if len(file) != 1:
            raise ValueError("{} component file {!r} does not have a length of one."
                             .format(cls.__name__, file))

        if file not in 'abcdefgh':
            raise ValueError("{} component file {!r} is out of range."
                             .format(cls.__name__, file))

        if rank not in range(1, 9):
            raise ValueError("{} component rank {!r} is out of range."
                             .format(cls.__name__, rank))

        key = (file, rank)
        if key not in cls._interned:
            obj = super().__new__(cls)
            obj._file = file
            obj._rank = rank
            cls._interned[key] = obj

        return cls._interned[key]


    @property
    def file(self):
        return self._file

    @property
    def rank(self):
        return self._rank

    def __repr__(self):
        return "{}(file={}, rank={})".format(self.__class__.__name__, self.file, self.rank)

    def __str__(self):
        return '{}{}'.format(self.file, self.rank)


def starting_board():
    return {'♕♖': ChessCoordinate('a', 1),
            '♕♘': ChessCoordinate('b', 1),
            '♕♗': ChessCoordinate('c', 1),
            '♕♕': ChessCoordinate('d', 1),
            '♔♔': ChessCoordinate('e', 1),
            '♔♗': ChessCoordinate('f', 1),
            '♔♘': ChessCoordinate('g', 1),
            '♔♖': ChessCoordinate('h', 1),
            '♕♖♙': ChessCoordinate('a', 2),
            '♕♘♙': ChessCoordinate('b', 2),
            '♕♗♙': ChessCoordinate('c', 2),
            '♕♕♙': ChessCoordinate('d', 2),
            '♔♔♙': ChessCoordinate('e', 2),
            '♔♗♙': ChessCoordinate('f', 2),
            '♔♘♙': ChessCoordinate('g', 2),
            '♔♖♙': ChessCoordinate('h', 2),
            '♛♜': ChessCoordinate('a', 8),
            '♛♞': ChessCoordinate('b', 8),
            '♛♝': ChessCoordinate('c', 8),
            '♛♛': ChessCoordinate('d', 8),
            '♚♚': ChessCoordinate('e', 8),
            '♚♝': ChessCoordinate('f', 8),
            '♚♞': ChessCoordinate('g', 8),
            '♚♜': ChessCoordinate('h', 8),
            '♛♜♟': ChessCoordinate('a', 7),
            '♛♞♟': ChessCoordinate('b', 7),
            '♛♝♟': ChessCoordinate('c', 7),
            '♛♛♟': ChessCoordinate('d', 7),
            '♚♚♟': ChessCoordinate('e', 7),
            '♚♝♟': ChessCoordinate('f', 7),
            '♚♞♟': ChessCoordinate('g', 7),
            '♚♜♟': ChessCoordinate('h', 7),
        }


def main():
    boards = [starting_board() for _ in range(10000)]
    pass


if __name__ == '__main__':
    main()