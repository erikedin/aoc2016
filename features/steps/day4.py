from behave import *
import aoc2016.rooms as rooms
import aoc2016.day4 as day4
import json

@given(u'a room {name_with_sector}')
def step_impl(context, name_with_sector):
    context.room = rooms.make_room(name_with_sector)

@then(u'the sector id is {sector_id:d}')
def step_impl(context, sector_id):
    assert context.room.sector_id == sector_id

@then(u'the checksum is {checksum}')
def step_impl(context, checksum):
    assert context.room.checksum == checksum, "Expected {}, but got {}".format(checksum, context.room.checksum)

@given(u'the rooms')
def step_impl(context):
    context.rooms = [rooms.make_room(r[0]) for r in context.table]

@when(u'I sum the sector ids')
def step_impl(context):
    context.sector_id_sum = rooms.sum_sector_ids(context.rooms)

@then(u'I should get the sector id sum {sector_id_sum:d}')
def step_impl(context, sector_id_sum):
    assert context.sector_id_sum == sector_id_sum

@when(u'I calculate the letter frequencies')
def step_impl(context):
    context.frequencies = context.room.calculate_letter_frequencies()

@then(u'I should get the frequencies')
def step_impl(context):
    expected_freqs = json.loads(context.text)
    assert context.frequencies == expected_freqs

@given(u'letters {l1} and {l2}, with respective frequencies {f1} and {f2}')
def step_impl(context, l1, l2, f1, f2):
    context.freqs = {l1: f1, l2: f2}
    context.l1 = l1
    context.l2 = l2

@when(u'I order them by frequency first and lexical order second')
def step_impl(context):
    ordering = rooms.RoomChecksumOrdering(context.freqs)
    context.first = context.l1 if ordering.less_than(context.l1, context.l2) else context.l2

@then(u'the first in order should be {first}')
def step_impl(context, first):
    assert context.first == first, "Expected {} to be first, got {}".format(first, context.first)

@when(u'I check if it is a real room')
def step_impl(context):
    context.real_or_decoy = "real" if context.room_with_checksum.is_real() else "decoy"

@then(u'I find that it is {real_or_decoy}')
def step_impl(context, real_or_decoy):
    assert context.real_or_decoy == real_or_decoy

@given(u'a checksum and room {room_with_sector} and {checksum}')
def step_impl(context, room_with_sector, checksum):
    room = rooms.make_room(room_with_sector)
    context.room_with_checksum = rooms.RoomWithChecksum(room, checksum)

@when(u'I calculate the sum of sector ids of the real rooms')
def step_impl(context):
    context.sector_id_sum = rooms.sector_id_sum_of_real_rooms(context.rooms_and_checksums)

@given(u'the rooms and checksums')
def step_impl(context):
    lines = context.text.split('\n')
    context.rooms_and_checksums = rooms.make_rooms_and_checksums(lines)

@when(u'I decrypt the name')
def step_impl(context):
    context.name = context.room.decrypt_name()

@then(u'the name should be "{name}"')
def step_impl(context, name):
    assert context.name == name, "Expected {} but got {}".format(name, context.name)

@given(u'a character {cipher_char} and a sector id {sector_id:d}')
def step_impl(context, cipher_char, sector_id):
    context.cipher_char = cipher_char
    context.sector_id = sector_id

@when(u'I decrypt the character')
def step_impl(context):
    context.decrypted_char = rooms.decrypt_char(context.cipher_char, context.sector_id)

@then(u'I should get the decrypted character "{decrypted_char}"')
def step_impl(context, decrypted_char):
    assert context.decrypted_char == decrypted_char, "Expected {}, but got {}".format(decrypted_char, context.decrypted_char)
