# Copyright (c) 2021, NVIDIA CORPORATION.  All rights reserved.
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

import os
import sys
sys.path.insert(0, os.getcwd())

from code.common.constants import Benchmark, Scenario
from code.common.system_list import System, Architecture, MIGConfiguration, MIGSlice
from configs.configuration import *


@ConfigRegistry.register(HarnessType.LWIS, AccuracyTarget.k_99, PowerSetting.MaxP)
class A100_PCIex1(BenchmarkConfiguration):
    system = System("A100-PCIe", Architecture.Ampere, 1)
    gpu_batch_size = 1
    gpu_copy_streams = 1
    gpu_inference_streams = 1
    input_dtype = "int8"
    input_format = "linear"
    map_path = "data_maps/imagenet/val_map.txt"
    precision = "int8"
    tensor_path = "${PREPROCESSED_DATA_DIR}/imagenet/ResNet50/int8_linear"
    use_graphs = True
    scenario = Scenario.SingleStream
    benchmark = Benchmark.ResNet50
    single_stream_expected_latency_ns = 660000


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99, PowerSetting.MaxP)
class A100_PCIex1_Triton(BenchmarkConfiguration):
    system = System("A100-PCIe", Architecture.Ampere, 1)
    gpu_batch_size = 1
    gpu_copy_streams = 1
    gpu_inference_streams = 1
    input_dtype = "int8"
    input_format = "linear"
    map_path = "data_maps/imagenet/val_map.txt"
    precision = "int8"
    tensor_path = "${PREPROCESSED_DATA_DIR}/imagenet/ResNet50/int8_linear"
    use_graphs = True
    scenario = Scenario.SingleStream
    benchmark = Benchmark.ResNet50
    use_triton = True
    single_stream_expected_latency_ns = 660000


@ConfigRegistry.register(HarnessType.LWIS, AccuracyTarget.k_99, PowerSetting.MaxP)
class A100_PCIe_80GB_aarch64x1(BenchmarkConfiguration):
    system = System("A100-PCIe-80GB", Architecture.Ampere, 1, cpu_arch=CPUArch.aarch64)
    gpu_batch_size = 1
    gpu_copy_streams = 1
    gpu_inference_streams = 1
    input_dtype = "int8"
    input_format = "linear"
    map_path = "data_maps/imagenet/val_map.txt"
    precision = "int8"
    tensor_path = "${PREPROCESSED_DATA_DIR}/imagenet/ResNet50/int8_linear"
    use_graphs = True
    scenario = Scenario.SingleStream
    benchmark = Benchmark.ResNet50
    single_stream_expected_latency_ns = 660000


@ConfigRegistry.register(HarnessType.LWIS, AccuracyTarget.k_99, PowerSetting.MaxP)
class A100_SXM_80GB_MIG_1x1g10gb(BenchmarkConfiguration):
    _mig_configuration = MIGConfiguration({0: {MIGSlice(1, 10): 1}})
    system = System("A100-SXM-80GB", Architecture.Ampere, 1, mig_conf=_mig_configuration)
    gpu_batch_size = 1
    gpu_copy_streams = 1
    gpu_inference_streams = 1
    input_dtype = "int8"
    input_format = "linear"
    map_path = "data_maps/imagenet/val_map.txt"
    precision = "int8"
    tensor_path = "${PREPROCESSED_DATA_DIR}/imagenet/ResNet50/int8_linear"
    start_from_device = True
    use_graphs = True
    scenario = Scenario.SingleStream
    benchmark = Benchmark.ResNet50
    single_stream_expected_latency_ns = 660000


@ConfigRegistry.register(HarnessType.HeteroMIG, AccuracyTarget.k_99, PowerSetting.MaxP)
class A100_SXM_80GB_MIG_1x1g10gb_Hetero(A100_SXM_80GB_MIG_1x1g10gb):
    pass


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99, PowerSetting.MaxP)
class A100_SXM_80GB_MIG_1x1g10gb_Triton(BenchmarkConfiguration):
    _mig_configuration = MIGConfiguration({0: {MIGSlice(1, 10): 1}})
    system = System("A100-SXM-80GB", Architecture.Ampere, 1, mig_conf=_mig_configuration)
    gpu_batch_size = 1
    gpu_copy_streams = 1
    gpu_inference_streams = 1
    input_dtype = "int8"
    input_format = "linear"
    map_path = "data_maps/imagenet/val_map.txt"
    precision = "int8"
    tensor_path = "${PREPROCESSED_DATA_DIR}/imagenet/ResNet50/int8_linear"
    start_from_device = True
    use_graphs = True
    scenario = Scenario.SingleStream
    benchmark = Benchmark.ResNet50
    use_triton = True
    single_stream_expected_latency_ns = 660000


