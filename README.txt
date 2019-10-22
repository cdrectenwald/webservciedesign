Hello,

Here is the task: 

Please write a web service that takes in a list of email addresses and returns an integer indicating the number of unique email addresses. Where "unique" email addresses means they will be delivered to the same account using Gmail account matching. Specifically: Gmail will ignore the placement of "." in the username. And it will ignore any portion of the username after a "+".

Examples: test.email@gmail.com, test.email+spam@gmail.com and testemail@gmail.com will all go to the same address, and thus the result should be 1.

For this I designed a simple function that takes in an array, then evaluates each element in array with multiple regex expressions then evaluate if each elemnt is unique. At the end of the function, the amount of unique values are returned.

Because this is a web service, there is a possibility that there will be an array read or a csv. That was ambigious so I made my function as if the input was an array. Going forward, I could make a helper function to convert a csv to array if the file read is a csv. 

