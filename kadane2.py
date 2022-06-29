def kad(x):
 
   
    max_now = 0
 
   
    max_last = 0
 
   
    for i in x:
        
        max_last = max_last + i
 
       
        max_last = max(max_last, 0)
 
        
        max_now = max(max_now, max_last)
 
    return max_now
 
 
if __name__ == '__main__':
 
    x = [-3, 4, -5, 1, 2, -6, 8]
 
    print("The sum of list with the largest sum is",
        kad(x))