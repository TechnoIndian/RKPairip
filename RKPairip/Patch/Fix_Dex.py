from ..ANSI_COLORS import ANSI; C = ANSI()
from ..MODULES import IMPORT; M = IMPORT()

from RKPairip.Utils.Files_Check import FileCheck

F = FileCheck(); F.Set_Path()

C_Line = f"{C.CC}{'_' * 61}"


# ---------------- Scan Application ----------------
def Scan_Application(apk_path, manifest_path, d_manifest_path, isAPKTool):

    App_Name = ''

    if not isAPKTool:
        App_Name = M.re.search(
            r'<application[^>]*android:name="([^"]*)"',
            open(manifest_path, 'r', encoding='utf-8', errors='ignore').read()
        )[1]

        if App_Name:
            print(f"\n{C.S} Match Application {C.E} {C.OG}➸❥ {C.P}'{C.G}{App_Name}{C.P}' {C.G} ✔\n")

            return App_Name

    if M.os.name == 'posix':
        result = M.subprocess.run(
            ['aapt', 'dump', 'xmltree', apk_path, 'AndroidManifest.xml'],
            check=True, capture_output=True, text=True
        )

        App_Name = M.re.search(
            r'E: application.*[\s\S]*?A: android:name.*="([^"]*)"',
            result.stdout
        )[1]

        if App_Name:
            print(f"\n{C.S} Match Application {C.E} {C.OG}➸❥ {C.P}'{C.G}{App_Name}{C.P}' {C.G} ✔\n")

            return App_Name

    if not App_Name:
        # ---------------- Decode_Manifest ----------------
        M.subprocess.run(
            ['java', '-jar', F.Axml2Xml_Path, 'd', manifest_path, d_manifest_path],
            capture_output=True, text=True, check=True
        )

        App_Name = M.re.search(
            r'<application[^>]*android:name="([^"]*)"',
            open(d_manifest_path, 'r', encoding='utf-8', errors='ignore').read()
        )[1]

        if App_Name:
            print(f"\n{C.S} Match Application {C.E} {C.OG}➸❥ {C.P}'{C.G}{App_Name}{C.P}' {C.G} ✔\n")

            return App_Name

            M.os.remove(manifest_path)

    return App_Name


# ---------------- Delete Pairip Folder ----------------
def Delete_Folders(smali_folders, L_S_F):

    print(
        f"{C_Line}\n\n"
        f"\n{C.X}{C.C} Deleting Pairip Folders {C.G} ✔"
    )

    Pairip_Folders = M.os.path.join("com", "pairip")

    Target_Regex = M.re.compile(r'\.class public L([^;]+);\n\.super Ljava/lang/Object;\n.source "\d+.java"\s+# static fields\n\.field public static [^: ]+:Ljava/lang/String;\n')
    
    Exclude_File = []

    for root, _, files in M.os.walk(M.os.path.join(L_S_F, Pairip_Folders)):
        for file in files:
            Smali_Path = M.os.path.join(root, file)

            with open(Smali_Path, 'r', encoding='utf-8', errors='ignore') as f:
                if Target_Regex.search(f.read()):
                    Exclude_File.append(Smali_Path)

    for smali_folder in smali_folders:
        Pairip_Folder_Path = M.os.path.join(smali_folder, Pairip_Folders)

        Logs_Smali_Path = M.os.path.join(L_S_F, "RK_TECHNO_INDIA")

        if M.os.path.isdir(Logs_Smali_Path):
            M.shutil.rmtree(Logs_Smali_Path)

            print(f"{C.G}  |\n  └──── {C.CC}Deleting Folder ~{C.G}$  {C.Y}{M.os.path.basename(Logs_Smali_Path)} {C.G} ✔")

        if M.os.path.isdir(Pairip_Folder_Path):
            if Exclude_File:
                for root, dirs, files in M.os.walk(Pairip_Folder_Path, topdown=False):
                    for file in files:
                        file_path = M.os.path.realpath(M.os.path.join(root, file))

                        if file_path not in Exclude_File:
                            M.os.remove(file_path)

                            print(f"{C.G}  |\n  └──── {C.CC}Deleting File ~{C.G}$  {C.Y}{M.os.path.basename(file_path)} {C.G} ✔")
            else:
                M.shutil.rmtree(Pairip_Folder_Path)

                print(f"{C.G}  |\n  └──── {C.CC}Deleting Folder ~{C.G}$  {C.Y}{M.os.path.basename(Pairip_Folder_Path)} {C.G} ✔")

    print(f"\n{C_Line}\n\n")


# ---------------- Scan Target Regex ----------------
def Regex_Scan(Smali_Path, Target_Regex, Count, Lock):
            
    Smali = open(Smali_Path, 'r', encoding='utf-8', errors='ignore').read()
        
    Patterns = [M.re.compile(Regex) for Regex in Target_Regex]

    for Pattern in Patterns:
        if Pattern.search(Smali):

            if Lock:
                try:
                    with Lock:
                        Count.value += 1

                        print(f"\r{C.S} Find Target Smali {C.E} {C.OG}➸❥ {C.PN}{Count.value}", end='', flush=True)

                except Exception:
                    return None

            else:
                Count[0] += 1

                print(f"\r{C.S} Find Target Smali {C.E} {C.OG}➸❥ {C.PN}{Count[0]}", end='', flush=True)

            return Smali_Path


