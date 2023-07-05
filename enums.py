from enum import Enum, auto

class NovellAsset(Enum):
    SHY=auto()
    IEF=auto()
    TLT=auto()
    TIP=auto()
    LQD=auto()
    HYG=auto()
    BWX=auto()
    EMB=auto()

class BAACanaryAsset(Enum):
    SPY=auto()
    VEA=auto()
    VWO=auto()
    BND=auto()

class BAAAggroAsset(Enum):
    QQQ=auto()
    VEA=auto()
    VWO=auto()
    BND=auto()

class BAASafeAsset(Enum):
    TIP=auto()
    PDBC=auto()
    IEF=auto()
    TLT=auto()
    LQD=auto()
    BND=auto()

class HAACanaryAsset(Enum):
    TIP=auto()

class HAAAggroAsset(Enum):
    SPY=auto()
    IWM=auto()
    VEA=auto()
    VWO=auto()
    VNQ=auto()
    PDBC=auto()
    IEF=auto()
    TLT=auto()

class HAASafeAsset(Enum):
    IEF=auto()