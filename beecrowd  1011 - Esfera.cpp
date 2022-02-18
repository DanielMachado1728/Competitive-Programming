#include <iostream>
#include <cmath>
using namespace std;
# define pi 3.14159
int main() {
  double raio, volume_esfera;
  cin >> raio;
  volume_esfera = (4.0/3)*pi*(pow(raio,3));
  cout.precision(3);
  cout << "VOLUME = "<< fixed << volume_esfera << endl;

return 0;
}
