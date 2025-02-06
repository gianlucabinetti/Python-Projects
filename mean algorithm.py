from time import time

start_time = time()

list1 = [1,5,7,9,12,59,23,4,15]

def Mean_calculator():
    
    total = sum(list1) / len(list1)
    print("The average is :", total)
    
Mean_calculator()

end_time = time()
elapsed = end_time

print(f"Execution Time: {elapsed:.3f} seconds")