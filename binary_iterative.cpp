#include <bits/stdc++.h> 
using namespace std;  
int bS(int arr[], int l, int r, int x) 
{ 
    while (l <= r) { 
        int mid = l + (r - l) / 2; 
  
        if (arr[mid] == x){return mid; } 
         
        if (arr[mid] < x) 
           { l = mid + 1; }
    
        else
            {r = mid - 1;} 
    } 
  
    return -1; 
} 
  
int main() 
{ 
    int *arr=new int[10];
    for(int i=0;i<10;i++){arr[i]=i+1;} 
    

    int x;
    cout<<"enter element to be searched using binary search , search elemnt is  "<<"5"<<endl;
    x=5;
    
    
    int result = bS(arr, 0, 9, x); 
    if (result!=-1) 
    {
        cout<<"elemet is present";
    }else{
        cout<<"element not found";
    }
    cout<<endl;


for( int i=0;i<10;i++)
{
    if(arr[i]==x)
    {
        cout<<endl<<"Element Found using linear search";
        break;
    }
    
}
delete [] arr;
    return 0; 
} 