@ConfigRegistry.register(HarnessType.LWIS, AccuracyTarget.k_99, PowerSetting.MaxP)
class A100_SXM_80GB_MIG_56x1g10gb(BenchmarkConfiguration):
    _mig_configuration = MIGConfiguration({
        0: {MIGSlice(1, 10): 7},
        1: {MIGSlice(1, 10): 7},
        2: {MIGSlice(1, 10): 7},
        3: {MIGSlice(1, 10): 7},
        4: {MIGSlice(1, 10): 7},
        5: {MIGSlice(1, 10): 7},
        6: {MIGSlice(1, 10): 7},
        7: {MIGSlice(1, 10): 7},
    })
    system = System("A100-SXM-80GB", Architecture.Ampere, 8, mig_conf=_mig_configuration)
    gpu_batch_size = 1
    gpu_copy_streams = 1
    gpu_inference_streams = 1
    input_dtype = "int8"
    input_format = "linear"
    map_path = "data_maps/imagenet/val_map.txt"
    precision = "int8"
    tensor_path = "${PREPROCESSED_DATA_DIR}/imagenet/ResNet50/int8_linear"
    start_from_device = True
    use_graphs = True
    scenario = Scenario.SingleStream
    benchmark = Benchmark.ResNet50
    single_stream_expected_latency_ns = 660000


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99, PowerSetting.MaxP)
class A100_SXM_80GB_MIG_56x1g10gb_Triton(BenchmarkConfiguration):
    _mig_configuration = MIGConfiguration({
        0: {MIGSlice(1, 10): 7},
        1: {MIGSlice(1, 10): 7},
        2: {MIGSlice(1, 10): 7},
        3: {MIGSlice(1, 10): 7},
        4: {MIGSlice(1, 10): 7},
        5: {MIGSlice(1, 10): 7},
        6: {MIGSlice(1, 10): 7},
        7: {MIGSlice(1, 10): 7},
    })
    system = System("A100-SXM-80GB", Architecture.Ampere, 8, mig_conf=_mig_configuration)
    gpu_batch_size = 1
    gpu_copy_streams = 1
    gpu_inference_streams = 1
    input_dtype = "int8"
    input_format = "linear"
    map_path = "data_maps/imagenet/val_map.txt"
    precision = "int8"
    tensor_path = "${PREPROCESSED_DATA_DIR}/imagenet/ResNet50/int8_linear"
    start_from_device = True
    use_graphs = True
    scenario = Scenario.SingleStream
    benchmark = Benchmark.ResNet50
    use_triton = True
    single_stream_expected_latency_ns = 660000


@ConfigRegistry.register(HarnessType.LWIS, AccuracyTarget.k_99, PowerSetting.MaxP)
class A100_SXM_80GBx1(BenchmarkConfiguration):
    system = System("A100-SXM-80GB", Architecture.Ampere, 1)
    gpu_batch_size = 1
    gpu_copy_streams = 1
    gpu_inference_streams = 1
    input_dtype = "int8"
    input_format = "linear"
    map_path = "data_maps/imagenet/val_map.txt"
    precision = "int8"
    tensor_path = "${PREPROCESSED_DATA_DIR}/imagenet/ResNet50/int8_linear"
    start_from_device = True
    use_graphs = True
    scenario = Scenario.SingleStream
    benchmark = Benchmark.ResNet50
    single_stream_expected_latency_ns = 660000


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99, PowerSetting.MaxP)
class A100_SXM_80GBx1_Triton(BenchmarkConfiguration):
    system = System("A100-SXM-80GB", Architecture.Ampere, 1)
    gpu_batch_size = 1
    gpu_copy_streams = 1
    gpu_inference_streams = 1
    input_dtype = "int8"
    input_format = "linear"
    map_path = "data_maps/imagenet/val_map.txt"
    precision = "int8"
    tensor_path = "${PREPROCESSED_DATA_DIR}/imagenet/ResNet50/int8_linear"
    start_from_device = True
    use_graphs = True
    scenario = Scenario.SingleStream
    benchmark = Benchmark.ResNet50
    use_triton = True
    single_stream_expected_latency_ns = 660000


