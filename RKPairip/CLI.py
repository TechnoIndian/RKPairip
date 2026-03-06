from .ANSI_COLORS import ANSI; C = ANSI()
from .MODULES import IMPORT; M = IMPORT()

from RKPairip.Utils.Files_Check import __version__


FE = f"{C.P}\n   |\n   ╰{C.CC}┈{C.OG}➢ {C.G}RKPairip{C.OG}"

EX = f"{FE} -i {C.G}Your_Apk_Path.apk{C.OG}"


class CustomArgumentParser(M.argparse.ArgumentParser):
    # ---------------- Error Handling ----------------
    def error(self, message):

        suggestion = ""
        for action in self._actions:
            if action.option_strings and any(option in message for option in action.option_strings):

                if action.dest == 'input':
                    suggestion = (
                        f'\n{C.FYI}{C.G} Make Sure There Is "No Extra Space" In The Folder / Apk Name In The Input Text. If Yes, Then Remove Extra Space & Correct It By Renaming It.\n\n'
                        f'\n{C.INFO} With APKEditor {C.P}( Default )\n'
                        f'{EX}\n\n'
                        f'\n{C.INFO} With APKTool Use {C.C}Flag: {C.OG}-a\n'
                        f'{EX} -a\n\n'
                        f'\n{C.INFO} Pairip New Method By NullRE Use Flag: {C.OG}-n\n'
                        f'{EX} -n\n\n'
                        f'\n{C.INFO} Merge Skip Use Flag: {C.OG}-s {C.P}( Do U Want Last Dex Add Seprate For Dex Redivision )\n'
                        f'{EX} -s\n\n'
                        f'\n{C.INFO} Pairip Dex Fix Use {C.C}Flag: {C.OG}-r {C.P}( Try After Translate String to MT )\n'
                        f'{EX} -r\n\n'
                        f'\n{C.INFO} Hook CoreX {C.P}( For Unity / Flutter & Crashed Apk Apk ) {C.OG}-x {C.Y}/ {C.OG}-a -x \n'
                        f'{EX} -x\n'
                    )

                elif action.dest == 'Merge':
                    suggestion = (
                        f'\n{C.INFO} Only Merge Apk\n\n'
                        f'\n{C.INFO} Merge Extension {C.OG}( .apks / .xapk / .apkm )\n'
                        f'{FE} {C.OG}-m {C.G}Your_Apk_Path.apks\n'
                    )

                break

        exit(
            f'\n{C.ERROR} {message}\n'
            f'\n{suggestion}'
        )


# ---------------- Parse Arguments ----------------
def parse_arguments():

    args = M.sys.argv[1:]

    if any(arg.startswith('-') for arg in args):
        parser = CustomArgumentParser(description=f'{C.C}RKPairip v{__version__}')
    else:
        parser = M.argparse.ArgumentParser()

    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument(
        '-i',
        dest = 'input',
        help = f'{C.Y}➸ {C.G}Input APK Path...{C.C}'
    )

    group.add_argument(
        '-m',
        dest = 'Merge',
        help = f'{C.Y}➸ {C.G}Anti-Split ( Only Merge Apk ){C.C}'
    )

    group.add_argument(
        '-C',
        dest = 'Credits_Instruction',
        action = 'store_true',
        help = f'{C.Y}➸ {C.G}Show Instructions & Credits{C.C}'
    )

    additional = parser.add_argument_group(f'{C.OG}[ * ] Additional Flags{C.C}')

    additional.add_argument(
        '-a', '--ApkTool',
        action = 'store_true',
        help = f'{C.Y}➸ {C.G}ApkTool ( Fast, But Not Stable Comparison To APKEditor ){C.C}'
        )

    additional.add_argument(
        '-n', '--NullRE',
        action = 'store_true',
        help = f'{C.Y}➸ {C.G}Pairip New Method By NullRE{C.C}'
        )

    additional.add_argument(
        '-s', '--MergeSkip',
        action = 'store_true',
        help = f'{C.Y}➸ {C.G}Do U Want Last Dex Add Seprate ( For Dex Redivision & The script will be in listen mode, so you can do Max Value Dex Redivision {C.PN}( like 65536 ) {C.G}using MT/ApkTool_M and correct the name of the APK again and then press enter in the script, which will bypass CRC ){C.C}'
    )

    additional.add_argument(
        '-r', '--Repair_Dex',
        action = 'store_true',
        help = f'{C.Y}➸ {C.G}Pairip Dex Fix ( Try After Translate String to MT ){C.C}'
    )

    additional.add_argument(
        '-x', '--Hook_CoreX',
        action = 'store_true',
        help = f'{C.Y}➸{C.G} Hook CoreX ( For Unity / Flutter & Crashed Apk ){C.CC}'
    )

    Ext = ('.apk', '.apks', '.apkm', '.xapk')

    fixed = []; start = None; Valid_Ext = False

    for index, option in enumerate(args):
        if option in ['-i', '-m', '-C']:
            start, fixed = index + 1, fixed + [option]
        elif start and (option.endswith(Ext) or M.os.path.isdir(option)):
            fixed, start = fixed + [' '.join(args[start:index+1])], None
            Valid_Ext = True
        elif not start:
            fixed.append(option)

    if not Valid_Ext and M.sys.argv[1:2] != ['-C']:
        print(f"\n{C.X}{C.C} Only Supported Extensions {C.G}{Ext}\n")

    print(f"\n{C.S} Input Path {C.E} {C.OG}➸❥{C.Y}", *fixed, f"{C.CC}\n")

    return parser.parse_args(fixed)