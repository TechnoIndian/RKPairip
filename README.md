<p align="center">
<a href="https://t.me/rktechnoindians"><img title="Made in INDIA" src="https://img.shields.io/badge/MADE%20IN-INDIA-SCRIPT?colorA=%23ff8100&colorB=%23017e40&colorC=%23ff0000&style=for-the-badge"></a>
</p>

<a name="readme-top"></a>


# RKPairip


<p align="center"> 
<a href="https://t.me/rktechnoindians"><img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=800&size=35&pause=1000&color=F74848&center=true&vCenter=true&random=false&width=435&lines=RKPairip" /></a>
 </p>

Installation Method
-------

**💢 Requirement PKG 💢**

```bash
termux-setup-storage
pkg update -y
pkg upgrade -y
pkg install python -y
```

**👉🏻 To install RKPairip, Run only any one cmd from the Installation Method**

**💢 PYPI ( Just Testing ) 💢**

    pip install Pairip

[![PyPI](https://img.shields.io/badge/pypi-3776AB?style=for-the-badge&logo=python&logoColor=FFD43B)](https://pypi.org/project/Pairip) [![Version](https://img.shields.io/pypi/v/Pairip?label=&style=for-the-badge&color=FF8C00&labelColor=FF8C00)](https://pypi.org/project/Pairip)


**1st. Method**

`💢 For Latest Commit ( From Main  Branch )  💢`

    pip install --force-reinstall https://github.com/TechnoIndian/RKPairip/archive/refs/heads/main.zip

`OR`

    pip install --force-reinstall https://github.com/TechnoIndian/RKPairip/archive/refs/heads/main.tar.gz

`OR`

    curl -Ls https://github.com/TechnoIndian/Tools/releases/download/Tools/RKPairip.sh | bash

**2nd. Method**

    pkg install python git && pip install --force-reinstall git+https://github.com/TechnoIndian/RKPairip.git


Uninstall RKPairip
-----

    pip uninstall Pairip



# Usage Example


RKPairip ( Input Mode )
-----

**Mode `-i` ➸ Default APKEditor ( Input Your APK Path )**

    RKPairip -i YourApkPath.apk

**Flag: `-a` ➸ Decompile With APKTool**

    RKPairip -i YourApkPath.apk -a

**Flag: `-n` ➸ Pairip New Method By NullRE**

    RKPairip -i YourApkPath.apk -n

**Flag: `-s` ➸ Merge Skip ( Do U Want Last Dex Add Seprate )**

    RKPairip -i YourApkPath.apk -s
    
**Flag `-r` ➸ Pairip Dex Fix ( Try After Translate String to MT )**

    RKPairip -i YourApkPath.apk -r

**Flag: `-x` Hook CoreX ( For Unity / Flutter & Crashed APK )**

    RKPairip -i YourApkPath.apk -x


RKPairip ( Merge Mode )
-----

**Mode `-m` ➸ Anti-Split ( Only Merge APK )**

`Supported Extensions ( .apks / .apkm / .xapk )`

    RKPairip -m YourApkPath.apks


RKPairip ( Credits Mode )
-----

**Mode `-C` ➸ Show Instructions & Credits**

    RKPairip -C


Fix Dex Regex
-------------

**Manually Repair Dex Regexs**


**Patch 1**

`regex`

    (# direct methods\n.method public static )FuckUByRK\(\)V([\s\S]*?.end method)[\w\W]*
    
`Replace`

    $1constructor <clinit>()V$2

**Patch 2**

`regex`

    sget-object v0, L[^;]+;->[^:]*:Ljava/lang/String;\s+const-string v1, ("(\d+.java:\d+)")\s+.line \d+\s+.local v0, "(\d+.java:\d+)":V\s+invoke-static \{v0\}, LRK_TECHNO_INDIA/ObjectLogger;->logstring\(Ljava/lang/Object;\)V
    
`Replace`

    const-string v0, $1

**Patch 3**

`regex`

    invoke-static \{\}, L[^;]+;->callobjects\(\)V\n
    
`Replace`

    # Nothing(Means Empty) 

**Patch 4**

`regex`

    (\.method public.*onReceive\(Landroid/content/Context;Landroid/content/Intent;\)V\s+\.(registers|locals) \d+)[\s\S]*?const-string/jumbo[\s\S]*?(\s+return-void\n.end method)
    
`Replace`

    $1$3


**Patch 5**

`Search 1st without regex`

    pairip
    
`Search regex in Current Results`

    invoke.*pairip/(?!licensecheck/).*

`Replace`

    # Nothing(Means Empty) 


Note
----

## 🇮🇳 Welcome By Techno India 🇮🇳

[![Telegram](https://img.shields.io/badge/TELEGRAM-CHANNEL-red?style=for-the-badge&logo=telegram)](https://t.me/rktechnoindians)
  </a><p>
[![Telegram](https://img.shields.io/badge/TELEGRAM-OWNER-red?style=for-the-badge&logo=telegram)](https://t.me/RK_TECHNO_INDIA)
</p>