@ConfigRegistry.register(HarnessType.LWIS, AccuracyTarget.k_99, PowerSetting.MaxP)
class A100_SXM4_40GB_MIG_1x1g5gb(BenchmarkConfiguration):
    _mig_configuration = MIGConfiguration({0: {MIGSlice(1, 5): 1}})
    system = System("A100-SXM4-40GB", Architecture.Ampere, 1, mig_conf=_mig_configuration)
    gpu_batch_size = 1
    gpu_copy_streams = 1
    gpu_inference_streams = 1
    input_dtype = "int8"
    input_format = "linear"
    map_path = "data_maps/imagenet/val_map.txt"
    precision = "int8"
    tensor_path = "${PREPROCESSED_DATA_DIR}/imagenet/ResNet50/int8_linear"
    start_from_device = True
    use_graphs = True
    scenario = Scenario.SingleStream
    benchmark = Benchmark.ResNet50
    single_stream_expected_latency_ns = 660000


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99, PowerSetting.MaxP)
class A100_SXM4_40GB_MIG_1x1g5gb_Triton(BenchmarkConfiguration):
    _mig_configuration = MIGConfiguration({0: {MIGSlice(1, 5): 1}})
    system = System("A100-SXM4-40GB", Architecture.Ampere, 1, mig_conf=_mig_configuration)
    gpu_batch_size = 1
    gpu_copy_streams = 1
    gpu_inference_streams = 1
    input_dtype = "int8"
    input_format = "linear"
    map_path = "data_maps/imagenet/val_map.txt"
    precision = "int8"
    tensor_path = "${PREPROCESSED_DATA_DIR}/imagenet/ResNet50/int8_linear"
    start_from_device = True
    use_graphs = True
    scenario = Scenario.SingleStream
    benchmark = Benchmark.ResNet50
    use_triton = True
    single_stream_expected_latency_ns = 660000


@ConfigRegistry.register(HarnessType.LWIS, AccuracyTarget.k_99, PowerSetting.MaxP)
class A100_SXM4_40GBx1(BenchmarkConfiguration):
    system = System("A100-SXM4-40GB", Architecture.Ampere, 1)
    gpu_batch_size = 1
    gpu_copy_streams = 1
    gpu_inference_streams = 1
    input_dtype = "int8"
    input_format = "linear"
    map_path = "data_maps/imagenet/val_map.txt"
    precision = "int8"
    tensor_path = "${PREPROCESSED_DATA_DIR}/imagenet/ResNet50/int8_linear"
    start_from_device = True
    use_graphs = True
    scenario = Scenario.SingleStream
    benchmark = Benchmark.ResNet50
    single_stream_expected_latency_ns = 660000


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99, PowerSetting.MaxP)
class A100_SXM4_40GBx1_Triton(BenchmarkConfiguration):
    system = System("A100-SXM4-40GB", Architecture.Ampere, 1)
    gpu_batch_size = 1
    gpu_copy_streams = 1
    gpu_inference_streams = 1
    input_dtype = "int8"
    input_format = "linear"
    map_path = "data_maps/imagenet/val_map.txt"
    precision = "int8"
    tensor_path = "${PREPROCESSED_DATA_DIR}/imagenet/ResNet50/int8_linear"
    start_from_device = True
    use_graphs = True
    scenario = Scenario.SingleStream
    benchmark = Benchmark.ResNet50
    use_triton = True
    single_stream_expected_latency_ns = 660000


