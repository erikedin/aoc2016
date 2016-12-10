import collections
import re

class Room:
    def __init__(self, name, sector_id):
        self.name = name
        self.sector_id = sector_id
        self.checksum = self.calculate_checksum()

    def calculate_letter_frequencies(self):
        name = filter(lambda x: x != '-', self.name)
        return dict(collections.Counter(name))

    def calculate_checksum(self):
        freqs = self.calculate_letter_frequencies()
        ordering = RoomChecksumOrdering(freqs)
        def comp(x, y):
            if x == y: return 0
            return -1 if ordering.less_than(x, y) else 1
        checksum_letters = sorted(freqs.keys(), cmp=comp)
        return ''.join(checksum_letters[:5])
    
    def decrypt_name(self):
        return ''.join([decrypt_char(x, self.sector_id) for x in self.name])

class RoomWithChecksum:
    def __init__(self, room, checksum):
        self.room = room
        self.checksum = checksum
    
    def is_real(self):
        return self.room.checksum == self.checksum

class RoomChecksumOrdering:
    def __init__(self, freqs):
        self.freqs = freqs
    
    def less_than(self, l1, l2):
        if self.freqs.get(l1, 0) == self.freqs.get(l2, 0):
            return l1 < l2
        
        return self.freqs.get(l1, 0) > self.freqs.get(l2, 0)

def make_room(room_with_sector_id):
    m = re.match("([a-z\-]+)-([0-9]+)", room_with_sector_id)
    if not m:
        raise ValueError()
    name = m.group(1)
    sector_id = int(m.group(2))
    return Room(name, sector_id)

def sum_sector_ids(rooms):
    return sum([r.sector_id for r in rooms])

def sector_id_sum_of_real_rooms(room_with_checksums):
    real_rooms = [x.room for x in filter(lambda x: x.is_real(), room_with_checksums)]
    return sum_sector_ids(real_rooms)

def make_rooms_and_checksums(lines):
    r = re.compile("([a-z0-9\-]+)\[([a-z]+)\]")
    matches = [r.search(x) for x in lines]
    return [RoomWithChecksum(make_room(m.group(1)), m.group(2)) for m in matches]

def decrypt_char(c, sector_id):
    if c == "-": return " "
    ordinal = ord(c)
    shift = sector_id % 26
    if shift + ordinal > ord('z'):
        shift -= 26
    return chr(ordinal + shift)