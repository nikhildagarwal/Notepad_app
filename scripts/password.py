import random


class Password:

    def __init__(self, input_var):
        self.output = None
        self.input = input_var

    def encrypt(self):
        out = ""
        for char in self.input:
            coeff = 1 / 300
            const = 32
            power = ord(char) ** 2.1
            val = (coeff*power) + const
            rounded_val = round(val)
            signal = 0
            if rounded_val < val:
                signal = 125
            elif rounded_val > val:
                signal = 126
            else:
                signal = 124
            out += chr(rounded_val) + chr(signal)
        uu.output = out


uu = Password("abc")
uu.encrypt()
print(uu.output)
