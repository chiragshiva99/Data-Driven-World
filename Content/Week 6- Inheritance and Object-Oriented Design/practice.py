class Fraction:
    def __init__(self, num, den):
        self._num = 0
        self._den = 1

        # set the attributes according to user input
        self.num = num
        self.den = den

    @property
    def num(self):
        return self._num

    @num.setter
    def num(self, val):
        if isinstance(val, int):
            self._num = val
        # self._num = int(val)

    @property
    def den(self):
        return self._den

    @den.setter
    def den(self, val):
        if isinstance(val, int):
            if val == 0:
                self._den = 1
            else:
                self._den = val
        # if (int(val) == 0):
        #     self._den = 1
        # else:
        #     self._den = int(val)

    def __str__(self):
        return f"{self.num:d}/{self.den:d}"


f0 = Fraction(0, 1)
assert f0.num == 0
assert f0.den == 1
assert str(f0) == "0/1"

f1 = Fraction(1, 2)
assert f1.num == 1
assert f1.den == 2
assert str(f1) == "1/2"

f1.num = 3
f1.den = 4
assert str(f1) == "3/4"