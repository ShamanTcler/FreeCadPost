# ***************************************************************************
# *   Copyright (c) 2014 sliptonic <shopinthewoods@gmail.com>               *
# *   Copyright (c) 2022 Larry Woestman <LarryWoestman2@gmail.com>          *
# *   Copyright (c) 2024 Carl Slater <CandLWorkshopLLC@gmail.com>           *
# *                                                                         *
# *   This file is part of the FreeCAD CAx development system.              *
# *                                                                         *
# *   This program is free software; you can redistribute it and/or modify  *
# *   it under the terms of the GNU Lesser General Public License (LGPL)    *
# *   as published by the Free Software Foundation; either version 2 of     *
# *   the License, or (at your option) any later version.                   *
# *   for detail see the LICENCE text file.                                 *
# *                                                                         *
# *   FreeCAD is distributed in the hope that it will be useful,            *
# *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
# *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
# *   GNU Lesser General Public License for more details.                   *
# *                                                                         *
# *   You should have received a copy of the GNU Library General Public     *
# *   License along with FreeCAD; if not, write to the Free Software        *
# *   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
# *   USA                                                                   *
# *                                                                         *
# ***************************************************************************


from base_class_post import base_post

class linuxcnc_post(base_post):

    def __init__(self, job):
        super().__init__(job)
        self.Values["ENABLE_COOLANT"] = True
    
        # the order of parameters
        self.Values["PARAMETER_ORDER"] = [
            "X",
            "Y",
            "Z",
            "A",
            "B",
            "C",
            "I",
            "J",
            "F",
            "S",
            "T",
            "Q",
            "R",
            "L",
            "H",
            "D",
            "P",
        ]
        #
        # Used in the argparser code as the "name" of the postprocessor program.
        # This would normally show up in the usage message in the TOOLTIP_ARGS,
        # but we are suppressing the usage message, so it doesn't show up after all.
        #
        self.Values["MACHINE_NAME"] = "LinuxCNC"
        #
        # Any commands in this value will be output as the last commands
        # in the G-code file.
        #
        self.Values["POSTAMBLE"] = """M05
           G17 G54 G90 G80 G40
           M2"""
    
        self.Values["POSTPROCESSOR_FILE_NAME"] = __name__

        #
        # Any commands in this value will be output after the header and
        # safety block at the beginning of the G-code file.
        #
        self.Values["PREAMBLE"] = """G17 G54 G40 G49 G80 G90"""
        #self.Values["UNITS"] = UNITS

