# -*- coding: utf-8 -*- 
import wx
import wx.xrc

class MainFrame(wx.Frame):
    def __init__(self, parent, cfg):
        wx.Frame.__init__ (self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL)

        self.cfg = cfg
        
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        sizer_frame = wx.BoxSizer(wx.VERTICAL)
        
        self.tabs = wx.Notebook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.tabs.check_list = []
        self.tabs.panels = []

        for tab in cfg["tabs"]:
            panel = wx.Panel(self.tabs, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
            sizer = wx.BoxSizer(wx.VERTICAL)

            self.tabs.check_list.append(wx.CheckListBox(
                panel,
                wx.ID_ANY,
                wx.DefaultPosition,
                wx.DefaultSize,
                map(lambda x: x["desc"], tab["contents"]),
                0
            )) # todo: implement default checked(cfg has param, but don't use it)
            sizer.Add(self.tabs.check_list[-1], 1, wx.ALL|wx.EXPAND, 5)

            panel.SetSizer(sizer)
            panel.Layout()
            sizer.Fit(panel)

            self.tabs.AddPage(panel, tab["title"], True)
            self.tabs.panels.append(panel)
      
        sizer_frame.Add(self.tabs, 1, wx.EXPAND|wx.ALL, 0)
        
        self.action_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        sizer_action = wx.BoxSizer(wx.HORIZONTAL)

        if len(self.cfg["tabs"]) > 0:
            self.btn_apply = wx.Button(self.action_panel, wx.ID_ANY, u"Apply", wx.DefaultPosition, wx.DefaultSize, 0)
            sizer_action.Add(self.btn_apply, 0, wx.ALL, 5)
            self.btn_apply.Bind(wx.EVT_BUTTON, self.cmd_apply)

        self.btn_exit = wx.Button(self.action_panel, wx.ID_ANY, u"Exit", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer_action.Add(self.btn_exit, 0, wx.ALL, 5)
        self.btn_exit.Bind(wx.EVT_BUTTON, self.app_exit)

        self.action_panel.SetSizer(sizer_action)
        self.action_panel.Layout()
        sizer_action.Fit(self.action_panel)
        sizer_frame.Add(self.action_panel, 0, wx.EXPAND|wx.ALL, 0)

        self.SetSizer(sizer_frame)
        self.Layout()
        self.Centre(wx.BOTH)

        self.menubar = wx.MenuBar( 0 )
        self.menu = wx.Menu()
        self.menu_about = wx.MenuItem( self.menu, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL )
        self.menu.AppendItem(self.menu_about)
        self.menubar.Append(self.menu, u"Menu") 
        self.SetMenuBar(self.menubar)

        self.Bind(wx.EVT_MENU, self.app_about, id = self.menu_about.GetId())
    
    def __del__(self):
        pass
    
    def app_exit(self, event):
        event.Skip()

    def app_about( self, event ):
        event.Skip()

    def cmd_apply( self, event ):
        event.Skip()