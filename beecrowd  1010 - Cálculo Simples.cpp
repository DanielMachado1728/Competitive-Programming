#include <iostream>
using namespace std;

int main() {
  int numero1,quantidade1,numero2,quantidade2;
  double preco1, preco2,total;
  cin >> numero1 >> quantidade1 >> preco1 >> numero2 >> quantidade2 >> preco2;
  total = (quantidade1*preco1) + (quantidade2*preco2);
  cout.precision(2);
  cout << "VALOR A PAGAR: R$ " << fixed << total << endl;

  return 0;
}
