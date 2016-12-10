import hashlib

class DoorBreaker:
    def __init__(self, door_id):
        self.door_id = door_id
        self.hash_condition = None
        self.password_char = None
        self.length = None
        self.hash_function = None
        self.current_index = 0
        self.current_hash = 0

    def set_length(self, length):
        self.length = 8

    def hash(self):
        s = self.door_id + str(self.current_index)
        return self.hash_function.hash(s)

    def find_next_valid_index(self):
        while True:
            self.current_hash = self.hash()
            if self.hash_condition(self.current_hash):
                break
            self.current_index += 1

    def find_password(self):
        password = ""
        for i in xrange(0, self.length):
            self.find_next_valid_index()
            c = self.password_char.get_char(self.current_hash)
            self.current_index += 1
            password += c
        return password

def five_zeroes_condition(hash):
    return hash.hex()[:5] == "00000"

class PasswordCharIndex:
    def __init__(self, index):
        self.index = index
    
    def get_char(self, hash):
        return hash.hex()[self.index - 1]

class MD5:
    def hash(self, s):
        m = hashlib.md5()
        m.update(s)
        return MD5HashResult(m.hexdigest())

class MD5HashResult:
    def __init__(self, h):
        self.h = h
    
    def hex(self):
        return self.h
