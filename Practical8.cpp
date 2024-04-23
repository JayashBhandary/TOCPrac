#include <iostream>

int main() {
    int a[] = {1, 0, 0, 1, 0, 0, 1};
    int one = 0;
    int zero = 0;
    
    // Calculate the length of the array
    int length = sizeof(a) / sizeof(a[0]);

    for (int i = 0; i < length; i++) {
        if (a[i] == 1) {
            one++;
        } else if (a[i] == 0) {
            zero++;
        }
    }
    
    std::cout << "Number of 1's: " << one << std::endl;
    std::cout << "Number of 0's: " << zero << std::endl;

    return 0;
}
