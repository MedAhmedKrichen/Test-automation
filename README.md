# Test-automation


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
