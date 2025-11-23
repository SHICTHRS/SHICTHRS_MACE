
import wmi
import copy
from ..SHRMACE_Data import SHRMACEResult
from ..SHRMACE_ErrorBase import SHRMACEException

def get_mb_info() -> None:
    try:
        c = wmi.WMI()
        MB_INFO = ''
        for board in c.Win32_BaseBoard():
            MB_INFO = board.Manufacturer + board.Product
        SHRMACEResult['MotherBoardINFO'] = copy.deepcopy(MB_INFO)
    except:
        raise SHRMACEException('SHRMACEException [ERROR.2005] unable to get MotherBoard info.')