# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""Minimal example of how to read samples from a dataset generated by `generate_pycarbon_dataset.py`
using tensorflow."""

from __future__ import print_function

import argparse
import jnius_config
import tensorflow as tf

from pycarbon.reader import make_reader
from pycarbon.reader import make_tensor, make_dataset

from pycarbon.tests import DEFAULT_CARBONSDK_PATH


def tensorflow_hello_world(dataset_url='file:///tmp/carbon_pycarbon_dataset/'):
  # Example: tf_tensors will return tensors with dataset data
  with make_reader(dataset_url, is_batch=False) as reader:
    tensor = make_tensor(reader)
    with tf.Session() as sess:
      sample = sess.run(tensor)
      print(sample.id)

  with make_reader(dataset_url, is_batch=False) as reader:
    dataset = make_dataset(reader)
    iterator = dataset.make_one_shot_iterator()
    tensor = iterator.get_next()
    with tf.Session() as sess:
      sample = sess.run(tensor)
      print(sample.id)


if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='TensorFlow hello world')
  parser.add_argument('-c', '--carbon-sdk-path', type=str, default=DEFAULT_CARBONSDK_PATH,
                      help='carbon sdk path')

  args = parser.parse_args()

  jnius_config.set_classpath(args.carbon_sdk_path)

  tensorflow_hello_world()
