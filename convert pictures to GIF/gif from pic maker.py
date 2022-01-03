import imageio
import os
files = os.listdir('C:\\Users\\eddie\\Desktop\\Ironhack\\MY PROJECTS\\GIF from picture maker\\images for GIF')
images_path = [os.path.join('C:\\Users\\eddie\\Desktop\\Ironhack\\MY PROJECTS\\GIF from picture maker\\images for GIF',file) for file in files]
images_original = []
for img in images_path:
    images_original.append(imageio.imread(img))
imageio.mimsave('C:\\Users\\eddie\\Desktop\\Ironhack\\MY PROJECTS\\GIF from picture maker\\output\\new_gif.gif', images_original, fps=1.5) # can change FPS

print("Done!")