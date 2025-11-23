
import subprocess
import copy
from ..SHRMACE_Data import SHRMACEResult
from ..SHRMACE_ErrorBase import SHRMACEException

def get_gpu_id() -> None:
    try:
        output = subprocess.check_output('wmic path win32_VideoController get PNPDeviceID' , shell=True, text=True, stderr=subprocess.STDOUT)
        lines = output.strip().split('\n')
        if len(lines) > 1:
            device_id = lines[-1]
            SHRMACEResult['GPUID'] = copy.deepcopy(device_id)
    except:
        raise SHRMACEException('SHRMACEException [ERROR.2008] unable to get GPU id.')