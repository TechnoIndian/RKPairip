from ..ANSI_COLORS import ANSI; C = ANSI()
from ..MODULES import IMPORT; M = IMPORT()


# ---------------- Scan Target Regex ----------------
def Regex_Scan(Smali_Path, Count, Lock):

    Target_Strings = [
        r'\.class public L([^;]+);\n\.super Ljava/lang/Object;\s+# static fields\n\.field public static [^: ]+:Ljava/lang/String;\n',
        r'\.class public Lcom/pairip/application/Application;\n'
    ]

    Smali = open(Smali_Path, 'r', encoding='utf-8', errors='ignore').read()

    Patterns = [M.re.compile(Regex) for Regex in Target_Strings]

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


# ---------------- Extract Smali ----------------
def Extract_Smali(decompile_dir, smali_folders, isAPKTool):

    Extract_Dir = M.os.path.join(decompile_dir, *(['smali_classes'] if isAPKTool else ['smali', 'classes']))

    Matching_Files, Smali_Files, Folder_Suffix = [], [], 2

    while M.os.path.exists(f"{Extract_Dir}{Folder_Suffix}"):
        Folder_Suffix += 1

    Extract_Dir = f"{Extract_Dir}{Folder_Suffix}"

    M.os.makedirs(Extract_Dir, exist_ok=True)

    for smali_folder in smali_folders:
        for root, _, files in M.os.walk(smali_folder):
            for file in files:
                Smali_Files.append(M.os.path.join(root, file))

    print()
    try:
        # ---------------- Multiple Threading ----------------
        with M.Manager() as MT:
            Count = MT.Value('i', 0); Lock = MT.Lock()

            with M.Pool(M.cpu_count()) as PL:
                Matching_Files = [path for path in PL.starmap(Regex_Scan, [(Smali_Path, Count, Lock) for Smali_Path in Smali_Files]) if path]

    except Exception:
        # ---------------- Single Threading ----------------
        Count = [0]

        for Smali_Path in Smali_Files:
            result = Regex_Scan(Smali_Path, Count, None)

            if result:
                Matching_Files.append(result)

    print(f" {C.G} ✔\n")

    if Matching_Files:
        print(f"\n{C.S} Extract Smali {C.E} {C.OG}➸❥ {C.G}{M.os.path.basename(Extract_Dir)}")

        for Smali_File in Matching_Files:
            Relative_Path = M.os.path.relpath(Smali_File, M.os.path.dirname(Extract_Dir)).split(M.os.sep, 1)[1]

            Target_Path = M.os.path.join(Extract_Dir, Relative_Path)

            M.os.makedirs(M.os.path.dirname(Target_Path), exist_ok=True)

            M.shutil.move(Smali_File, Target_Path)

            print(f"{C.G}  |\n  └────{C.CC} Move ~{C.G}$ {C.Y}{M.os.path.basename(Smali_File)} {C.G} ✔")

        print(
            f"\n\n{C.S} Moved {C.E} {C.OG}➸❥ {C.PN}1 {C.G}Application Smali  ✔\n"
            f"\n{C.S} Moved {C.E} {C.OG}➸❥ {C.PN}32 {C.G}Pairip Smali  ✔"
        )

# ---------------- Logs Injected ----------------
def Logs_Injected(L_S_F):

    Class_Names, Last_Smali_Path, Sequence = [], None, 1

    for root, _, files in M.os.walk(L_S_F):
        for file in files:
            path = M.os.path.join(root, file)

            content = open(path, 'r', encoding='utf-8', errors='ignore').read()

            Class_Match = M.re.search(
                r'\.class public L([^;]+);',
                content
            )

            Static_Fields = M.re.findall(
                r'\.field public static ([^: ]+):Ljava/lang/String;\n',
                content
            )

            if Class_Match and Static_Fields:
                Class_Names.append(Class_Match[1])

                content = M.re.sub(
                    r'(\.super Ljava/lang/Object;)',
                    rf'\1\n.source "{Sequence:1d}.java"',
                    content
                )

                log_method = ['.method public static FuckUByRK()V', '    .registers 2']

                for i, field in enumerate(Static_Fields):
                    log_method += [
                        f'    sget-object v0, L{Class_Match[1]};->{field}:Ljava/lang/String;',
                        f'    const-string v1, "{Sequence:1d}.java:{i+1}"',
                        f'    .line {i+1}',
                        f'    .local v0, "{Sequence:1d}.java:{i+1}":V',
                        f'    invoke-static {{v0}}, LRK_TECHNO_INDIA/ObjectLogger;->logstring(Ljava/lang/Object;)V',
                        f'    sput-object v0, L{Class_Match[1]};->{field}:Ljava/lang/String;'
                    ]

                log_method += ['    return-void', '.end method']

                content += '\n' + '\n'.join(log_method)

                open(path, 'w', encoding='utf-8', errors='ignore').write(content)

                Last_Smali_Path = path

                Sequence += 1

    print(f"\n{C.G}    |\n    └────{C.CC} Logs Injected ~{C.G}$ ➸❥ {C.PN}32 {C.G}Pairip Smali  ✔\n")


    # ---------------- Added Callobjects Method ----------------

    if Class_Names and Last_Smali_Path:
        print(f'\n{C.X} {C.C} Added Callobjects Method\n')

        code = ('\n.method public static callobjects()V\n\t'
                '.registers 2\n\t' +
                ''.join(f'invoke-static {{}}, L{CN};->FuckUByRK()V\n\t' for CN in Class_Names) +
                'return-void\n.end method\n')

        open(Last_Smali_Path, 'a', encoding='utf-8', errors='ignore').write(code)

        print(f"{C.G}  |\n  └────{C.CC} Target Smali ~{C.G}$ ➸❥ {C.Y}{M.os.path.basename(Last_Smali_Path)} {C.G} ✔\n")


    # ---------------- Hook Callobjects Method ----------------

    H_App_Smali = M.os.path.join(L_S_F, 'com', 'pairip', 'application', 'Application.smali')

    if Last_Smali_Path and M.os.path.exists(H_App_Smali):
        print(f'\n{C.X} {C.C} Hook Callobjects Method\n')

        C_Name = M.os.path.splitext(M.os.path.relpath(Last_Smali_Path, L_S_F).replace(M.os.sep, "/"))[0]

        content = open(H_App_Smali, 'r', encoding='utf-8', errors='ignore').read()

        Hook_Callobjects = M.re.sub(
            r'(\.method public constructor <init>\(\)V[\s\S]*?)(\s+return-void\n.end method)',
            rf'\1\n\tinvoke-static {{}}, L{C_Name};->callobjects()V\n\2',
            content
        )

        open(H_App_Smali, 'w', encoding='utf-8', errors='ignore').write(Hook_Callobjects)

        print(f"{C.G}  |\n  └────{C.CC} Target Smali ~{C.G}$ ➸❥ {C.Y}{M.os.path.basename(H_App_Smali)} {C.G} ✔\n")

    print(
        f"\n{C.X} {C.C} Patching Done {C.G} ✔\n"
        f"\n{C.CC}{'_' * 61}\n"
    )