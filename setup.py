# -*- coding: utf-8 -*-

from distutils.core import setup
import py2exe

setup(
    version = "0.1.1",
    description = "Simple config-based tweaker",
    name = "SD Tweaker",
    windows=[{
        "script": "sd_tweaker.py",
        "icon_resources": [(1, "icon.ico")],
        "uac_info": "requireAdministrator",
        }
    ],
    options={"py2exe": {
        "compressed": True,
        "bundle_files": 1
        }
    },
    zipfile=None
) 