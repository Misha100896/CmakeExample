#include "main.h"

int main() {
    std::cout << "Write 2 number:" << std::endl;
    int a, b;
    std::cin >> a >> b;

    std::cout << "GCD(" << a << ',' << b << ')' << " = ";
    red_print(gcd(a, b));
    rainbow();

    return 0;
}