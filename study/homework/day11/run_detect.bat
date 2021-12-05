python detect.py  ^
--cfg cfg/yolov4-tiny.cfg ^
--weights weights/best.pt ^
--names datasets/faces.names ^
--source imgs/  ^
--img-size 640 ^
--iou-thres 0.2 ^
--conf-thres 0.3 ^
--device 0
