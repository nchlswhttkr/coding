import sys


highest_id = 0
for seat in sys.stdin.readlines():
    seat_id = int(seat.translate(str.maketrans('BFRL', '1010')), base=2)
    highest_id = max(highest_id, seat_id)
print(highest_id)
