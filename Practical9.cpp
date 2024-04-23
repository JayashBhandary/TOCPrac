#include <iostream>
#include <stack>

using namespace std;
stack<int> st;
string s = "";
int i = 0;

void q0();
void q1();

void q1() {
    if(st.empty() && i == s.size()) {
        return;
    } else if (s[i] == st.top()){
        st.pop();
        i++;
        q1();
    } else {
        cout<<"invalid";
        exit(1);
    }
}

void q0() {
    if(s[i] == 'c') {
        i++;
        q1();
    } else {
        st.push(s[i]);
        i++;
        q0();
    }
}


int main() {
    cout<<"Input the string: ";
    cin>>s;

    cout<<"Input string is: ";
    q0();
    cout<<"Valid";
    return 0;
}