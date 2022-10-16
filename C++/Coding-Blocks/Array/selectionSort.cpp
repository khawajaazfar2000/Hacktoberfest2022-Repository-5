#include<iostream>
using namespace std;
//Linear Search
//Arranging of elements in ascending or descending order
void selection_sort(int a[], int n){
    for(int i = 0; i<n-1; i++){
        int min_index = i;
        //find out the smallest element index in the unsorted part
        for(int j=i; j<=n; j++){
            if(a[j] < a[min_index]){
                min_index = j;
            }
        }
        //After this loop we can do swap finally
        swap(a[i], a[min_index]);
    }
}
int main(){
    int n;
    cin>>n;
    int a[1000];
    for(int i =0; i<n; i++){
        cin>>a[i];
    } 
    selection_sort(a, n);
    for(int i =0; i<n; i++){
    cout<<a[i]<<" ";
    }
    return 0;
}