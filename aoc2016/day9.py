import re

def parse(lines):
    return ''.join([x.strip() for x in lines])

class Marker(object):
    def __init__(self, chars, repeats):
        self.chars = chars
        self.repeats = repeats
    
    @classmethod
    def parse(clazz, text):
        """
        >>> m, rest = Marker.parse('(10x2)abc')
        >>> m.chars
        10
        >>> m.repeats
        2
        >>> rest
        'abc'
        """
        pattern = r"\((\d+)x(\d+)\)"
        m = re.match(pattern, text)
        if not m:
            return None, text
        return Marker(int(m.group(1)), int(m.group(2))), text[len(m.group(0)):]

def take(s, n):
    return s[:n], s[n:]

def decompress(compressed):
    """
    >>> decompress('ADVENT')
    'ADVENT'
    >>> decompress('A(1x5)BC')
    'ABBBBBC'
    >>> decompress('(3x3)XYZ')
    'XYZXYZXYZ'
    """
    result = []
    while compressed:
        m, compressed = Marker.parse(compressed)
        if m is None:
            c, compressed = take(compressed, 1)
            result.append(c)
        else:
            s, compressed = take(compressed, m.chars)
            result.append(s * m.repeats)
    return ''.join(result)            

def decompressed_length2(compressed):
    """
    >>> decompress2('ADVENT')
    'ADVENT'
    >>> decompress2('X(8x2)(3x3)ABCY')
    'XABCABCABCABCABCABCY'
    """
    result = 0
    while compressed:
        m, compressed = Marker.parse(compressed)
        if m is None:
            c, compressed = take(compressed, 1)
            result += 1
        else:
            s, compressed = take(compressed, m.chars)
            d = decompressed_length2(s)
            result += d * m.repeats
    return result

def step1(input):
    return len(decompress(input))

def step2(input):
    return decompressed_length2(input)