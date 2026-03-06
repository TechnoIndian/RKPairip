from .CLI import parse_arguments
from .ANSI_COLORS import ANSI; C = ANSI()
from .MODULES import IMPORT; M = IMPORT()

from RKPairip.Utils.CRC import CRC_Fix
from RKPairip.Utils.Credits import Credits
from RKPairip.Utils.Scan import Scan_Apk
from RKPairip.Utils.DexLib import DexLib2_Logged
from RKPairip.Utils.Anti_Splits import Anti_Split, Check_Split
from RKPairip.Utils.Files_Check import FileCheck, __version__
from RKPairip.Utils.Extract import Extract_Smali, Logs_Injected
from RKPairip.Utils.Decompile_Compile import Decompile_Apk, Recompile_Apk, FixSigBlock

from RKPairip.Patch.Flutter_SO import Flutter_SO
from RKPairip.Patch.Smali_Patch import Smali_Patch
from RKPairip.Patch.Pairip_CoreX import Check_CoreX, Hook_Core, Delete_SO
from RKPairip.Patch.Fix_Dex import Scan_Application, Smali_Patcher, Replace_Strings
from RKPairip.Patch.Manifest_Patch import Patch_Manifest, Replace_Application, Encode_Manifest
from RKPairip.Patch.Other_Patch import Application_Name, Translate_Smali_Name, Merge_Smali_Folders, UnMerge


def Clear():
    M.os.system('cls' if M.os.name == 'nt' else 'clear')
Clear()


# ---------------- Install Require Module ---------------
required_modules = ['requests', 'multiprocess']
for module in required_modules:
    try:
        __import__(module)
    except ImportError:
        print(f"{C.S} Installing {C.E} {C.OG}➸❥ {C.G}{module}...\n")
        try:
            M.subprocess.check_call([M.sys.executable, "-m", "pip", "install", module])
            Clear()
        except (M.subprocess.CalledProcessError, Exception):
            exit(
                f"\n{C.ERROR} No Internet Connection.  ✘\n"
                f"\n{C.INFO} Internet Connection is Required to Install {C.G} pip install {module}\n"
            )


# ---------------- Check Dependencies ----------------
def check_dependencies():
    try:
        M.subprocess.run(['java', '-version'], check=True, text=True, capture_output=True)
    except (M.subprocess.CalledProcessError, FileNotFoundError):
        if M.os.name == 'posix':
            install_package('openjdk-17')
        else:
            exit(
                f'\n\n{C.ERROR} Java is not installed on Your System.  ✘\n'
                f'\n{C.INFO} Install Java & Run Script Again in New CMD.  ✘\n'
                f'\n{C.INFO} Verify Java Installation {C.G} java --version\n'
            )

    if M.os.name == 'posix': install_package('aapt')


# ---------------- Install Package ----------------
def install_package(pkg):
    try:
        result = M.subprocess.run(['pkg', 'list-installed'], capture_output=True, text=True, check=True)
        if pkg not in result.stdout:
            print(f"{C.S} Installing {C.E} {C.OG}➸❥ {C.G}{pkg}...\n")
            M.subprocess.check_call(['pkg', 'install', '-y', pkg])
            Clear()
    except (M.subprocess.CalledProcessError, Exception):
        exit(
            f"\n\n{C.ERROR} No Internet Connection.  ✘\n"
            f"\n{C.INFO} Internet Connection is Required to Installation {C.G} pkg install {pkg}\n"
        )

check_dependencies()


F = FileCheck(); F.Set_Path(); F.F_D()

Date = M.datetime.now().strftime('%d/%m/%y')

print(f"{C.OG}{f'v{__version__}':>22}")


