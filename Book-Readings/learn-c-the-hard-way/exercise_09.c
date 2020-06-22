#include <stdio.h>

int main(int argc, char *argv[])
{
    int i = 0;
    while (i < 20) {
        printf("%d\n", i);
        i++;
    }

    // add newline
    printf("\n");

    while (i > 0) {
        printf("%d\n", i);
        i--;
    }

    return 0;
}
