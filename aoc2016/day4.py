import aoc2016.rooms as rooms

def parse(lines): return lines

def step1(input):
    rooms_and_checksums = rooms.make_rooms_and_checksums(input)
    return rooms.sector_id_sum_of_real_rooms(rooms_and_checksums)

def step2(input):
    rooms_and_checksums = rooms.make_rooms_and_checksums(input)
    north_pole_object_storage = filter(lambda x: x.room.decrypt_name() == "northpole object storage", rooms_and_checksums)
    return north_pole_object_storage[0].room.sector_id