@ConfigRegistry.register(HarnessType.LWIS, AccuracyTarget.k_99, PowerSetting.MaxP)
class A10x1(BenchmarkConfiguration):
    system = System("A10", Architecture.Ampere, 1)
    gpu_batch_size = 1
    gpu_copy_streams = 1
    gpu_inference_streams = 1
    input_dtype = "int8"
    input_format = "linear"
    map_path = "data_maps/imagenet/val_map.txt"
    precision = "int8"
    tensor_path = "${PREPROCESSED_DATA_DIR}/imagenet/ResNet50/int8_linear"
    use_graphs = True
    scenario = Scenario.SingleStream
    benchmark = Benchmark.ResNet50
    single_stream_expected_latency_ns = 450000


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99, PowerSetting.MaxP)
class A10x1_Triton(BenchmarkConfiguration):
    system = System("A10", Architecture.Ampere, 1)
    gpu_batch_size = 1
    gpu_copy_streams = 1
    gpu_inference_streams = 1
    input_dtype = "int8"
    input_format = "linear"
    map_path = "data_maps/imagenet/val_map.txt"
    precision = "int8"
    tensor_path = "${PREPROCESSED_DATA_DIR}/imagenet/ResNet50/int8_linear"
    use_graphs = True
    scenario = Scenario.SingleStream
    benchmark = Benchmark.ResNet50
    use_triton = True
    single_stream_expected_latency_ns = 450000


@ConfigRegistry.register(HarnessType.LWIS, AccuracyTarget.k_99, PowerSetting.MaxP)
class A30_MIG_1x1g6gb(BenchmarkConfiguration):
    _mig_configuration = MIGConfiguration({0: {MIGSlice(1, 6): 1}})
    system = System("A30", Architecture.Ampere, 1, mig_conf=_mig_configuration)
    gpu_batch_size = 1
    gpu_copy_streams = 1
    gpu_inference_streams = 1
    input_dtype = "int8"
    input_format = "linear"
    map_path = "data_maps/imagenet/val_map.txt"
    precision = "int8"
    tensor_path = "${PREPROCESSED_DATA_DIR}/imagenet/ResNet50/int8_linear"
    use_graphs = True
    scenario = Scenario.SingleStream
    benchmark = Benchmark.ResNet50
    single_stream_expected_latency_ns = 715769


@ConfigRegistry.register(HarnessType.HeteroMIG, AccuracyTarget.k_99, PowerSetting.MaxP)
class A30_MIG_1x1g6gb_Hetero(A30_MIG_1x1g6gb):
    single_stream_expected_latency_ns = 746040


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99, PowerSetting.MaxP)
class A30_MIG_1x1g6gb_Triton(BenchmarkConfiguration):
    _mig_configuration = MIGConfiguration({0: {MIGSlice(1, 6): 1}})
    system = System("A30", Architecture.Ampere, 1, mig_conf=_mig_configuration)
    gpu_batch_size = 1
    gpu_copy_streams = 1
    gpu_inference_streams = 1
    input_dtype = "int8"
    input_format = "linear"
    map_path = "data_maps/imagenet/val_map.txt"
    precision = "int8"
    tensor_path = "${PREPROCESSED_DATA_DIR}/imagenet/ResNet50/int8_linear"
    use_graphs = False
    scenario = Scenario.SingleStream
    benchmark = Benchmark.ResNet50
    use_triton = True
    single_stream_expected_latency_ns = 861136


@ConfigRegistry.register(HarnessType.LWIS, AccuracyTarget.k_99, PowerSetting.MaxP)
class A30_MIG_32x1g6gb(BenchmarkConfiguration):
    _mig_configuration = MIGConfiguration({
        0: {MIGSlice(1, 6): 4},
        1: {MIGSlice(1, 6): 4},
        2: {MIGSlice(1, 6): 4},
        3: {MIGSlice(1, 6): 4},
        4: {MIGSlice(1, 6): 4},
        5: {MIGSlice(1, 6): 4},
        6: {MIGSlice(1, 6): 4},
        7: {MIGSlice(1, 6): 4},
    })
    system = System("A30", Architecture.Ampere, 8, mig_conf=_mig_configuration)
    gpu_batch_size = 1
    gpu_copy_streams = 1
    gpu_inference_streams = 1
    input_dtype = "int8"
    input_format = "linear"
    map_path = "data_maps/imagenet/val_map.txt"
    precision = "int8"
    tensor_path = "${PREPROCESSED_DATA_DIR}/imagenet/ResNet50/int8_linear"
    use_graphs = True
    scenario = Scenario.SingleStream
    benchmark = Benchmark.ResNet50
    single_stream_expected_latency_ns = 817316


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99, PowerSetting.MaxP)
class A30_MIG_32x1g6gb_Triton(BenchmarkConfiguration):
    _mig_configuration = MIGConfiguration({
        0: {MIGSlice(1, 6): 4},
        1: {MIGSlice(1, 6): 4},
        2: {MIGSlice(1, 6): 4},
        3: {MIGSlice(1, 6): 4},
        4: {MIGSlice(1, 6): 4},
        5: {MIGSlice(1, 6): 4},
        6: {MIGSlice(1, 6): 4},
        7: {MIGSlice(1, 6): 4},
    })
    system = System("A30", Architecture.Ampere, 8, mig_conf=_mig_configuration)
    gpu_batch_size = 1
    gpu_copy_streams = 1
    gpu_inference_streams = 1
    input_dtype = "int8"
    input_format = "linear"
    map_path = "data_maps/imagenet/val_map.txt"
    precision = "int8"
    tensor_path = "${PREPROCESSED_DATA_DIR}/imagenet/ResNet50/int8_linear"
    use_graphs = False
    scenario = Scenario.SingleStream
    benchmark = Benchmark.ResNet50
    use_triton = True
    single_stream_expected_latency_ns = 861136


