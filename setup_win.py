from distutils.core import setup
import py2exe

setup(windows = [{"script": "burner.py", "icon_resources": [(1, "burner.ico")]},],
      options = {"py2exe": {"bundle_files": 1,
                            "dll_excludes": ["w9xpopen.exe"],
                            "compressed": 1,
                            "excludes": ['_ssl', 'pickle', 'calendar', 'Tkconstants', 'Tkinter', 'tcl', 'email']
                            }
                 }
      )
