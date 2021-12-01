# DepthAI - Model ZOO
[![GitHub](https://img.shields.io/github/license/luxonis/depthai-model-zoo?color=blue&style=flat-square&label=LICENSE)](https://github.com/luxonis/depthai-model-zoo/blob/main/LICENSE) [![stars](https://img.shields.io/github/stars/luxonis?affiliations=OWNER&label=LUXONIS%20STARS&style=flat-square)](https://github.com/luxonis) [![maintained](https://img.shields.io/maintenance/yes/2021?label=MAINTAINED&style=flat-square)](https://zoo.luxonis.com/) [![web-interface](https://img.shields.io/static/v1?label=WEB&message=INTERFACE&color=orange&style=flat-square)](https://zoo.luxonis.com/)

![DepthAI-Model-Zoo](https://user-images.githubusercontent.com/56075061/141786001-33055085-693f-4a7b-a359-90adb5f3509d.png)



DepthAI Model Zoo is a collection of open-source neural network models and datasets created and maintained by DepthAI developers and the community. A web interface for easier navigation is available at [zoo.luxonis.com](zoo.luxonis.com).

We try to provide already converted latest state-of-the-art models ready for use with DepthAI and our OAK cameras. Most models are accompanied by additional metadata (FPS, accuracy, number of parameters, and FLOPs) and links to the experiments that show the example usage of each model.



## Usage

You can download each model from our [web interface](https://zoo.luxonis.com/). Alternatively, you can use the [blobconverter](https://github.com/luxonis/blobconverter) API:

1. install `blobconverter` using `pip`:
    ```
    pip install blobconverter
    ```
2. use the following snippet to download the YOLOP model and get its blob path:
    ```
    model_path = blobconverter.from_zoo(name="yolop_320x320",
                                        zoo_type="depthai",
                                        shaves=6)
    model_path = str(model_path)
    ```

In the example above we use the YOLOP model from the DepthAI Model ZOO. In case you wish to download the model from the OpenVINO ZOO, you can omit the `zoo_type` flag. 



## Additional information

For more information please visit:

* [blobconverter](https://github.com/luxonis/blobconverter) repository for more information on how to use the API,
* [blobconverter web interface](https://blobconverter.luxonis.com/) for easy conversion of the models that are not in our model zoo,
* our [documentation](https://docs.luxonis.com/en/latest/) for more information on how to convert and deploy the models.



## Contribute

We invite the community to help out by uploading their models via Pull Requests. Help with performance estimation of the models on our devices is also appreciated.

Thanks to everyone who has already contributed!

#### Contributors

[![Contributors](https://contrib.rocks/image?repo=luxonis/depthai-model-zoo)](https://github.com/luxonis/depthai-model-zoo/graphs/contributors)
