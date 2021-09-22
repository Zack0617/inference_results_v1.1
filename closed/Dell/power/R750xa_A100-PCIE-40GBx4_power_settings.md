# Boot/BIOS Firmware Settings

## Idrac settings
Set perf/watt profile inside Dell IDRAC

## Bios setting
  - Set "WorkloadProfile = WriteOnly" in BIOS
  - Set "LogicalProc = Disabled" in BIOS
  - Set "CpuInterconnectBusSpeed = MaxDataRate" in BIOS
  - Set "ProcVirtualization = Enabled" in BIOS
  - Set "DirectoryMode = Enabled" in BIOS
  - Set "ProcAdjCacheLine = Enabled" in BIOS
  - Set "ProcHwPrefetcher = Enabled" in BIOS
  - Set "DcuStreamerPrefetcher = Enabled" in BIOS
  - Set "DcuIpPrefetcher = Enabled" in BIOS
  - Set "SubNumaCluster = Disabled" in BIOS
  - Set "MadtCoreEnumeration = RoundRobin" in BIOS
  - Set "UpiPrefetch = Enabled" in BIOS
  - Set "XptPrefetch = Enabled" in BIOS
  - Set "LlcPrefetch = Enabled" in BIOS
  - Set "DeadLineLlcAlloc = Enabled" in BIOS
  - Set "DirectoryAtoS = Disabled" in BIOS
  - Set "DynamicCoreAllocation = Disabled" in BIOS
  - Set "ProcAvxP1 = Normal" in BIOS
  - Set "ProcessorActivePbf = Disabled" in BIOS
  - Set "ProcessorRaplPrioritization = Disabled" in BIOS
  - Set "ProcX2Apic = Enabled" in BIOS
  - Set "AvxIccpPreGrantLicense = Disabled" in BIOS
  - Set "ProcCores = 32" in BIOS
  - Set "LmceEn = Disabled" in BIOS
  - Set "OptimizerMode = Auto" in BIOS
  - Set "EmbSata = RaidMode" in BIOS
  - Set "NvmeMode = NonRaid" in BIOS
  - Set "BiosNvmeDriver = DellQualifiedDrives" in BIOS
  - Set "BootMode = Uefi" in BIOS
  - Set "BootSeqRetry = Enabled" in BIOS
  - Set "GenericUsbBoot = Disabled" in BIOS
  - Set "HddPlaceholder = Disabled" in BIOS
  - Set "SysPrepClean = None" in BIOS
  - Set "SetBootOrderEn = NIC.PxeDevice.1-1" in BIOS
  - Set "PxeDev1EnDis = Enabled" in BIOS
  - Set "PxeDev2EnDis = Disabled" in BIOS
  - Set "PxeDev3EnDis = Disabled" in BIOS
  - Set "PxeDev4EnDis = Disabled" in BIOS
  - Set "HttpDev1EnDis = Disabled" in BIOS
  - Set "HttpDev2EnDis = Disabled" in BIOS
  - Set "HttpDev3EnDis = Disabled" in BIOS
  - Set "HttpDev4EnDis = Disabled" in BIOS
  - Set "IscsiInitiatorName = None" in BIOS
  - Set "IscsiDev1EnDis = Disabled" in BIOS
  - Set "PxeDev1Interface = NIC.Embedded.1-1-1" in BIOS
  - Set "PxeDev1Protocol = IPv4" in BIOS
  - Set "PxeDev1VlanEnDis = Disabled" in BIOS
  - Set "PxeDev1VlanId = 1" in BIOS
  - Set "PxeDev1VlanPriority = 0" in BIOS
  - Set "IscsiDev1Con1EnDis = Disabled" in BIOS
  - Set "IscsiDev1Con2EnDis = Disabled" in BIOS
  - Set "IscsiDev1ConOrder = Con1Con2" in BIOS
  - Set "IscsiDev1Con1Interface = NIC.Embedded.1-1-1" in BIOS
  - Set "IscsiDev1Con1Protocol = IPv4" in BIOS
  - Set "IscsiDev1Con1VlanEnDis = Disabled" in BIOS
  - Set "IscsiDev1Con1VlanId = 1" in BIOS
  - Set "IscsiDev1Con1VlanPriority = 0" in BIOS
  - Set "IscsiDev1Con1Retry = 3" in BIOS
  - Set "IscsiDev1Con1Timeout = 10000" in BIOS
  - Set "IscsiDev1Con1DhcpEnDis = Disabled" in BIOS
  - Set "IscsiDev1Con1Gateway = None" in BIOS
  - Set "IscsiDev1Con1TgtDhcpEnDis = Disabled" in BIOS
  - Set "IscsiDev1Con2TargetName = None" in BIOS
  - Set "IscsiDev1Con2TargetIp = None" in BIOS
  - Set "IscsiDev1Con2Port = 3260" in BIOS
  - Set "IscsiDev1Con2Lun = 0" in BIOS
  - Set "UsbPorts = AllOn" in BIOS
  - Set "UsbManagedPort = On" in BIOS
  - Set "EmbNic1Nic2 = Enabled" in BIOS
  - Set "IoatEngine = Disabled" in BIOS
  - Set "EmbVideo = Enabled" in BIOS
  - Set "SnoopHldOff = Roll2KCycles" in BIOS
  - Set "SriovGlobalEnable = Disabled" in BIOS
  - Set "OsWatchdogTimer = Disabled" in BIOS
  - Set "PCIRootDeviceUnhide = Disabled" in BIOS
  - Set "MmioAbove4Gb = Enabled" in BIOS
  - Set "MemoryMappedIOH = 12TB" in BIOS
  - Set "DellAutoDiscovery = PlatformDefault" in BIOS
  - Set "Slot3 = Enabled" in BIOS
  - Set "Slot4 = Enabled" in BIOS
  - Set "Slot5 = Enabled" in BIOS
  - Set "Slot6 = Enabled" in BIOS
  - Set "Slot31 = Enabled" in BIOS
  - Set "Slot32 = Enabled" in BIOS
  - Set "Slot33 = Enabled" in BIOS
  - Set "Slot34 = Enabled" in BIOS
  - Set "SerialComm = OnNoConRedir" in BIOS
  - Set "SerialPortAddress = Com1" in BIOS
  - Set "FailSafeBaud = 115200" in BIOS
  - Set "ConTermType = Vt100Vt220" in BIOS
  - Set "RedirAfterBoot = Enabled" in BIOS
  - Set "SysProfile = Custom" in BIOS
  - Set "ProcPwrPerf = OsDbpm" in BIOS
  - Set "MemFrequency = MaxPerf" in BIOS
  - Set "ProcTurboMode = Disabled" in BIOS
  - Set "ProcC1E = Enabled" in BIOS
  - Set "ProcCStates = Enabled" in BIOS
  - Set "MemPatrolScrub = Standard" in BIOS
  - Set "MemRefreshRate = 1x" in BIOS
  - Set "UncoreFrequency = DynamicUFS" in BIOS
  - Set "EnergyPerformanceBias = BalancedPerformance" in BIOS
  - Set "MonitorMwait = Enabled" in BIOS
  - Set "CpuInterconnectBusLinkPower = Enabled" in BIOS
  - Set "PcieAspmL1 = Enabled" in BIOS
  - Set "ProcessorEist = Enabled" in BIOS
  - Set "PasswordStatus = Unlocked" in BIOS
  - Set "MemoryEncryption = Disabled" in BIOS
  - Set "PwrButton = Enabled" in BIOS
  - Set "AcPwrRcvry = Last" in BIOS
  - Set "AcPwrRcvryDelay = Immediate" in BIOS
  - Set "AcPwrRcvryUserDelay = 60" in BIOS
  - Set "UefiVariableAccess = Standard" in BIOS
  - Set "InBandManageabilityInterface = Enabled" in BIOS
  - Set "SmmSecurityMitigation = Enabled" in BIOS
  - Set "SecureBoot = Disabled" in BIOS
  - Set "SecureBootPolicy = Standard" in BIOS
  - Set "SecureBootMode = DeployedMode" in BIOS
  - Set "RedundantOsLocation = None" in BIOS
  - Set "MemTest = Disabled" in BIOS
  - Set "MemOpMode = OptimizerMode" in BIOS
  - Set "NodeInterleave = Disabled" in BIOS
  - Set "MemoryTraining = MemoryTrainingFast" in BIOS
  - Set "CorrEccSmi = Enabled" in BIOS
  - Set "CECriticalSEL = Enabled" in BIOS
  - Set "NumLock = On" in BIOS
  - Set "ErrPrompt = Disabled" in BIOS
  - Set "ForceInt10 = Disabled" in BIOS
  - Set "DellWyseP25BIOSAccess = Enabled" in BIOS
  
## Accelerator power limit setting 
Run the `set_gpu_power.sh` script to set the GPU power constraints 
 