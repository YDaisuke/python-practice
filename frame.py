#coding=utf-8
import wxPython

application = wx.App()

frame = wx.Frame(None, wx.ID_ANY, 'テストフレーム')
frame.Show()

application.MainLoop()
