import imageio
import os
# can also optimize gif image through ezgif optimizer

#------clip path goes here----------------
clip = os.path.abspath('test_clip.mp4')
print(clip)

#gifmaker function
def makeGIF(inputPath, targetFormat):
    outputPath = os.path.splitext(inputPath)[0] + targetFormat    
    print(f'converting {inputPath} \n to {outputPath}')
    
    reader = imageio.get_reader(inputPath)
    fps = reader.get_meta_data()['fps']
    
    writer = imageio.get_writer(outputPath, fps = fps)
    for frames in reader:
        writer.append_data(frames)
        print(f'Frames{frames}')
    
    print('Finished')
    writer.close()
    
#call function
makeGIF(clip,'.gif')

