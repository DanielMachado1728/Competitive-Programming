#include <iostream>
using namespace std;
int main() {
  int distancia;
  double consumo;
  cin >> distancia >> consumo;
  consumo = distancia/consumo;
  cout.precision(3);
  cout << fixed << consumo << " km/l" << endl;

  return 0;
}
