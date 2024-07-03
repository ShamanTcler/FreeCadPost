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
import Path
import FreeCAD
import uuid

Path.Log.setLevel(Path.Log.Level.INFO, Path.Log.thisModule())

translate = FreeCAD.Qt.translate

debug = True
if debug:
    Path.Log.setLevel(Path.Log.Level.DEBUG, Path.Log.thisModule())
    Path.Log.trackModule(Path.Log.thisModule())
else:
    Path.Log.setLevel(Path.Log.Level.INFO, Path.Log.thisModule())


##   Cnc_controller is a Python base class, that inherits from the PostProcessor class.
#
#    It will house the most generic operations over all the post processors. A Cnc_controller 
#    will be contained in a Cnc_machine.
#
#    A Cnc_controller object stores all of it parameters in a python dictionary called "values".
#
#    The base post processor class will have the following parameters set by default. These should be a
#    good starting point for most post processors.
#     
#   Grouping values by role:
#
#   Controller information:
#   | Value Name           |  Default        |   Description                                                |
#   |:---------------------|:----------------|:-------------------------------------------------------------|
#   |VENDOR                |"Undefined"      |Manufacturer of the controller i.e. Linuxcnc, Grnl, Fanuc etc |
#   |MODEL                 |"Undefined"      |Model of the controller                                       |
#   |VERSION               |"Undefined"      |Version of the controller                                     |
#
#   CAM information:
#   | Value Name           |  Default        |   Description                                                |
#   |:---------------------|:----------------|:-------------------------------------------------------------|
#   |UNITS                 |"Undefined"      |Inches or Metric, valid values: inch, mm                      |
#   |PRECISION             |"Undefined"      |Number of decimals after the decimal point                    |
#   |UNIT_SPEED_FORMAT     |"Undefined"      |length/time valid values: inch/min, mm/sec                    |
#
#
#   GCode information:
#   | Value Name           |  Default        |   Description                                                |
#   |:---------------------|:----------------|:-------------------------------------------------------------|
#   |OUTPUT_COMMENTS       |"Undefined"      |True comments are included, False no comments                 |
#   |OUTPUT_LINE_NUMBERS   |"Undefined"      |True line numbers are printed, False no line numbers          |
#   |TOOL_CHANGE           |"Undefined"      |                                                              |
#

#   GCode information:
#   | Value Name           |  Default        |   Description                                                |
#   |:---------------------|:----------------|:-------------------------------------------------------------|
#   |OUTPUT_COMMENTS       |"Undefined"      |True comments are included, False no comments                 |
#   |OUTPUT_LINE_NUMBERS   |"Undefined"      |True line numbers are printed, False no line numbers          |
#   |TOOL_CHANGE           |"Undefined"      |                                                              |
#
#    GCode information:
#   | Value Name           |  Default        |   Description                                                |
#   |:---------------------|:----------------|:-------------------------------------------------------------|
#   |OUTPUT_COMMENTS       |"Undefined"      |True comments are included, False no comments                 |
#   |OUTPUT_LINE_NUMBERS   |"Undefined"      |True line numbers are printed, False no line numbers          |
#   |TOOL_CHANGE           |"Undefined"      |                                                              |
#
        
class cnc_controller(PostProcessor):
 
    

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
        
        self.Values = {}  # Initialize the dictionary
        self.ValuesDefinitions = {}  # Initialize the dictionary

        # Initialize the parser
        self.parser = argparse.ArgumentParser(description="Process some integers.")
        
        # Add arguments to the parser as needed
        self.parser.add_argument("--job", help="the job to be processed")

        # Parse the arguments
        self.args = self.parser.parse_args()


