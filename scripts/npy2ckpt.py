# -*- coding: utf-8 -*-

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import argparse
import tensorflow as tf
from examples.models.lenet import lenet
from examples.models.bvlc_googlenet import googlenet
from examples.models.aesthetics_caffenet import model

if __name__ == '__main__':
    # Let's allow the user to pass the filename as an argument
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_dir", default="../examples/models/lenet/",
                        type=str, help="model files location")
    args = parser.parse_args()
    BATCH_SIZE = 10
    CHANNELS = 3
    RESOLUTION = 227

    IMAGES = tf.placeholder(tf.float32, [BATCH_SIZE, RESOLUTION, RESOLUTION, CHANNELS])
    # LABELS = tf.placeholder(tf.float32, [BATCH_SIZE, 10])
    # NET = lenet.LeNet({'data': IMAGES})
    # NET = googlenet.GoogleNet({'data': IMAGES})
    NET = model.AestheticsCaffe({'data': IMAGES})

    SAVER = tf.train.Saver()
    with tf.Session() as sess:
        # Load the data
        sess.run(tf.initialize_all_variables())
        NET.load(args.model_dir+'model.npy', sess)

        SAVE_PATH = SAVER.save(sess, args.model_dir + 'model.ckpt')
        print "Model saved in file: %s" % SAVE_PATH
