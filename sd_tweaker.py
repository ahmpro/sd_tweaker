# -*- coding: utf-8 -*-

import wx
import sys
import os
from subprocess import call
from tweaker_gui import MainFrame
import json

class WorkFrame(MainFrame):
    def __init__(self, *args, **kwds):
        MainFrame.__init__(self, *args, **kwds)

    def app_exit(self, e):
        sys.exit(0)

    def app_about( self, event ):
        info = wx.AboutDialogInfo()

        info.SetName("SD Tweaker")
        info.SetVersion("0.1")
        info.SetDescription("Simple config-based tweaker. Source and readme:")
        info.SetCopyright("(C) 2014 ahmpro (ahmpro@rslayers.com)")
        info.SetWebSite("http://www.github.com/ahmpro/sd_tweaker")

        wx.AboutBox(info)

    def cmd_apply(self, e):
        current_tab = self.tabs.GetSelection()
        for checked in self.tabs.check_list[current_tab].GetChecked():
            call(self.cfg["tabs"][current_tab]["contents"][checked]["cmd"], shell=True)

def without_ext():
    basename = os.path.basename(sys.argv[0])
    return os.path.splitext(basename)[0]

if __name__ == "__main__":
    config_json = without_ext()+".json"
    app = wx.App(redirect=False)

    try:
        cfg = json.load(open(config_json))
    except:
        cfg = {"tabs": []}
        dlg = wx.MessageDialog(None, config_json+" doesn't exists or incorrect, please go website to get help (Menu -> About)", "Can't load config", wx.OK | wx.ICON_WARNING)
        dlg.ShowModal()
        #sys.exit(1)

    wnd = WorkFrame(None, cfg)

    wnd.Show(True)
    app.MainLoop()