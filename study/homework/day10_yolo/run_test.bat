python test.py  ^
--data datasets/coco128.data ^
--cfg cfg/yolov4-tiny.cfg ^
--weights weights/best.pt ^
--img 640 ^
--iou-thr 0.6 ^
--conf-thres 0.5 ^
--batch-size 1