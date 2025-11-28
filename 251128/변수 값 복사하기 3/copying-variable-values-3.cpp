#include <iostream>
using namespace std;

int main() {
    int a = 1;
    int b = 5;
    int c = 3;

    a += b;
    b -= c;

    cout << a << "\n" << b << "\n" << c << endl;
    return 0;
}