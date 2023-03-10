An implementational list of some important image dataset processing operations.

1. [bing_image_downloader.ipynb](https://github.com/yes-its-shivam/image-processing-scripts/blob/main/bing_image_downloader.ipynb): download images from bing.com
2. [cropimage_cv2.ipynb](https://github.com/yes-its-shivam/image-processing-scripts/blob/main/cropimage_cv2.ipynb): crop image
3. [ind2sub.py](https://github.com/yes-its-shivam/image-processing-scripts/blob/main/ind2sub.py): linear index  of matrix to subscript index
   # ```linear index of a matrix to subscript index
   # |00 01 02|    |01 02 03| 
   # |04 05 06| -> |10 11 12|
   # |07 08 09|    |20 21 22|```

4. [splitter.py](https://github.com/yes-its-shivam/image-processing-scripts/blob/main/splitter.py): split image into parts of image\
  # split image into smaller segments of images 
  #            |00 01 02 03| 
  # image ->   |10 11 12 13| 
  #            |20 21 22 23|    
  #            |30 31 32 33|    

  #            |00 01|  |02 03|
  #            |10 11|  |12 13|
  # splitted-> 
  #            |20 21|  |22 23|
  #            |30 31|  |32 33|
5. [sub2ind.py](https://github.com/yes-its-shivam/image-processing-scripts/blob/main/sub2ind.py): subscript index  of matrix to linear index
  # subscript index of a matrix to linear index
  # |00 01 02|    |01 02 03|
  # |10 11 12| -> |04 05 06|
  # |20 21 22|    |07 08 09|
6. [selenium_img_screenshot_colab.ipynb](https://github.com/yes-its-shivam/image-processing-scripts/blob/main/selenium_img_screenshot_colab.ipynb): screenshot image using selenium

7. [urllib_image_download.ipynb](https://github.com/yes-its-shivam/image-processing-scripts/blob/main/urllib_image_download.ipynb): download image from url
