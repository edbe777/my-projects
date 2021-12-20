{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "a4d82f0c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "BATCH_THUMBNAIL_MAKER\n",
      "Please enter the desired Thumbnail width in pixels: 100\n",
      "Please enter the desired Thumbnail height in pixels: 75\n",
      "C:\\Users\\eddie\\Desktop\\Ironhack\\MY PROJECTS\\images\\1635629991_996467_1635630216_noticia_normal_recorte1.jpg --batch_thumbnail_maker\n",
      "C:\\Users\\eddie\\Desktop\\Ironhack\\MY PROJECTS\\images\\agathe.JPG --batch_thumbnail_maker\n",
      "C:\\Users\\eddie\\Desktop\\Ironhack\\MY PROJECTS\\images\\andy.JPG --batch_thumbnail_maker\n",
      "C:\\Users\\eddie\\Desktop\\Ironhack\\MY PROJECTS\\images\\arek activity 8.1.JPG --batch_thumbnail_maker\n",
      "C:\\Users\\eddie\\Desktop\\Ironhack\\MY PROJECTS\\images\\arek artists.JPG --batch_thumbnail_maker\n",
      "C:\\Users\\eddie\\Desktop\\Ironhack\\MY PROJECTS\\images\\arek2.JPG --batch_thumbnail_maker\n",
      "C:\\Users\\eddie\\Desktop\\Ironhack\\MY PROJECTS\\images\\azure speaker foodie.JPG --batch_thumbnail_maker\n",
      "C:\\Users\\eddie\\Desktop\\Ironhack\\MY PROJECTS\\images\\Capture.JPG --batch_thumbnail_maker\n",
      "C:\\Users\\eddie\\Desktop\\Ironhack\\MY PROJECTS\\images\\Capture1.JPG --batch_thumbnail_maker\n",
      "C:\\Users\\eddie\\Desktop\\Ironhack\\MY PROJECTS\\images\\Capture10.JPG --batch_thumbnail_maker\n",
      "C:\\Users\\eddie\\Desktop\\Ironhack\\MY PROJECTS\\images\\Capture3.JPG --batch_thumbnail_maker\n",
      "C:\\Users\\eddie\\Desktop\\Ironhack\\MY PROJECTS\\images\\Capture6.JPG --batch_thumbnail_maker\n",
      "C:\\Users\\eddie\\Desktop\\Ironhack\\MY PROJECTS\\images\\Capture7.JPG --batch_thumbnail_maker\n",
      "C:\\Users\\eddie\\Desktop\\Ironhack\\MY PROJECTS\\images\\Capture8.JPG --batch_thumbnail_maker\n",
      "C:\\Users\\eddie\\Desktop\\Ironhack\\MY PROJECTS\\images\\Capture9.JPG --batch_thumbnail_maker\n",
      "C:\\Users\\eddie\\Desktop\\Ironhack\\MY PROJECTS\\images\\class_poll.JPG --batch_thumbnail_maker\n",
      "C:\\Users\\eddie\\Desktop\\Ironhack\\MY PROJECTS\\images\\erin.JPG --batch_thumbnail_maker\n",
      "DONE!\n"
     ]
    }
   ],
   "source": [
    "import os, sys\n",
    "from PIL import Image\n",
    "import time\n",
    "\n",
    "original = \"C:\\\\Users\\\\eddie\\\\Desktop\\\\Ironhack\\\\MY PROJECTS\\\\images\\\\\"\n",
    "destination = \"thumbnail_images_destination\"\n",
    "\n",
    "if not os.path.exists(destination):\n",
    "    os.makedirs('batch_thumbnail_maker_images')\n",
    "\n",
    "dirs = os.listdir(original)\n",
    "print(\"BATCH_THUMBNAIL_MAKER\")\n",
    "thumb_width = int(input(\"Please enter the desired Thumbnail width in pixels, and press enter: \"))\n",
    "thumb_height = int(input(\"Please enter the desired Thumbnail height in pixels, and press enter: \"))\n",
    "\n",
    "for file in dirs:\n",
    "    original_image= original + file\n",
    "    print(original_image,\"---converted_to_thumbnail\")\n",
    "    img = Image.open(original_image)\n",
    "    resize = img.resize((thumb_width,thumb_height),Image.ANTIALIAS)\n",
    "    resize.save(\"batch_thumbnail_maker_images/resized\" + file + \".jpg\")\n",
    "\n",
    "\n",
    "t =  time.sleep(2)\n",
    "print(\"DONE!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "320795de",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
