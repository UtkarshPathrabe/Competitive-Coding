#include <bits/stdc++.h>

using namespace std;

// Complete the minimumNumber function below.
int minimumNumber(int n, string password) {
    int ans = 0;
    bool type[4] = {false};  
    for (int i=0; i<password.length(); i++) {
        if (password[i] >= '0' && password[i] <= '9') {
            type[0] = true;
        } else if (password[i] >= 'a' && password[i] <= 'z') {
            type[1] = true;
        } else if (password[i] >= 'A' && password[i] <= 'Z') {
            type[2] = true;
        } else {
            type[3] = true;
        }
    }
    for (int i=0; i<4; i++) {
        if (!type[i]) {
            ans++;
        }
    }    
    return max(ans, 6-n);
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    string password;
    getline(cin, password);

    int answer = minimumNumber(n, password);

    fout << answer << "\n";

    fout.close();

    return 0;
}
