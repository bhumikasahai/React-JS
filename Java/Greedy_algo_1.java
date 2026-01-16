//Activity Selection (flipkart,facebook,JP Morgan)

//Problem statement - n actovites are given ith their start and end times, select max no of activities that can be performed by a single person assuming that a person can only work on a single activity at a time

//eg - strt =[10,12,20]   end=[20,25,30]  result =A0 + A2(10-20 & 20-30 that is not overlapped)
//end arr is sorted where as strt arr is not sorted

import java.util.*;
public class Greedy_algo_1{
    public static void main(String[] args) {  //O(n)
        int start[] = {1,3,0,5,8,5};
        int end[] = {2,4,6,7,9,9};
        // end time basis sorted
        int maxAct = 0;
        ArrayList<Integer> ans = new ArrayList<>();
        // 1st Activity
        maxAct = 1;
        ans.add(0);
        int lastEnd = end[0];
        for(int i=0;i<end.length;i++){
            if(start[i]>=lastEnd){
                //activity select
                maxAct++;
                ans.add(i);
                lastEnd=end[i];
            }
        }
        System.out.println("Max activities = " + maxAct);
        for(int i=0;i<ans.size();i++){
            System.out.print("A"+ans.get(i)+" ");
        }  
        System.out.println();
    }
}