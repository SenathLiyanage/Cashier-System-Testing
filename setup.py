# type in terminal ' pip install cx_Freeze '
# and do changes in the code
# then type in terminal ' python setup.py bdist_msi '

from cx_Freeze import setup,Executable,sys
includefiles=['icon.ico']
excludes=[]
packages=[]
base=None
if sys.platform=="win32":
    base="Win32GUI"

shortcut_table=[
    ("DesktopShortcut",
     "DesktopFolder",
     # add software name
     "Cashier System",
     "TARGETDIR",
     # enter python file name
     "[TARGETDIR]\main.exe",
     None,
     None,
     None,
     None,
     None,
     None,
     "TARGETDIR",
     )
]
msi_data={"Shortcut":shortcut_table}

bdist_msi_options={'data':msi_data}
setup(
    version="0.1",
    description="Cashier System",
    author="Senath Liyanage",
    name="Cashier System",
    options={'build_exe':{'include_files':includefiles},'bdist_msi':bdist_msi_options,},
    executables=[
        Executable(
            # enter python file name
            script="main.py",
            base=base,
            # enter icon name
            icon='icon.ico',
        )
    ]
)