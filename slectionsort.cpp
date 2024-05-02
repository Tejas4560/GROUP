#include<bits/stdc++.h>
using namespace std;

int main(){
int n;
vector<int> v;
cout<<"Enter number of elements: ";
cin>>n;
cout<<"\nEnter values: ";
for(int i=0;i<n;i++){
int x;
cout<<"\nElement "<<i+1<<": ";
cin>>x;
v.push_back(x);
}
int z;
cout<<"\nThe array you entered is: ";
for(int i=0;i<n;i++){
cout<<v[i]<<" ";
}
cout<<"\n\nPerforming Selection Sort on the given array\n";
for(int i=0;i<n;i++){
z=i;
for(int j=i+1;j<n;j++){
if(v[j]<v[z]){
z=j;
}
}
int t=v[z];
v[z]=v[i];
v[i]=t;
}
cout<<"\nThe sorted array is: ";
for(int i=0;i<n;i++){
cout<<v[i]<<" ";
}
return 1;
}