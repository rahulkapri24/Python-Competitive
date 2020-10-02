import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
import java.lang.reflect.*;

import static java.lang.System.in;
class Prime
{
public void checkPrime(int ... a)
{
    for(int i : a)
    {
    if(i==1 || i<2)
    {
        
       System.out.print("");
        
    }
    else if(i==2)
    {
        System.out.print(i + " ");
    }
    else
    {
            int sum=1;
            for(int y=2;y<i;y++)
            {
            if(i%y==0)
            {
                sum=0;
                break;
            }
        }
        if(sum==1)
        {
            System.out.print(i + " ");
        }
           
    }
   
    }
    System.out.println("");
}}
 

public class Solution {
