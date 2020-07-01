#include <stdio.h>

int main(int argc, char *argv[])
{
    // create two arays we care about
    int ages[] = { 23, 43, 12, 89, 2 };
    char *names[] = {
        "Alan", "Frank",
        "Mary", "John", "Lisa"
    };

    // safely get the size of ages
    int count = sizeof(ages) / sizeof(int);
    int i = 0;

    //first way using indexing
    for(i = count - 1; i >= 0; i--) {
        printf("%s has %d years alive.\n", names[i], ages[i]);
    }

    printf("---\n");

    // setup the pointers to the start of the arrays
    // Or the end!
    int *cur_age = &ages[count - 1];
    char **cur_name = &names[count - 1];

    // second way using pointers
    for(i = 0; i < count; i++) {
        printf("%s is %d years old.\n",
                *(cur_name - i), *(cur_age - i));
    }

    printf("---\n");

    // third way, pointers are just arrays
    for(i = 0; i > -count; i--) {
        printf("%s is %d years old again.\n", *(cur_name + i), *(cur_age + i));
    }

    printf("---\n");

    // fourth way with pointers in a complex way
    for(cur_name = &names[count - 1], cur_age = &ages[count - 1];
            (cur_age - ages) >= 0; cur_name--, cur_age--) {
        printf("%s lived %d years so far.\n", *cur_name, *cur_age);
    }

    printf("---\n");

    //extra credit: print the addresses
    for(i = 0; i < count; i++) {
        printf("%s lives at %p.\n", *(cur_name + i + 1), &names[i]);
    }

    return 0;
}
