# SBD-Mask classification model

Model converted from .onnx from [sbdcv/sbd_mask](https://github.com/sbdcv/sbd_mask/tree/41c6730e6837f63c1285a0fb46f4a2143e02b7d2/model).

### Conversion

It was converted to OpenVINO's IR fomrat with the following command:

```
mo --input_model sbd_mask.onnx --data_type=FP16 --mean_values=[0,0,0] --scale_values=[255,255,255] --reverse_input_channels
```

### Turorial

**Tutorial on how to deploy** a custom model (this .onnx) to the OAK camera can be [found here](https://docs.luxonis.com/en/latest/pages/tutorials/deploying-custom-model/#face-mask-recognition-model).