# SHICTHRS MACE (Machine Access Control Engine)

[![License: GPL-3.0](https://img.shields.io/badge/License-GPL--3.0-blue.svg)](https://opensource.org/licenses/GPL-3.0)
[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/platform-Windows-lightgrey)](https://www.microsoft.com/windows/)

## 介绍

SHICTHRS MACE (Machine Access Control Engine) 是一个用于获取机器硬件指纹信息的Python库，专为机器身份认证和授权系统设计。该库能够通过多线程并发方式高效获取机器的唯一硬件标识信息，如UUID、CPU ID、主板ID、GPU ID等，为软件授权和设备管理提供可靠的机器身份识别。

## 功能特性

- 🚀 **多线程并发**：采用多线程技术，显著提高硬件信息获取效率
- 🔒 **线程安全**：解决Windows COM组件线程安全问题，避免程序卡死
- ⚙️ **完整硬件信息**：获取包括UUID、CPU、主板、GPU、磁盘、内存和MAC地址在内的完整硬件信息
- 🛡️ **异常处理**：完善的错误处理机制，确保程序稳定运行
- 🔄 **守护线程**：自动管理线程资源，防止资源泄漏
- ⏱️ **超时机制**：内置超时机制，防止硬件操作阻塞主程序

## 安装

### 从源码安装

```bash
git clone https://github.com/JNTMTMTM/SHICTHRS_MACE.git
cd SHICTHRS_MACE/SHICTHRSMACE
pip install -e .
```

### 使用pip安装

```bash
pip install SHICTHRSMACE
```

### 依赖项

- Python 3.6+
- colorama==0.4.6
- pywin32==311
- WMI==1.5.1

## 使用方法

### 基本用法

```python
from SHICTHRSMACE.SHICTHRSMACE import SHRMACE_get_mace_info

# 获取机器硬件信息
result, errors = SHRMACE_get_mace_info()

print("硬件信息:")
print(result)

if errors:
    print(f"以下信息获取失败: {errors}")
```

### 输出示例

```python
{
    'WindowsUUID': '4C4C4544-004A-3110-8056-C4C04F504E32',
    'WindowsProductId': '00330-80000-00000-AA123',
    'CPUINFO': 'Intel(R) Core(TM) i7-9700K CPU @ 3.60GHz',
    'CPUID': 'BFEBFBFF000906EA',
    'CPUVendor': 'GenuineIntel',
    'MotherBoardINFO': 'ASUSTeK COMPUTER INC.PRIME Z390-A',
    'MotherBoardID': 'BASE_BOARD_UUID_HERE',
    'GPUINFO': 'NVIDIA GeForce RTX 2070',
    'GPUID': 'GPU_ID_HERE',
    'DiskINFO': 'Samsung SSD 970 EVO 1TB',
    'DiskID': 'DISK_ID_HERE',
    'MemeroyINFO': '16384MB',
    'MACAddress': '00:1A:2B:3C:4D:5E'
}
```

## 获取的硬件信息

MACE库可以获取以下硬件信息：

| 信息类型 | 描述 | 键名 |
|---------|------|------|
| 系统UUID | Windows系统唯一标识符 | `WindowsUUID` |
| 产品ID | Windows产品ID | `WindowsProductId` |
| CPU信息 | 处理器型号和规格 | `CPUINFO` |
| CPU ID | 处理器唯一标识 | `CPUID` |
| CPU厂商 | 处理器制造商 | `CPUVendor` |
| 主板信息 | 主板制造商和型号 | `MotherBoardINFO` |
| 主板ID | 主板唯一标识 | `MotherBoardID` |
| GPU信息 | 显卡型号和规格 | `GPUINFO` |
| GPU ID | 显卡唯一标识 | `GPUID` |
| 磁盘信息 | 硬盘型号和规格 | `DiskINFO` |
| 磁盘ID | 硬盘唯一标识 | `DiskID` |
| 内存信息 | 内存容量 | `MemeroyINFO` |
| MAC地址 | 网卡物理地址 | `MACAddress` |

## 技术架构

MACE采用模块化设计，主要包含以下组件：

- **核心模块**：`SHRMACE_Data.py` - 数据容器定义
- **调度器**：`SHRMACE_dispatcher.py` - 多线程任务调度
- **硬件API**：独立的硬件信息获取模块
- **异常处理**：`SHRMACE_ErrorBase.py` - 统一异常处理

### 线程安全设计

MACE解决了Windows环境中WMI操作在线程中使用的常见问题：

1. **COM组件初始化**：每个线程中正确初始化和清理COM组件
2. **守护线程设置**：确保主线程结束时资源正确回收
3. **超时机制**：防止硬件操作导致的程序阻塞
4. **线程同步**：使用适当的同步机制避免资源冲突

## 错误处理

MACE提供完整的错误处理机制：

```python
from SHICTHRSMACE.SHICTHRSMACE import SHRMACE_get_mace_info
from SHICTHRSMACE.SHICTHRSMACE.SHRMACE_ErrorBase import SHRMACEException

try:
    result, errors = SHRMACE_get_mace_info()
    # 处理结果
except SHRMACEException as e:
    print(f"获取硬件信息失败: {e}")
```

## 常见问题

### Q: 程序运行时出现"thread._ident is None in _get_related_thread!"错误
A: 这是线程管理问题，MACE已通过守护线程和超时机制解决此问题。

### Q: WMI操作导致程序卡死
A: MACE已实现5秒超时机制，确保即使硬件操作失败，程序也能继续执行。

### Q: "WMI returned a syntax error"错误
A: 这是COM组件未在线程中初始化导致，MACE已在所有WMI操作中添加了适当的COM初始化代码。

## 贡献指南

欢迎提交Issue和Pull Request来改进这个项目。在提交代码前，请确保：

1. 代码符合PEP 8规范
2. 添加适当的注释和文档
3. 通过所有测试
4. 提交信息清晰明了

## 许可证

本项目采用 [GPL-3.0许可证](LICENSE)。

## 作者

**SHICTHRS** - 初始开发 - [GitHub](https://github.com/JNTMTMTM)

## 致谢

感谢所有为这个项目做出贡献的开发者和社区成员。

---

**注意**：本库目前仅支持Windows平台，因为依赖Windows特定的WMI API。未来版本可能会添加对其他平台的支持。