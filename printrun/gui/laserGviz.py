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

import math

from printrun.gviz import *
from .viz import *
from .log import LogPane

class LaserGviz( Gviz ):
    def __init__(self, parent, size = (200, 200), build_dimensions = [200, 200, 100, 0, 0, 0], grid = (10, 50),
                 extrusion_width = 0.5, bgcolor = "#000000", realparent = None):
        super( LaserGviz, self).__init__(parent, size, build_dimensions, grid, extrusion_width, bgcolor, realparent)
        self.SetMinSize(wx.Size(560, 560))
        self.SetMaxSize(wx.Size(560, 560))

    def repaint_everything(self):
        width = self.scale[0] * self.build_dimensions[0]
        height = self.scale[1] * self.build_dimensions[1]
        self.blitmap = wx.EmptyBitmap(width + 1, height + 1, -1)
        dc = wx.MemoryDC()
        dc.SelectObject(self.blitmap)
        dc.SetBackground(wx.Brush((252, 238, 0)))
        dc.Clear()
        dc.SetBrush(wx.Brush(colour='black', style=wx.TRANSPARENT))
        # dc.SetPen(wx.Pen(wx.Colour(252, 238, 0)))
        center_x = 0.5 + self.build_dimensions[0]*self.scale[0]/2.
        center_y = 0.5 + self.build_dimensions[1]*self.scale[1]/2.
        radius = self.build_dimensions[0]*self.scale[0]/2.
        dc.SetPen(wx.Pen(colour='black', width=2))
        dc.DrawCircle(center_x, center_y, radius)
        dc.SetPen(wx.Pen(colour='black', width=3))
        dc.DrawLine(center_x, 0, center_x, radius*2-1)
        dc.DrawLine(0, center_y, radius*2-1, center_y)
        dc.SetPen(wx.Pen(colour='black', width=1))
        grid_unit = 10
        for x in xrange(int(self.build_dimensions[0] / grid_unit) + 1):
            draw_x = self.scale[0] * x * grid_unit
            chordlength = radius*radius - (center_x - draw_x)*(center_x - draw_x)
            if chordlength > 0.:
                chordlength = math.sqrt(chordlength)*2
            else:
                chordlength = 0.
            dc.DrawLine(draw_x, center_y-chordlength/2., draw_x, center_y+chordlength/2.)
        for y in xrange(int(self.build_dimensions[1] / grid_unit) + 1):
            draw_y = self.scale[1] * (self.build_dimensions[1] - y * grid_unit)
            chordlength = radius*radius - (center_y - draw_y)*(center_y - draw_y)
            if chordlength > 0.:
                chordlength = math.sqrt(chordlength)*2
            else:
                chordlength = 0.
            dc.DrawLine(center_x-chordlength/2., draw_y, center_x+chordlength/2., draw_y)

        if self.layerindex < len(self.layers) and self.layerindex in self.lines:
            for layer_i in range(max(0, self.layerindex - 6), self.layerindex):
                self._drawlines(dc, self.lines[layer_i], self.fades[self.layerindex - layer_i - 1])
                self._drawarcs(dc, self.arcs[layer_i], self.fades[self.layerindex - layer_i - 1])
            self._drawlines(dc, self.lines[self.layerindex], self.pens[self.layerindex])
            self._drawarcs(dc, self.arcs[self.layerindex], self.arcpens[self.layerindex])

        self._drawlines(dc, self.hilight, self.hlpen)
        self._drawarcs(dc, self.hilightarcs, self.hlpen)

        self.paint_hilights(dc)

        dc.SelectObject(wx.NullBitmap)

