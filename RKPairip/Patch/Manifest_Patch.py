from ..ANSI_COLORS import ANSI; C = ANSI()
from ..MODULES import IMPORT; M = IMPORT()

from RKPairip.Utils.Files_Check import FileCheck

F = FileCheck(); F.Set_Path()


# ---------------- Decode Manifest ----------------
def Decode_Manifest(manifest_path, d_manifest_path):

    try:
        process = M.subprocess.run(
            ['java', '-jar', F.Axml2Xml_Path, 'd', manifest_path, d_manifest_path],
            check=True, capture_output=True, text=True
        )

        if process.returncode == 0:
            print(f"\n{C.S} Decoded Manifest {C.E} {C.P}'{C.G}{M.os.path.basename(manifest_path)}{C.P}' {C.OG}➸❥ {C.P}'{C.B}{M.os.path.basename(d_manifest_path)}{C.P}' {C.G} ✔\n")

            M.os.remove(manifest_path)

        else:
            print(f"\n{C.ERROR} Decoding Failed  ✘\n")

    except Exception as e:
        print(f"\n{C.ERROR} {e}  ✘\n")


# ---------------- Generate ObjectLogger ----------------
def Generate_Objectlogger(decompile_dir, manifest_path, d_manifest_path, L_S_F):

    Target_Dest = M.os.path.join(L_S_F, 'RK_TECHNO_INDIA', 'ObjectLogger.smali')

    M.os.makedirs(M.os.path.dirname(Target_Dest), exist_ok=True)

    M.shutil.copy(F.Objectlogger, Target_Dest)
    
    print(f"\n{C.S} Generate {C.E} {C.G}ObjectLogger.smali {C.OG}➸❥ {C.Y}{M.os.path.relpath(Target_Dest, decompile_dir)} {C.G} ✔")


    # ---------------- Update Package Name ----------------
    PKG_Name = M.re.search(
        r'package="([^"]+)"',
        open(d_manifest_path, 'r', encoding='utf-8', errors='ignore'
    ).read())[1]

    content = open(Target_Dest, 'r', encoding='utf-8', errors='ignore').read()

    Update_PKG = content.replace('PACKAGENAME', PKG_Name)

    open(Target_Dest, 'w', encoding='utf-8', errors='ignore').write(Update_PKG)

    print(f"{C.G}     |\n     └──── {C.CC}Package Name ~{C.G}$ {C.OG}➸❥ {C.P}'{C.G}{PKG_Name}{C.P}' {C.G} ✔\n")


# ---------------- Fix Manifest ----------------
def Fix_Manifest(d_manifest_path):

    patterns = [
        (
            r'\s+android:(splitTypes|requiredSplitTypes)="[^"]*?"',
            r'',
            'Splits'
        ),
        (
            r'(isSplitRequired=)"true"',
            r'\1"false"',
            'isSplitRequired'
        ),
        (
            r'\s+<meta-data\s+[^>]*"com.android.(vending.|stamp.|dynamic.apk.)[^"]*"[^>]*/>',
            r'',
            '<meta-data>'
        ),
        (
            r'\s+<[^>]*"com.(pairip.licensecheck|android.vending.CHECK_LICENSE)[^"]*"[^>]*/>',
            r'',
            'CHECK_LICENSE'
        )
    ]

    for pattern, replacement, description in patterns:
        content = open(d_manifest_path, 'r', encoding='utf-8', errors='ignore').read()

        new_content = M.re.sub(pattern, replacement, content)

        if new_content != content:
            print(
                f"\n{C.S} Tag {C.E} {C.OG}{description}\n"
                f"\n{C.S} Pattern {C.E} {C.OG}➸❥ {C.P}{pattern}\n"
                f"{C.G}     |\n     └──── {C.CC}Patch Cleaned Up {C.OG}➸❥ {C.P}'{C.G}{M.os.path.basename(d_manifest_path)}{C.P}' {C.G} ✔\n"
            )

        open(d_manifest_path, 'w', encoding='utf-8', errors='ignore').write(new_content)


