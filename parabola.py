#!/usr/bin/env python
# coding=utf-8
#
# Copyright (C) 2021 Reginald Waters opensourcebear@nthebare.com
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#
"""
This extension renders a wireframe shape and then draws lines to form a parabola 
shape.

The height and width are independently variable. The number of lines will change 
the density of the end product.
"""
import inkex

from inkex import turtle as pturtle

class parabola(inkex.GenerateExtension):
    container_label = 'Parabola'
    def add_arguments(self, pars):
        pars.add_argument("--height", type=int, default=300,
                          help="Shape Height")
        pars.add_argument("--width", type=int, default=300,
                          help="Shape Width")
        pars.add_argument("--seg_count", type=int, default=10,
                          help="Number of line segments")
        pars.add_argument("--shape", default="square")
        pars.add_argument("--border", default="false")
        pars.add_argument("--tab", default="common")
        pars.add_argument("--c1", default="true")
        pars.add_argument("--c2", default="false")
        pars.add_argument("--c3", default="false")
        pars.add_argument("--c4", default="false")

    def generate(self):
        # Let's simplify the variable names
        ht = int(self.options.height)
        wt = int(self.options.width)
        sc = int(self.options.seg_count)
        bd = self.options.border
        shape = self.options.shape
        c1 = self.options.c1
        c2 = self.options.c2
        c3 = self.options.c3
        c4 = self.options.c4

        point = self.svg.namedview.center
        style = inkex.Style({
                'stroke-linejoin': 'miter', 'stroke-width': str(self.svg.unittouu('1px')),
                'stroke-opacity': '1.0', 'fill-opacity': '1.0',
                'stroke': '#000000', 'stroke-linecap': 'butt',
                'fill': 'none'
        })
        
        # Setting the amount to move across the horizontal and vertical
        increaseht = (ht / sc)
        increasewt = (wt / sc)

        tur = pturtle.pTurtle()

        tur.pu()  # Pen up
        tur.setpos(point) # start in the center
        
        if shape == "cross":
            # We draw the cross shape and store the 4 points
            # Can this be looped?
            # Should I store the coordinates in an array/list?
            tur.forward((ht / 2)) # from center go forward (up) half the object height
            toppoint = tur.getpos() # store the coordinates for the top most point
            if bd == 'true':
                tur.pd()
            tur.backward((ht)) 
            tur.pu()
            bottompoint = tur.getpos()
            tur.setpos(point)
            tur.right(90)
            tur.forward((wt / 2))
            rightpoint = tur.getpos()
            if bd == 'true':
                tur.pd()
            tur.backward((wt))
            leftpoint = tur.getpos()

            while sc > 0:
                if c1 == 'true':
                # Drawing the SE Corner based on SW coordinates
                # We always draw this corner
                    tur.pu()
                    tur.setpos((bottompoint[0], bottompoint[1] - ( (increaseht / 2) * sc ) ))
                    tur.pd()    
                    tur.setpos((bottompoint[0] + ( (increasewt / 2) * sc ), bottompoint[1] - (ht / 2) ))
                
                if c2 == 'true': # Drawing the SW Corner based on SE Coordinates
                    tur.pu()
                    tur.setpos((bottompoint[0], bottompoint[1] - ( (increaseht / 2) * sc ) ))
                    tur.pd()    
                    tur.setpos((bottompoint[0] - ( (increasewt / 2) * sc ), bottompoint[1] - (ht / 2) ))
                
                if c3 == 'true': # Drawing the NW Corner based on NE Coordinates
                    tur.pu()
                    tur.setpos((toppoint[0], toppoint[1] + ( (increaseht / 2) * sc ) ))
                    tur.pd()    
                    tur.setpos((toppoint[0] - ( (increasewt / 2) * sc ), toppoint[1] + (ht / 2) ))
                
                if c4 == 'true': # Drawing the NE Corner based on NW Coordinates
                    tur.pu()
                    tur.setpos((toppoint[0], toppoint[1] + ( (increaseht / 2) * sc ) ))
                    tur.pd()    
                    tur.setpos((toppoint[0] + ( (increasewt / 2) * sc ), toppoint[1] + (ht / 2) ))

                sc = sc - 1

        if shape == "triangle":
            # We draw the triangle and store the 3 corner points
            # Loopable?
            tur.backward((ht / 2))
            tur.right(90)
            tur.forward((wt /2))
            cornera = tur.getpos()
            if bd == 'true':
                tur.pd()
            tur.backward((wt))
            cornerb = tur.getpos()
            tur.setpos((point[0], (cornera[1] - ht) ))
            cornerc = tur.getpos()
            tur.setpos(cornera)

