
key_array = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
key1 = ["q","2","w","e","4","r","5","t","y","7","u","8","i","9","0","p","-","[","=","z","x","d","c","f","v","g","b","n",
       "j","m","k",",",".",";","/","'"]
key = input()

count = 0
for i in range(len(key1)):
    if key == key1[i]:
        count = i

print(count)

ic = 0
alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
for i in range(len(alpha)):
    if key == alpha[i]:
        ic = i
print(ic)
