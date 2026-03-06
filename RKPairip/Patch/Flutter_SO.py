from ..ANSI_COLORS import ANSI; C = ANSI()
from ..MODULES import IMPORT; M = IMPORT()


# ---------------- Download libflutter.so ----------------
def Flutter_SO(apk_path, isFlutter):

    import requests

    Arch, Flutter_Libs = set(), []
    
    with M.zipfile.ZipFile(apk_path, 'r') as zip_ref:
        for item in zip_ref.infolist():
            if item.filename.startswith('lib/'):
                if item.filename.endswith('libflutter.so'):
                    Flutter_Libs.append(item.filename)
                if "arm64-v8a" in item.filename:
                    Arch.add("arm64-v8a")
                elif "armeabi-v7a" in item.filename:
                    Arch.add("armeabi-v7a")

        if isFlutter:
            print(
                f"\n{C.CC}{'_' * 61}\n\n"
                f"\n{C.WARN} This is {C.G}Flutter + Pairip {C.B}APK, So For Pairip Bypass, Need Replace {C.P}'{C.G}libflutter.so{C.P}' {C.B}in Your APK Arch"
            )

            for lib in Flutter_Libs:
                with zip_ref.open(lib) as so_file:
                    read = so_file.read().decode('ascii', errors='ignore').replace('\x00', '')

                    if " (stable)" in read:
                        version_code = M.re.findall(r'\d+\.\d+\.\d+', read[:read.find(" (stable)")])[-1]
                    else:
                        version_code = "Unknown"

                    print(f"\n\n{C.S} Flutter Dart Version {C.E} {C.OG}➸❥  {C.G}{version_code}  ✔")
                    break

            if version_code == "Unknown":
                print(f"\n\n{C.INFO} {C.B}Version Not Founded in {C.P}'{C.G}libflutter.so{C.P}'")
                return

            URLS = []

            if "arm64-v8a" in Arch:
                URLS.append(
                    (
                        f"https://github.com/TechnoIndian/Flutter-SO-Build/releases/download/v{version_code}/libflutter_so_arm64.zip",
                        M.os.path.join(
                            M.os.path.dirname(apk_path),
                            "libflutter_so_arm64.zip"
                        )
                    )
                )

            if "armeabi-v7a" in Arch:
                URLS.append(
                    (
                        f"https://github.com/TechnoIndian/Flutter-SO-Build/releases/download/v{version_code}/libflutter_so_armeabi_v7a.zip", 
                        M.os.path.join(
                            M.os.path.dirname(apk_path),
                            "libflutter_so_armeabi_v7a.zip"
                        )
                    )
                )

            for File_URL, File_Path in URLS:
                File_Name = M.os.path.basename(File_Path)

                try:
                    print(f'\n\n{C.S} Downloading {C.E} {C.Y}{File_Name}')
                    
                    with requests.get(File_URL, stream=True) as response:
                        if response.status_code == 200:
                            total_size = int(response.headers.get('content-length', 0))
                            with open(File_Path, 'wb') as f:
                                print(f'       |')
                                for data in response.iter_content(1024 * 64):
                                    f.write(data)

                                    print(f"\r       {C.CC}╰┈ PS {C.OG}➸❥ {C.G}{f.tell()/(1024*1024):.2f}/{total_size/(1024*1024):.2f} MB ({f.tell()/total_size*100:.1f}%)", end='', flush=True)

                            print('  ✔')

                        else:
                            print(
                                f'\n\n{C.ERROR} Download Failed {C.Y}{File_Name} {C.R}| Status Code: {response.status_code}  ✘\n'
                                f'\n{C.INFO} Please Download Manually\n'
                                f'    |\n    {C.CC}╰┈ URL {C.OG}➸❥ {C.G}{File_URL}'
                            )

                except requests.exceptions.RequestException:
                    print(
                        f'\n\n{C.ERROR} No Internet Connection  ✘\n'
                        f'\n{C.INFO} Internet Connection is Required to Download\n'
                        f'    |\n    {C.CC}╰┈ URL {C.OG}➸❥ {C.G}{File_URL}'
                    )