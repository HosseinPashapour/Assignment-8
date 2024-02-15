import os
import imageio

file_list =sorted(os.listdir("E:\Assignment-8\images"))

IMAGES = []
for file_name in file_list:
    file_path = "E:\Assignment-8\images/" + file_name
    image = imageio.imread(file_path)
    IMAGES.append(image)

print(IMAGES)
imageio.mimsave("E:\Assignment-8\my_output.gif", IMAGES)