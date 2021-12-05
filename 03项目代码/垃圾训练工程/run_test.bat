python test.py  ^
--data datasets/garbages.data ^
--cfg cfg/yolov4-tiny.cfg ^
--weights weights/best.pt ^
--img 640 ^
--iou-thr 0.6 ^
--conf-thres 0.3 ^
--batch-size 1