import sys


highest_id = 0
seat_ids = set()
for seat in sys.stdin.readlines():
    seat_id = int(seat.translate(str.maketrans('BFRL', '1010')), base=2)
    highest_id = max(highest_id, seat_id)
    seat_ids.add(seat_id)
while highest_id in seat_ids:
    highest_id -= 1
print(highest_id)
