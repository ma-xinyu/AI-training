from distutils.core import setup

setup(
    name="garbage_yolov4",
    version="1.0",
    description="垃圾识别模块",
    author="Martin maxinyu",
    packages=[
        "garbage_yolov4",
        "garbage_yolov4.data",
        "garbage_yolov4.utils",
    ],
    package_data={
        "garbage_yolov4.data":[
            "garbages.names",
            "garbages.pt",
            "yolov4-tiny.cfg"
        ],
    }
)