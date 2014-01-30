# -*- coding: utf-8 -*-

from distutils.core import setup
import py2exe

setup(
    windows=[{"script": "sd_tweaker.py"}],
    options={"py2exe": {
        "dll_excludes": ["MSVCP90.dll", "w9xpopen.exe"],
        "compressed": True,
        "bundle_files": 1
        }
    },
    zipfile=None
) 