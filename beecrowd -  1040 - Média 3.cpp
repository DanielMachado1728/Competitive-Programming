#include <iostream>
using namespace std;
int main() {
  float a,b,c,d,media,exame;
  cin >> a >> b >> c >> d;
  media = (a*2+b*3+c*4+d)/10;
  cout.precision(1);
  if(media>=7){
    cout << fixed << "Media: " << media << endl << "Aluno aprovado." << endl;
  }
  else if(media < 5){
    cout << fixed << "Media: " << media << endl << "Aluno reprovado." << endl;
  }
  else{
    cout << fixed << "Media: " << media << endl << "Aluno em exame." << endl;
    cin >> exame;
    media = (media+exame)/2;
    cout << fixed << "Nota do exame: " << exame << endl;
    if (media >= 5){
      cout << fixed << "Aluno aprovado." << endl << "Media final: " << media << endl;
    }
    else{
      cout << fixed << "Aluno reprovado." << endl << "Media final: " << media << endl;
    }
  
 
  }

  return 0;
}