# Logo ( 🙏 )
b64 = """eJzVlc1KAzEQx8/NK3gZwl6FWvELL9YPcCnUUgsiPZRSFy02LVRzEHooKnpRqVTxJOJZ0IMXQcQXUPARtPXkxT6CSTbJJttW1Juz2/3I/zeTmcluF0DYQHaIDGSHxydHJmPRGOlc7F+z3y0seaVChXiWPkamt+TARIxkvMJauQJueaWYZ6NR7YtQJALUNwSmUeoEZomW0qVzMZQoyOkHjQS4k+XTyzThA7ocSMXdtJuC6eVUfHFRxevifxDSwewSG2cTwQoQOJWjYlCnznkIIzx2D4Lal0FLsd9DdpA8tSfRqZlpWnpQsj6HltPBxsZFtuJBitQBuVGRhL/ODBPhjFI4Sh0aDAoAKY3a6ar2qUcG2Q+VQLnJ6QwVCWeMTZyC9fD5KuuCDMBj2eHZPdPMRvBJIBQVyZUxQocgqakq1ezYCGzhYkps1N9lPq5y68+Bet4ivUX9SnSau9vwdnT5cXXe2j2GTnOvAZ939+2d/dZp4/2uDq+PZ/By8/Tw3EzwA7/n7w1q1U967rV+wvf7X9x+4WOhyOrBKEnmicdrkr2p2WrGK3mr1TzRRC3kvrCUnEuH/LU4m9/0/n2/Qv/L7fqB+WFo1w9F9TX1IRkhU9X1TUEUOVDe6NLTiVxmbmY+uZBzk7NuXHToCwiuFdA="""
print(f"{M.zlib.decompress(M.base64.b64decode(b64)).decode('utf-8').rstrip('\n')} | {C.B}{Date}{C.CC}")
print("————————|——————————————————|—————————————————|——————————————|————")


# ---------------- Target All Classes Folder ----------------
def Find_Smali_Folders(decompile_dir, isAPKTool, Fix_Dex):

    smali_path = decompile_dir if isAPKTool or Fix_Dex else M.os.path.join(decompile_dir, "smali")

    prefix = "smali_classes" if isAPKTool or Fix_Dex else "classes"

    folders = sorted([f for f in M.os.listdir(smali_path) if f == "smali" or f.startswith(prefix)], key=lambda x: int(x.split(prefix)[-1]) if x.split(prefix)[-1].isdigit() else 0)
    
    return [M.os.path.join(smali_path, f) for f in folders]


# ---------------- Target Last Classes Folder ----------------
def L_S_C_F(decompile_dir, isAPKTool, Fix_Dex):

    smali_folders = Find_Smali_Folders(decompile_dir, isAPKTool, Fix_Dex)

    return smali_folders[-1] if smali_folders else None


