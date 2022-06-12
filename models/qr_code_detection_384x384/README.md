# WeChat QR code detector

Model converted from .onnx from [opencv_zoo/qrcode_wechatqrcode](https://github.com/opencv/opencv_zoo/tree/4fb591053ba1201c07c68929cc324787d5afaa6c/models/qrcode_wechatqrcode). DepthAI demo with this model can be found [here](https://github.com/luxonis/depthai-experiments/tree/master/gen2-qr-code-scanner)


### Conversion

It was converted to OpenVINO's IR fomrat with the following command:

```
mo --input_model detect_2021nov.caffemodel --scale 255 --data_type FP16
```

### Turorial

**Tutorial on how to deploy** a custom model (the .caffemodel) to the OAK camera can be [found here](https://docs.luxonis.com/en/latest/pages/tutorials/deploying-custom-model/#qr-code-detector).