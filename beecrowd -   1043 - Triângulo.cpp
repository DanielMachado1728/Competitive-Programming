#include <iostream>
using namespace std;

int main() {
  double a,b,c,perimetro;
  cin >> a >> b >> c;
  cout.precision(1);
  if(a+b>c && a+c>b && b+c>a){
    perimetro = a+b+c;
    cout << fixed << "Perimetro = " << perimetro << endl;
  }
  else{
    cout << fixed << "Area = " << (a+b)*c/2 << endl;
  }

  return 0;
}
