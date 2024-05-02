#include <bits/stdc++.h>
using namespace std;

bool isValid(vector<vector<int>> &grid, int row, int col){
    int i = col;
    while (i >= 0){
        if (grid[row][i] == 1){
            return false;
        }
        i--;
    }
    i = row;
    int j = col;
    while (i >= 0 && j >= 0){
        if (grid[i][j] == 1){
            return false;
        }
        i--;
        j--;
    }
    i = row;
    j = col;
    while (i < grid.size() && j >= 0){
        if (grid[i][j] == 1){
            return false;
        }
        i++;
        j--;
    }
    return true;
}

bool placeQueens(vector<vector<int>> &grid, int n){
    if (n >= grid.size())
        return true;
    for (int i = 0; i < grid.size(); i++){
        if (isValid(grid, i, n)){
            grid[i][n] = 1;
            if (placeQueens(grid, n + 1)){
                return true;
            }
            grid[i][n] = 0;
        }
    }
    return false;
}

void display(vector<vector<int>> &grid){
    for (int i = 0; i < grid.size(); i++){
        for (int j = 0; j < grid.size(); j++){
            if (grid[i][j]){
                cout << "Q ";
            }
            else{
                cout << ". ";
            }
        }
        cout << endl;
    }
}

int main(){
    int n;
    cout << "Enter the value of n : ";
    cin >> n;

    vector<vector<int>> grid(n, vector<int>(n, 0));
    placeQueens(grid, 0);
    display(grid);
    return 0;
}
