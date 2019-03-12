# Space Hopper

A problem I read somewhere on the internet, I can't recall the source

## Problem

You are jumping on a space hopper at a great speed along a linear runway. Noticing you are reaching the end of the runway, you would like to come to a gradual stop. However, there are spikes placed along the ground at 1m intervals you must avoid, lest you pop your space hopper.

You are travelling in m/s, and with each hop you can either keep your current speed or slow/accelerate by 1 m/s. Knowing your starting position and speed, are you able to come to complete stop (0 m/s) on the runway without landing on a spike? If so, after how far?

Your answer should be given as your position on the runway (your distance from the start of the runway in metres). If you are unable to stop as required above, your answer should be -1.

## Solution

An initial naive solution would involves a recursive function that observes your current speed and position on the runway, and then determines if you are able to stop safely by changing your speed (-1/+0/+1) in the current jump, then recursively checking if you can stop from the position and speed you move to.

We can improve this solution to be iterative though. As long as we remember the possible speeds we can have at safe positions, from our starting position we can determine all the positions we can jump to in the next step by adjusting our speed. Going from the start position and checking each subsequent position for a speed of 1 (we can stop at this position, it is a safe position).
