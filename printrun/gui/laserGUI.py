# -*- coding: utf-8 -*-

# This file is part of the Burner suite.
#
# Burner is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Burner is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Burner.  If not, see <http://www.gnu.org/licenses/>.

import wx
import wx.xrc
import platform
from wx.lib.masked import NumCtrl

from .laserGviz import LaserVizPane

###########################################################################
## Class MyPanel3
###########################################################################

WIDTH_TOTAL = 1200
HEIGHT_TOTAL = 700
WIDTH_P1 = 700
WIDTH_P2 = 500

HEIGHT_P3_1 = 90
HEIGHT_P3_2 = 250

BUTTONGPX1 = 25
BUTTONGPX2 = 110

class laserGUI(wx.Panel):
    def __init__(self, parent, root):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(WIDTH_TOTAL, HEIGHT_TOTAL),
                          style=wx.TAB_TRAVERSAL)

        self.SetBackgroundColour(wx.Colour(252, 238, 0))
        mainSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.gvizPanel = LaserVizPane(root, self)
        mainSizer.Add(self.gvizPanel, 0, 0, 0)

        self.controlPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(WIDTH_P2, HEIGHT_TOTAL), wx.TAB_TRAVERSAL)
        self.controlPanel.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        ControlSizer = wx.BoxSizer(wx.VERTICAL)

        # Right Panel 1
        GRAYSCALE_1 = wx.Colour(230, 230, 230)
        Y_BASELINE = 10
        self.ConnectPanel = wx.Panel(self.controlPanel, wx.ID_ANY, wx.DefaultPosition, wx.Size(WIDTH_P2, HEIGHT_P3_1),
                                     wx.TAB_TRAVERSAL)
        self.ConnectPanel.SetMinSize(wx.Size(WIDTH_P2, HEIGHT_P3_1))
        self.ConnectPanel.SetMaxSize(wx.Size(WIDTH_P2, HEIGHT_P3_1))

        root.toolbarsizer = wx.GridBagSizer(0, 0)
        root.toolbarsizer.SetFlexibleDirection(wx.BOTH)
        root.toolbarsizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        root.toolbarsizer.SetEmptyCellSize(wx.Size(1, 1))

        # Set Fonts
        labelfont = wx.Font(9, 74, 90, 90, False)
        if platform.system() == "Darwin":
            labelfont = wx.Font(12, 74, 90, 90, False)

        root.toolbarsizer.SetMinSize(wx.Size(WIDTH_P2, HEIGHT_P3_1))
        self.ConnectImage = wx.StaticBitmap(self.ConnectPanel, wx.ID_ANY,
                                            wx.Bitmap(u"Button/Icon_01.png", wx.BITMAP_TYPE_ANY),
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.ConnectImage.SetBackgroundColour(wx.Colour(255, 255, 255))
        root.toolbarsizer.Add(self.ConnectImage, wx.GBPosition(Y_BASELINE, BUTTONGPX1), wx.GBSpan(50, 50), 0, 0)

        self.ConnectText = wx.StaticText(self.ConnectPanel, wx.ID_ANY, u"Connect", wx.DefaultPosition, wx.Size(60, -1),
                                         wx.ALIGN_CENTRE)
        self.ConnectText.SetFont(labelfont)
        root.toolbarsizer.Add(self.ConnectText, wx.GBPosition(Y_BASELINE+50, 20), wx.GBSpan(20, 60),
                              wx.ALIGN_CENTER_HORIZONTAL, 0)

        root.rescanbtn = wx.BitmapButton(self.ConnectPanel, wx.ID_ANY,wx.Bitmap(u"Button/Button_port.png",
                                                                                 wx.BITMAP_TYPE_ANY),
                                          wx.DefaultPosition,wx.DefaultSize , wx.NO_BORDER)
        root.rescanbtn.SetBitmapHover(wx.Bitmap(u"Button/Button_port_MouseOn.png", wx.BITMAP_TYPE_ANY ))
        root.toolbarsizer.Add(root.rescanbtn, wx.GBPosition(Y_BASELINE+5, BUTTONGPX2), wx.GBSpan(21, 60), 0, 5)

        root.connectbtn = wx.BitmapButton(self.ConnectPanel, wx.ID_ANY,wx.Bitmap(u"Button/Button_connect.png",
                                                                                 wx.BITMAP_TYPE_ANY),
                                          wx.DefaultPosition,wx.DefaultSize , wx.NO_BORDER)
        root.connectbtn.SetBitmapHover(wx.Bitmap(u"Button/Button_connect_MouseOn.png", wx.BITMAP_TYPE_ANY ))
        root.toolbarsizer.Add(root.connectbtn, wx.GBPosition(Y_BASELINE+35, BUTTONGPX2), wx.GBSpan(21, 75), 0, 5)

        root.checkmark = wx.StaticBitmap(self.ConnectPanel, wx.ID_ANY,
                                            wx.Bitmap(u"Button/Icon_checkmark.png", wx.BITMAP_TYPE_ANY),
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        root.checkmark.SetBackgroundColour(wx.Colour(255, 255, 255))
        root.toolbarsizer.Add(root.checkmark, wx.GBPosition(Y_BASELINE+35, BUTTONGPX2+85), wx.GBSpan(21, 20), 0, 0)

        # root.resetbtn = wx.Button(self.ConnectPanel, wx.ID_ANY, u"Reset", wx.DefaultPosition, wx.Size(80, 25),
        #                              wx.NO_BORDER)
        # root.resetbtn.SetBackgroundColour(wx.Colour(230, 230, 230))
        #
        # root.toolbarsizer.Add(root.resetbtn, wx.GBPosition(17, 230), wx.GBSpan(4, 80), 0, 5)

        root.serialport = wx.ComboBox(self.ConnectPanel, -1, choices=root.scanserial(), style=wx.CB_DROPDOWN,
                                size=(160, -1))
        root.serialport.SetBackgroundColour(GRAYSCALE_1)
        root.toolbarsizer.Add(root.serialport, wx.GBPosition(Y_BASELINE+5, BUTTONGPX2+60+5), wx.GBSpan(21, 160), 0, 0)

        root.baud = wx.ComboBox(self.ConnectPanel, -1, choices=["2400", "9600", "19200", "38400",
                                                          "57600", "115200", "250000"],
                                style=wx.CB_DROPDOWN, size=(100, -1))
        try:
            root.baud.SetValue("115200")
            root.baud.SetValue(str(root.settings.baudrate))
        except:
            pass
        root.baud.SetBackgroundColour(GRAYSCALE_1)
        root.toolbarsizer.Add(root.baud, wx.GBPosition(Y_BASELINE+5, BUTTONGPX2+60+5+160+5), wx.GBSpan(21, 100), 0, 0)

        self.ConnectPanel.SetSizer(root.toolbarsizer)
        self.ConnectPanel.Layout()
        ControlSizer.Add(self.ConnectPanel, 0, wx.ALL, 0)

        # Right Panel 2
        BGCOLOR = wx.Colour(230, 230, 230)
        Y_BASELINE = 5
        self.CorrectionPanel = wx.Panel(self.controlPanel, wx.ID_ANY, wx.DefaultPosition,
                                        wx.Size(WIDTH_P2, HEIGHT_P3_1), wx.TAB_TRAVERSAL)
        self.CorrectionPanel.SetBackgroundColour(BGCOLOR)
        self.CorrectionPanel.SetMinSize(wx.Size(WIDTH_P2, HEIGHT_P3_1))
        self.CorrectionPanel.SetMaxSize(wx.Size(WIDTH_P2, HEIGHT_P3_1))

        CorrectionGBSizer = wx.GridBagSizer(0, 0)
        CorrectionGBSizer.SetFlexibleDirection(wx.BOTH)
        CorrectionGBSizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        CorrectionGBSizer.SetEmptyCellSize(wx.Size(1, 1))

        self.CorrectionImage = wx.StaticBitmap(self.CorrectionPanel, wx.ID_ANY,
                                               wx.Bitmap(u"Button/Icon_02.png", wx.BITMAP_TYPE_ANY),
                                               wx.DefaultPosition, wx.DefaultSize, 0)
        CorrectionGBSizer.Add(self.CorrectionImage, wx.GBPosition(Y_BASELINE, BUTTONGPX1), wx.GBSpan(50, 50), 0, 0)

        self.CorrectionText = wx.StaticText(self.CorrectionPanel, wx.ID_ANY, u"Auto\nCorrect", wx.DefaultPosition,
                                            wx.Size(60, 30), wx.ALIGN_CENTRE)
        self.CorrectionText.SetFont(labelfont)
        CorrectionGBSizer.Add(self.CorrectionText, wx.GBPosition(Y_BASELINE+50, 20), wx.GBSpan(30, 60),
                              wx.ALIGN_CENTER_HORIZONTAL, 0)

        Y_BASELINE = 12
        self.G29Text = wx.StaticBitmap(self.CorrectionPanel, wx.ID_ANY,
                                               wx.Bitmap(u"Button/Icon_G29.png", wx.BITMAP_TYPE_ANY),
                                               wx.DefaultPosition, wx.Size(30, 25), 0)
        CorrectionGBSizer.Add(self.G29Text, wx.GBPosition(Y_BASELINE+20, BUTTONGPX2), wx.GBSpan(25, 30), 0, 0)

        self.CorrectionButton = wx.BitmapButton(self.CorrectionPanel,
                                                wx.ID_ANY,wx.Bitmap(u"Button/Button_autolevel.png", wx.BITMAP_TYPE_ANY),
                                                wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
        self.CorrectionButton.SetBitmapHover(wx.Bitmap(u"Button/Button_autolevel_MouseOn.png", wx.BITMAP_TYPE_ANY))
        self.CorrectionButton.SetBackgroundColour(BGCOLOR)
        CorrectionGBSizer.Add(self.CorrectionButton, wx.GBPosition(Y_BASELINE+20, BUTTONGPX2+50), wx.GBSpan(21, 100),
                              wx.ALIGN_BOTTOM, 0)

        self.ACText1 = wx.StaticText(self.CorrectionPanel, wx.ID_ANY, u"Install Laser Module", wx.DefaultPosition,
                                     wx.DefaultSize, 0)
        self.ACText1.SetFont(labelfont)
        CorrectionGBSizer.Add(self.ACText1, wx.GBPosition(Y_BASELINE+20, BUTTONGPX2+150), wx.GBSpan(20, 50),
                              wx.ALIGN_CENTER_VERTICAL, 5)

        self.ACText2 = wx.StaticText(self.CorrectionPanel, wx.ID_ANY,
                                     u"CAUTION! Use eye protection before continuing...",
                                     wx.DefaultPosition, wx.Size(300, 15), 0)

        if platform.system() == "Darwin":
            self.ACText2.SetFont(wx.Font(9, 74, 90, 92, False))
        else:
            self.ACText2.SetFont(wx.Font(7, 74, 90, 92, False))
        self.ACText2.SetForegroundColour(wx.Colour(237, 28, 36))
        CorrectionGBSizer.Add(self.ACText2, wx.GBPosition(Y_BASELINE+45, BUTTONGPX2+150), wx.GBSpan(15, 300), 0, 0)

        self.DoneButton = wx.BitmapButton(self.CorrectionPanel, wx.ID_ANY, wx.Bitmap(u"Button/Button_home.png",
                                                                                 wx.BITMAP_TYPE_ANY),
                                          wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
        self.DoneButton.SetBitmapHover(wx.Bitmap(u"Button/Button_home_MouseOn.png", wx.BITMAP_TYPE_ANY))
        self.DoneButton.SetBackgroundColour(BGCOLOR)
        CorrectionGBSizer.Add(self.DoneButton, wx.GBPosition(Y_BASELINE+20, BUTTONGPX2+220), wx.GBSpan(21, 50), wx.ALIGN_BOTTOM, 0)

        self.CorrectionPanel.SetSizer(CorrectionGBSizer)
        self.CorrectionPanel.Layout()
        ControlSizer.Add(self.CorrectionPanel, 0, wx.EXPAND | wx.ALL, 0)

        # Right Panel 3
        BGCOLOR = wx.Colour(204, 204, 204)
        self.FocalPanel = wx.Panel(self.controlPanel, wx.ID_ANY, wx.DefaultPosition, wx.Size(WIDTH_P2, HEIGHT_P3_1),
                                   wx.TAB_TRAVERSAL)
        self.FocalPanel.SetBackgroundColour(BGCOLOR)
        self.FocalPanel.SetMinSize(wx.Size(WIDTH_P2, HEIGHT_P3_1))
        self.FocalPanel.SetMaxSize(wx.Size(WIDTH_P2, HEIGHT_P3_1))

        FocalGBSizer = wx.GridBagSizer(0, 0)
        FocalGBSizer.SetFlexibleDirection(wx.BOTH)
        FocalGBSizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        FocalGBSizer.SetEmptyCellSize(wx.Size(1, 1))

        Y_BASELINE = 5
        self.FocalImage = wx.StaticBitmap(self.FocalPanel, wx.ID_ANY,
                                          wx.Bitmap(u"Button/Icon_03.png", wx.BITMAP_TYPE_ANY),
                                          wx.DefaultPosition, wx.DefaultSize, 0)
        FocalGBSizer.Add(self.FocalImage, wx.GBPosition(Y_BASELINE, BUTTONGPX1), wx.GBSpan(50, 50), 0, 0)

        self.FocalText = wx.StaticText(self.FocalPanel, wx.ID_ANY, u"Focal\nDistance", wx.DefaultPosition,
                                       wx.Size(60, 30), wx.ALIGN_CENTRE)
        self.FocalText.SetFont(labelfont)
        FocalGBSizer.Add(self.FocalText, wx.GBPosition(Y_BASELINE+50, BUTTONGPX1-5), wx.GBSpan(30, 60), 0, 0)

        Y_BASELINE = 32
        self.FDText1 = wx.StaticText(self.FocalPanel, wx.ID_ANY, u"Laser\nFunction", wx.DefaultPosition,
                                     wx.Size(55, 40), 0)
        self.FDText1.SetFont(labelfont)
        FocalGBSizer.Add(self.FDText1, wx.GBPosition(Y_BASELINE, BUTTONGPX2), wx.GBSpan(40, 55),
                         wx.ALIGN_CENTER_HORIZONTAL, 0)

        self.FDBtnOn = wx.BitmapButton(self.FocalPanel, wx.ID_ANY, wx.Bitmap(u"Button/Button_on.png",
                                                                                 wx.BITMAP_TYPE_ANY),
                                          wx.DefaultPosition,wx.DefaultSize , wx.NO_BORDER)
        self.FDBtnOn.SetBitmapHover(wx.Bitmap(u"Button/Button_on_MouseOn.png", wx.BITMAP_TYPE_ANY))
        self.FDBtnOn.SetBackgroundColour(BGCOLOR)
        FocalGBSizer.Add(self.FDBtnOn, wx.GBPosition(Y_BASELINE+3, BUTTONGPX2+55), wx.GBSpan(20, 40), 0, 0)

        self.FDBtnOff =wx.BitmapButton(self.FocalPanel, wx.ID_ANY, wx.Bitmap(u"Button/Button_off.png",
                                                                                 wx.BITMAP_TYPE_ANY),
                                          wx.DefaultPosition,wx.DefaultSize , wx.NO_BORDER)
        self.FDBtnOff.SetBitmapHover(wx.Bitmap(u"Button/Button_off_MouseOn.png", wx.BITMAP_TYPE_ANY))
        self.FDBtnOff.SetBackgroundColour(BGCOLOR)
        FocalGBSizer.Add(self.FDBtnOff, wx.GBPosition(Y_BASELINE+3, BUTTONGPX2+55+40+5), wx.GBSpan(20, 40), 0, 0)

        self.FDText2 = wx.StaticText(self.FocalPanel, wx.ID_ANY, u"Focal\nDistance", wx.DefaultPosition,
                                     wx.Size(60, 40), 0)
        self.FDText2.SetFont(labelfont)
        FocalGBSizer.Add(self.FDText2, wx.GBPosition(Y_BASELINE, BUTTONGPX2+150), wx.GBSpan(40, 60), 0, 0)

        root.FDValue = NumCtrl(self.FocalPanel, wx.ID_ANY, 10, wx.DefaultPosition, size=wx.Size(60, 24),
                               autoSize=False, min=0, max=99, limited=True, integerWidth=2, fractionWidth=1)
        root.FDValue.SetBackgroundColour(GRAYSCALE_1)
        FocalGBSizer.Add(root.FDValue, wx.GBPosition(BUTTONGPX1+10, BUTTONGPX2+210), wx.GBSpan(24, 60), 0, 0)

        self.FDBtnUp = wx.BitmapButton(self.FocalPanel, wx.ID_ANY,
                                       wx.Bitmap(u"Button/Button_up.png", wx.BITMAP_TYPE_ANY), wx.DefaultPosition,
                                       wx.DefaultSize, wx.NO_BORDER)
        self.FDBtnUp.SetBitmapHover(wx.Bitmap(u"Button/Button_up_MouseOn.png", wx.BITMAP_TYPE_ANY))
        self.FDBtnUp.SetBackgroundColour(BGCOLOR)
        FocalGBSizer.Add(self.FDBtnUp, wx.GBPosition(Y_BASELINE-5, 385), wx.GBSpan(18, 23), 0, 0)

        self.FDBtnDown = wx.BitmapButton(self.FocalPanel, wx.ID_ANY,
                                       wx.Bitmap(u"Button/Button_down.png", wx.BITMAP_TYPE_ANY), wx.DefaultPosition,
                                       wx.DefaultSize, wx.NO_BORDER)
        self.FDBtnDown.SetBitmapHover(wx.Bitmap(u"Button/Button_down_MouseOn.png", wx.BITMAP_TYPE_ANY))
        self.FDBtnDown.SetBackgroundColour(BGCOLOR)
        FocalGBSizer.Add(self.FDBtnDown, wx.GBPosition(Y_BASELINE+16, 385), wx.GBSpan(18, 23), 0, 0)

        self.FDBtnSet = wx.BitmapButton(self.FocalPanel, wx.ID_ANY,
                                       wx.Bitmap(u"Button/Button_set.png", wx.BITMAP_TYPE_ANY), wx.DefaultPosition,
                                       wx.DefaultSize, wx.NO_BORDER)
        self.FDBtnSet.SetBitmapHover(wx.Bitmap(u"Button/Button_set_MouseOn.png", wx.BITMAP_TYPE_ANY))
        self.FDBtnSet.SetBackgroundColour(BGCOLOR)
        FocalGBSizer.Add(self.FDBtnSet, wx.GBPosition(Y_BASELINE+3, 414), wx.GBSpan(20, 50), 0, 0)

        self.FocalPanel.SetSizer(FocalGBSizer)
        self.FocalPanel.Layout()
        ControlSizer.Add(self.FocalPanel, 0, wx.EXPAND | wx.ALL, 0)

        # Right Panel 4
        BGCOLOR = wx.Colour(153, 153, 153)
        self.SetupPanel = wx.Panel(self.controlPanel, wx.ID_ANY, wx.DefaultPosition, wx.Size(WIDTH_P2, 250),
                                   wx.TAB_TRAVERSAL)
        self.SetupPanel.SetBackgroundColour(BGCOLOR)
        self.SetupPanel.SetMinSize(wx.Size(WIDTH_P2, 250))
        self.SetupPanel.SetMaxSize(wx.Size(WIDTH_P2, 250))

        SetupGBSizer = wx.GridBagSizer(0, 0)
        SetupGBSizer.SetFlexibleDirection(wx.BOTH)
        SetupGBSizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        SetupGBSizer.SetEmptyCellSize(wx.Size(1, 1))

        SetupGBSizer.SetMinSize(wx.Size(WIDTH_P2, 250))

        # Right Panel 4-1
        Y_BASELINE = 20
        self.ResolutionImage = wx.StaticBitmap(self.SetupPanel, wx.ID_ANY,
                                               wx.Bitmap(u"Button/Icon_04.png", wx.BITMAP_TYPE_ANY),
                                               wx.DefaultPosition, wx.DefaultSize, 0)
        SetupGBSizer.Add(self.ResolutionImage, wx.GBPosition(Y_BASELINE, BUTTONGPX1), wx.GBSpan(50, 50), 0, 0)

        self.ResText = wx.StaticText(self.SetupPanel, wx.ID_ANY, u'Resolution', wx.DefaultPosition, wx.Size(80, -1),
                                     wx.ALIGN_CENTRE)
        self.ResText.SetFont(labelfont)
        self.ResText.SetForegroundColour(wx.Colour(255, 255, 255))
        SetupGBSizer.Add(self.ResText, wx.GBPosition(Y_BASELINE+50, 10), wx.GBSpan(10, 80), 0, 0)

        self.ResBtnLow = wx.BitmapButton(self.SetupPanel, wx.ID_ANY,
                                       wx.Bitmap(u"Button/Button_dark.png", wx.BITMAP_TYPE_ANY), wx.DefaultPosition,
                                       wx.DefaultSize, wx.NO_BORDER)
        self.ResBtnLow.SetBitmapHover(wx.Bitmap(u"Button/Button_dark_MouseOn.png", wx.BITMAP_TYPE_ANY))
        self.ResBtnLow.SetBackgroundColour(BGCOLOR)
        SetupGBSizer.Add(self.ResBtnLow, wx.GBPosition(Y_BASELINE+20, BUTTONGPX2), wx.GBSpan(20, 50), 0, 0)

        self.ResBtnHigh = wx.BitmapButton(self.SetupPanel, wx.ID_ANY,
                                       wx.Bitmap(u"Button/Button_light.png", wx.BITMAP_TYPE_ANY), wx.DefaultPosition,
                                       wx.DefaultSize, wx.NO_BORDER)
        self.ResBtnHigh.SetBitmapHover(wx.Bitmap(u"Button/Button_light_MouseOn.png", wx.BITMAP_TYPE_ANY))
        self.ResBtnHigh.SetBackgroundColour(BGCOLOR)
        SetupGBSizer.Add(self.ResBtnHigh, wx.GBPosition(Y_BASELINE+20, BUTTONGPX2+50+5), wx.GBSpan(20, 50), 0, 0)

        root.ResValue = NumCtrl(self.SetupPanel, wx.ID_ANY, 100, wx.DefaultPosition, size=wx.Size(100, 20),
                                autoSize=False, min=1, max=9999, limited=True, integerWidth=5,
                                style=wx.TE_PROCESS_ENTER)
#         root.ResValue.SetBackgroundColour(GRAYSCALE_1)
        SetupGBSizer.Add(root.ResValue, wx.GBPosition(Y_BASELINE+20, BUTTONGPX2+165), wx.GBSpan(20 , 100), 0, 0)

        root.ResType = wx.ComboBox(self.SetupPanel, -1, choices=["Pixel/cm", "Pixel/inch"], style=wx.CB_READONLY,
                                   size=(100, -1))
        root.ResType.SetSelection(0)
#        root.ResType.SetBackgroundColour(GRAYSCALE_1)
        SetupGBSizer.Add(root.ResType, wx.GBPosition(Y_BASELINE+18, BUTTONGPX2+270), wx.GBSpan(30, 100), 0, 0)


        # Right Panel 4-2
        Y_BASELINE = 85
        self.SpeedImage = wx.StaticBitmap(self.SetupPanel, wx.ID_ANY,
                                          wx.Bitmap(u"Button/Icon_05.png", wx.BITMAP_TYPE_ANY),
                                          wx.DefaultPosition, wx.Size(50,40), 0)
        SetupGBSizer.Add(self.SpeedImage, wx.GBPosition(Y_BASELINE, BUTTONGPX1), wx.GBSpan(40, 50), 0, 0)

        self.SpeedText = wx.StaticText(self.SetupPanel, wx.ID_ANY, u"Speed", wx.DefaultPosition, wx.Size(60, 15),
                                       wx.ALIGN_CENTRE)
        self.SpeedText.SetFont(labelfont)
        self.SpeedText.SetForegroundColour(wx.Colour(255, 255, 255))
        SetupGBSizer.Add(self.SpeedText, wx.GBPosition(Y_BASELINE+40, 20), wx.GBSpan(15, 60), wx.ALIGN_CENTER_HORIZONTAL, 0)

        Y_BASELINE = 90
        self.SpeedText1 = wx.StaticText(self.SetupPanel, wx.ID_ANY, u"Engrave Speed", wx.DefaultPosition,
                                        wx.Size(100, 15), 0)
        self.SpeedText1.SetFont(labelfont)
        self.SpeedText1.SetForegroundColour(wx.Colour(255, 255, 255))
        SetupGBSizer.Add(self.SpeedText1, wx.GBPosition(Y_BASELINE, BUTTONGPX2), wx.GBSpan(15, 100), 0, 0)

        root.EngSpeed = NumCtrl(self.SetupPanel, wx.ID_ANY, 200, wx.DefaultPosition, size=wx.Size(100, 20),
                                autoSize=False, min=0, max=9999, limited=True, integerWidth=5)
        root.EngSpeed.SetBackgroundColour(GRAYSCALE_1)
        SetupGBSizer.Add(root.EngSpeed, wx.GBPosition(Y_BASELINE+20, BUTTONGPX2), wx.GBSpan(20 , 100), 0, 0)

        self.SpeedText2 = wx.StaticText(self.SetupPanel, wx.ID_ANY, u"mm/min", wx.DefaultPosition, wx.Size(60, 15), 0)
        self.SpeedText2.SetForegroundColour(wx.Colour(255, 255, 255))
        self.SpeedText2.SetFont(labelfont)
        SetupGBSizer.Add(self.SpeedText2, wx.GBPosition(Y_BASELINE+26, BUTTONGPX2+105), wx.GBSpan(15, 60), 0, 0)

        self.SpeedText3 = wx.StaticText(self.SetupPanel, wx.ID_ANY, u"Travel Speed", wx.DefaultPosition,
                                        wx.Size(100, 15), 0)
        self.SpeedText3.SetFont(labelfont)
        self.SpeedText3.SetForegroundColour(wx.Colour(255, 255, 255))
        SetupGBSizer.Add(self.SpeedText3, wx.GBPosition(Y_BASELINE, BUTTONGPX2+165), wx.GBSpan(15, 100), 0, 5)

        root.TraSpeed = NumCtrl(self.SetupPanel, wx.ID_ANY, 3000, wx.DefaultPosition, size=wx.Size(100, 20),
                                autoSize=False, min=0, max=99999, limited=True, integerWidth=5)
        root.TraSpeed.SetBackgroundColour(GRAYSCALE_1)
        SetupGBSizer.Add(root.TraSpeed, wx.GBPosition(Y_BASELINE+20, BUTTONGPX2+165), wx.GBSpan(20, 100), 0, 0)

        self.SpeedText4 = wx.StaticText(self.SetupPanel, wx.ID_ANY, u"mm/min", wx.DefaultPosition, wx.Size(60, 15), 0)
        self.SpeedText4.SetForegroundColour(wx.Colour(255, 255, 255))
        self.SpeedText4.SetFont(labelfont)
        SetupGBSizer.Add(self.SpeedText4, wx.GBPosition(Y_BASELINE+26, BUTTONGPX2+270), wx.GBSpan(15, 60), 0, 0)

        # Right Panel 4-3
        Y_BASELINE = 150
        self.FDMImage = wx.StaticBitmap(self.SetupPanel, wx.ID_ANY,
                                        wx.Bitmap(u"Button/Icon_06.png", wx.BITMAP_TYPE_ANY),
                                        wx.DefaultPosition, wx.DefaultSize, 0)
        SetupGBSizer.Add(self.FDMImage, wx.GBPosition(Y_BASELINE, BUTTONGPX1), wx.GBSpan(50, 50), 0, 0)

        self.FDMText = wx.StaticText(self.SetupPanel, wx.ID_ANY, u"Focal Distance\nwith Material", wx.DefaultPosition,
                                     wx.Size(90, 40), wx.ALIGN_CENTRE)
        self.FDMText.SetFont(labelfont)
        self.FDMText.SetForegroundColour(wx.Colour(255, 255, 255))
        SetupGBSizer.Add(self.FDMText, wx.GBPosition(Y_BASELINE+50, 5), wx.GBSpan(40, 90), wx.ALIGN_CENTER_HORIZONTAL, 0)

        self.FDMText1 = wx.StaticText(self.SetupPanel, wx.ID_ANY, u"Focal", wx.DefaultPosition, wx.Size(100, 15), 0)
        self.FDMText1.SetFont(labelfont)
        self.FDMText1.SetForegroundColour(wx.Colour(255, 255, 255))
        SetupGBSizer.Add(self.FDMText1, wx.GBPosition(Y_BASELINE+20, BUTTONGPX2), wx.GBSpan(10, 100), 0, 0)

        self.FDMText2 = wx.StaticText(self.SetupPanel, wx.ID_ANY, u"Thickness", wx.DefaultPosition, wx.Size(100, 15), 0)
        self.FDMText2.SetFont(labelfont)
        self.FDMText2.SetForegroundColour(wx.Colour(255, 255, 255))
        SetupGBSizer.Add(self.FDMText2, wx.GBPosition(Y_BASELINE+20, BUTTONGPX2+165), wx.GBSpan(15, 100), 0, 0)

        self.FDMtextCtrl = wx.StaticText(self.SetupPanel, wx.ID_ANY, "10.0", wx.DefaultPosition, wx.Size(80, 30), 0)
        Y_OFFSET = 35
        if platform.system() == "Darwin":
            self.FDMtextCtrl.SetFont(wx.Font(28, 74, 90, 90, False))
            Y_OFFSET = 30
        else:
            self.FDMtextCtrl.SetFont(wx.Font(18, 74, 90, 90, False))
        self.FDMtextCtrl.SetForegroundColour(wx.Colour(255, 255, 255))
        self.FDMtextCtrl.SetBackgroundColour(wx.Colour(153, 153, 153))
        SetupGBSizer.Add(self.FDMtextCtrl, wx.GBPosition(Y_BASELINE+Y_OFFSET, BUTTONGPX2), wx.GBSpan(30, 80), 0, 0)

        self.thicklabel = wx.StaticText(self.SetupPanel, wx.ID_ANY, u"mm", wx.DefaultPosition, wx.Size(30, 15), 0)
        self.thicklabel.SetForegroundColour(wx.Colour(255, 255, 255))
        self.thicklabel.SetFont(labelfont)
        SetupGBSizer.Add(self.thicklabel, wx.GBPosition(Y_BASELINE+Y_OFFSET+10, BUTTONGPX2+270), wx.GBSpan(15, 30), 0, 0)

        self.FDMPlusImage = wx.StaticBitmap(self.SetupPanel, wx.ID_ANY,
                                            wx.Bitmap(u"Button/Icon_Plus.png", wx.BITMAP_TYPE_ANY),
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        SetupGBSizer.Add(self.FDMPlusImage, wx.GBPosition(Y_BASELINE+40, BUTTONGPX2+105), wx.GBSpan(25, 25), 0, 0)

        # root.Thickness = NumCtrl(self.SetupPanel, wx.ID_ANY, 0, wx.DefaultPosition, size=wx.Size(110, 20),
        #                                 integerWidth=3, fractionWidth=2, autoSize=False)
        root.Thickness = NumCtrl(self.SetupPanel, wx.ID_ANY, 0, wx.DefaultPosition, size=wx.Size(100, 20),
                                 autoSize=False, min=0, max=9999, limited=True, fractionWidth=1, integerWidth=5)
        root.Thickness.SetBackgroundColour(GRAYSCALE_1)
        SetupGBSizer.Add( root.Thickness, wx.GBPosition(Y_BASELINE+40, BUTTONGPX2+165), wx.GBSpan(20, 100), 0, 0)

        self.SetupPanel.SetSizer(SetupGBSizer)
        self.SetupPanel.Layout()
        ControlSizer.Add(self.SetupPanel, 0, 0, 0)

        # Right Panel 5
        BGCOLOR = wx.Colour(128, 128, 128)
        self.ImportPanel = wx.Panel(self.controlPanel, wx.ID_ANY, wx.DefaultPosition, wx.Size(WIDTH_P2, 90),
                                    wx.TAB_TRAVERSAL)
        self.ImportPanel.SetBackgroundColour(BGCOLOR)
        self.ImportPanel.SetMinSize(wx.Size(WIDTH_P2, 90))
        self.ImportPanel.SetMaxSize(wx.Size(WIDTH_P2, 90))

        ImpotyGBSizer = wx.GridBagSizer(0, 0)
        ImpotyGBSizer.SetFlexibleDirection(wx.BOTH)
        ImpotyGBSizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        ImpotyGBSizer.SetEmptyCellSize(wx.Size(1, 1))
        ImpotyGBSizer.SetMinSize(wx.Size(115, 90))

        Y_BASELINE = 15
        self.ImportImage = wx.StaticBitmap(self.ImportPanel, wx.ID_ANY,
                                           wx.Bitmap(u"Button/Icon_07.png", wx.BITMAP_TYPE_ANY),
                                           wx.DefaultPosition, wx.Size(50,50), 0)
        ImpotyGBSizer.Add(self.ImportImage, wx.GBPosition(15, BUTTONGPX1), wx.GBSpan(50, 50), 0, 0)

        self.ImportText = wx.StaticText(self.ImportPanel, wx.ID_ANY, u"Import", wx.DefaultPosition, wx.Size(60, -1),
                                        wx.ALIGN_CENTRE)
        self.ImportText.SetFont(labelfont)
        self.ImportText.SetForegroundColour(wx.Colour(255, 255, 255))

        ImpotyGBSizer.Add(self.ImportText, wx.GBPosition(Y_BASELINE+50, BUTTONGPX1-5), wx.GBSpan(15, 60), 0, 0)

        root.FilePathLabel = wx.TextCtrl(self.ImportPanel, wx.ID_ANY, "", wx.DefaultPosition, wx.Size(280, 25),
                                         wx.TE_READONLY)
        root.FilePathLabel.SetForegroundColour(wx.Colour(0, 0, 0))
        root.FilePathLabel.SetBackgroundColour(wx.Colour(255, 255, 255))
        root.FilePathLabel.SetMaxSize(wx.Size(280, 25))
        root.FilePathLabel.SetMinSize(wx.Size(280, 25))
        root.FilePathLabel.SetBackgroundColour(GRAYSCALE_1)
        ImpotyGBSizer.Add(root.FilePathLabel, wx.GBPosition(Y_BASELINE+20, BUTTONGPX2), wx.GBSpan(25, 280), 0, 0)

        self.ImportBtn = wx.BitmapButton(self.ImportPanel, wx.ID_ANY,
                                       wx.Bitmap(u"Button/Button_open.png", wx.BITMAP_TYPE_ANY), wx.DefaultPosition,
                                       wx.DefaultSize, wx.NO_BORDER)
        self.ImportBtn.SetBitmapHover(wx.Bitmap(u"Button/Button_open_MouseOn.png", wx.BITMAP_TYPE_ANY))
        self.ImportBtn.SetBackgroundColour(BGCOLOR)
        ImpotyGBSizer.Add(self.ImportBtn, wx.GBPosition(Y_BASELINE+22, BUTTONGPX2+280+5), wx.GBSpan(20, 60), 0, 0)

        self.ImportPanel.SetSizer(ImpotyGBSizer)
        self.ImportPanel.Layout()
        ControlSizer.Add(self.ImportPanel, 0, wx.EXPAND, 0)

        # Right Panel 6
        self.ActionPanel = wx.Panel(self.controlPanel, wx.ID_ANY, wx.DefaultPosition, wx.Size(WIDTH_P2, HEIGHT_P3_1),
                                    wx.TAB_TRAVERSAL)
        BGCOLOR = wx.Colour(102, 102, 102)
        self.ActionPanel.SetBackgroundColour(BGCOLOR)
        self.ActionPanel.SetMinSize(wx.Size(WIDTH_P2, HEIGHT_P3_1))
        self.ActionPanel.SetMaxSize(wx.Size(WIDTH_P2, HEIGHT_P3_1))

        ActionGBSizer = wx.GridBagSizer(0, 0)
        ActionGBSizer.SetFlexibleDirection(wx.BOTH)
        ActionGBSizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        ActionGBSizer.SetEmptyCellSize(wx.Size(1, 1))

        ActionGBSizer.SetMinSize(wx.Size(WIDTH_P2, HEIGHT_P3_1))

        # Preview btn
        Y_BASELINE = 10
        Y_BASELINE2 = Y_BASELINE+50
        BTNXPOS = BUTTONGPX1
        BTNWIDTH = 40
        BTNXSPACE = 40
        self.ActPreviewBtn = wx.BitmapButton(self.ActionPanel, wx.ID_ANY,
                                             wx.Bitmap(u"Button/Button_preview.png", wx.BITMAP_TYPE_ANY),
                                             wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
        self.ActPreviewBtn.SetBitmapHover( wx.Bitmap(u"Button/Button_preview_MouseOn.png", wx.BITMAP_TYPE_ANY))
        self.ActPreviewBtn.SetBackgroundColour(BGCOLOR)
        ActionGBSizer.Add(self.ActPreviewBtn, wx.GBPosition(Y_BASELINE, BTNXPOS), wx.GBSpan(50, 50), 0, 0)

        self.ActPreviewLabel = wx.StaticText(self.ActionPanel, wx.ID_ANY, u"Preview", wx.DefaultPosition,
                                             wx.Size(60, 20), wx.ALIGN_CENTRE)
        self.ActPreviewLabel.SetFont(labelfont)
        self.ActPreviewLabel.SetForegroundColour(wx.Colour(255, 255, 255))
        ActionGBSizer.Add(self.ActPreviewLabel, wx.GBPosition(Y_BASELINE2, BTNXPOS-5), wx.GBSpan(10, 60), 0, 0)

        # Start btn
        BTNXPOS += BTNWIDTH+BTNXSPACE
        root.printbtn = wx.BitmapButton(self.ActionPanel, wx.ID_ANY,
                                           wx.Bitmap(u"Button/Button_play.png", wx.BITMAP_TYPE_ANY),
                                           wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
        root.printbtn.SetBitmapHover(wx.Bitmap(u"Button/Button_play_MouseOn.png", wx.BITMAP_TYPE_ANY))
        root.printbtn.SetBackgroundColour(BGCOLOR)
        ActionGBSizer.Add(root.printbtn, wx.GBPosition(Y_BASELINE, BTNXPOS), wx.GBSpan(50, 50), 0, 0)

        self.ActStartLabel = wx.StaticText(self.ActionPanel, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.Size(60, 20),
                                           wx.ALIGN_CENTRE)
        self.ActStartLabel.SetFont(labelfont)
        self.ActStartLabel.SetForegroundColour(wx.Colour(255, 255, 255))
        ActionGBSizer.Add(self.ActStartLabel, wx.GBPosition(Y_BASELINE2, BTNXPOS-5), wx.GBSpan(10, 60), 0, 0)

        # Pause btn
        BTNXPOS += BTNWIDTH+BTNXSPACE
        root.pausebtn = wx.BitmapButton(self.ActionPanel, wx.ID_ANY,
                                           wx.Bitmap(u"Button/Button_pause.png", wx.BITMAP_TYPE_ANY),
                                           wx.DefaultPosition, wx.Size(50, 50), wx.NO_BORDER)
        root.pausebtn.SetBitmapHover(wx.Bitmap(u"Button/Button_pause_MouseOn.png", wx.BITMAP_TYPE_ANY))
        root.pausebtn.SetBackgroundColour(BGCOLOR)
        ActionGBSizer.Add(root.pausebtn, wx.GBPosition(Y_BASELINE, BTNXPOS), wx.GBSpan(50, 50), 0, 0)

        self.ActPauseLabel = wx.StaticText(self.ActionPanel, wx.ID_ANY, u"Pause", wx.DefaultPosition, wx.Size(60, 20),
                                           wx.ALIGN_CENTRE)
        self.ActPauseLabel.SetFont(labelfont)
        self.ActPauseLabel.SetForegroundColour(wx.Colour(255, 255, 255))
        ActionGBSizer.Add(self.ActPauseLabel, wx.GBPosition(Y_BASELINE2, BTNXPOS-5), wx.GBSpan(10, 60), 0, 0)

        # Stop btn
        BTNXPOS += BTNWIDTH+BTNXSPACE
        root.offbtn = wx.BitmapButton(self.ActionPanel, wx.ID_ANY,
                                          wx.Bitmap(u"Button/Button_stop.png", wx.BITMAP_TYPE_ANY),
                                          wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
        root.offbtn.SetBitmapHover(wx.Bitmap(u"Button/Button_stop_MouseOn.png"))
        root.offbtn.SetBackgroundColour(BGCOLOR)
        ActionGBSizer.Add(root.offbtn, wx.GBPosition(Y_BASELINE, BTNXPOS), wx.GBSpan(50, 50), 0, 0)

        self.ActStopLabel = wx.StaticText(self.ActionPanel, wx.ID_ANY, u"Stop", wx.DefaultPosition, wx.Size(60, 20),
                                          wx.ALIGN_CENTRE)
        self.ActStopLabel.SetFont(labelfont)
        self.ActStopLabel.SetForegroundColour(wx.Colour(255, 255, 255))
        ActionGBSizer.Add(self.ActStopLabel, wx.GBPosition(Y_BASELINE2, BTNXPOS-5), wx.GBSpan(10, 60), 0, 0)

        # Export btn
        BTNXPOS += BTNWIDTH+BTNXSPACE
        self.ActExportBtn = wx.BitmapButton(self.ActionPanel, wx.ID_ANY,
                                            wx.Bitmap(u"Button/Button_export.png", wx.BITMAP_TYPE_ANY),
                                            wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
        self.ActExportBtn.SetBitmapHover(wx.Bitmap(u"Button/Button_export_MouseOn.png"))
        self.ActExportBtn.SetBackgroundColour(BGCOLOR)
        ActionGBSizer.Add(self.ActExportBtn, wx.GBPosition(Y_BASELINE, BTNXPOS), wx.GBSpan(50, 50), 0, 0)

        self.ActExportLabel = wx.StaticText(self.ActionPanel, wx.ID_ANY, u"Export", wx.DefaultPosition, wx.Size(60, 20),
                                            wx.ALIGN_CENTRE)
        self.ActExportLabel.SetFont(labelfont)
        self.ActExportLabel.SetForegroundColour(wx.Colour(255, 255, 255))
        ActionGBSizer.Add(self.ActExportLabel, wx.GBPosition(Y_BASELINE2, BTNXPOS-5), wx.GBSpan(10, 60), 0, 0)

        self.ActionPanel.SetSizer(ActionGBSizer)
        self.ActionPanel.Layout()
        ControlSizer.Add(self.ActionPanel, 0, wx.EXPAND, 0)

        self.controlPanel.SetSizer(ControlSizer)
        self.controlPanel.Layout()
        mainSizer.Add(self.controlPanel, 0, 0, 0)

        self.SetSizer(mainSizer)
        self.Layout()

        self.BindCommand(root)

        #Hide checkmark after layout
        root.checkmark.Hide()

    def __del__(self):
        pass

    def BindCommand(self, root):
        root.rescanbtn.Bind(wx.EVT_BUTTON, root.rescanports)
        root.connectbtn.Bind(wx.EVT_BUTTON, root.connect)
        # root.resetbtn.Bind(wx.EVT_BUTTON, root.reset)

        def sendGCodeCommand(command):
            def sendCmd(event):
                root.sendGCodeCommand(command)
            return sendCmd

        self.CorrectionButton.Bind(wx.EVT_BUTTON, sendGCodeCommand('G29'))
        self.DoneButton.Bind(wx.EVT_BUTTON, sendGCodeCommand('G28'))

        self.FDBtnOn.Bind(wx.EVT_BUTTON, sendGCodeCommand('M03'))
        self.FDBtnOff.Bind(wx.EVT_BUTTON, sendGCodeCommand('M05'))

        def addValue(value):
            def addvalue(event):
                newValue = str(float(root.FDValue.GetValue())+float(value))
                root.FDValue.SetValue(newValue)
                root.FDValue.Refresh()
                self.FDMtextCtrl.SetLabel(newValue)
                root.sendGCodeCommand('G0 Z'+newValue)
            return addvalue
        self.FDBtnUp.Bind(wx.EVT_BUTTON, addValue(0.1))
        self.FDBtnDown.Bind(wx.EVT_BUTTON, addValue(-0.1))
        self.FDBtnSet.Bind(wx.EVT_BUTTON, addValue(0))

        def setEngSpeed(value):
            def setengspeed(event):
                root.EngSpeed.SetValue(value)
                root.EngSpeed.Layout()
            return setengspeed

        self.ResBtnHigh.Bind(wx.EVT_BUTTON, setEngSpeed(400))
        self.ResBtnLow.Bind(wx.EVT_BUTTON, setEngSpeed(200))

        root.ResValue.Bind(wx.EVT_TEXT, root.reloadPNG)
        root.ResType.Bind(wx.EVT_COMBOBOX, root.reloadPNG)

        self.ImportBtn.Bind(wx.EVT_BUTTON, root.loadpng)

        self.ActPreviewBtn.Bind(wx.EVT_BUTTON, root.LaserPreview)
        root.printbtn.Bind(wx.EVT_BUTTON, root.LaserStart)
        root.pausebtn.Bind(wx.EVT_BUTTON, root.pause)
        root.offbtn.Bind(wx.EVT_BUTTON, root.off)
        self.ActExportBtn.Bind(wx.EVT_BUTTON, root.savefile)
