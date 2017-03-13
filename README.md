# Caffe to pb

This repo uses the code from https://github.com/ethereon/caffe-tensorflow to
convert caffemodel to npy file, and adds more scripts to convert to ckpt, then
to pb file.
There is also a notebook giving example code of how to use a pb file within
a python code.

## Usage :
```
python caffe2npy.py ../examples/models/bvlc_googlenet/deploy.prototxt --caffemodel=../examples/models/bvlc_googlenet/bvlc_googlenet.caffemodel --data-output-path=../examples/models/bvlc_googlenet/googlenet.npy --code-output-path=../examples/models/bvlc_googlenet/googlenet.py
```
