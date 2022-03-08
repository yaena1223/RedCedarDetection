## YOLO Training Environment
### Google Colab setting
1. Make the folder name "yolov4".
2. Upload all the file from here in "yolov4" folder except "yolo_final.ipynb".
3. "yolo_final.ipynb" should be outside of "yolov4" folder.
4. Make the folder name "train" in "yolov4" folder. (Trained weight file will be stored in here)
5. The result should be like this.  
![image](https://user-images.githubusercontent.com/38778937/146697942-0f7795d9-1f2b-4690-b92c-7592299cb91a.png)

### Training
1. Open "yolo_final.ipynb".
2. By executing every line in a row until the row has remark as '#Training'
3. Train over

### Testing 
1. Based the weight file that has been trained, test conducted
2. Upload the test videos and images and get the root. 
3. ex) !./darknet detector demo data/obj.data cfg/yolov4-custom.cfg /mydrive/yolov4/training/yolov4-custom_real_best.weights -dont_show /mydrive/yolov4/MAX_0040.MP4 -thresh 0.5 -i 0 -out_filename /mydrive/yolov4/results5.avi 
    - /mydrive/yolov4/training/yolov4-custom_real_best.weights : weight file that has been trained
    - /mydrive/yolov4/MAX_0040.MP4 : the video that needs to be tested
    - -out_filename /mydrive/yolov4/results5.avi : tested video output as this name
    
