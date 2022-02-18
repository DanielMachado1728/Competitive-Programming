#include <iostream>
#include <cmath>

using namespace std;

# define pi 3.14159

int main() {
 double raio, area;
 cin >> raio;
 area = pi*pow(raio,2);
 cout.precision(4);
 cout << "A=" << fixed << area << endl;
 
 return 0;
}
