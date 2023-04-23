# OpenCV Training Image Thresholding
Global/Binary/Inverse Binary/Truncate/Threshold to Zero/Inverted Threshold Image using OpenCV.

These are the types covered in this repository:

+ Global Thresholding
+ Binary Thresholding
+ Inverse-Binary Thresholding
+ Truncate Thresholding
+ Threshold to Zero
+ Inverted Threshold to Zero

## Contents :
Thresholding therefore has numerous applications in computer vision, and is often performed in the initial stages in  many processing pipelines. There are several types of thresholding algorithms.

| Function        |Action                                                                        |
|----------------:|------------------------------------------------------------------------------|
|cv2.bilateralFilter()   |We apply the filter, that accepts 3 arguments:|
|**src**          | Source image|
|**sigmaColor**       | Defines the spatial extent of the kernel, in both the x and y directions|
|**sigmaSpace**       |Defines the one-dimensional Gaussian distribution.|

## Test Image used: 
I have used test.jpg & bilateral_filtering.jpg that can be found in the repository.

![Source Image Sequence](test.jpg)
![Source Image Sequence](bilateral_filtering.jpg)

## Summary:

```python
#Read image
image = cv2.imread('test.jpg')
```
```python
bilateral_filter = cv2.bilateralFilter(src=image, d=10, sigmaColor=55, sigmaSpace=55)
```



