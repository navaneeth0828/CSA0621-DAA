#Linear search 
arr=[10,25,30,45,50]
key=30
found=False
for i in range(len(arr)):
    if arr[i]==key:
        print("key found in index", i)
        found =True
        break
if not found:
    print("key not found")       