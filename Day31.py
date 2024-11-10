# import os
# os.mkdir("Project")

# for i in range(0,10):
#     os.mkdir(f"Project/Day{i+1}")

# import os

# for i in range(0,10):
#     os.rename(f"Project/Day{i+1}",f"Project/Urge {i+1}")

import os
folders = os.listdir("Project")

print(folders)

for folder in folders:
    print(folder)