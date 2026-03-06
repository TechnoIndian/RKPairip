from ..ANSI_COLORS import ANSI; C = ANSI()
from ..MODULES import IMPORT; M = IMPORT()

from .Files_Check import FileCheck;

F = FileCheck(); F.Set_Path()

C_Line = f"{C.CC}{'_' * 61}"


# ---------------- Decompile APK ----------------
def Decompile_Apk(apk_path, decompile_dir, isAPKTool, Fix_Dex):

    AA = f"{'APKTool' if isAPKTool else 'APKEditor'}"

    print(
        f"\n{C_Line}\n\n"
        f"\n{C.X} {C.C} Decompile APK with {AA}..."
    )

    if isAPKTool or Fix_Dex:
        cmd = ["java", "-jar", F.APKTool_Path, "d", apk_path, "-o", decompile_dir, "-f", "-r", "--only-main-classes"]

        print(
            f"{C.G}  |\n  └──── {C.CC}Decompiling ~{C.G}$ java -jar {M.os.path.basename(F.APKTool_Path)} d -f {apk_path} -o {M.os.path.basename(decompile_dir)}\n"
            f"\n{C_Line}{C.G}\n"
        )

    else:
        cmd = ["java", "-jar", F.APKEditor_Path, "d", "-i", apk_path, "-o", decompile_dir,  "-f", "-no-dex-debug", "-dex-lib", "jf"]

        print(
            f"{C.G}  |\n  └──── {C.CC}Decompiling ~{C.G}$ java -jar {M.os.path.basename(F.APKEditor_Path)} d -i {apk_path} -o {M.os.path.basename(decompile_dir)} -f -no-dex-debug -dex-lib jf\n"
            f"\n{C_Line}{C.G}\n"
        )

    try:
        M.subprocess.run(cmd, check=True)

        print(
            f"\n{C.X} {C.C} Decompile Successful {C.G} ✔\n"
            f"\n{C_Line}\n"
        )

    except M.subprocess.CalledProcessError:
        M.shutil.rmtree(decompile_dir)

        exit(f"\n{C.ERROR} Decompile APK Failed with {AA}  ✘\n")


# ---------------- Recompile APK ----------------
def Recompile_Apk(decompile_dir, isAPKTool, build_dir, isFlutter):

    AA = f"{'APKTool' if isAPKTool else 'APKEditor'}"

    print(
        f"{C_Line}\n\n"
        f"\n{C.X} {C.C} Recompile APK with {AA}..."
    )

    if isAPKTool:
        cmd = ["java", "-jar", F.APKTool_Path, "b", "-f", decompile_dir, "-o", build_dir]

        print(
            f"{C.G}  |\n  └──── {C.CC}Recompiling ~{C.G}$ java -jar {M.os.path.basename(F.APKTool_Path)} b -f {M.os.path.basename(decompile_dir)} -o {M.os.path.basename(build_dir)}\n"
            f"\n{C_Line}{C.G}\n"
        )

    else:
        cmd = ["java", "-jar", F.APKEditor_Path, "b", "-i", decompile_dir, "-o", build_dir, "-f", "-dex-lib", "jf"]

        if isFlutter:
            cmd += ["-extractNativeLibs", "true"]

        print(
            f"{C.G}  |\n  └──── {C.CC}Recompiling ~{C.G}$ java -jar {M.os.path.basename(F.APKEditor_Path)} b -i {M.os.path.basename(decompile_dir)} -o {M.os.path.basename(build_dir)} -f -dex-lib jf"
            + (" -extractNativeLibs true" if isFlutter else "")
            + f"\n\n{C_Line}{C.G}\n"
        )

    try:
        M.subprocess.run(cmd, check=True)

        print(
            f"\n{C.X} {C.C} Recompile Successful {C.G} ✔\n"
            f"\n{C_Line}\n"
        )

    except M.subprocess.CalledProcessError:
        M.shutil.rmtree(decompile_dir)

        exit(f"\n{C.ERROR} Recompile APK Failed with {AA}...  ✘\n")

    if M.os.path.exists(build_dir):
        print(
            f"\n{C.S} APK Created {C.E} {C.G}➸❥ {C.Y}{build_dir} {C.G} ✔\n"
            f"\n{C_Line}\n"
        )


# ---------------- FixSigBlock ----------------
def FixSigBlock(decompile_dir, apk_path, build_dir, rebuild_dir):

    M.os.rename(build_dir, rebuild_dir)

    sig_dir = decompile_dir.replace('_decompiled', '_SigBlock')

    for operation in ["d", "b"]:
        cmd = ["java", "-jar", F.APKEditor_Path, operation, "-t", "sig", "-i", (apk_path if operation == "d" else rebuild_dir), "-f", "-sig", sig_dir]

        if operation == "b":
            cmd.extend(["-o", build_dir])

        M.subprocess.run(cmd, check=True, text=True, capture_output=True)

    M.shutil.rmtree(sig_dir); M.os.remove(rebuild_dir)