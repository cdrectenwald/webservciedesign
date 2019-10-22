#''''
#This program will be a webservice that can take a list of email addresses and returns an integer indicting the number of email addresses.

#Ignore the placement of "." in the username, and also ignore any portion of a username after "+"
#
#"""

import re

example =["test.email@gmail.com", "test.email+spam@gmail.com", "testemail@gmail.com"]


def uniqueAddressCounter(arr):
	

	# Assumptions are: that each email address has a valid @<website>.<end>, the type is a string, and an array is read in. 

	# Time Complexity should be O(n) with a space complexity of O(1)

	#base cases
	if len(arr) == 1 or len(arr)==0:
		return len(arr)
	
	#clean up email addresses with regex expressions  
	for i in range(0,len(arr)):
		arr[i]= re.sub("\+(.*?)\@", "@") # this subs any string that starts with + and ends with @ and replaces with @
		arr[i]= re.sub("\G[^\.]*\K\.(?=[^@]*@gmail\.com)","")  #replaces any "period" in username while preserving the rest of email address
		
	#create array of unique values
	for x in range(0, len(arr)):
		ans = []
		if i not in ans:
			ans.append(i)

	return len(ans)
