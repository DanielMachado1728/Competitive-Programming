#include <iostream>
using namespace std;

int main() {
    int vezes=0;
    int total=0;
    int pulo=0;
    cin >> vezes;
    for(int vez=1; vez<=vezes; vez++){
        int resposta = 0;
        cin >> total >> pulo;
        for(int i=1; i<=total; i++){
            resposta = (resposta+pulo)%i;
        }
        cout << "Case " << vez << ": " << resposta+1 << endl;
    }
return 0;
}
