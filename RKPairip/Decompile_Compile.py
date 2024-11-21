_D=True
_C='-o'
_B='-jar'
_A='java'
from.C_M import CM
C=CM()
from.Files_Check import FileCheck
F=FileCheck()
F.set_paths()
apkeditor_path,apktool_path=F.apkeditor_path,F.apktool_path
class De_Compiler:
	def decompile_apk_choice(E,apk_path,decompile_dir,use_apktool,Fix_dex):
		B=decompile_dir;A=apk_path;print(f"\n{C.r}_____________________________________________________________\n")
		if use_apktool or Fix_dex:D=[_A,_B,apktool_path,'d','-f','-r',A,_C,B];print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Decompile with ApkTool...");print(f"{C.g}  |\n  └──── {C.r}Decompiling ~{C.g}$ java -jar {C.os.path.basename(apktool_path)} d -f -r {A} -o {C.os.path.basename(B)}\n");print(f"{C.r}_____________________________________________________________{C.g}\n")
		else:D=[_A,_B,apkeditor_path,'d','-f','-no-dex-debug','-i',A,_C,B];print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Decompile with APKEditor...");print(f"{C.g}  |\n  └──── {C.r}Decompiling ~{C.g}$ java -jar {C.os.path.basename(apkeditor_path)} d -f -i {A} -o {C.os.path.basename(B)}\n");print(f"{C.r}_____________________________________________________________{C.g}\n")
		try:C.subprocess.run(D,check=_D);print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Decompile Successful  {C.g}✔{C.r}\n");print(f"{C.r}_____________________________________________________________\n")
		except C.subprocess.CalledProcessError:exit(f"\n{C.lb}[ {C.rd}Error ! {C.lb}] {C.rd} Decompile Failed ! ✘{C.r}\n");return None,None
	def Application_Name(K,base_dir,target_class):
		E=C.re.compile(f"\\.class\\s+public\\s+{C.re.escape(target_class)}\\s+\\.super\\s+L([^;\\s]+)");A=None
		for(F,L,G)in C.os.walk(base_dir):
			for B in G:
				if B.endswith('.smali'):
					H=C.os.path.join(F,B)
					with open(H,'r')as I:J=I.read()
					D=E.search(J)
					if D:A=D.group(1).replace('/','.');break
			if A:break
		return A
	def replace_application_value(E,manifest_path,old_value,new_value):
		B=manifest_path
		with open(B,'r')as A:C=A.read()
		D=C.replace(old_value,new_value)
		with open(B,'w')as A:A.write(D)
	def recompile_apk(F,decompile_dir,use_apktool,build_dir):
		E='b';B=decompile_dir;A=build_dir
		if C.os.path.isfile(A):print(f"\n{C.r}_____________________________________________________________\n");print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} APK Already Exists.\n{C.g}  |\n  └──── {C.g}Removed Old APK... {C.y}{A} {C.g}✔{C.r}\n");C.os.remove(A)
		if use_apktool:
			D=[_A,_B,apktool_path,E,'-c',B,_C,A];print(f"{C.r}_____________________________________________________________\n");print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Recompile APK...");print(f"{C.g}  |\n  └──── {C.r}Recompiling with aapt ~{C.g}$ java -jar {C.os.path.basename(apktool_path)} b -c {C.os.path.basename(B)} -o {C.os.path.basename(A)}\n");print(f"{C.r}_____________________________________________________________{C.g}\n");print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} ApkTool Default...{C.g}\n")
			try:C.subprocess.run(D,check=_D);print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Recompile Successful  {C.g}✔{C.r}\n");print(f"{C.r}_____________________________________________________________\n")
			except C.subprocess.CalledProcessError:
				print(f"\n{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} Default Recompile Failed! ✘{C.r}\n");D=[_A,_B,apktool_path,E,'-c','-use-aapt2',B,_C,A];print(f"{C.r}_____________________________________________________________\n");print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Recompile APK...");print(f"{C.g}  |\n  └──── {C.r}Recompiling with aapt2 ~{C.g}$ java -jar {C.os.path.basename(apktool_path)} b -c -use-aapt2 {C.os.path.basename(B)} -o {C.os.path.basename(A)}\n");print(f"{C.r}_____________________________________________________________{C.g}\n");print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} ApkTool AAPT2...{C.g}\n")
				try:C.subprocess.run(D,check=_D);print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Recompile Successful with aapt2 {C.g} ✔{C.r}\n");print(f"{C.r}_____________________________________________________________\n")
				except C.subprocess.CalledProcessError:exit(f"\n{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} AAPT2 Recompile Failed! ✘{C.r}\n\n{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} Recompile Failed with both Default & aapt2 ! ✘{C.r}\n")
		else:
			D=[_A,_B,apkeditor_path,E,'-i',B,_C,A];print(f"{C.r}_____________________________________________________________\n");print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Recompile APK...");print(f"{C.g}  |\n  └──── {C.r}Recompiling ~{C.g}$ java -jar {C.os.path.basename(apkeditor_path)} b -i {C.os.path.basename(B)} -o {C.os.path.basename(A)}\n");print(f"{C.r}_____________________________________________________________{C.g}\n")
			try:C.subprocess.run(D,check=_D);print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Recompile Successful  {C.g}✔{C.r}\n");print(f"{C.r}_____________________________________________________________\n")
			except C.subprocess.CalledProcessError:exit(f"\n{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} Recompile Failed with APKEditor ! ✘{C.r}\n")