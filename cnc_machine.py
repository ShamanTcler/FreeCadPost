# -*- coding: utf-8 -*-
# ***************************************************************************
# *   Copyright (c) 2024 Ondsel <development@ondsel.com>                    *
# *                                                                         *
# *   This program is free software; you can redistribute it and/or modify  *
# *   it under the terms of the GNU Lesser General Public License (LGPL)    *
# *   as published by the Free Software Foundation; either version 2 of     *
# *   the License, or (at your option) any later version.                   *
# *   for detail see the LICENCE text file.                                 *
# *                                                                         *
# *   This program is distributed in the hope that it will be useful,       *
# *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
# *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
# *   GNU Library General Public License for more details.                  *
# *                                                                         *
# *   You should have received a copy of the GNU Library General Public     *
# *   License along with this program; if not, write to the Free Software   *
# *   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
# *   USA                                                                   *
# *                                                                         *
# ***************************************************************************

## @package
#  Documentation for this module.
#
#  More details.
#

import argparse
from typing import Any, Dict, Union

import os
from Path.Post.Processor import PostProcessor
from cnc_controller import cnc_controller

from linuxcnc_controller import linuxcnc_controller
from masso_controller import masso_controller
from grbl_controller import grbl_controller 
from mach_controller import mach_controller

import Path
import FreeCAD

Path.Log.setLevel(Path.Log.Level.INFO, Path.Log.thisModule())

translate = FreeCAD.Qt.translate

debug = True
if debug:
    Path.Log.setLevel(Path.Log.Level.DEBUG, Path.Log.thisModule())
    Path.Log.trackModule(Path.Log.thisModule())
else:
    Path.Log.setLevel(Path.Log.Level.INFO, Path.Log.thisModule())


## Cnc_machine is a Python base class.
#
#    It will contain information about the selected machine.
#
#    A "cnc_machine" will have one and only one "cnc_controller".
#
#    A machine object stores all of it parameters in a python dictionary called "values"
#    
#
#   | Value Name           |  Default        |   Description                                   |
#   |:---------------------|:----------------|:------------------------------------------------|
#   |VENDOR                |"Undefined"      |Manufacturer of the machine i.e. Haas, Fanuc etc |
#   |TYPE                  |"Undefined"      |Mill, Lathe etc                                  |
#   |MODEL                 |"Undefined"      |Model of the machine                             |
#   |VERSION               |"Undefined"      |Version of the machine                           |
        
class cnc_machine(PostProcessor):
 
    

     ## Init this class
     #
     #  Parameters
     # ----------
     #
     # job: This is a job object passed to the post processor
     # 
    def __init__(self, job):
        super().__init__(
            job,
            tooltip=translate("CAM", "Base_post post processor"),
            tooltipargs=["arg1", "arg2"],
            units="kg",
        )
        
        self.controller =masso_controller(PostProcessor)                         #create and assign a cnc_controller
        self.Values = {}  # Initialize the dictionary

        # Initialize the parser
        self.parser = argparse.ArgumentParser(description="Process some integers.")
        
        # Add arguments to the parser as needed
        self.parser.add_argument("--job", help="the job to be processed")

        # Parse the arguments
        self.args = self.parser.parse_args()
        
        ## Init_values store values for the class.
        # Common values are:
        #   ENABLE_COOLANT
        #   MACHINE_NAME
        #   PARAMETER_ORDER
        #   POSTAMBLE
        #   PREAMBLE
        #   POSTPROCESSOR_FILE_NAME
        #   UNITS


# These globals set common customization preferences
        self.Values["VENDOR"] = "Undefined"
        self.Values["TYPE"] = "Undefined"             # Mill, Lathe etc
        self.Values["MODEL"] = "Undefined"
        self.Values["VERSION"] = "Undefined"

        #Values[""] = "Undefined"

        print("CNC_MACHIBE initialized")
        print(self.Values)
        print("CNC_MACHIBE initialized end printout")
        #Path.Log.debug("Base_post post processor initialized")
        print("\n\n")


    def print_values(self):
        print(self.Values)
        for k,v in self.Values():
            print(k, v)


    ## The export routine actually writes the file(s) to be sent to the CNC machine.
    #
    def export(self):

        Path.Log.debug("Exporting the job")

        postables = self._buildPostList()
        Path.Log.debug(f"postables count: {len(postables)}")

        g_code_sections = []
        for idx, section in enumerate(postables):
            partname, sublist = section

            # here is where the sections are converted to gcode.
            g_code_sections.append((idx, partname))

        return g_code_sections


    ## This is a generic post processor. 
    #  It doesn't do anything yet because we haven't implemented it.
    #  Implementing it would be a good idea
    @property
    def tooltip(self):
        tooltip = """
        This is a generic post processor. 
        It doesn't do anything yet because we haven't implemented it.

        Implementing it would be a good idea
        """
        return  tooltip

    @property
    def tooltipArgs(self):
        argtooltip = """
        --arg1: This is the first argument
        --arg2: This is the second argument

        """
        return argtooltip

    @property
    def units(self):
        return self._units
