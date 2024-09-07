#include <iostream>
#include <vector>
#include <string>

using namespace std;

string should_delete_message(const vector<string>& stop_words, const string& message) {
    for (const string& word : stop_words) {
        if (message.find(word) != string::npos) {
            return "DELETE";
        }
    }
    return "KEEP";
}

int main() {
    int n, m;
    cin >> n >> m;
    cin.ignore();

    vector<string> stop_words(n);
    for (int i = 0; i < n; i++) {
        getline(cin, stop_words[i]);
    }

    vector<string> messages(m);
    for (int i = 0; i < m; i++) {
        getline(cin, messages[i]);
    }

    for (const string& message : messages) {
        string result = should_delete_message(stop_words, message);
        cout << result << endl;
    }

    return 0;
}