# ---------------- Patch Manifest ----------------
def Patch_Manifest(decompile_dir, manifest_path, d_manifest_path, isAPKTool, L_S_F, CoreX_Hook, isFlutter, isCoreX):

    if isAPKTool:
        Decode_Manifest(manifest_path, d_manifest_path)

    Fix_Manifest(d_manifest_path)

    if not (CoreX_Hook or isCoreX):
        Generate_Objectlogger(decompile_dir, manifest_path, d_manifest_path, L_S_F)

    if not CoreX_Hook:
        content = open(d_manifest_path, 'r', encoding='utf-8', errors='ignore').read()

        application_tag = M.re.search(
            r'<application\s+[^>]*>',
            content
        )[0]

        if isCoreX or isFlutter:
            cleaned_tag = M.re.sub(
                r'\s+android:extractNativeLibs="[^"]*?"',
                '',
                application_tag
            )

            content = content.replace(application_tag,
                M.re.sub(
                    r'>',
                    '\n\tandroid:extractNativeLibs="true">',
                    cleaned_tag
                )
            )

        else:
            new_permissions = '''\t<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE"/>\n\t<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>\n\t<uses-permission android:name="android.permission.MANAGE_EXTERNAL_STORAGE"/>'''

            content = M.re.sub(
                r'\s+<uses-permission[^>]*android:name="(android.permission.((READ|WRITE|MANAGE)_EXTERNAL_STORAGE))"[^>]*>',
                '',
                content
            )
        
            #content = M.re.sub(r'android:targetSdkVersion="\d+"', 'android:targetSdkVersion="28"', content)

            content = M.re.sub(
                r'(<uses-sdk\s+[^>]*>)',
                r'\1\n'
                + new_permissions, content
            )

            cleaned_tag = M.re.sub(
                r'\s+android:(request|preserve)LegacyExternalStorage="[^"]*?"',
                '',
                application_tag
            )

            content = content.replace(application_tag, M.re.sub(r'>','\n\tandroid:requestLegacyExternalStorage="true"\n\tandroid:preserveLegacyExternalStorage="true">', cleaned_tag))
        
        open(d_manifest_path, 'w', encoding='utf-8', errors='ignore').write(content)
        
        print(f"\n{C.S} Storage Permission {C.E} {C.OG}➸❥ {C.P}'{C.G}AndroidManifest.xml{C.P}' {C.G} ✔\n")

    if (isCoreX or isFlutter) and isAPKTool:
        Encode_Manifest(decompile_dir, manifest_path, d_manifest_path)


# ---------------- Replace Application ----------------
def Replace_Application(manifest_path, d_manifest_path, Super_Value, App_Name, isAPKTool, Fix_Dex):

    if isAPKTool or Fix_Dex:
        Decode_Manifest(manifest_path, d_manifest_path)

        manifest_path = d_manifest_path

    f = open(manifest_path, 'r', encoding='utf-8', errors='ignore').read()

    updated = f.replace(App_Name, Super_Value)

    open(manifest_path, 'w', encoding='utf-8', errors='ignore').write(updated)
    
    print(f"\n{C.S} Replaced {C.E} {C.P}'{C.G}{App_Name}{C.P}' {C.OG}➸❥ {C.P}'{C.C}{Super_Value}{C.P}' {C.G} ✔\n")


# ---------------- Encoded Mainfest ----------------
def Encode_Manifest(decompile_dir, manifest_path, d_manifest_path):

    try:
        process = M.subprocess.run(
            ['java', '-jar', F.Axml2Xml_Path, 'e', d_manifest_path, manifest_path],
            check=True, capture_output=True, text=True
        )

        if process.returncode == 0:
            print(f"\n{C.S} Encoded Manifest {C.E} {C.P}'{C.B}{M.os.path.basename(d_manifest_path)}{C.P}' {C.OG}➸❥ {C.P}'{C.G}{M.os.path.basename(manifest_path)}{C.P}' {C.G} ✔\n")

            M.os.remove(d_manifest_path)

        else:
            print(f"\n{C.ERROR} Encoding Failed  ✘\n")

    except Exception as e:
        print(f"\n{C.ERROR} {e}  ✘\n")