class LaserVizPane(wx.GridBagSizer):
    def __init__(self, root, parentpanel = None):
        super(LaserVizPane, self).__init__(0, 0)
        self.SetFlexibleDirection(wx.BOTH)
        self.SetEmptyCellSize(wx.Size(1, 1))
        self.SetMinSize(wx.Size(700, 700))

        root.gviz = LaserGviz(parentpanel, (560, 560),
                              build_dimensions = [220, 220, 100, -110, -110, 0],
                              grid = (root.settings.preview_grid_step1, root.settings.preview_grid_step2),
                              extrusion_width = root.settings.preview_extrusion_width,
                              bgcolor = "#FCEE00")

        #root.gviz.SetToolTip(wx.ToolTip(_("Click to examine / edit\n  layers of loaded file")))
        root.gviz.showall = 1
        # root.gwindow = GvizWindow(build_dimensions = root.build_dimensions_list,
        #                           grid = (root.settings.preview_grid_step1, root.settings.preview_grid_step2),
        #                           extrusion_width = root.settings.preview_extrusion_width,
        #                           bgcolor = root.bgcolor)
        #
        # root.gwindow.Bind(wx.EVT_CLOSE, lambda x: root.gwindow.Hide())
        if not isinstance(root.gviz, NoViz):
            self.Add(root.gviz, wx.GBPosition(70, 100), wx.GBSpan(560, 1))

        root.laserLogpanel = LogPane(root, parentpanel)
        root.laserLogpanel.SetMinSize( wx.Size(610, 700))
        self.Add(root.laserLogpanel, wx.GBPosition(0, 91), wx.GBSpan(700, 1), wx.EXPAND)
        root.laserLogpanel.ShowItems(False)

        X_BASELINE = 20
        Y_BASELINE = 20
        root.pathbtn = wx.BitmapButton(parentpanel, wx.ID_ANY,
                                       wx.Bitmap(u"Button/Button_path.png", wx.BITMAP_TYPE_ANY),
                                       wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
        root.pathbtn.SetBitmapHover(wx.Bitmap(u"Button/Button_path_MouseOn.png"))
        root.pathbtn.SetBackgroundColour( wx.Colour(252, 238, 0))
        self.Add(root.pathbtn, wx.GBPosition(Y_BASELINE, X_BASELINE), wx.GBSpan(50, 50), 0, 0)

        pathLabel = wx.StaticText(parentpanel, wx.ID_ANY, u"Paths", wx.DefaultPosition, wx.Size(70, 15),
                                           wx.ALIGN_CENTRE)
        pathLabel.SetFont(wx.Font(10, 74, 90, 92, False))
        self.Add(pathLabel, wx.GBPosition(Y_BASELINE+50, X_BASELINE-10), wx.GBSpan(15, 70), 0, 5)

        root.consolebtn = wx.BitmapButton(parentpanel, wx.ID_ANY,
                                          wx.Bitmap(u"Button/Button_console.png", wx.BITMAP_TYPE_ANY),
                                          wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
        root.consolebtn.SetBitmapHover(wx.Bitmap(u"Button/Button_console_MouseOn.png"))
        root.consolebtn.SetBackgroundColour( wx.Colour(252, 238, 0))
        self.Add(root.consolebtn, wx.GBPosition(Y_BASELINE+80, X_BASELINE), wx.GBSpan(50, 50), 0, 0)

        consoleLabel = wx.StaticText(parentpanel, wx.ID_ANY, u"Console", wx.DefaultPosition, wx.Size(70, 15),
                                           wx.ALIGN_CENTRE)
        consoleLabel.SetFont(wx.Font(10, 74, 90, 92, False))
        self.Add(consoleLabel, wx.GBPosition(Y_BASELINE+130, X_BASELINE-10), wx.GBSpan(15, 70), 0, 0)

        CCIcon = wx.StaticBitmap(parentpanel, wx.ID_ANY, wx.Bitmap(u"Button/CC.png", wx.BITMAP_TYPE_ANY),
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.Add(CCIcon, wx.GBPosition(600, 15), wx.GBSpan(90, 60), 0, 0)

        # Bind Events

        def ShowConsole(event):
            root.gviz.Hide()
            root.laserLogpanel.ShowItems(True)
            root.logbox.SetMinSize((610, 600))
            root.logbox.SetMinSize((610, 600))
            self.Layout()

        def ShowPath(event):
            root.gviz.Show()
            root.laserLogpanel.ShowItems(False)
            self.Layout()

        root.pathbtn.Bind(wx.EVT_BUTTON, ShowPath)
        root.consolebtn.Bind(wx.EVT_BUTTON, ShowConsole)



