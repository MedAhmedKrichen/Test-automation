# Test-automation

This an automation for computer vision classification testing that help you to: 
  - preprocesse image with (greyscale/rescale/resize) 
  - predict one image classe.
  - evaluate the test set for the chosen model by multiple metrics(categorical crossentropy/F1 score/accuracy/recall/precision).   

## Image Testing:
```
python auto_test_image.py --testimg Img_test/8.jpg --model model.h5 --resize 128 --rescale --classes cat  dog --binary
```
```
--testimg: Image to test
--model: model path
--resize: new size
--rescale: rescale the image
--greyscale: greyscale the image
--classes: all wanted classes
--binary: binary classification
```

## Image Directory Testing:
```
python auto_test_Dir.py --testdir Dir_test --model model.h5 --resize 128 --rescale
```
```
--testdir: Directory of images to test
--model: model path
--resize: new size
--rescale: rescale the image
--greyscale: greyscale the image
```

## The MIT License
### MIT
```
License: MIT
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
```
