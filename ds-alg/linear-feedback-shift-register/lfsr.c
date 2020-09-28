#include <stdio.h>
#include <math.h>
#include <stdlib.h>

void run_shift_register(int ceil, int cbits, int *taps, int ctaps)
{
    u_int32_t reg = 1;
    do
    {
        int bit = 0;
        for (int i = 0; i < ctaps; i++)
        {
            bit ^= (reg >> (cbits - taps[i])) % 2;
        }
        reg = (reg >> 1) + bit * pow(2, cbits - 1);
        if (reg <= ceil)
        {
            printf("%u\n", reg);
        }
    } while (reg > 1);
}

int main(int argc, char **argv)
{
    if (argc != 2)
    {
        fprintf(stderr, "Incorrect number of arguments\n");
        return 1;
    }

    u_int32_t *ceil = malloc(sizeof(u_int32_t));
    if (sscanf(argv[1], "%u", ceil) != 1)
    {
        fprintf(stderr, "Failed to get range limit\n");
        return 1;
    }

    int cbits = 3;
    while ((u_int32_t)pow(2, cbits) <= *ceil)
    {
        cbits++;
    }

    int ctaps;
    int *taps = NULL;
    switch (cbits)
    {
    case 3:
        ctaps = 2;
        taps = malloc(ctaps * sizeof(int));
        taps[0] = 3;
        taps[1] = 2;
        break;
    case 4:
        ctaps = 2;
        taps = malloc(ctaps * sizeof(int));
        taps[0] = 4;
        taps[1] = 3;
        break;
    case 5:
        ctaps = 2;
        taps = malloc(ctaps * sizeof(int));
        taps[0] = 5;
        taps[1] = 3;
        break;
    case 6:
        ctaps = 2;
        taps = malloc(ctaps * sizeof(int));
        taps[0] = 6;
        taps[1] = 5;
        break;
    case 7:
        ctaps = 2;
        taps = malloc(ctaps * sizeof(int));
        taps[0] = 7;
        taps[1] = 6;
        break;
    case 8:
        ctaps = 4;
        taps = malloc(ctaps * sizeof(int));
        taps[0] = 8;
        taps[1] = 6;
        taps[2] = 5;
        taps[3] = 4;
        break;
    case 9:
        ctaps = 2;
        taps = malloc(ctaps * sizeof(int));
        taps[0] = 9;
        taps[1] = 5;
        break;
    case 10:
        ctaps = 2;
        taps = malloc(ctaps * sizeof(int));
        taps[0] = 10;
        taps[1] = 7;
        break;
    case 11:
        ctaps = 2;
        taps = malloc(ctaps * sizeof(int));
        taps[0] = 11;
        taps[1] = 9;
        break;
    case 12:
        ctaps = 4;
        taps = malloc(ctaps * sizeof(int));
        taps[0] = 12;
        taps[1] = 6;
        taps[2] = 4;
        taps[3] = 1;
        break;
    case 13:
        ctaps = 4;
        taps = malloc(ctaps * sizeof(int));
        taps[0] = 13;
        taps[1] = 4;
        taps[2] = 3;
        taps[3] = 1;
        break;
    case 14:
        ctaps = 4;
        taps = malloc(ctaps * sizeof(int));
        taps[0] = 14;
        taps[1] = 5;
        taps[2] = 3;
        taps[3] = 1;
        break;
    case 15:
        ctaps = 2;
        taps = malloc(ctaps * sizeof(int));
        taps[0] = 15;
        taps[1] = 14;
        break;
    case 16:
        ctaps = 4;
        taps = malloc(ctaps * sizeof(int));
        taps[0] = 16;
        taps[1] = 15;
        taps[2] = 13;
        taps[3] = 4;
        break;
    case 17:
        ctaps = 2;
        taps = malloc(ctaps * sizeof(int));
        taps[0] = 17;
        taps[1] = 14;
        break;
    case 18:
        ctaps = 2;
        taps = malloc(ctaps * sizeof(int));
        taps[0] = 18;
        taps[1] = 11;
        break;
    case 19:
        ctaps = 4;
        taps = malloc(ctaps * sizeof(int));
        taps[0] = 19;
        taps[1] = 6;
        taps[2] = 2;
        taps[3] = 1;
        break;
    case 20:
        ctaps = 2;
        taps = malloc(ctaps * sizeof(int));
        taps[0] = 20;
        taps[1] = 17;
        break;
    default:
        fprintf(stderr, "Could not find taps for %d bits\n", cbits);
        return 1;
    }

    run_shift_register(*ceil, cbits, taps, ctaps);

    free(ceil);
    free(taps);

    return 0;
}
