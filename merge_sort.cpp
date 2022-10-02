/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>

void merge(int *arr,int start, int end){
    
    int mid=start+(end-start)/2;
    
    int len1=mid-start+1;
    int len2=end-mid;
    
    
    //left part
    int *first=new int[len1];
    
    //right part
    int *second=new int[len2];
    
    //copy values
    
    int main_array_index=start;
    
    for (int i=0;i<len1;i++){
        first[i]=arr[main_array_index++];
    }
    
    main_array_index=mid+1;
    
    for(int i=0;i<len2;i++){
        second[i]=arr[main_array_index++];
    }
    
    //merge two sorted lists
    
    int index1=0;
    int index2=0;
    
    main_array_index=start;
    
    while (index1<len1 && index2<len2){
        if(first[index1]<second[index2]){
            arr[main_array_index++]=first[index1++];
        }
        else{
            arr[main_array_index++]=second[index2++];
        }
    }
    
    while(index1<len1){
        arr[main_array_index++]=first[index1++];
        
    }
    while (index2<len2){
        arr[main_array_index++]=second[index2++];
    }
    
    delete []first;
    delete []second;
    
    
}

void merge_sort(int *arr, int start,int end){
    
    //base case 
    
    if (start>=end){
        return;
    }
    
    int mid=start+(end-start)/2;
    
    
    //merge sort on left part
    merge_sort(arr,start,mid);
    
    
    //merge sort on right part
    merge_sort(arr,mid+1,end);
    
    merge(arr,start,end);
}





using namespace std;

int main()
{
    int arr[5]={5,4,3,2,1};
    
    int n=5;
    
    merge_sort(arr,0,n-1);
    
    for (int i=0;i<n;i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;

    return 0;
}
