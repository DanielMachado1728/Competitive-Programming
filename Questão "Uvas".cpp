#include <bits/stdc++.h>

using namespace std
int main(){
	long long a, d m;
	long long v, r, p;
	cin >> a >>  d >> m;
	cin >> v >>  r >> p;
        if(v - a >= 0){
	       v = v - a;
		r = r+v;
		if(r - d >= 0){
			r = r - d;
		        p = p + r;

			if(m >= p){
				cout << "YES" << endl;

			}
			else 
				cout << "NO" << endl;
		}
		else 
			cout << "NO" << endl;
	}
	else 
		cout << "NO" << endl;

	return 0;
}
