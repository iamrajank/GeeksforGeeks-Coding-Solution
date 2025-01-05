//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;
 
// Driver program to test above function

// } Driver Code Ends
class Solution{
  public:
    /*you are required to complete this method*/
    int convertFive(int n)
    {
    //Your code here
    string temp = to_string(n);
        for(int i = 0 ; i < temp.size() ; i++){
            if(temp[i] == '0') temp[i] = '5';
        }
        return stoi(temp);
    }
};


//{ Driver Code Starts.
int main()
{
    int T;
    cin>>T;
    while(T--)
    {
    	int n;
    	cin>>n;
    	Solution obj;
    	cout<<obj.convertFive(n)<<endl;
    
cout << "~" << "\n";
}
}
// } Driver Code Ends