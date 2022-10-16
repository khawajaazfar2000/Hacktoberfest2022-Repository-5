#include<iostream>
using namespace std;
//Linear Search
//A particular element in array
int main(){
    int n, key;
    cin>>n;
    int a[1000];
    for(int i = 0; i<n; i++){
        cin>>a[i];
    }
    //Asking for the element user want to search
    cout<<"Enter the element you want to search: ";
    cin>>key;
    //Find out the index of that element by tranversing the array
    //Linear Search Algorithm
    int i;
    for(i = 0; i<n; i++){
        if(a[i]==key){
            cout<<key<<" found at "<<i+1<<" index";
            break;
        }
    }
    if(i == n){
            cout<<key<<" is not present "<<endl;
        }
    return 0;
}