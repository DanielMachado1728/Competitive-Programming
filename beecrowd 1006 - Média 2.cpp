#include <iostream>
using namespace std;

int main() {
  //peso 2 3 5
  double a,b,c, media;
  cin >> a >> b >> c;
  media = ((a*2)+(b*3)+(c*5))/10;
  cout.precision(1);
  cout << "MEDIA = " << fixed << media << endl;

  return 0;

}
