from collections import Counter

def parse(lines): 
    return [x.strip() for x in lines]

def step1(input):
    """
    >>> step1([   \
        "eedadn", \
        "drvtee", \
        "eandsr", \
        "raavrd", \
        "atevrs", \
        "tsrnev", \
        "sdttsa", \
        "rasrtv", \
        "nssdts", \
        "ntnada", \
        "svetve", \
        "tesnvt", \
        "vntsnd", \
        "vrdear", \
        "dvrsen", \
        "enarar"  \
        ])
    'easter'
    """
    zipped = zip(*input)
    counted = [Counter(x) for x in zipped]
    message = [c.most_common(1)[0][0] for c in counted]
    return ''.join(message)

def step2(input):
    """
    >>> step2([   \
        "eedadn", \
        "drvtee", \
        "eandsr", \
        "raavrd", \
        "atevrs", \
        "tsrnev", \
        "sdttsa", \
        "rasrtv", \
        "nssdts", \
        "ntnada", \
        "svetve", \
        "tesnvt", \
        "vntsnd", \
        "vrdear", \
        "dvrsen", \
        "enarar"  \
        ])
    'advent'
    """
    zipped = zip(*input)
    counted = [Counter(x) for x in zipped]
    message = [c.most_common()[-1][0] for c in counted]
    return ''.join(message)    