
import subprocess
import copy
from ..SHRMACE_Data import SHRMACEResult
from ..SHRMACE_ErrorBase import SHRMACEException

def get_mem_info() -> None:
    try:
        command = 'wmic memorychip get Manufacturer, PartNumber, SerialNumber, Capacity, Speed, DeviceLocator, MemoryType, FormFactor'
        output = subprocess.check_output(
            command, 
            shell=True, 
            text=True, 
            stderr=subprocess.STDOUT,
            encoding='utf-8'
        )
        lines = [line.strip() for line in output.split('\n') if line.strip()]
        if len(lines) < 2:
            return []
        
        headers = [h.strip() for h in lines[0].split() if h.strip()]
        modules = []
        
        for line in lines[1:]:
            values = [v.strip() for v in line.split(None, len(headers) - 1)]
            if len(values) != len(headers):
                continue
                
            module_info = dict(zip(headers, values))
            modules.append(module_info)
        
        SHRMACEResult['MemeroyINFO'] = copy.deepcopy(modules)

    except:
        raise SHRMACEException('SHRMACEException [ERROR.2011] unable to get memory info.')