@ConfigRegistry.register(HarnessType.LWIS, AccuracyTarget.k_99, PowerSetting.MaxP)
class A30x1(BenchmarkConfiguration):
    system = System("A30", Architecture.Ampere, 1)
    gpu_batch_size = 1
    gpu_copy_streams = 1
    gpu_inference_streams = 1
    input_dtype = "int8"
    input_format = "linear"
    map_path = "data_maps/imagenet/val_map.txt"
    precision = "int8"
    tensor_path = "${PREPROCESSED_DATA_DIR}/imagenet/ResNet50/int8_linear"
    use_graphs = True
    scenario = Scenario.SingleStream
    benchmark = Benchmark.ResNet50
    single_stream_expected_latency_ns = 660000


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99, PowerSetting.MaxP)
class A30x1_Triton(BenchmarkConfiguration):
    system = System("A30", Architecture.Ampere, 1)
    gpu_batch_size = 1
    gpu_copy_streams = 1
    gpu_inference_streams = 1
    input_dtype = "int8"
    input_format = "linear"
    map_path = "data_maps/imagenet/val_map.txt"
    precision = "int8"
    tensor_path = "${PREPROCESSED_DATA_DIR}/imagenet/ResNet50/int8_linear"
    use_graphs = False
    scenario = Scenario.SingleStream
    benchmark = Benchmark.ResNet50
    use_triton = True
    single_stream_expected_latency_ns = 498000


@ConfigRegistry.register(HarnessType.LWIS, AccuracyTarget.k_99, PowerSetting.MaxP)
class AGX_Xavier(BenchmarkConfiguration):
    system = System("AGX_Xavier", Architecture.Xavier, 1, cpu_arch=CPUArch.aarch64)
    gpu_batch_size = 1
    gpu_copy_streams = 2
    gpu_inference_streams = 1
    input_dtype = "int8"
    input_format = "linear"
    map_path = "data_maps/imagenet/val_map.txt"
    precision = "int8"
    tensor_path = "${PREPROCESSED_DATA_DIR}/imagenet/ResNet50/int8_linear"
    use_graphs = True
    scenario = Scenario.SingleStream
    benchmark = Benchmark.ResNet50
    single_stream_expected_latency_ns = 2273000


@ConfigRegistry.register(HarnessType.LWIS, AccuracyTarget.k_99, PowerSetting.MaxQ)
class AGX_Xavier_MaxQ(BenchmarkConfiguration):
    system = System("AGX_Xavier", Architecture.Xavier, 1, cpu_arch=CPUArch.aarch64)
    gpu_batch_size = 1
    gpu_copy_streams = 2
    gpu_inference_streams = 1
    input_dtype = "int8"
    input_format = "linear"
    map_path = "data_maps/imagenet/val_map.txt"
    precision = "int8"
    tensor_path = "${PREPROCESSED_DATA_DIR}/imagenet/ResNet50/int8_linear"
    use_graphs = True
    scenario = Scenario.SingleStream
    benchmark = Benchmark.ResNet50
    single_stream_expected_latency_ns = 2273000


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99, PowerSetting.MaxP)
class AGX_Xavier_Triton(BenchmarkConfiguration):
    system = System("AGX_Xavier", Architecture.Xavier, 1, cpu_arch=CPUArch.aarch64)
    gpu_batch_size = 1
    gpu_copy_streams = 2
    gpu_inference_streams = 1
    input_dtype = "int8"
    input_format = "linear"
    map_path = "data_maps/imagenet/val_map.txt"
    precision = "int8"
    tensor_path = "${PREPROCESSED_DATA_DIR}/imagenet/ResNet50/int8_linear"
    use_graphs = True
    scenario = Scenario.SingleStream
    benchmark = Benchmark.ResNet50
    use_triton = True
    single_stream_expected_latency_ns = 2273000


