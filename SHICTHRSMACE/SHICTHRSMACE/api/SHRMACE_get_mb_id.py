
import wmi
import copy
from ..SHRMACE_Data import SHRMACEResult
from ..SHRMACE_ErrorBase import SHRMACEException

def get_mb_id() -> None:
    try:
        c = wmi.WMI()
        MB_ID = ''
        for board_id in c.Win32_BaseBoard():
            MB_ID += board_id.SerialNumber + ' '
        SHRMACEResult['MotherBoardID'] = copy.deepcopy(MB_ID.strip().upper())
    except:
        raise SHRMACEException('SHRMACEException [ERROR.2006] unable to get MotherBoard id.')