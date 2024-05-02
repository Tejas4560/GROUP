#include<bits/stdc++.h>
using namespace std;

int main(){
int n,m;
cout<<"\nEnter number of vertices: ";
cin>>n;
cout<<"\nEnter number of edges: ";
cin>>m;
int a[n][n];
cout<<"\nNow enter vertex numbers between which edges are present\n";
int v1,v2;
for(int i=0;i<m;i++){
cout<<"\nVertex :";
cin>>v1;
cout<<"\nVertex :";
cin>>v2;
cout<<"\nVertex "<<v1<<" <---------> Vertex "<<v2<<endl;
a[v1][v2]=1;
a[v2][v1]=1;
}
queue<int> q;
bool v[n];
for(int i=0;i<n;i++){
v[i]=false;
}
cout<<"\nEnter the root vertex: ";
cin>>m;
q.push(m);
cout<<"\nFollowing is the BFS traversal of the provided graph:\n";
while(!q.empty()){
int x=q.front();
q.pop();
cout<<x<<" ";
v[x]=true;
for(int i=0;i<n;i++){
if(a[x][i]==1 && v[i]==false){
v[i]=true;
q.push(i);
}
}
}

for(int i=0;i<n;i++){
v[i]=false;
}
stack<int> s;
s.push(m);
cout<<"\n\nFollowing is the DFS traversal of the providedgraph:\n";
while(!s.empty()){
int x=s.top();
s.pop();
cout<<x<<" ";
v[x]=true;
for(int i=0;i<n;i++){
if(a[x][i]==1 && v[i]==false){
v[i]=true;
s.push(i);
}
}
}
return 1;
}