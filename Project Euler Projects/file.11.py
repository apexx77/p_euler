# c++ program

# #include <bits/stdc++.h>
# #include<vector>
# #define ll      long long
# using namespace std;
# int main() {
#     int arr[20][20];
#     vector <int> ans;
#     for(int i = 0; i<20; i++) {
#         for(int j = 0; j<20; j++) {
#             cin >> arr[i][j];
#         }
#     }for(int i = 0; i<20; i++) {
#         for(int j = 0; j<17; j++) {
#             ans.push_back(arr[i][j]*arr[i][j+1]*arr[i][j+2]*arr[i][j+3]);
#         }
#     }
#     for(int i = 0; i<17; i++) {
#         for(int j = 0; j<20; j++) {
#             ans.push_back(arr[i][j]*arr[i+1][j]*arr[i+2][j]*arr[i+3][j]);
#         }
#     }for(int i = 0; i<17; i++) {
#         for(int j = 0; j<17; j++) {
#             ans.push_back(arr[i][j]*arr[i+1][j+1]*arr[i+2][j+2]*arr[i+3][j+3]);
#         }
#     }for(int i = 0; i<17; i++) {
#         for(int j = 3; j<20; j++) {
#             ans.push_back(arr[i][j]*arr[i+1][j-1]*arr[i+2][j-2]*arr[i+3][j-3]);
#         }
#     }cout << *max_element(ans.begin(), ans.end());
# return 0;
# }