import random
import secrets
import string


mappings = {1: '{', 2: '}', 3: '|', 4: '~'}
mappings_set = {'{','}','|','~'}


def generate_random_string(length=10):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(secrets.choice(characters) for i in range(length))
    return random_string


class MyCrypt:

    def __init__(self, input_var, param):
        self.output = None
        self.input = input_var
        self.param = param
        while len(self.param) < len(self.input):
            self.param += self.param

    def encrypt(self):
        out = ""
        i = 0
        for char in self.input:
            avg = (ord(char) + ord(self.param[i])) / 2
            if (avg - round(avg)) != 0:
                r = random.randint(1, 4)
                random_char = mappings.get(r)
                out += (random_char + chr(int(avg+0.5)))
            else:
                out += chr(round(avg))
            i += 1
        self.output = out

    def decrypt(self):
        out = ""
        i = 0
        j = 0
        input_length = len(self.input)
        while i < input_length:
            curr = self.input[i]
            if curr in mappings_set:
                i += 1
                new_curr = self.input[i]
                x = ((ord(new_curr) - 0.5) * 2) - ord(self.param[j])
                out += chr(int(x))
            else:
                x = (ord(curr) * 2) - ord(self.param[j])
                out += chr(x)
            j += 1
            i += 1
        self.output = out


