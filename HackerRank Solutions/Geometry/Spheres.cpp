#include <bits/stdc++.h>

using namespace std;

typedef struct Point {
	int x;
	int y;
	int z;
} Point;

typedef struct Sphere {
	Point origin;
	int radius;
	Point movement;
} Sphere;

int main (void) {
	int testNum;
	cin >> testNum;
	while(testNum--){
		//getting the input and putting it into spheres
		int r1, r2;
		int x, y, z;
		int xA, yA, zA;
		cin >> r1 >> r2;
		cin >> x >> y >> z;
		cin >> xA >> yA >> zA;
		Point origin1 = {x, y, z};
		Point move1 = {xA, yA, zA};
		Sphere s1 = {origin1, r1, move1};
		cin >> x >> y >> z;
		cin >> xA >> yA >> zA;
		Point origin2 = {x, y, z};
		Point move2 = {xA, yA, zA};
		Sphere s2 = {origin2, r2, move2};
		//Turning the acceleration of the second one into inverse acceleration of first
		s1.movement.x -= s2.movement.x;
		s1.movement.y -= s2.movement.y;
		s1.movement.z -= s2.movement.z;
		//Check if spheres start together
		int dist = pow((s1.origin.x - s2.origin.x), 2) + pow((s1.origin.y - s2.origin.y), 2) + pow((s1.origin.z - s2.origin.z), 2);
		int radiusSquared = pow((s1.radius + s2.radius), 2);;
		dist -= radiusSquared;
		if (dist <= 0) {
			cout << "YES" << endl;
			continue;
		}
		//Normalize the given movement vector
		Point movement = {(s1.movement.x * s1.movement.x), (s1.movement.y * s1.movement.y), (s1.movement.z * s1.movement.z)};
		double magnitude = sqrt(movement.x + movement.y + movement.z);
		Point normalize = {(s1.movement.x/magnitude), (s1.movement.y/magnitude), (s1.movement.z/magnitude)};
		Point collisionVector = {(s2.origin.x - s1.origin.x), (s2.origin.y - s1.origin.y), (s2.origin.z - s1.origin.z)};
		double magnitudeCollision = sqrt(pow(collisionVector.x,2) + pow(collisionVector.y,2) + pow(collisionVector.z,2));
		double d = (collisionVector.x * normalize.x) + (collisionVector.y * normalize.y) + (collisionVector.z * normalize.z);
		if (d <= 0) {
			cout << "NO" << endl;
			continue;
		}
		double f = pow(magnitudeCollision,2) - pow(d, 2);
		double t = radiusSquared - f;
		if (t < 0) {
			cout << "NO" << endl;
			continue;
		}
		cout << "YES" << endl;
	}
	return 0;
}
