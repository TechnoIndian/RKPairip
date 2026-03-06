from ..ANSI_COLORS import ANSI; C = ANSI()
from ..MODULES import IMPORT; M = IMPORT()

from importlib.metadata import version

__version__ = version("Pairip")


# ---------------- Set Path ----------------
run_dir = M.os.path.dirname(M.os.path.abspath(M.sys.argv[0]))
script_dir = M.os.path.dirname(M.os.path.abspath(__file__))

files_dir = M.os.path.join(script_dir, "Files")
M.os.makedirs(files_dir, exist_ok=True)


class FileCheck:
    # ---------------- Set Jar & Files Paths ----------------
    def Set_Path(self):
        # ---------------- Jar Tools ----------------
        self.APKEditor_Path, self.APKTool_Path, self.Axml2Xml_Path, self.Pairip_Jar_Path = (
            M.os.path.join(run_dir, jar)
            for jar in ("APKEditor.jar", "APKTool_OR.jar", "Axml2Xml.jar", "Pairip.jar")
        )

        # ---------------- HooK Files ----------------
        self.Objectlogger, self.Pairip_CoreX = (
            M.os.path.join(files_dir, files)
            for files in ("Objectlogger.smali", "lib_Pairip_CoreX.so")
        )


    # ---------------- SHA-256 CheckSum ----------------
    def Calculate_CheckSum(self, file_path):
        sha256_hash = M.hashlib.sha256()
        try:
            with open(file_path, "rb") as f:
                for byte_block in iter(lambda: f.read(4096), b""):
                    sha256_hash.update(byte_block)
            return sha256_hash.hexdigest()
        except FileNotFoundError:
            return None


    # ---------------- Download Files ----------------    
    def Download_Files(self, Jar_Files):

        import requests

        for File_URL, File_Path, Expected_CheckSum in Jar_Files:
            File_Name = M.os.path.basename(File_Path)

            if M.os.path.exists(File_Path):
                if self.Calculate_CheckSum(File_Path) == Expected_CheckSum:
                    continue
                else:
                    print(
                        f"{C.ERROR} {C.C}{File_Name} {C.R}is Corrupt (Checksum Mismatch).  ✘\n"
                        f"\n{C.INFO} Re-Downloading, Need Internet Connection.\n"
                    )

                    M.os.remove(File_Path)

            try:
                Version = requests.get("https://raw.githubusercontent.com/TechnoIndian/RKPairip/main/VERSION").text.strip()

                if Version != str(__version__):
                    print(f"\n{C.S} Updating {C.E}{C.G} RKPairip {C.OG}➸❥ {C.PN}{Version} {C.G}\n\n")

                    if M.os.name == "nt":
                        cmd = "pip install --force-reinstall git+https://github.com/TechnoIndian/RKPairip.git"
                    else:
                        cmd = "pip install --force-reinstall https://github.com/TechnoIndian/RKPairip/archive/refs/heads/main.zip"

                    M.subprocess.run(cmd, shell=isinstance(cmd, str), check=True)

                print(f'\n{C.S} Downloading {C.E} {C.G}{File_Name}')

                with requests.get(File_URL, stream=True) as response:
                    if response.status_code == 200:
                        total_size = int(response.headers.get('content-length', 0))
                        with open(File_Path, 'wb') as f:
                            print(f'       |')
                            for data in response.iter_content(1024 * 64):
                                f.write(data)

                                print(f"\r       {C.CC}╰┈ PS {C.OG}➸❥ {C.G}{f.tell()/(1024*1024):.2f}/{total_size/(1024*1024):.2f} MB ({f.tell()/total_size*100:.1f}%)", end='', flush=True)

                        print('  ✔\n')

                    else:
                        exit(
                            f'\n\n{C.ERROR} Failed to download {C.Y}{File_Name} {C.R}Status Code: {response.status_code}  ✘\n'
                            f'\n{C.INFO} Restart Script...\n'
                        )

            except requests.exceptions.RequestException:
                exit(
                    f'\n\n{C.ERROR} Got an error while Fetching {C.Y}{File_Path}\n'
                    f'\n{C.ERROR} No internet Connection\n'
                    f'\n{C.INFO} Internet Connection is Required to Download {C.Y}{File_Name}\n'
                )


    # ---------------- Files Download Link ----------------
    def F_D(self):

        self.Download_Files(
            [
                (
                    "https://github.com/TechnoIndian/Tools/releases/download/Tools/APKEditor.jar",
                    self.APKEditor_Path,
                    "bec1dd156850df8392c9a45a735b86ae71bc913325ee029ffbb4080a8b41ca1c"
                ),
                (
                    "https://github.com/TechnoIndian/Tools/releases/download/Tools/Pairip.jar",
                    self.Pairip_Jar_Path,
                    "3914376b749a973e8880cbc2f930f3b53dcdf4bd8c8977d0a13b525fcbaad0f2"
                ),
                (
                    "https://raw.githubusercontent.com/TechnoIndian/Objectlogger/main/Objectlogger.smali",
                    self.Objectlogger,
                    "ff31dd1f55d95c595b77888b9606263256f1ed151a5bf5706265e74fc0b46697"
                ),
                (
                    "https://github.com/TechnoIndian/Tools/releases/download/Tools/lib_Pairip_CoreX.so",
                    self.Pairip_CoreX,
                    "22a7954092001e7c87f0cacb7e2efb1772adbf598ecf73190e88d76edf6a7d2a"
                )
            ]
        )

        M.os.system('cls' if M.os.name == 'nt' else 'clear')


    # ---------------- Files Download Link ----------------
    def F_D_A(self):

        self.Download_Files(
            [
                (
                    "https://github.com/TechnoIndian/Tools/releases/download/Tools/APKTool.jar",
                    self.APKTool_Path,
                    "b947b945b4bc455609ba768d071b64d9e63834079898dbaae15b67bf03bcd362"),
                (
                    "https://github.com/TechnoIndian/Tools/releases/download/Tools/Axml2Xml.jar",
                    self.Axml2Xml_Path,
                    "e3a09af1255c703fc050e17add898562e463c87bb90c085b4b4e9e56d1b5fa62"
                )
            ]
        )