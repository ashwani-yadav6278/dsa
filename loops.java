
import java.util.*;

public class loops {

    // public static void largestElement(int arr[]) {
    //     int n = arr.length;
    //     // Using sort method TC=O(n log n)

    //     // Arrays.sort(arr);

    //     // System.out.println(arr[n - 1]);

    //     // Optimal approach TC= O(n)
    //     int largest = arr[0];
    //     for (int i = 1; i < n; i++) {
    //         if (arr[i] > arr[i - 1]) {
    //             largest = arr[i];
    //         }
    //     }

    //     System.out.println(largest);

    // }

    // public static void secondLargest(int arr[]) {
    //     int n = arr.length;
        // Brute force approach TC=O(2n)
        // int largest=arr[0];
        // int secondLargest=arr[0];
        // for(int i=1;i<n;i++){
        // if(arr[i]>largest){
        // largest=arr[i];
        // }
        // }

        // for(int i=1;i<n;i++){
        // if(arr[i]>secondLargest && arr[i]<largest){
        // secondLargest=arr[i];
        // }
        // }
        // System.out.println(secondLargest);

        // BETTER APPROACH TC =O(n log n)

        // Arrays.sort(arr);
        // int largest=arr[n-1];
        // int secondLargest=-1;
        // for(int i=n-2;i>=0;i--){
        // if(arr[i]>secondLargest && arr[i]<largest){
        // secondLargest=arr[i];
        // break;
        // }
        // }
        // System.out.println(secondLargest);

        // OPTIMAL APPROACH TC= O(n)

    //     int largest = arr[0];
    //     int secondLargest = -1;
    //     for (int i = 1; i < n; i++) {
    //         if (arr[i] > largest) {
    //             secondLargest = largest;
    //             largest = arr[i];
    //         } else if (arr[i] > secondLargest && arr[i] < largest) {
    //             secondLargest = arr[i];

    //         }
    //     }

    //     System.out.println(secondLargest);

    // }

    // public static void secondSmallest(int arr[]){
    // int n=arr.length;
    // int smallest=arr[0];
    // int sec_Smallest=Integer.MAX_VALUE;

    // for(int i=1;i<n;i++){
    // if(arr[i]<smallest){
    // sec_Smallest=smallest;
    // smallest=arr[i];
    // }else if(arr[i]<sec_Smallest && arr[i]>smallest){
    // sec_Smallest=arr[i];
    // }
    // }
    // System.out.println(sec_Smallest);
    // }

    // public static boolean sorted(int arr []){
    // int n=arr.length;
    // for(int i=1;i<n;i++){
    // if(arr[i]<arr[i-1]){
    // return false;
    // }

    // }
    // return true;

    // }

    // public static void removeDuplicates(int arr []){

    // Brute force TC=O(n), SC=O(n)

    // Set<Integer> set= new LinkedHashSet<>();

    // for(int num:arr){
    // set.add(num);
    // }
    // Integer [] uniqueArr=set.toArray(new Integer[0]);
    // System.out.println(Arrays.toString(uniqueArr));

    // OPTIMAL APPROACH TC=O(n), SC=O(1)

    // int n=arr.length;
    // int i=0;

    // for(int j=1;j<n;j++){
    // if(arr[j] !=arr[j-1]){
    // arr[i+1]=arr[j];
    // i++;
    // }
    // }

    // for (int k=0;k<=i;k++){
    // System.out.print(arr[k]+" ");
    // }

    // }

    // Question=Left rotate an array by one place

    // public static void rotate(int arr []){
    // int n=arr.length;
    // int temp=arr[0];
    // for(int i=1;i<n;i++){
    // arr[i-1]=arr[i];
    // }
    // arr[n-1]=temp;

    // }

    // QUESTION MOVE ZEORS TO END
    // public static void moveZeros(int arr[]) {
    //     int n = arr.length;
    //     int j = -1;
    //     for (int i = 0; i < n; i++) {
    //         if (arr[i] == 0) {
    //             j = i;
    //             break;
    //         }

    //     }

    //     for (int i = j + 1; i < n; i++) {
    //         if (arr[i] != 0) {
    //             int temp = arr[j];
    //             arr[j] = arr[i];
    //             arr[i] = temp;
    //             j++;
    //         }
    //     }

    // }


    //QUESTION UNION OF TWO SORTED ARRAY
    // BRUTE FORCE APPROACH TC= O(n + m), Space = O(n + m) for storing union.


        // public static void union(int arr[],int arr2[]) {
        //     Set<Integer>result=new LinkedHashSet<>();

        //     for(int i=0;i<arr.length;i++){
        //         result.add(arr[i]);
        //     }

        //     for(int j=0;j<arr2.length;j++){
        //         result.add(arr2[j]);
        //     }

        //     int ans[]=new int[result.size()];
        //     int i=0;
        //     for(int itr:result){
        //         ans[i++]=itr;
        //     }
        //      // Print result
        // System.out.println(Arrays.toString(ans));
            
