# Mediapipe's Palm detection

This is a converted [Mediapipe's palm detection](https://google.github.io/mediapipe/solutions/hands.html#palm-detection-model) model. Model was converted using [PINTO's tflite2tensorflow](https://github.com/PINTO0309/tflite2tensorflow) tool, which converts tflite models to OpenVINO format (.xml/.bin).

### Demo

- Geaxgx's [Hand tracker](https://github.com/geaxgx/depthai_hand_tracker) app. Runs palm detection and hand landmark model. Optionally decodes hand gestures.
- [Human-machine safety](https://github.com/luxonis/depthai-experiments/tree/master/gen2-human-machine-safety) demo - uses palm detection model to calculate palm's distance to "dangerous" objects and warns users if distance is under the specified threshold