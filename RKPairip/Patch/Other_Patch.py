from ..ANSI_COLORS import ANSI; C = ANSI()
from ..MODULES import IMPORT; M = IMPORT()


# ---------------- Application Name ----------------
def Application_Name(L_S_F):

    pattern = M.re.compile(r'\.class public Lcom/pairip/application/Application;\s+\.super L([^;\s]+)', M.re.DOTALL)

    super_value = None

    for root, _, files in M.os.walk(L_S_F):
        for file in files:
            if file == 'Application.smali':
                smali_file_path = M.os.path.join(root, file)

                content = open(smali_file_path, 'r', encoding='utf-8', errors='ignore').read()

                match = pattern.search(content)

                if match:
                    super_value = match[1].replace(M.os.sep, ".")
                    break

        if super_value:
            break

    return super_value


# ---------------- Translate Smali Name ----------------
def Translate_Smali_Name(folder_name, isAPKTool):

    if isAPKTool:
        if folder_name == "smali":
            return "classes.dex"
        elif folder_name.startswith("smali_classes"):
            number = folder_name.replace("smali_classes", "")
            return f"classes{number}.dex" if number else "classes.dex"
    else:
        if folder_name == "classes":
            return "classes.dex"
        elif folder_name.startswith("classes"):
            number = folder_name.replace("classes", "")
            return f"classes{number}.dex" if number else "classes.dex"

    return folder_name


moved_files = []; smali_folders = []


# ---------------- Merge Smali Folders ----------------
def Merge_Smali_Folders(decompile_dir, isAPKTool, L_S_F):

    global moved_files, smali_folders

    moved_files = []; smali_folders = []

    smali_path = decompile_dir if isAPKTool else M.os.path.join(decompile_dir, "smali")

    prefix = "smali_classes" if isAPKTool else "classes"

    smali_folder = sorted([f for f in M.os.listdir(smali_path) if f == "smali" or f.startswith(prefix)], key=lambda x: int(x.split(prefix)[-1]) if x.split(prefix)[-1].isdigit() else 0)
    
    smali_folders = [M.os.path.join(smali_path, f) for f in smali_folder]

    last_path, prev_path = smali_folders[-1], smali_folders[-2]

    if M.os.path.isdir(last_path) and M.os.path.isdir(prev_path):
        for root, _, files in M.os.walk(last_path):
            for file in files:
                src = M.os.path.join(root, file)

                dest = M.os.path.join(prev_path, M.os.path.relpath(src, last_path))

                M.os.makedirs(M.os.path.dirname(dest), exist_ok=True)

                M.shutil.move(src, dest)

                moved_files.append((src, dest))

        print(f"\n{C.S} Merge {C.E} {C.OG}➸❥ {C.P}'{C.G}{M.os.path.basename(last_path)}{C.P}' {C.CC}& {C.P}'{C.G}{M.os.path.basename(prev_path)}{C.P}' {C.G} ✔\n")

        M.shutil.rmtree(L_S_F)

    return moved_files


# ---------------- UnMerge Smali Folder ----------------
def UnMerge():

    global moved_files, smali_folders

    for src, dest in moved_files:
        M.os.makedirs(M.os.path.dirname(src), exist_ok=True)

        M.shutil.move(dest, src)

    print(f"\n\n{C.S} Reverse Merge {C.E} {C.OG}➸❥ {C.P}'{C.G}{M.os.path.basename(smali_folders[-2])}{C.P}' {C.CC}& {C.P}'{C.G}{M.os.path.basename(smali_folders[-1])}{C.P}' {C.G} ✔\n")