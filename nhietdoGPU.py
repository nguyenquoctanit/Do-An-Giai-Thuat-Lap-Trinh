import pynvml
import time

info = 71
while info > 70:
    # handle = pynvml.nvmlDeviceGetHandleByIndex(0)
    # info = pynvml.nvmlDeviceGetTemperature(handle, pynvml.NVML_TEMPERATURE_GPU)
    # print(f"GPU 0: {info} độ C")
    handle = pynvml.nvmlDeviceGetHandleByIndex(1)
    info = pynvml.nvmlDeviceGetTemperature(handle, pynvml.NVML_TEMPERATURE_GPU)
    print(f"GPU 1: {info} độ C")
    time.sleep(3)