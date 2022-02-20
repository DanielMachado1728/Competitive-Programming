#include <iostream>
#include <cmath>
using namespace std;
int main() {
  double a,b,c,x,z, delta;
  cin >> a >> b >> c;
  delta = pow(b,2)-4*a*c;
  x = (-b + pow(delta,0.5))/(2*a);
  z = (-b - pow(delta,0.5))/(2*a);

  if (a == 0 || delta < 0){
    cout << "Impossivel calcular\n";   
  }
  else {
    cout.precision(5);
    cout << "R1 = " << fixed << x << endl << "R2 = " << z << endl;
  }
  return 0;
}
