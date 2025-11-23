
import wmi
import copy
from ..SHRMACE_Data import SHRMACEResult
from ..SHRMACE_ErrorBase import SHRMACEException

def get_disk_id() -> None:
    try:
        c = wmi.WMI()
        Disk_ID = ''
        for physical_disk in c.Win32_DiskDrive():
            Disk_ID += physical_disk.SerialNumber + ' '
        SHRMACEResult['DiskID'] = copy.deepcopy(Disk_ID.strip().upper())
    except:
        raise SHRMACEException('SHRMACEException [ERROR.2010] unable to get disk id.')