# Face recognition MobileFaceNet ArcFace

:bell: **The model is available for non-commercial research purposes only.** (As specified [here](https://github.com/deepinsight/insightface/blob/master/model_zoo/README.md))

Model converted from [deepinsight/insightface](https://github.com/deepinsight/insightface) - See their license!

### Conversion

Model was downloaded from [here](https://github.com/deepinsight/insightface/blob/master/model_zoo/README.md#list-of-models-by-mxnet-and-paddlepaddle) (`MFN (mxnet) - MS1MV1`). It was converted to OpenVINO's IR format with the following command:

```
mo --input_model=model-0000.params --input_shape=[1,3,112,112] --reverse_input_channels --data_type=FP16
```

### Demo

This model is used in [DepthAI face-recognition demo](https://github.com/luxonis/depthai-experiments/tree/master/gen2-face-recognition).