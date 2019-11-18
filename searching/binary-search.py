def  search(arr, l, r, x): 
  
    # Check base case 
    if r >= l: 
  
        mid = int(l + (r - l)/2)
  
        # If element is present at the middle itself 
        if arr[mid] == x: 
            return mid 
          
        # If element is smaller than mid, then it can only 
        # be present in left subarray 
        elif arr[mid] > x: 
            return search(arr, l, mid-1, x) 
  
        # Else the element can only be present in right subarray 
        else: 
            return search(arr, mid+1, r, x) 
  
    else: 
        # Element is not present in the array 
        return -1
    




arr = [ 2, 3, 4, 10, 40,50,60,70 ] 
x = 60
  
# Function call 
result = search(arr, 0, len(arr)-1, x) 
  

if result != -1: 
    print("Element is present at index %d" % result)
else: 
    print("Element is not present in array")