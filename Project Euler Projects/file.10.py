n = int(input())
arr = []
for i in range(2, n) :
    for j in range(2, i-1) :
        if i%j == 0 :
            break
    else :
        arr.append(i)
ans = 0
for i in arr :
    ans += i
print(ans)
#c++ program:

#   #include <bits/stdc++.h>
#   #include<vector>
#   #define ll      long long
#   using namespace std;
#   int main() {
#        ll n, ans = 0;
#        vector <ll> arr{2, 3};
#        cin >> n;
#        for(ll i = 2; i<n; i++) {
#            for(ll j = 2; j*j<=i; j++) {
#                if(i%j == 0) {
#                    break;
#                }else if(j+1 > sqrt(i)) {
#                    arr.push_back(i);
#                }
#            }
#
#            }for(auto i = arr.begin(); i != arr.end(); ++i) {
#                ans+=*i;
#            }cout << ans;
#    return 0;
#    }
