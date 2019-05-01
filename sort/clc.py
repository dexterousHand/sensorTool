import os
for i in range(4,8):

    for j in range(71,201):
        filename="./"+str(i)+"/"+str(j)+".png"
        if os.path.exists(filename):
            os.remove(filename)
    print(i)