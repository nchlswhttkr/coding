from random import randint
from time import sleep


def can_stop(spikes, position, speed):
    # Must stay on the runway and not land on a spike
    if position >= len(spikes) or spikes[position]:
        return -1

    # Able to stop safely
    elif speed == 0:
        return position

    # Determine whether adjusting speed can allow us to stop
    else:
        for adjusted_speed in range(speed - 1, speed + 2):
            stopping_position = can_stop(
                spikes, position + adjusted_speed, adjusted_speed)
            if stopping_position >= 0:
                return stopping_position

    return -1


def can_stop_revised(spikes, start_position, initial_speed):
    # We can't start on a spike
    if spikes[start_position]:
        return -1

    # By knowing the achievable speeds we can have at any position, as well as
    # how far we can travel, we only deal with valid speeds/positions
    position = start_position
    speeds = [{} for _ in range(len(spikes))]
    speeds[position][initial_speed] = True
    furthest_position = position  # furthest we can go

    # Knowing the furthest we can travel (hypthotically/end of runway)
    while position < min(furthest_position + 1, len(spikes)):
        for current_speed in speeds[position].keys():

            # We can stop on any flat ground once slow enough
            if current_speed == 1 and not spikes[position]:
                return position

            # Note down the possible speeds/positions that we can reach by
            # adjusting, remember them if they do not correspond to a spike
            for adjusted_speed in range(current_speed - 1, current_speed + 2):
                next_position = position + adjusted_speed
                if next_position < len(spikes) and not spikes[next_position]:
                    speeds[next_position][adjusted_speed] = True
                    furthest_position = max(furthest_position, next_position)

        position += 1

    return -1


def main():
    SPIKE_CHANCE = 40  # out of 100%
    RUNWAY_LENGTH = 1000
    POSITION = randint(0, RUNWAY_LENGTH - 200)
    SPEED = randint(10, 30)

    spikes = [SPIKE_CHANCE >= randint(1, 100) for _ in range(RUNWAY_LENGTH)]
    stopping_position = can_stop_revised(spikes, POSITION, SPEED)
    if stopping_position >= 0:
        print('Can stop, ends at {}'.format(stopping_position))
    else:
        print('Could not stop')


if __name__ == '__main__':
    main()
