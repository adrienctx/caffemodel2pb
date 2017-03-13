# Caffe to pb

## Usage :
```
python caffe2npy.py ../examples/models/lenet/lenet.prototxt --caffemodel=../examples/models/lenet/lenet_iter_10000.caffemodel --data-output-path=../examples/models/lenet/lenet.npy --code-output-path=../examples/models/lenet/lenet.py

python caffe2npy.py ../examples/models/aesthetics_caffenet/deploy.prototxt --caffemodel=../examples/models/aesthetics_caffenet/aesthetics_caffenet.caffemodel --data-output-path=../examples/models/aesthetics_caffenet/model.npy --code-output-path=../examples/models/aesthetics_caffenet/model.py

python caffe2npy.py ../examples/models/bvlc_googlenet/deploy.prototxt --caffemodel=../examples/models/bvlc_googlenet/bvlc_googlenet.caffemodel --data-output-path=../examples/models/bvlc_googlenet/googlenet.npy --code-output-path=../examples/models/bvlc_googlenet/googlenet.py

python caffe2npy.py ../examples/models/SqueezeNet_v1.0/deploy.prototxt --caffemodel=../examples/models/SqueezeNet_v1.0/squeezenet_v1.0.caffemodel --data-output-path=../examples/models/SqueezeNet_v1.0/squeezenet.npy --code-output-path=../examples/models/SqueezeNet_v1.0/squeezenet.py

python caffe2npy.py ../examples/models/SqueezeNetRes/trainval.prototxt --caffemodel=../examples/models/SqueezeNetRes/SqueezeNet_residual_top1_0.6038_top5_0.8250.caffemodel --data-output-path=../examples/models/SqueezeNetRes/squeezenetres.npy --code-output-path=../examples/models/SqueezeNetRes/squeezenetres.py
```
