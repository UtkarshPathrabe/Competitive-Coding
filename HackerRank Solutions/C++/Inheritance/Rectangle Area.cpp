#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <cassert>
using namespace std;

class Rectangle {
    public:
        int width, height;
        void Display() {
            cout << width << " " << height << endl;
        }
};
class RectangleArea: public Rectangle {
    public:
        void Input() {
            cin >> width >> height;
        }
        void Display() {
            cout << width * height << endl;
        }
};
int main() {
	RectangleArea r_area;
	r_area.Input();
	Rectangle *r;
	r=&r_area;
	r->Display();
	r_area.Display();
	return 0;
}
