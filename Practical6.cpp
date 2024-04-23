#include <iostream>

int main() {
    int i;
    printf("Enter the number: ");
    scanf("%d", &i);
    if (i % 2 == 0) {
        printf("The number is divisible by 2\n");
    } else {
        printf("The number is not divisible by 2\n");
    }
    return 0;
}
