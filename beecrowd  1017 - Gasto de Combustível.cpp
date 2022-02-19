#include <iostream>
#include <cmath>
using namespace std;

int main() {
  double tempo_gasto, velocidade_media, litros_necessario;
  cin >> tempo_gasto >> velocidade_media;
  litros_necessario = (tempo_gasto*velocidade_media)/12;
  cout.precision(3);
  cout << fixed << litros_necessario << endl;

  return 0;
}
