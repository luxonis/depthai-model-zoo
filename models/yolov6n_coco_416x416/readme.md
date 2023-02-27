# YoloV6n, COCO 416x416

Nano version of YoloV6, Trained on COCO 80 dataset, input size of 416x416.

YoloV6 is **anchorless**, meaning your [config.json](config.json) can look like this:

```
{
    "model": {
        "bin": "yolov6n_coco_416x416.bin",
        "xml": "yolov6n_coco_416x416.xml"
    },
    "nn_config":
    {
        "output_format" : "detection",
        "NN_family" : "YOLO",
        "input_size": "416x416",
        "NN_specific_metadata" :
        {
            "classes" : 80,
            "coordinates" : 4,
            "anchors" : [], # No anchors!
            "anchor_masks" : {}, # No anchors!
            "iou_threshold" : 0.5,
            "confidence_threshold" : 0.5
        }
    },
    "mappings":
    {
        "labels":
        [...]
    }
}

```