// implementation for the day05 quiz of "advent of code" 

#include <stdio.h>
#include <math.h>
#include <stdlib.h>

void part1();
void part2();
void check();

int main (int argc, char** argv)
{
    // check();
    part1();
    return 0;
}

void part1()
{
    int* seats = (int *)malloc(1024*sizeof(int));
    int mul = 1;
    int max = -1;
    char c = '1';
    while(c != EOF)
    {
        int id = 0;
        int pos = 7;
        int row = 0, col = 0;
        while (pos > 0) // read rows first
        {
            c = getchar_unlocked();
            id = id << 1;
            if (c == 'B')
                id += 1;
            pos--;
        }
        pos = 3;
        while (pos > 0) // read columns
        {
            c = getchar_unlocked();
            id = id << 1;
            if (c == 'R')
                id += 1;
            pos--;
        }
        c = getchar_unlocked(); // skip \n
        // mul = row*8 + col;
        max = ((id > max)?(id):(max));
        seats[id] = 1;
    }
    printf("Part 1: %d\n", max);
    int myseat;
    for (int i=1; i<1023; i+=2)
    {
        if (seats[i-1] - seats[i] != 0)
            myseat = i;
            // printf("%d\n", i);
    }
    printf("Part 2: %d\n", myseat);
    free(seats);
}

void check()
{
    int i = 1;
    for (int k=0; k<10; ++k)
    {
        i = i << 1;
        // i+=1;
        printf("%d\n", i);
    }
}