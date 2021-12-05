from distutils.core import setup

setup(
    name="yolov4",
    version="1.0",
    description="我们的人脸登录模块",
    author="Louis Young",
    packages=[
        "yolov4",
        "yolov4.data",
        "yolov4.utils",
    ],
    package_data={
        "yolov4.data":[
            "faces.names",
            "faces.pt",
            "yolov4-tiny.cfg"
        ],
    }
)