@ConfigRegistry.register(HarnessType.LWIS, AccuracyTarget.k_99, PowerSetting.MaxP)
class T4x1(BenchmarkConfiguration):
    system = System("T4", Architecture.Turing, 1)
    gpu_batch_size = 1
    gpu_copy_streams = 1
    gpu_inference_streams = 1
    input_dtype = "int8"
    input_format = "linear"
    map_path = "data_maps/imagenet/val_map.txt"
    precision = "int8"
    tensor_path = "${PREPROCESSED_DATA_DIR}/imagenet/ResNet50/int8_linear"
    use_graphs = True
    scenario = Scenario.SingleStream
    benchmark = Benchmark.ResNet50
    single_stream_expected_latency_ns = 996648


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99, PowerSetting.MaxP)
class T4x1_Triton(BenchmarkConfiguration):
    system = System("T4", Architecture.Turing, 1)
    gpu_batch_size = 1
    gpu_copy_streams = 1
    gpu_inference_streams = 1
    input_dtype = "int8"
    input_format = "linear"
    map_path = "data_maps/imagenet/val_map.txt"
    precision = "int8"
    tensor_path = "${PREPROCESSED_DATA_DIR}/imagenet/ResNet50/int8_linear"
    use_graphs = True
    scenario = Scenario.SingleStream
    benchmark = Benchmark.ResNet50
    use_triton = True
    single_stream_expected_latency_ns = 996648


@ConfigRegistry.register(HarnessType.LWIS, AccuracyTarget.k_99, PowerSetting.MaxP)
class Xavier_NX(BenchmarkConfiguration):
    system = System("Xavier_NX", Architecture.Xavier, 1, cpu_arch=CPUArch.aarch64)
    gpu_batch_size = 1
    gpu_copy_streams = 2
    gpu_inference_streams = 1
    input_dtype = "int8"
    input_format = "linear"
    map_path = "data_maps/imagenet/val_map.txt"
    precision = "int8"
    tensor_path = "${PREPROCESSED_DATA_DIR}/imagenet/ResNet50/int8_linear"
    use_graphs = True
    scenario = Scenario.SingleStream
    benchmark = Benchmark.ResNet50
    single_stream_expected_latency_ns = 4546000


@ConfigRegistry.register(HarnessType.LWIS, AccuracyTarget.k_99, PowerSetting.MaxQ)
class Xavier_NX_MaxQ(BenchmarkConfiguration):
    system = System("Xavier_NX", Architecture.Xavier, 1, cpu_arch=CPUArch.aarch64)
    gpu_batch_size = 1
    gpu_copy_streams = 2
    gpu_inference_streams = 1
    input_dtype = "int8"
    input_format = "linear"
    map_path = "data_maps/imagenet/val_map.txt"
    precision = "int8"
    tensor_path = "${PREPROCESSED_DATA_DIR}/imagenet/ResNet50/int8_linear"
    use_graphs = True
    scenario = Scenario.SingleStream
    benchmark = Benchmark.ResNet50
    single_stream_expected_latency_ns = 4546000


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99, PowerSetting.MaxP)
class Xavier_NX_Triton(BenchmarkConfiguration):
    system = System("Xavier_NX", Architecture.Xavier, 1, cpu_arch=CPUArch.aarch64)
    gpu_batch_size = 1
    gpu_copy_streams = 2
    gpu_inference_streams = 1
    input_dtype = "int8"
    input_format = "linear"
    map_path = "data_maps/imagenet/val_map.txt"
    precision = "int8"
    tensor_path = "${PREPROCESSED_DATA_DIR}/imagenet/ResNet50/int8_linear"
    use_graphs = True
    scenario = Scenario.SingleStream
    benchmark = Benchmark.ResNet50
    use_triton = True
    single_stream_expected_latency_ns = 4546000