# ---------------- Smali Patcher ----------------
def Smali_Patcher(smali_folders, L_S_F):

    matching_files, Smali_Paths = [], []

    patterns = [
        (
            r'(\.method public static )FuckUByRK\(\)V([\s\S]*?.end method)[\w\W]*',
            r'\1constructor <clinit>()V\2',
            "Patch 1"
        ),
        (
            r'sget-object v0, L[^;]+;->[^:]*:Ljava/lang/String;\s+const-string v1, ("(\d+.java:\d+)")\s+.line \d+\s+.local v0, "(\d+.java:\d+)":V\s+invoke-static \{v0\}, LRK_TECHNO_INDIA/ObjectLogger;->logstring\(Ljava/lang/Object;\)V',
            r'const-string v0, \1',
            "Patch 2"
        ),
        (
            r'invoke-static \{\}, L[^;]+;->callobjects\(\)V\n',
            r'',
            "Patch 3"
        ),
        (
            r'(\.method public [^(]*onReceive\(Landroid/content/Context;Landroid/content/Intent;\)V\s+\.locals \d+)[\s\S]*?const-string/jumbo[\s\S]*?(\s+return-void\n.end method)',
            r'\1\2',
            "Patch 4"
        ),
        (
            r'invoke-[^\}]*\}, Lcom/pairip/[^;]+;->.*',
            r'',
            "Patch 5"
        )
    ]

    Delete_Folders(smali_folders, L_S_F)

    Target_Regex = [p[0] for p in patterns]

    for smali_folder in smali_folders:
        for root, _, files in M.os.walk(smali_folder):
            for file in files:
                if file.endswith('.smali'):
                    Smali_Paths.append(M.os.path.join(root, file))

    try:
        # ---------------- Multiple Threading ----------------
        with M.Manager() as MT:
            Count = MT.Value('i', 0); Lock = MT.Lock()

            with M.Pool(M.cpu_count()) as PL:
                matching_files = [path for path in PL.starmap(Regex_Scan, [(Smali_Path, Target_Regex, Count, Lock) for Smali_Path in Smali_Paths]) if path]

    except Exception:
        # ---------------- Single Threading ----------------
        Count = [0]

        for Smali_Path in Smali_Paths:
            result = Regex_Scan(Smali_Path, Target_Regex, Count, None)

            if result:
                matching_files.append(result)

    print(f" {C.G} ✔", flush=True)

    print(f'\n{C_Line}\n')

    if matching_files:
        for pattern, replacement, description in patterns:
            count_applied = 0; applied_files = set()

            for file_path in matching_files:
                content = open(file_path, 'r', encoding='utf-8', errors='ignore').read()

                new_content = M.re.sub(pattern, replacement, content)

                if new_content != content:
                    if file_path not in applied_files:
                        applied_files.add(file_path)

                    count_applied += 1
                    
                    open(file_path, 'w', encoding='utf-8', errors='ignore').write(new_content)

            if count_applied > 0:
                print(f"\n{C.S} Patch {C.E} {C.G}{description}")

                print(f"\n{C.S} Pattern {C.E} {C.OG}➸❥ {C.P}{pattern}")

                for file_path in applied_files:
                    print(f"{C.G}     |\n     └──── {C.CC}~{C.G}$ {C.Y}{M.os.path.basename(file_path)} {C.G} ✔")

                print(
                    f"\n{C.S} Applied {C.E} {C.OG}➸❥ {C.PN}{count_applied} {C.C}Time/Smali {C.G} ✔\n"
                    f"\n{C_Line}\n"
                )


# ---------------- Replace Strings ----------------
def Replace_Strings(L_S_F, mtd_p):

    mappings = dict(
        M.re.findall(
            r'\s"(.*)"\s"(.*)"',
            open(mtd_p, 'r', encoding='utf-8', errors='ignore').read()
        )
    )

    file_counter = 0

    for root, _, files in M.os.walk(L_S_F):
        for file in files:
            if file.endswith(".smali"):
                line_counter = 1

                path = M.os.path.join(root, file)

                lines = open(path, 'r', encoding='utf-8', errors='ignore').readlines()

                with open(path, 'w', encoding='utf-8', errors='ignore') as f:
                    for line in lines:
                        if match := M.re.match(r'\s*const-string v0, "([^"]+)"', line):
                            value = mappings.get(match[1])

                            if value:
                                line = line.split('"')[0] + f'"{value}"\n'
                            else:
                                value = f"{file_counter}.java:{line_counter}"
                                line = line.split('"')[0] + f'""\n'

                            line_counter += 1
                        f.write(line)
                file_counter += 1

    print(f"\n{C.S} Translate Dex {C.E} {C.G}➸❥ {C.PN}{file_counter} {C.C}Time/Smali {C.G} ✔\n")