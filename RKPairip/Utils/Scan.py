from ..ANSI_COLORS import ANSI; C = ANSI()
from ..MODULES import IMPORT; M = IMPORT()

from .Files_Check import FileCheck

F = FileCheck(); F.Set_Path();


# ---------------- Scan APK ----------------
def Scan_Apk(apk_path):

    print(f"\n{C.CC}{'_' * 61}\n")

    Package_Name = ''

    isPairip = License_Check = App_Name = False


    # ---------------- Extract Package Name with AAPT ----------------
    if M.os.name == 'posix':
        Package_Name = M.subprocess.run(
            ['aapt', 'dump', 'badging', apk_path],
            capture_output=True, text=True
        ).stdout.split("package: name='")[1].split("'")[0]

        if Package_Name:
            print(f"\n{C.S} Package Name {C.E} {C.OG}➸❥ {C.P}'{C.G}{Package_Name}{C.P}' {C.G} ✔")
 
 
        # ---------------- Match Application & License  ----------------
        A_N, L_C = '"com.pairip.application.Application"', '"com.pairip.licensecheck.LicenseActivity"'

        manifest = M.subprocess.run(
            ['aapt', 'dump', 'xmltree', apk_path, 'AndroidManifest.xml'],
            capture_output=True, text=True
        ).stdout

        App_Name = A_N in manifest

        if App_Name:
            print(f"\n\n{C.S} Application Name {C.E} {C.OG}➸❥ {C.P}'{C.G}{A_N[1:-1]}{C.P}' {C.G} ✔")

        else:
            License_Check = L_C in manifest

            if License_Check:
                print(f"\n\n{C.S} License Check {C.E} {C.OG}➸❥ {C.P}'{C.G}{L_C[1:-1]}{C.P}' {C.G} ✔")


    # ---------------- Extract Package Name with APKEditor ----------------
    if not Package_Name:
        Package_Name = M.subprocess.run(
            ["java", "-jar", F.APKEditor_Path, "info", "-package", "-i", apk_path],
            capture_output=True, text=True
        ).stdout.split('"')[1]

        print(f"\n{C.S} Package Name {C.E} {C.OG}➸❥ {C.P}'{C.G}{Package_Name}{C.P}' {C.G} ✔")


    # ---------------- Check for APK protections ----------------
    Detect_Protection = []
    with M.zipfile.ZipFile(apk_path, 'r') as zip_ref:
        for item in zip_ref.infolist():
            if item.filename.startswith('lib/'):
                if item.filename.endswith('libpairipcore.so'):
                    print(f"\n\n{C.S} Pairip Protection {C.E} {C.OG}➸❥ {C.P}'{C.G}Google加固{C.P}' {C.G} ✔")
                    isPairip = True
                    break
        
    if not any([App_Name, isPairip, License_Check]):
        exit(f"\n{C.ERROR} Your APK Has No Pairip Protection  ✘\n")


    # ---------------- Check Flutter / Unity Protection ----------------
    isDex = []
    isUnity = isFlutter = False

    with M.zipfile.ZipFile(apk_path, 'r') as zip_ref:
        for item in zip_ref.infolist():
            if item.filename.startswith('lib/'):
                if item.filename.endswith('libunity.so'):
                    isUnity = True
                if item.filename.endswith('libflutter.so'):
                    isFlutter = True

            elif item.filename.startswith("classes") and item.filename.endswith('.dex'):
                isDex.append(item.filename)

        Methods = Fields = 0

        if isDex:
            try:
                data = zip_ref.open(isDex[-1], 'r').read()

                Methods = int.from_bytes(data[88:91], "little")

                Fields = int.from_bytes(data[80:83], "little")

            except (OSError, ValueError, KeyError, M.zipfile.BadZipFile) as e:
                print(f"\n\n{C.WARN} {e}, Skipping Methods & Fields Count.")

    if isUnity:
        print(
            f"\n\n{C.S} Unity Protection {C.E} {C.OG}➸❥ {C.P}'{C.G}libunity.so{C.P}' {C.G} ✔\n"
            f"\n{C.WARN} This is {C.G}Unity + Pairip {C.B}APK. Completely removing Pairip may not be possible unless you can bypass the libpairipcore.so check from Unity libraries."
        )

    if isFlutter:
        print(f"\n\n{C.S} Flutter Protection {C.E} {C.OG}➸❥ {C.P}'{C.G}libflutter.so{C.P}' {C.G} ✔")

    if Methods and Fields:
        print(f"\n\n{C.S} Last Dex Total {C.E} {C.OG}➸❥ {C.C}Methods: {C.PN}{Methods} {C.OG}➸❥ {C.C}Field: {C.PN}{Fields} {C.G} ✔")

    else:
        pass

    return Package_Name, License_Check, isFlutter