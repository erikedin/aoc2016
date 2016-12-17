import re

class IP(object):
    def __init__(self):
        self.normals = []
        self.hypernets = []
    
    def add_hypernet(self, h):
        self.hypernets.append(h)
    
    def add(self, a):
        self.normals.append(a)

def parse_address(address):
    hypernet_pattern = "\[[a-z]*\]"
    addr_pattern = "[a-z]+"
    pattern = "([a-z]+|[a-z\[]+\])".format(addr_pattern, hypernet_pattern)
    parts = re.findall(pattern, address)
    ip = IP()
    for p in parts:
        if '[' == p[0]:
            ip.add_hypernet(p[1:-1])
        else:
            ip.add(p)
    return ip

def parse(lines):
    return [parse_address(x.strip()) for x in lines]

def starts_with_abba(s):
    if s[0] == s[1]: return False
    return s[0] == s[3] and s[1] == s[2]

def has_abba(s):
    """
    >>> has_abba('abba')
    True
    >>> has_abba('mnop')
    False
    >>> has_abba('aaa')
    False
    """
    for i in xrange(0, len(s) - 3):
        sub = s[i:]
        if starts_with_abba(sub): return True
    return False

def starts_with_aba(s):
    if s[0] == s[1]: return False
    return s[0] == s[2]    

def find_abas_in(s):
    result = []
    for i in xrange(0, len(s) - 2):
        sub = s[i:]
        if starts_with_aba(sub): result.append(s[i:i+3])
    return result
    
def find_abas(normals):
    r = []
    for x in normals:
        r.extend(find_abas_in(x))
    return r

def supports_abba(ip):
    n = [has_abba(x) for x in ip.normals]
    h = [has_abba(x) for x in ip.hypernets]
    return any(n) and not any(h)

def invert_aba(x):
    return ''.join([x[1], x[0], x[1]])

def supports_ssl(ip):
    abas = find_abas(ip.normals)
    for x in abas:
        for h in ip.hypernets:
            if invert_aba(x) in h: return True
    return False
    

def step1(input):
    return len(filter(supports_abba, input))

def step2(input):
    return len(filter(supports_ssl, input))

