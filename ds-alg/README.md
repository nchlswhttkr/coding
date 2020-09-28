# ds-alg

### Linear-feedback Shift Register

Linear-feedback shift registers can generate a sequences of numbers that is _pseudorandom_ but _deterministic_. With the right arrangement, a register of N bits can produce a sequence of 2<sup>N</sup>-1 before it cycles.

The implementation in [`linear-feedback-shift-register/lfsr.c`](./ds-alg/linear-feedback-shift-register/lfsr.c) can produce sequences of up to length 2<sup>20</sup>, using an arrangement of taps for a maximal LFSR.

```sh
cd ds-alg/linear-feedback-shift-register
make
./lfsr 5
# 4
# 2
# 5
# 3
# 1
make test -s
```

Further reading:

- [Linear-feedback shift register](https://en.wikipedia.org/wiki/Linear-feedback_shift_register)
- [Wolfenstein 3D's fizzlefade algorithm](https://fabiensanglard.net/fizzlefade/index.php)
