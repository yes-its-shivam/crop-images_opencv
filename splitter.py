#split image into smaller segments of images 
#            |00 01 02 03| 
# image ->   |10 11 12 13| 
#            |20 21 22 23|    
#            |30 31 32 33|    

#            |00 01|  |02 03|
#            |10 11|  |12 13|
# splitted-> 
#            |20 21|  |22 23|
#            |30 31|  |32 33|
import numpy as np
from PIL import Image

def splitter(path,name):
    pieces = []
    M = 50
    N = 50
    for i in name:
        im = np.array(Image.open(path+'/'+i).convert('RGB'))
        im = np.array(im).astype('float16')
        im = im / 255 - 0.5
        tiles = [im[x:x+M,y:y+N] for x in range(0,im.shape[0],M) for y in range(0,im.shape[1],N)]
        pieces.append(tiles)
    return np.array(pieces)