# So..  The math below took a lot of trial and error to figure out...
# I probably need to take some geography classes...

            while sc > 0:
                if c1 == 'true':
                    tur.pu()
                    tur.setpos(( (cornerb[0] + ((increasewt / 2) * (sc)) - (wt / 2)), cornerb[1] + (increaseht * sc) - ht ))
                    tur.pd()    
                    tur.setpos(( (cornera[0] + (increasewt / 2) * (sc)), cornera[1] - (increaseht * sc) ))

                if c2 == 'true':
                    tur.pu()
                    tur.setpos((cornerb[0] - (increasewt * sc ) , cornerb[1] ))
                    tur.pd()    
                    tur.setpos(( (cornerb[0] + ((increasewt / 2) * sc) - (wt / 2)), cornerb[1] + (increaseht * sc) - ht ))

                if c3 == 'true':
                    tur.pu()
                    tur.setpos((cornera[0] + (increasewt * sc ) , cornera[1] ))
                    tur.pd()    
                    tur.setpos(( (cornera[0] - ((increasewt / 2) * sc) + (wt / 2)), cornera[1] + (increaseht * sc) - ht ))

                sc = sc - 1


        if shape == "square":
            # We draw out the square shape and store the coordinates for each corner
            # Can this be looped?
            tur.right(90)
            tur.forward((wt / 2))
            tur.right(90)
            tur.forward((ht / 2))
            swcorner = tur.getpos()
            if bd == 'true':
                tur.pd()  # Pen Down
            tur.right(90)
            tur.forward(wt)
            secorner = tur.getpos()
            tur.right(90)
            tur.forward(ht)
            necorner = tur.getpos()
            tur.right(90)
            tur.forward(wt)
            nwcorner = tur.getpos()
            tur.right(90)
            tur.forward(ht)

            while sc > 0:
                if c1 == 'true':
                # Drawing the NW Corner based on SW coordinates
                # We always draw this corner
                    tur.pu()
                    tur.setpos((swcorner[0], swcorner[1] - ( increaseht * sc ) ))
                    tur.pd()    
                    tur.setpos((swcorner[0] + ( increasewt * sc ), swcorner[1] - ht))
                
                if c2 == 'true': # Drawing the NE Corner based on SE Coordinates
                    tur.pu()
                    tur.setpos((secorner[0], secorner[1] - ( increaseht * sc ) ))
                    tur.pd()    
                    tur.setpos((secorner[0] - ( increasewt * sc ), secorner[1] - ht))
                
                if c3 == 'true': # Drawing the SE Corner based on NE Coordinates
                    tur.pu()
                    tur.setpos((necorner[0], necorner[1] + ( increaseht * sc ) ))
                    tur.pd()    
                    tur.setpos((necorner[0] - ( increasewt * sc ), necorner[1] + ht))
                
                if c4 == 'true': # Drawing the SW Corner based on NW Coordinates
                    tur.pu()
                    tur.setpos((nwcorner[0], nwcorner[1] + ( increaseht * sc ) ))
                    tur.pd()    
                    tur.setpos((nwcorner[0] + ( increasewt * sc ), nwcorner[1] + ht))

                sc = sc - 1
    
        return inkex.PathElement(d=tur.getPath(), style=str(style))

if __name__ == "__main__":
    # execute only if run as a script
    parabola().run()
