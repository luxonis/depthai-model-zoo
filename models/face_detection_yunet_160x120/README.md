# Face detection YuNet

Model source: [ShiqiYu/libfacedetection](https://github.com/ShiqiYu/libfacedetection)

### Conversion

Model was downloaded from [here](https://github.com/opencv/opencv_zoo/commit/4fb591053ba1201c07c68929cc324787d5afaa6c) (`face_detection_yunet_2022mar.onnx`). It was converted to OpenVINO's IR format with the following command:

```
mo --input_model face_detection_yunet_2022mar.onnx --data_type FP16
```

### Demo

This model is used in [DepthAI face-detection demo](https://github.com/luxonis/depthai-experiments/tree/master/gen2-face-detection).