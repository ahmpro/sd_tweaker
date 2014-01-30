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

if __name__ == "__main__":
    filename, ext = os.path.splitext(os.path.basename(sys.argv[0]))
    config_json = filename+".json"
    app = wx.App(redirect=False)

    try:
        cfg = json.load(open(config_json))
    except:
        cfg = {"tabs": []}
        dlg = wx.MessageDialog(None, config_json+" doesn't exists or incorrect, please go website to get help (Menu -> About)", "Can't load config", wx.OK | wx.ICON_WARNING)
        dlg.ShowModal()

    wnd = WorkFrame(None, cfg)

    if ext == ".exe":
        wnd.SetIcon(wx.Icon(filename+ext, wx.BITMAP_TYPE_ICO))
    elif ext == ".py" and os.path.exists("icon.ico"):
        wnd.SetIcon(wx.Icon("icon.ico", wx.BITMAP_TYPE_ICO))

    wnd.Show(True)
    app.MainLoop()