# Copyright 2020 MONAI Consortium
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import sys
from collections import OrderedDict

import numpy as np
import torch

import monai

try:
    import ignite

    ignite_version = ignite.__version__
except ImportError:
    ignite_version = "NOT INSTALLED"


def get_config_values():
    """
    Read the package versions into a dictionary.
    """
    output = OrderedDict()

    output["MONAI version"] = monai.__version__
    output["Python version"] = sys.version.replace("\n", " ")
    output["Numpy version"] = np.version.full_version
    output["Pytorch version"] = torch.__version__
    output["Ignite version"] = ignite_version

    return output


def print_config(file=sys.stdout):
    """
    Print the package versions to `file`.
    Defaults to `sys.stdout`.
    """
    for k, v in get_config_values().items():
        print(f"{k}: {v}", file=file, flush=True)


def set_visible_devices(*dev_inds):
    os.environ["CUDA_VISIBLE_DEVICES"] = ",".join(map(str, dev_inds))


def get_torch_version_tuple():
    """
    Returns:
        tuple of ints represents the pytorch major/minor version.
    """
    return tuple([int(x) for x in torch.__version__.split(".")[:2]])
