# Write your solution here
def times_ten(start_index: int, end_index: int):
    
   
    dictionary={}
    
    my_list=[]
    for g in range(start_index, end_index + 1):
        my_list.append(g)
        dictionary[g]= g*10
       
    for i in range(start_index, end_index):
           
        return dictionary


if __name__ == "__main__":
    d = times_ten(3, 6)
    print(d)
    