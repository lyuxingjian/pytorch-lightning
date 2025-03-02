# Copyright The PyTorch Lightning team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import torch
from torchmetrics.functional import mean_absolute_error as _mean_absolute_error

from pytorch_lightning.utilities.deprecation import deprecated


@deprecated(target=_mean_absolute_error, ver_deprecate="1.3.0", ver_remove="1.5.0")
def mean_absolute_error(preds: torch.Tensor, target: torch.Tensor) -> torch.Tensor:
    """
    .. deprecated::
        Use :func:`torchmetrics.functional.mean_absolute_error`. Will be removed in v1.5.0.
    """
