#include <bits/stdc++.h>
using namespace std;
int main(){
    string s,t;
    cin>>s>>t;
    bool ans=false;
    if(s.length()!=t.length())
    ans=false;
    else{
    
    vector<int>v(150,1000);
        for(int a=0;a<s.length();a++){
            if(v[s[a]]==1000)
            v[s[a]]=s[a]-t[a];
            else {
            if(v[s[a]]!=s[a]-t[a])
            ans=false;
            }
        }
        for(int a=0;a<150;a++)
        v[a]=1000;
        for(int a=0;a<s.length();a++){
            if(v[t[a]]==1000)
            v[t[a]]=s[a]-t[a];
            else {
            if(v[t[a]]!=s[a]-t[a])
            ans=false;
            }
        }
        ans=true;
        cout<<ans;
    }    
}
