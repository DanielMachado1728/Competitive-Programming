#include <iostream>
using namespace std;

int main() {
  int numero, horas;
  double valor;
  cin >> numero >> horas >> valor;
  valor *= horas;
  cout.precision(2);
  cout << "NUMBER = "<< numero << endl << "SALARY = U$ " << fixed << valor << endl;

  return 0;
}
