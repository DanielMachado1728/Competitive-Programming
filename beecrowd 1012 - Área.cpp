#include <iostream>
using namespace std;
# define pi 3.14159
int main() {
  double a,b,c, triangulo, circulo, trapezio, quadrado, retangulo;
  cin >> a >> b >> c;
  triangulo = (a*c)/2;
  circulo = pi*c*c;
  trapezio = (a+b)*c/2;
  quadrado = b*b;
  retangulo = a*b;
  cout.precision(3);
  cout << "TRIANGULO: " << fixed << triangulo << endl <<"CIRCULO: " << circulo << endl << "TRAPEZIO: " << trapezio << endl << "QUADRADO: " << quadrado << endl << "RETANGULO: " << retangulo << endl;

return 0;
}