# ---------------- Execute Main Function ----------------
def RK_Techno_IND():

    args = parse_arguments()

    M_Skip = args.MergeSkip

    CoreX_Hook = args.Hook_CoreX; isCoreX = False

    isAPKTool = args.ApkTool; Fix_Dex = args.Repair_Dex


    if args.Credits_Instruction:
        Credits()
    
    if isAPKTool or Fix_Dex: F.F_D_A()
    
    apk_path = args.input or args.Merge

    if not M.os.path.isfile(apk_path):
        exit(f"\n{C.ERROR}  APK file '{apk_path}' not found.  ✘\n")

    apk_path = Anti_Split(apk_path, args.Merge, CoreX_Hook)


    # ---------------- Set All Paths Directory ----------------
    decompile_dir = M.os.path.join(M.os.path.expanduser("~"), f"{M.os.path.splitext(M.os.path.basename(apk_path))[0]}_decompiled")

    build_dir = M.os.path.abspath(M.os.path.join(M.os.path.dirname(apk_path), f"{M.os.path.splitext(M.os.path.basename(apk_path))[0]}_Pairip.apk"))

    rebuild_dir = build_dir.replace('_Pairip.apk', '_Patched.apk')

    manifest_path = M.os.path.join(decompile_dir, 'AndroidManifest.xml')

    d_manifest_path = M.os.path.join(decompile_dir, 'AndroidManifest_d.xml')

    mtd_path = "/sdcard/MT2/dictionary/"


    C_Line = f"{C.CC}{'_' * 61}"

    Logo = f'\n🚩 {C.CC}࿗ {C.OG}Jai Shree Ram {C.CC}࿗ 🚩\n     🛕🛕🙏🙏🙏🛕🛕\n'

    START = f'\n{C.S}  Time Spent  {C.E} {C.OG}➸❥ {C.PN}'

    END = f'{C.CC} Seconds\n'


    if M.os.name == 'posix':
        M.subprocess.run(['termux-wake-lock'])

        print(f"\n{C.X} {C.C} Acquiring Wake Lock...\r")

    start_time = M.time.time()


    # ---------------- Scan & Decompile APK ---------------
    Package_Name, License_Check, isFlutter = Scan_Apk(apk_path)

    if input and isFlutter:
        Flutter_SO(apk_path, isFlutter)

    if args.NullRE:
        DexLib2_Logged(apk_path)
    else:
        Decompile_Apk(apk_path, decompile_dir, isAPKTool, Fix_Dex)


    # ---------------- Last Smali Folder & All Smali Folder ---------------
    L_S_F = L_S_C_F(decompile_dir, isAPKTool, Fix_Dex)

    smali_folders = Find_Smali_Folders(decompile_dir, isAPKTool, Fix_Dex)


    # ---------------- Fix Dex Flag: -r ---------------
    if Fix_Dex:
        try:
            App_Name = Scan_Application(apk_path, manifest_path, d_manifest_path, Fix_Dex)

            if App_Name:
                Super_Value = Application_Name(L_S_F)

                print(f'\n{C.S}  APPLICATION  {C.E} {C.OG}➸❥ {C.G}{Super_Value}  ✔\n')

                Replace_Application(manifest_path, d_manifest_path, Super_Value, App_Name, isAPKTool, Fix_Dex)

                Encode_Manifest(decompile_dir, manifest_path, d_manifest_path)

            else:
                M.os.remove(d_manifest_path)
                pass

            Smali_Patcher(smali_folders, L_S_F); build_dir = rebuild_dir

            Recompile_Apk(decompile_dir, Fix_Dex, build_dir, isFlutter)

            M.shutil.rmtree(decompile_dir)

            print(
                START
                + f'{M.time.time() - start_time:.2f}' +
                END
            )

            print(Logo)

            if M.os.name == 'posix':
                M.subprocess.run(['termux-wake-unlock'])

                exit(f"\n{C.X} {C.C} Releasing Wake Lock...\n")

            exit(0)

        except Exception as e:
            exit(f"\n{C.ERROR} {e}  ✘\n")


    # ---------------- Extract Target Smali & Logs Inject ---------------
    if not (CoreX_Hook or License_Check):
        Extract_Smali(decompile_dir, smali_folders, isAPKTool)

    L_S_F = L_S_C_F(decompile_dir, isAPKTool, Fix_Dex)

    if not (CoreX_Hook or License_Check):
        Logs_Injected(L_S_F)

        Super_Value = Application_Name(L_S_F)

        OR_App = f'\n{C.S}  APPLICATION  {C.E} {C.OG}➸❥ {C.G}{Super_Value}  ✔\n'

        smali_folders = Find_Smali_Folders(decompile_dir, isAPKTool, Fix_Dex)


    # ---------------- Hook CoreX ---------------
    if CoreX_Hook and Check_CoreX(decompile_dir, isAPKTool):
        M.shutil.rmtree(decompile_dir);

        exit(1)

    Smali_Patch(smali_folders, CoreX_Hook, isCoreX)

    if CoreX_Hook or isCoreX:
        Hook_Core(args.input, decompile_dir, isAPKTool, Package_Name)

    if not isAPKTool:
        d_manifest_path = manifest_path


    # ---------------- Patch Manifest ---------------
    Patch_Manifest(decompile_dir, manifest_path, d_manifest_path, isAPKTool, L_S_F, CoreX_Hook, isFlutter, isCoreX)

    if isAPKTool:
        Encode_Manifest(decompile_dir, manifest_path, d_manifest_path)
    
    if not (CoreX_Hook or License_Check):
        # ---------------- Merge Smali ---------------
        if M_Skip:
            print(f"\n{C.INFO} {C.G} Skip Merge Last Dex {C.Y}{M.os.path.basename(L_S_F)} {C.G} & Add Seprate (For Dex Redivision)\n")
            pass
        else:
            Merge_Smali_Folders(decompile_dir, isAPKTool, L_S_F)

        if L_S_C_F(decompile_dir, isAPKTool, Fix_Dex):
            Translate_Smali = Translate_Smali_Name(M.os.path.basename(L_S_C_F(decompile_dir, isAPKTool, Fix_Dex)), isAPKTool)


    # ---------------- Recompile APK ---------------
    Recompile_Apk(decompile_dir, isAPKTool, build_dir, isFlutter)

    if CoreX_Hook or License_Check:
        CRC_Fix(M_Skip, apk_path, build_dir, ["AndroidManifest.xml", ".dex"])

        M.shutil.rmtree(decompile_dir)

        print(f"{C_Line}\n\n"
            + START +
            f'{M.time.time() - start_time:.2f}'
            + END +
            f'\n{Logo}'
        )

        if M.os.name == 'posix':
            M.subprocess.run(['termux-wake-unlock'])

            exit(f"\n{C.X} {C.C} Releasing Wake Lock...\n")

        exit(0)


    # ---------------- CRCFix ---------------
    Final_Apk = CRC_Fix(M_Skip, apk_path, build_dir, ["AndroidManifest.xml", ".dex"])

    if isAPKTool:
        FixSigBlock(decompile_dir, apk_path, build_dir, rebuild_dir)

    print(f'\n{C.S}  Final APK  {C.E} {C.OG}➸❥ {C.Y} {Final_Apk}  {C.G}✔\n')

    elapsed_time = M.time.time() - start_time

    print(
        f"{C_Line}\n\n"
        f"\n{C.S}  Last Dex  {C.E} {C.OG}➸❥ {C.P}'{C.G}{M.os.path.basename(Translate_Smali)}{C.P}' {C.Y}( Translate with MT )  {C.G}✔\n"
    )


    # ---------------- APPLICATION NAME ---------------
    print(OR_App)

    print(START + f'{elapsed_time:.2f}' + END + f"\n{C_Line}\n")

    if M.os.path.exists(mtd_path):
        mtd_files = [
            file 
            for file in M.os.listdir(mtd_path) 
            if file.startswith(Package_Name) and file.endswith('.mtd')
        ]

        for mtd_file in mtd_files:
            M.os.remove(M.os.path.join(mtd_path, mtd_file))

    print(f'\n{C.INFO} {C.G} If U Want Repair Dex Without Translate, So Generate {C.OG} ".mtd" {C.G} First & put the {C.OG} ".mtd" {C.G} in the path of {C.Y}"/sdcard/MT2/dictionary/"{C.G}, if {C.OG} ".mtd" {C.G} available in target path then The Script will handle Automatically, So Press Enter 🤗🤗\n')

    while True:
        UnMerge_input = input(f"\n{C.X} {C.C} Do U Want Repair Dex ( Press Enter To Proceed or 'q' to exit or 'm' to More Info ) | Hook If APK Crash Then Try with 'x'\n{C.G}  |\n  └──── {C.CC}~{C.G}$ : {C.Y}").strip().lower()

        if UnMerge_input == 'q':
            M.shutil.rmtree(decompile_dir)

            print(
                f"\n{C_Line}\n\n"
                f"\n{C.INFO} {C.C} Now you have to manually Translate the Last Dex with MT & again input with -r Flag the Command {C.G}( Copy Below Command & Run After Translate Dex )"
                f"\n{C.G}  |\n  └──── {C.CC}~{C.G}${C.Y}  RKPairip -i {build_dir} {C.OG}-r\n"
                f"\n{C_Line}\n"
            )

            break

        elif UnMerge_input == 'm':

            print(
                f'\n{C_Line}\n\n'
                f'\n{C.S} MORE INFO {C.E} {C.G} - To generate {C.OG} ".mtd" {C.G} file, first install the {C.OG}“{M.os.path.basename(build_dir)}”{C.G} in Multi App / Dual Space & save the {C.OG} ".mtd" {C.G} in {C.Y}"/sdcard/MT2/dictionary/{C.OG}{Package_Name}....mtd"\n'
                f'\n{C.NOTE} {C.G} - if you are use ROOT or VM so {C.OG} ".mtd" {C.G} will generated in path of {C.Y}"/data/data/{Package_Name}/dictionary/{C.OG}{Package_Name}....mtd", {C.G} then you just move {C.OG} ".mtd" {C.G} file to path of {C.Y}"/sdcard/MT2/dictionary/{C.OG}{Package_Name}....mtd"\n'
                f'\n{C.INFO} {C.G} - The script will handle it automatically if the {C.OG} ".mtd" {C.G} file exists in the target path.\n'
            )

            continue

        elif UnMerge_input == 'x' and not (CoreX_Hook or Check_CoreX(decompile_dir, isAPKTool) or Check_Split(args.input, isCoreX = True)):

            isCoreX = True

            print(
                f"\n{C_Line}\n\n"
                f"\n{C.INFO} {C.C}Hook lib_Pairip_CoreX.so & loadLibrary in VMRunner Class."
                f"{C.G}\n    |\n    └──── {C.CC}~{C.G}${C.Y} This Hook Work in Some Apk Like Flutter/Unity & Try on Crash Apk."
                f"{C.G}\n    |\n    └──── {C.CC}~{C.G}${C.Y} Note Some Time This Apk Working Directly with Sign When Directly Working Hook Then why need Bypass Pairip, because u can also modify dex in Apk."
                f"{C.G}\n    |\n    └──── {C.CC}~{C.G}${C.Y} Still U want Bypass Pairip then Dump '.mtd' & Press Enter ( for mtd dump Use  Multi_App cuz Storage Permission not added in Apk )\n"
                f"\n{C_Line}\n"
            )
            
            Smali_Patch(smali_folders, CoreX_Hook, isCoreX)

            Patch_Manifest(decompile_dir, manifest_path, d_manifest_path, isAPKTool, L_S_F, CoreX_Hook, isFlutter, isCoreX)

            Hook_Core(args.input, decompile_dir, isAPKTool, Package_Name)

            Recompile_Apk(decompile_dir, isAPKTool, build_dir, isFlutter)


            # ---------------- CRCFix ---------------
            CRC_Fix(M_Skip, apk_path, build_dir, ["AndroidManifest.xml", ".dex"])

            if isAPKTool:
                FixSigBlock(decompile_dir, apk_path, build_dir, rebuild_dir)

            continue

        else:
            print(f"\n{C_Line}")

            if UnMerge:
                mtd_files = None

                while True:
                    if M.os.path.exists(mtd_path):
                        mtd_files = [
                            file 
                            for file in M.os.listdir(mtd_path) 
                            if file.startswith(Package_Name) and file.endswith('.mtd')
                        ]

                        if not mtd_files:
                            print(f"\n\n{C.WARN} {C.OG} '{Package_Name}....mtd' {C.G} File Not Found in {C.Y}{mtd_path} {C.R} ✘\n")

                        else:
                            if not M_Skip: UnMerge()

                            mtd_file = max(mtd_files, key=lambda file: M.os.path.getmtime(M.os.path.join(mtd_path, file)))

                            print(
                                f"\n{C.S} Founded {C.E} {C.OG}➸❥ {C.G}{mtd_file}  ✔\n"
                                f"\n{C_Line}\n"
                            )

                            break

                    else:
                        print(f"\n\n{C.WARN} No such directory found: {C.Y}{mtd_path}{C.OG}{Package_Name}....mtd\n")

                    user_input = input(f"\n{C.S} Input {C.E}{C.C} If You Want To Retry, Press Enter & Exit To Script {C.P}'q' : {C.Y}")

                    if user_input.lower() == 'q':
                        break


                # ---------------- Restore Strings ---------------
                if mtd_files:
                    fix_time = M.time.time()

                    Smali_Patcher(smali_folders, L_S_F)

                    Replace_Strings(L_S_F, M.os.path.join(mtd_path, mtd_file))

                    if not M_Skip:
                        Merge_Smali_Folders(decompile_dir, isAPKTool, L_S_F)

                    App_Name = Scan_Application(apk_path, manifest_path, d_manifest_path, isAPKTool)

                    print(OR_App)

                    Replace_Application(manifest_path, d_manifest_path, Super_Value, App_Name, isAPKTool, Fix_Dex)

                    if isAPKTool:
                        Encode_Manifest(decompile_dir, manifest_path, d_manifest_path)

                    if isCoreX:
                        Delete_SO(decompile_dir, isAPKTool)

                    Recompile_Apk(decompile_dir, isAPKTool, build_dir, isFlutter)

                    M.shutil.rmtree(decompile_dir)

                    print(
                        START
                        + f'{M.time.time() - fix_time:.2f}' +
                        END
                    )

                    break

                else:
                    M.shutil.rmtree(decompile_dir)

                    print(
                        f"\n{C_Line}\n\n"
                        f"\n{C.WARN} {C.OG} '{Package_Name}....mtd' {C.G} File Not Found in {C.Y}{mtd_path} {C.R} ✘\n\n"
                        f"\n{C.INFO} Now you have to manually Translate the Last Dex with MT & again input with -r Flag the Command {C.G}( Copy Below Command & Run After Translate Dex )\n"
                        f"{C.G}  |\n  └──── {C.CC}~{C.G}$ {C.G} RKPairip -i {build_dir} {C.OG}-r\n"
                        f"\n{C_Line}\n"
                    )

                    break

    print(Logo)

    if M.os.name == 'posix':
        M.subprocess.run(['termux-wake-unlock'])

        exit(f"\n{C.X} {C.C} Releasing Wake Lock...\n")

    exit(0)