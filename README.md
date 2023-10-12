# DepthAI - Model ZOO

[![Discord](https://img.shields.io/discord/790680891252932659?label=Discord)](https://discord.gg/luxonis)
[![Forum](https://img.shields.io/badge/Forum-discuss-orange)](https://discuss.luxonis.com/)
[![Docs](https://img.shields.io/badge/Docs-DepthAI-yellow)](https://docs.luxonis.com)
[![GitHub](https://img.shields.io/github/license/luxonis/depthai-model-zoo?color=blue&style=flat-square&label=License)](https://github.com/luxonis/depthai-model-zoo/blob/main/LICENSE)
[![web-interface](https://img.shields.io/static/v1?label=Web&message=page&color=orange&style=flat-square)](https://zoo.luxonis.com/)

![DepthAI-Model-Zoo](https://user-images.githubusercontent.com/56075061/141786001-33055085-693f-4a7b-a359-90adb5f3509d.png)


DepthAI Model Zoo is a collection of open-source neural network models and datasets created and maintained by DepthAI developers and the community.

We provide already converted latest state-of-the-art models ready for use with DepthAI and our OAK cameras. Most models are accompanied by additional metadata (FPS, accuracy, number of parameters, and FLOPs) and links to the experiments that show the example usage of each model. Refer to `model.yml` inside each directory fr more information.

Models in DepthAI Model ZOO should expect **BGR color order** and **CHW (planar) channel layout**. You can change these values with [Model Optimizer's](https://docs.openvino.ai/2022.1/openvino_docs_MO_DG_Additional_Optimization_Use_Cases.html) `--layout` and `reverse_input_channels` arguments.

## Usage

To use the models on camera, use [blobconverter](https://github.com/luxonis/blobconverter) API:

1. install `blobconverter` using `pip`:
    ```
    pip install blobconverter
    ```
2. use the following snippet to download a model and get its blob path:
    ```
    model_path = blobconverter.from_zoo(name="yolop_320x320",
                                        zoo_type="depthai",
                                        shaves=6)
    ```

In the example above we use the YOLOP model from the DepthAI Model ZOO. In case you wish to download the model from the [Open Model ZOO](https://github.com/openvinotoolkit/open_model_zoo), you can omit the `zoo_type` flag.


## Additional information

For more information please visit:

* [blobconverter](https://github.com/luxonis/blobconverter) repository for instructions related to the API,
* [blobconverter web interface](https://blobconverter.luxonis.com/) for easy conversion of the models that are not in our model zoo,
* our [documentation](https://docs.luxonis.com/en/latest/) for more information on how to convert and deploy the models.


## Contribute

We invite the community to help out by uploading their models via Pull Requests. Help with performance estimation of the models on our devices is also appreciated.

Thanks to everyone who has already contributed!