        // }
    // OPTIMAL APPROACH TC=O(N+M) & SC=O(N+M) SPACE IS USED FOR RETURN THE RESULT NOT FOR SOLVE THE PROBLEM 
    // public static  ArrayList<Integer> union(int arr[],int arr2[]){
    //     ArrayList<Integer> result=new ArrayList<>();
    //     int n=arr.length;
    //     int m=arr2.length;
    //     int i=0;
    //     int j=0;

    //     while(i<n && j<m){
    //         // skip duplicates in arr1
    //         while(i>0 && i<n && arr[i]==arr[i-1]) i++;
    //          // skip duplicates in arr2
    //         while(j>0 && j<m && arr[j]==arr[j-1]) j++;

    //         // exit form loop when both array are exhausted
    //         while(i>=n || j>=m) break;

    //         if(arr[i]<arr2[j]){
    //             result.add(arr[i]);
    //             i++;
    //         }else if (arr2[j]<arr[i]) {
    //             result.add(arr2[j]);
    //             j++;
    //         }else{
    //             result.add(arr[i]); // when both equal we take ony one and increse both 
    //             i++;
    //             j++;
    //         }

           

    //     }
    //      while(i<n){
    //             if(result.isEmpty()||result.get(result.size()-1) != arr[i]){
    //                 result.add(arr[i]);
    //                 i++;
    //             }
    //         }

    //         while(j<m){
    //             if(result.isEmpty()||result.get(result.size()-1)!=arr2[j]){
    //                 result.add(arr2[j]);
    //                 j++;
    //             }
    //         }
    //     return result;
    // }

    // public static void print(int arr[]) {
    //     for (int i = 0; i < arr.length; i++) {
    //         System.out.print(arr[i]);
    //     }
    // }


    // QUESTION INTERSECTION OF TWO SORTED ARRAYS
    // BRUTE FORCE 
    // public static void inter(int arr[],int arr2[]){
    //     int visit[]=new int[arr2.length];
    //     ArrayList<Integer>ans=new ArrayList<>();
    //     for(int i=0;i<arr.length;i++){
    //         for(int j=0;j<arr2.length;j++){
    //             if(arr[i]==arr2[j] && visit[j]==0){
    //                 ans.add(arr[i]);
    //                 visit[j]=1;
    //                 break;
    //             }
    //             if(arr[i]<arr2[j]){
    //                 break;
    //             }
    //         }
    //     }
    //     System.out.println(ans);
    // }

    // QUESTION INTERSECTION OF TWO SORTED ARRAYS
    // public static void intersection(int arr[],int arr2[]){
    //     int n=arr.length;
    //     int m=arr2.length;
    //     int j=0;
    //     int i=0;

    //     while(i<n && j<m){
    //         if(arr[i]<arr2[j]){
    //             i++;
    //         }
    //         else if(arr[i]>arr2[j]){
    //             j++;

    //         }

    //         else{
    //             System.out.print(arr[i]+",");
                
    //             i++;
    //             j++;
    //         }
    //     }
       
    // }

    // QUESTION= Find missing number in an array
    // BRUTE FORCE 
    // public static int missingNum(int arr3[]){
        
    //     int N=6;
    //     for(int i=1;i<=N;i++){
    //         int flag=0;
    //         for(int j=0;j<arr3.length;j++){
    //             if(i==arr3[j]){
    //                 flag=1;
    //                 break;
    //             }
               
    //         }
    //          if(flag==0){
    //                 return i;
    //             }
    //     }
    //     return -1;
    // }

    public static int[] union(int arr1[], int arr2[]) {
        Set<Integer> set = new TreeSet<>();
        for (int i = 0; i < arr1.length; i++) {
            set.add(arr1[i]);
        }

        for (int i = 0; i < arr2.length; i++) {
            set.add(arr2[i]);

        }
        int union[] = new int[set.size()];
        int j = 0;
        for (int st : set) {
            union[j++] = st;
        }

        return union;
    }

    public static void main(String[] args) {

        int arr1[] = { 1, 2, 2, 3, 3, 4, 5, 6, 7 };
        int[] arr2 = { 2, 3, 3, 4, 5, 6, 7, 8 };
        // int arr3[]={1,2,3,5,6};

        // largestElement(arr);
        // secondLargest(arr);
        // secondSmallest(arr);
        // removeDuplicates(arr);

        // rotate(arr);
        // moveZeros(arr);
        // print(arr);

        // ArrayList<Integer> ans = union(arr, arr2);
        // System.out.println(ans);
        // }
        // union(arr, arr2);
        // inter(arr, arr2);
        // int result=missingNum(arr3);
        // System.out.println(result);
        int [] result=union(arr1, arr2);
        for(int num:result){
            System.out.print(num +" ");
        }
        // intersection(arr, arr2);

    }
}
