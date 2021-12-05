@rem 牛批
@rem 切换到ui所在目录
@cd bigapp\uis
@rem 编译
@pyuic5 -o videoui.py video.ui
@rem 重新切换回原目录
@cd..\..