## `palm_detection_128x128` decoding

This model decodes the [palm_detection_128x128](https://github.com/luxonis/depthai-model-zoo/tree/main/models/palm_detection_128x128), so everything can run on the edge. It was taken from [geaxgx/depthai_hand_tracker](https://github.com/geaxgx/depthai_hand_tracker/tree/main/custom_models).

It returns only the TOP 10 most confident results. Inference takes about 4ms (measured with depthai tracing).