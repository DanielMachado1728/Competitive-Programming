#include <iostream>
using namespace std;

int main() {
  int codigo, qtd;
  float total;
  cin >> codigo >> qtd;
  if (codigo == 1){
    total = qtd*4;
  }
  else if (codigo == 2){
    total = qtd*4.5;
  }
  else if (codigo == 3){
    total = qtd*5;
  }
  else if (codigo == 4){
    total = qtd*2;
  }
  else{
    total = qtd*1.5;
  }
  printf("Total: R$ %.2f\n",total);
  
  return 0;

}
