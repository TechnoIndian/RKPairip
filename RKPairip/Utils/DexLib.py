from ..ANSI_COLORS import ANSI; C = ANSI()
from ..MODULES import IMPORT; M = IMPORT()

from .Files_Check import FileCheck;

F = FileCheck(); F.Set_Path()

C_Line = f"{C.CC}{'_' * 61}"

X = f"   |\n   ╰{C.CC}┈{C.OG}➢ {C.G}"


# ---------------- DexLib2 Restored APK ----------------
def DexLib2_Restored(apk_path, json_files):
    
    print(
        f"\n{C_Line}\n\n"
        f"\n{C.X} {C.C} DexLib2 Restored APK, NullRE Method..."
    )

    cmd = ["java", "-jar", F.Pairip_Jar_Path, "-i", apk_path, "-t", json_files]

    print(
        f"{C.G}  |\n  └──── {C.CC}DexLib2 ~{C.G}$ java -jar {M.os.path.basename(F.Pairip_Jar_Path)} -i {apk_path} -t {M.os.path.basename(json_files)}\n"
        f"\n{C_Line}{C.G}\n"
    )

    M.subprocess.run(cmd, check=True)

    exit("\n")


# ---------------- DexLib2 Logged APK ----------------
def DexLib2_Logged(apk_path):

    print(
        f"\n{C_Line}\n\n"
        f"\n{C.X} {C.C} DexLib2 Logged APK, NullRE Method..."
    )

    cmd = ["java", "-jar", F.Pairip_Jar_Path, "-i", apk_path]

    print(
        f"{C.G}  |\n  └──── {C.CC}DexLib2 ~{C.G}$ java -jar {M.os.path.basename(F.Pairip_Jar_Path)} -i {apk_path}\n"
        f"\n{C_Line}{C.G}\n"
    )

    M.subprocess.run(cmd, check=True)


    json_path = "/sdcard/MT2/dictionary/"

    if M.os.path.exists(json_path):
        json_files = [
            file 
            for file in M.os.listdir(json_path) 
            if file.endswith('.json')
        ]

        for json_file in json_files:
            M.os.remove(M.os.path.join(json_path, json_file))
    
    print(
        f"\n{C_Line}\n\n"
        f'\n{C.INFO} {C.G} If U Want Repair Dex, So Generate {C.OG} ".json" {C.G} First & put the {C.OG} ".json" {C.G} in the path of {C.Y}"/sdcard/MT2/dictionary/"{C.G}, if {C.OG} ".json" {C.G} available in target path then The Script will handle Automatically, So Press Enter 🤗🤗\n'
        f"\n{X} Tutorial  - {C.B} https://t.me/NullRE_Channel/162\n"
    )

    while True:
        Repair_Dex = input(f"\n{C.X} {C.C} Do U Want Repair Dex ( Press Enter To Proceed or 'q' to exit )\n{C.G}  |\n  └──── {C.CC}~{C.G}$ : {C.Y}").strip().lower()

        if Repair_Dex == 'q':
             exit("\n")
             
        else:
            json_files = None

            while True:
                if M.os.path.exists(json_path):
                    json_files = [
                        file 
                        for file in M.os.listdir(json_path) 
                        if file.endswith('.json')
                    ]

                    if not json_files:
                        print(f"\n\n{C.WARN} {C.OG} 'pairip.json' {C.G} File Not Found in {C.Y}{json_path} {C.R} ✘\n")

                    else:

                        json_file = max(json_files, key=lambda file: M.os.path.getmtime(M.os.path.join(json_path, file)))

                        print(f"\n{C.S} Founded {C.E} {C.OG}➸❥ {C.G}{json_file}  ✔")

                        break

                else:
                    print(f"\n\n{C.WARN} No such directory found: {C.Y}{json_path}{C.OG}pairip.json\n")

                user_input = input(f"\n{C.S} Input {C.E}{C.C} If You Want To Retry, Press Enter & Exit To Script {C.P}'q' : {C.Y}")

                if user_input.lower() == 'q':
                    exit("\n")


            # ---------------- Restore Strings ---------------
            if json_files:
                json_log_file = M.os.path.join(json_path, json_file)

                DexLib2_Restored(apk_path, json_log_file)