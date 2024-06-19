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


from cnc_controller import cnc_controller

class masso_controller(cnc_controller):

    def __init__(self, job):
        super().__init__(job)
        # If this is set to True, then commands that are placed in
        # comments that look like (MC_RUN_COMMAND: blah) will be output.
        #
        self.Values["ENABLE_MACHINE_SPECIFIC_COMMANDS"] = True
        #
        # Used in the argparser code as the "name" of the postprocessor program.
        # This would normally show up in the usage message in the TOOLTIP_ARGS,
        # but we are suppressing the usage message, so it doesn't show up after all.
        #
        self.Values["MACHINE_NAME"] = "Masso"
        #
        # Default to outputting Path labels at the beginning of each Path.
        #
        self.Values["OUTPUT_PATH_LABELS"] = True
        #
        # Default to not outputting M6 tool changes (comment it) as Masso
        # currently does not handle it
        #
        self.Values["OUTPUT_TOOL_CHANGE"] = False
        #
        # The order of the parameters.
        # Arcs may only work on the XY plane (this needs to be verified).
        #
        self.Values["PARAMETER_ORDER"] = [
            "X",
            "Y",
            "Z",
            "A",
            "B",
            "C",
            "U",
            "V",
            "W",
            "I",
            "J",
            "K",
            "F",
            "S",
            "T",
            "Q",
            "R",
            "L",
            "P",
        ]
        #
        # Any commands in this value will be output as the last commands
        # in the G-code file.
        #
        self.Values[
            "POSTAMBLE"
        ] = """M5
            G17 G90
            M2"""
        self.Values["POSTPROCESSOR_FILE_NAME"] = __name__
        #
        # Any commands in this value will be output after the header and
        # safety block at the beginning of the G-code file.
        #
        self.Values["PREAMBLE"] = """G17 G90"""
        #
        # Do not show the current machine units just before the PRE_OPERATION.
        #
        self.Values["SHOW_MACHINE_UNITS"] = False
        #self.Values["UNITS"] = UNITS
        #
        # Default to not outputting a G43 following tool changes
        #
        self.Values["USE_TLO"] = False
    
