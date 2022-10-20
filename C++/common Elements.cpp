#include <iostream>
using namespace std ;
int commonElements(int arr1[],int arr2[],int arr3[],int s1,int s2,int s3){
	int i=0,j=0,k=0;
	while(i<s1&&j<s2&&k<s3){
		if(arr1[i]==arr2[j]&&arr2[j]==arr3[k]){
			cout<<arr1[i]<<" ";
			i++;
			j++;
			k++;
		}
		else if(arr1[i]<=arr2[j]&&arr1[i]<=arr3[k]){
			i++;
		}
		else if(arr2[j]<=arr3[k]&&arr2[j]<=arr1[i]){
			j++;
		}
		else {
			k++;
		}
	}
}
 int main(){
	 int arr1[] = {1, 2, 3};
        int arr2[] = {1, 3, 4, 5};
        int arr3[] = {1, 2, 3, 4, 6};
	int s1=3;
	int s2=4;
	int s3=5;
	commonElements(arr1,arr2,arr3,s1,s2,s3);
}