# These globals set common customization preferences


        self.Values["OUTPUT_COMMENTS"] = "True"
        self.ValuesDefinitions[""] = "Unknown"

        self.Values["OUTPUT_HEADER"] = "Undefined"
        self.ValuesDefinitions["OUTPUT_HEADER"] = "Unknown"
        self.Values["OUTPUT_LINE_NUMBERS"] = "False"
        self.ValuesDefinitions["OUTPUT_LINE_NUMBERS"] = "Unknown"

        # the order of parameters                                  
        self.Values["PARAMETER_ORDER"] = ["Undefined"]
        self.ValuesDefinitions["PARAMETER_ORDER"]= "the order of parameters"

        self.Values["SHOW_EDITOR"] = "True"
        self.ValuesDefinitions["SHOW_EDITOR"] = "Unknown"

        self.Values["USE_TLO"] = "True" # if true G43 will be output following tool changes
        self.ValuesDefinitions["USE_TLO"] = "Unknown"
        
        self.Values["OUTPUT_DOUBLES"] = "True" # if false duplicate axis values are suppressed if the same as previous line.
        self.ValuesDefinitions["OUTPUT_DOUBLES"] = "Unknown"
        #self.Values[""] = "True"
        #self.Values[""] = "True"
        #self.Values[""] = "True"
        #self.Values[""] = "True"
        #self.Values[""] = "True"

        self.Values["MODAL"] = "False"  # if true commands are suppressed if the same as previous line.
        self.ValuesDefinitions["MODAL"] = "Unknown"
        #Values[""] = "False"
        #Values[""] = "False"
        #Values[""] = "False"


        self.Values["LINENR"] = 100   # line number starting value
        self.ValuesDefinitions["LINENR"] = "Unknown"
        self.Values["PRECISION"] = 3
        self.ValuesDefinitions["PRECISION"] = "Unknown"
        #Values[""] = "Undefined"
        #Values[""] = "Undefined"
        #Values[""] = "Undefined"
        #Values[""] = "Undefined"
        #Values[""] = "Undefined"
        #Values[""] = "Undefined"

        self.Values["UNITS"] = "Undefined"
        self.ValuesDefinitions["UNITS"] = "Unknown"

        self.Values["UNIT_SPEED_FORMAT"] = "Undefined"
        self.ValuesDefinitions["UNIT_SPEED_FORMAT"] = "Unknown"

        self.Values["UNIT_FORMAT"] = "Undefined"
        self.ValuesDefinitions["UNIT_FORMAT"] = "Unknown"
        


        self.Values["ENABLE_COOLANT"] = "Undefined"
        self.ValuesDefinitions["ENABLE_COOLANT"] = "Unknown"
        


#
        # Used in the argparser code as the "name" of the postprocessor program.
        self.Values["MACHINE_NAME"] = "Unknown"
        self.ValuesDefinitions["MACHINE_NAME"] = "Used in the argparser code as the \"name\" of the postprocessor program."


        self.Values['MODEL'] = "Undefined"
        self.ValuesDefinitions["MODEL"] = "Unknown"

        self.Values['MANUFACTURER'] = "Undefined"
        self.ValuesDefinitions["MANUFACTURER"] = "Unknown"
        
        # Any commands in this value will be output as the last commands
        # in the G-code file.
        self.Values["POSTAMBLE"] = "Undefined"
        self.ValuesDefinitions["POSTAMBLE"] = "Any commands in this value will be output as the last commands in the G-code file."


        # Any commands in this value will be output after the header and
        # safety block at the beginning of the G-code file.
        self.Values["PREAMBLE"] = "Undefined"  
        self.ValuesDefinitions["PREAMBLE"] = "Commands in this value will be output after the header and safety block at the beginning of the G-code file."
        

        # The name of the file to be written by the post processor.
        self.Values["POSTPROCESSOR_FILE_NAME"] = "Undefined"
        self.ValuesDefinitions["POSTPROCESSOR_FILE_NAME"] = "The name of the file to be written by the post processor."

        #self.Values["PRE_OPERATION"] = "Undefined"
        #self.Values["POST_OPERATION"] = "Undefined"

        self.Values["TOOL_CHANGE"] = "Undefined"
        self.ValuesDefinitions["TOOL_CHANGE"] = "Unknown"
        #self.Values[""] = "Undefined"

        
        #Values[""] = "Undefined"

        print("Base_post post processor initialized")
        Path.Log.debug("Base_post post processor initialized")
        print("\n\n")


    def processArguments(self,argstring):
        try:
            args = parser.parse_args(shlex.split(argstring))
            if args.no_header:
                self.Values['OUTPUT_HEADER'] = False
            if args.no_comments:
                self.Values['OUTPUT_COMMENTS'] = False
            if args.line_numbers:
                self.Values['OUTPUT_LINE_NUMBERS'] = True
            if args.no_show_editor:
                self.Values['SHOW_EDITOR'] = False
            print("Show editor = %d" % self.Values['SHOW_EDITOR'])
            self.Values['PRECISION'] = args.precision
            if args.preamble is not None:
                self.Values['PREAMBLE'] = args.preamble
            if args.postamble is not None:
                self.Values['POSTAMBLE'] = args.postamble
            if args.inches:
                self.Values['UNITS'] = "G20"
                self.Values['UNIT_SPEED_FORMAT'] = "in/min"
                self.Values['UNIT_FORMAT'] = "in"
                self.Values['PRECISION'] = 4
            if args.modal:
                self.Values['MODAL'] = True
            if args.no_tlo:
                self.Values['USE_TLO ']= False
            if args.axis_modal:
                print("here")
                self.Values['OUTPUT_DOUBLES'] = False
        except Exception:
                return False

        return True





    def print_values(self):
        print("Key          |         Value         |               Definition")
        keys= self.Values.keys()
        for key in keys:
            if key in self.ValuesDefinitions:
                val_def=self.ValuesDefinitions[key]
            else:
                val_def="Missing, as in not defined"
            print(key," | ", self.Values[key]," | ", val_def)
        

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
