Hello,

Here is the task: 

Please write a web service that takes in a list of email addresses and returns an integer indicating the number of unique email addresses. Where "unique" email addresses means they will be delivered to the same account using Gmail account matching. Specifically: Gmail will ignore the placement of "." in the username. And it will ignore any portion of the username after a "+".

Examples: test.email@gmail.com, test.email+spam@gmail.com and testemail@gmail.com will all go to the same address, and thus the result should be 1.

For this I designed a simple function that takes in an array, then evaluates each element in array with multiple regex expressions then evaluate if each elemnt is unique. At the end of the function, the amount of unique values are returned.

Reflection: 
Because this is a web service, there is a possibility that there will be an array read or a csv. That was ambigious so I made my function as if the input was an array. Going forward, I could make a helper function to convert a csv to array if the file read is a csv.  I also assumed that each element in array is a string, and also has a @gmail.com email address. Going forward, I could make tweaks to accomadate for those instances as well. 

For storage of data is in arrays, because of size of web service. If the size of the the files for web service became large enough to the point where that could be an issue, I could make a database such as postgresql with each email being saved to a particular id. Then I would have stored reesults into a database then queried the count of unique values. In this case, however, the size and other specifications of web service were not clarified. There is a possibility to use a REST API to help develop the web service further such as editing an email address by id, or deleting an email by id, for a few examples. 


This program could be written in O(n) for time complexity. However, I believe if I had used hash tables and counted the amount of collisions and subtracted that amount from length of the array, O(1) for time complexity could have been achieved

