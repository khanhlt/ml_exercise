#include <iostream>
#include <fstream>

using namespace std;

int main() {
    ifstream f_in;
    ofstream f_out;
    f_in.open("test.csv", ios::in);
    f_out.open("test.txt", ios::out);

    string line;
    // skim the first line (contains label of features)
    getline(f_in, line);

    int cf; // features counter

    while (getline(f_in, line)) {
        cf = 0;
        string ch;
        for (unsigned int i = 0; i < line.length(); i++) {
            if (line.at(i) == ',') {
                cf++;
                if (cf == 1 || cf == 2 || cf == 5 || cf == 6 || cf == 7 || cf == 8) {
                    if (ch == "male")
                        f_out << "0,";
                    else if (ch == "female")
                        f_out << "1,";
                    else if (ch == ",")
                        f_out << "0,";
                    else
                        f_out << ch << ',';
                }
                if (cf == 10) {
                    if (ch == "female")
                        f_out << "1,";
                    else if (ch == "male")
                        f_out << "0,";
                    else if (ch == ",")
                        f_out << "0\n";
                    else
                        f_out << ch << endl;
                }
                ch.clear();
                if (line.at(i + 1) != ',')
                    i += 1;
            }
            ch.push_back(line.at(i));
        }
    }

    f_in.close();
    f_out.close();
    return 0;
}