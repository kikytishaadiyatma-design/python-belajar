import os

counter = 1

for file in os.listdir("."):
    if file.endswith(".jpg"):
        new_name = f"foto_{counter}.jpg"
        os.rename(file, new_name)
        counter += 1

print("Selesai mengganti nama file")
