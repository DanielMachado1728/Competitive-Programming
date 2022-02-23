#include <bits/stdc++.h>
using namespace std;

int main() {
  map <int, string> meses;
  meses[1] = "January";
  meses[2] = "February";
  meses[3] = "March";
  meses[4] = "April";
  meses[5] = "May";
  meses[6] = "June";
  meses[7] = "July";
  meses[8] = "August";
  meses[9] = "September";
  meses[10] = "October";
  meses[11] = "November";
  meses[12] = "December";
  int mes;
  cin >> mes;
  cout << meses[mes] << endl;
  return 0;
}
