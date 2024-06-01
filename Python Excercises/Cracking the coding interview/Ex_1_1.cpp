#include <bits/stdc++.h>
using namespace std;
int main(){
    string word;
    cin>>word;
    int arr[26]={0};
    for (int a=0;a<word.length();a++)
    {word[a]=tolower(word[a]);
    }
    for (int a=0;a<word.length();a++)
    {
        arr[word[a]-'a']++;
    }
    bool y=false;
    for (int a=0;a<26;a++){
        if(arr[a] > 1)
        {y=true;}
    }
    if(y==true){cout<<"yes";}
    else{cout<<"no";}
}