"""__author__ = 'anyu'

11.5 Given a sorted array of strings which is interspersed with empty strings, write a method to find the location of a given string.
Example: ["at","","","","ball","","","car","","","dad","",""] will return 4

Careful consideration should be given to the situation when someone searches for the empty string.
Should we find the location (which is an 0(n) operation)? Or should we handle this as an error?
There's no correct answer here. This is an issue you should raise with your interviewer.
Simply asking this question will demonstrate that you are a careful coder.
"""

def bsearch(a,start,end,s):

    # use another helper function to do array range check

    mid = (start+end)//2
    if a[mid] == s: return mid
    else:
        t = mid
        while a[t] == "" and t<=end:
            t +=1
        if t>end: bsearch(a,start,mid-1,s)
        else:
            if a[t] == s: return t
            elif a[t]<s: bsearch(a,t+1,end,s)
            elif a[t]>s: bsearch(a,start,t-1,s)

        return -1

a=["at","","","","ball","","","car","","","dad","",""]
print bsearch(a,0,12,"ball")
