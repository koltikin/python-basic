import os

path = "test2"
os.makedirs(f"{path}",exist_ok=True)

# if os.path.exists(path):
#     print("path exists")
#     if os.path.isfile(path):
#         print("that is a file")
#     elif os.path.isdir(path):
#         print("that is a diractory")
# else:
#     print("path not exists")
#     os.makedirs(f"{path}",exist_ok=True)
