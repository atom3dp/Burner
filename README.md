Burner is an open source python based laser engraving software for ATOM2.0.
http://www.atom3dp.com/

Burner is a fork of Printrun, with a png to gcode algorithm is adopted from 305engineering.
https://github.com/kliment/Printrun
https://github.com/305engineering/Inkscape

Built version can be download here
http://www.atom3dp.com/zh/support-ch/

## RUNNING FROM SOURCE

Run Printrun for source if you want to test out the latest features.

### Dependencies

To use pronterface, you need:

  * python (ideally 2.6.x or 2.7.x),
  * pyserial (or python-serial on ubuntu/debian)
  * pyreadline (not needed on Linux) and
  * argparse (installed by default with python >= 2.7)
  * wxPython (some features such as Tabbed mode work better with wx 2.9)
  * pyglet
  * numpy (for 3D view)
  * pycairo (to use Projector feature)
  * cairosvg (to use Projector feature)
  * dbus (to inhibit sleep on some Linux systems)

Please see specific instructions for Windows and Mac OS X below. Under Linux, you should use your package manager directly (see the "GETTING PRINTRUN" section), or pip:

```pip install -r requirements.txt```

### Cython-based G-Code parser

Printrun default G-Code parser is quite memory hungry, but we also provide a much lighter one which just needs an extra build-time dependency (Cython), plus compiling the extension with:

    python setup.py build_ext --inplace

The warning message

    WARNING:root:Memory-efficient GCoder implementation unavailable: No module named gcoder_line

means that this optimized G-Code parser hasn't been compiled. To get rid of it and benefit from the better implementation, please install Cython and run the command above.

### Windows

Download the following, and install in this order:

  1. http://python.org/ftp/python/2.7.2/python-2.7.2.msi
  2. http://pypi.python.org/packages/any/p/pyserial/pyserial-2.5.win32.exe
  3. http://downloads.sourceforge.net/wxpython/wxPython2.8-win32-unicode-2.8.12.0-py27.exe
  4. https://pypi.python.org/packages/any/p/pyreadline/pyreadline-1.7.1.win32.exe
  5. http://pyglet.googlecode.com/files/pyglet-1.1.4.zip

For the last one, you will need to unpack it, open a command terminal, 
go into the the directory you unpacked it in and run
`python setup.py install`

### Mac OS X Lion

  1. Ensure that the active Python is the system version. (`brew uninstall python` or other appropriate incantations)
  2. Download an install [wxPython2.8-osx-unicode] matching to your python version (most likely 2.7 on Lion, 
        check with: python --version) from: http://wxpython.org/download.php#stable
  Known to work PythonWX: http://superb-sea2.dl.sourceforge.net/project/wxpython/wxPython/2.8.12.1/wxPython2.8-osx-unicode-2.8.12.1-universal-py2.7.dmg
  3. Download and unpack pyserial from http://pypi.python.org/packages/source/p/pyserial/pyserial-2.5.tar.gz
  4. In a terminal, change to the folder you unzipped to, then type in: `sudo python setup.py install`
  5. Repeat 4. with http://http://pyglet.googlecode.com/files/pyglet-1.1.4.zip

The tools will probably run just fine in 64bit on Lion, you don't need to mess
with any of the 32bit settings. In case they don't, try 
  5. export VERSIONER_PYTHON_PREFER_32_BIT=yes
in a terminal before running Pronterface

### Mac OS X (pre Lion)

A precompiled version is available at http://koti.kapsi.fi/~kliment/printrun/

  1. Download and install http://downloads.sourceforge.net/wxpython/wxPython2.8-osx-unicode-2.8.12.0-universal-py2.6.dmg
  2. Grab the source for pyserial from http://pypi.python.org/packages/source/p/pyserial/pyserial-2.5.tar.gz
  3. Unzip pyserial to a folder. Then, in a terminal, change to the folder you unzipped to, then type in:
     
     `defaults write com.apple.versioner.python Prefer-32-Bit -bool yes`
     
     `sudo python setup.py install`

Alternatively, you can run python in 32 bit mode by setting the following environment variable before running the setup.py command:

This alternative approach is confirmed to work on Mac OS X 10.6.8. 

`export VERSIONER_PYTHON_PREFER_32_BIT=yes`

`sudo python setup.py install`

Then repeat the same with http://http://pyglet.googlecode.com/files/pyglet-1.1.4.zip

# LICENSE

```
Burner is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Burner is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Burner.  If not, see <http://www.gnu.org/licenses/>.
```

All scripts should contain this license note, if not, feel free to ask us. Please note that files where it is difficult to state this license note (such as images) are distributed under the same terms.
