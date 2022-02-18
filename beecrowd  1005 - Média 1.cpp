#include <iostream>
using namespace std;
// cout << fixed << setprecision(1);
int main() {
  double nota1, nota2, media;
  cin >> nota1 >> nota2;
  media = ((nota1 * 3.5) + (nota2 * 7.5))/11;
  cout.precision(5);
  cout << "MEDIA = " << fixed << media << endl;

  return 0;
}
