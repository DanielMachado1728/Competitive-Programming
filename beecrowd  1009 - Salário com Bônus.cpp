#include <iostream>
using namespace std;

int main() {
  string nome;
  double salario_fixo, vendas,total;
  cin >> nome >> salario_fixo >> vendas;
  total = (salario_fixo + (vendas * 0.15));
  cout.precision(2);
  cout << "TOTAL = R$ " << fixed << total << endl;

  return 0;
}
