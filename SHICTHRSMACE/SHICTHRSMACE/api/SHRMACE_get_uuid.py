
import wmi
import copy
from ..SHRMACE_Data import SHRMACEResult
from ..SHRMACE_ErrorBase import SHRMACEException

def get_uuid() -> None:
    try:
        c = wmi.WMI()
        for system in c.Win32_ComputerSystemProduct():
            SHRMACEResult['WindowsUUID'] = copy.deepcopy(system.UUID)
    except:
        raise SHRMACEException('SHRMACEException [ERROR.2000] unable to get uuid.')