#include<iostream>

using namespace std;

int callA=0;
int callB=0;
int callC=0;

class A {
	protected:
		void func(int  & a) {
			a = a * 2;
			callA++;
		}
};

class B {
	protected:
		void func(int & a) {
			a = a * 3;
			callB++;
		}
};

class C {
	protected:
		void func(int & a) {
			a = a * 5;
			callC++;
		}
};

class D : public A, public B, public C {
	int val;
	public:
		 D() {
		 	val = 1;
		 }
		 void update_val(int new_val) {
             int temp = new_val;
             while (temp % 2 == 0) {
                 temp /= 2;
                 A::func(val);
             }
             while (temp % 3 == 0) {
                 temp /= 3;
                 B::func(val);
             }
             while (temp % 5 == 0) {
                 temp /= 5;
                 C::func(val);
             }
		 }
		 void check(int);
};

void D::check (int new_val) {
	update_val(new_val);
	cout<<"Value = "<<val<<endl<<"A's func called "<<callA<<" times "<<endl<<"B's func called "<<callB<<" times "<<endl<<"C's func called "<<callC<<" times"<<endl;
}

int main() {
	D d;
	int new_val;
	cin>>new_val;
	d.check(new_val);
}
