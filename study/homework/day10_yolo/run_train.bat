python train.py ^
--epochs 200  ^
--batch-size 8 ^
--data datasets/coco128.data ^
--cfg cfg/yolov4-tiny.cfg ^
--weights weights/last.pt ^
--name yolov4-tiny ^
--img 640 640 640