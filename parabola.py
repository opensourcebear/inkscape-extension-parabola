#!/usr/bin/env python
# coding=utf-8
#
# 2/27/2021 - v.1.1.0
# 7/9/2021  - v.2.0
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

# Triangle has 3 sides and the sum of the 3 angles is 180 degrees 
# (sides - 2) * 180
# This can be 60/60/60   or 90/45/45

# Square has 4 sides and the sum of 4 angles is 360 degrees
# (sides - 2) * 180
# 90/90/90/90

# Pentagon has 5 sides and the sum of 5 angels is 540 degrees
# (sides - 2) * 180
# 108/108/108/108/108
...
"""
import inkex

from inkex import turtle as pturtle

class parabola(inkex.GenerateExtension):
    container_label = 'Parabola 2'
    def add_arguments(self, pars):
        pars.add_argument("--length", type=int, default=300,
                          help="Side Length")
        pars.add_argument("--segments", type=int, default=10,
                          help="Number of line segments")
        pars.add_argument("--shape", default="square")
        pars.add_argument("--tab", default="common")
        pars.add_argument("--c1", default="true")
        pars.add_argument("--c2", default="false")
        pars.add_argument("--c3", default="false")
        pars.add_argument("--c4", default="false")

        sideopts = [
        (1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8),
        (2,3),(2,4),(2,5),(2,6),(2,7),(2,8),
        (3,4),(3,5),(3,6),(3,7),(3,8),
        (4,5),(4,6),(4,7),(4,8),
        (5,6),(5,7),(5,8),
        (6,7),(6,8),
        (7,8)]

    def generate(self):
        # Let's simplify the variable names
        sl = int(self.options.length) # Side Length
        sc = int(self.options.segments) # Segment Count 
        shape = self.options.shape
        c1 = self.options.c1
        c2 = self.options.c2
        c3 = self.options.c3
        c4 = self.options.c4

        cp = self.svg.namedview.center # Center Point
        sp = (cp[0] + (sl / 2), cp[1] + (sl / 2)) # Start Point
        cords = []

        def mapshape(sides, sl, sc, sp):
            exteriorAngle = 360/sides
            movement = sl / sc
            tur.setpos(sp)
            for i in range(sides):
                sidecords = []
                tl = 0 # total length
                while tl < sl:
                    sidecords.append(tur.getpos())
                    tur.forward(movement)
                    tl += movement
#                sidecords.append(tur.getpos())
                tur.right(exteriorAngle)
                cords.append(sidecords)
            return cords
        
        def mapcross(sl, sc, sp):
            movement = sl / sc
            tur.setpos(sp)
            sidecords = []
            tl = 0 
            tur.forward(sl)
            while tl < sl:
                tur.backward(movement)
                sidecords.append(tur.getpos())
                tur.right(90)

        def drawshape(cords):
            tur.setpos(cords[0][0])
            for i in range(len(cords)):
#                tur.pd()
#                tur.setpos(cords[i][-1])
#                tur.pu()
                for side in range(len(cords)):
                    for cord in range(len(cords[0])):
                        if side == (len(cords) - 1):
                            tur.setpos(cords[side][cord])
                            tur.pd()
                            if cord != (len(cords[0])):
                                tur.setpos(cords[0][cord])
                                tur.pu()
                        else:
                            tur.setpos(cords[side][cord])
                            tur.pd()
                            tur.setpos(cords[side + 1][cord])
                            tur.pu()
                tur.pu()
            
# Debug
#             inkex.errormsg(_(cords))

        tur = pturtle.pTurtle()
        tur.pu()

        if shape == "triangle":
            sides = 3
            mapshape(sides, sl, sc, sp)
            drawshape(cords)
        elif shape == "square":
            sides = 4
            mapshape(sides, sl, sc, sp)
            drawshape(cords)
        elif shape == "pentagon":
            sides = 5
            mapshape(sides, sl, sc, sp)
            drawshape(cords)
        elif shape == "hexagon":
            sides = 6
            mapshape(sides, sl, sc, sp)
            drawshape(cords)
        elif shape == "septagon":
            sides = 7
            mapshape(sides, sl, sc, sp)
            drawshape(cords)
        elif shape == "octagon":
            sides = 8
            mapshape(sides, sl, sc, sp)
            drawshape(cords)
        elif shape == "cross":
            sides = 2
            mapshape(sides, sl, sc, sp)
            drawshape(cords)



        style = inkex.Style({
                'stroke-linejoin': 'miter', 'stroke-width': str(self.svg.unittouu('1px')),
                'stroke-opacity': '1.0', 'fill-opacity': '1.0',
                'stroke': '#000000', 'stroke-linecap': 'butt',
                'fill': 'none'
        })




        
        return inkex.PathElement(d=tur.getPath(), style=str(style))
        
"""
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
            tur.forward((ht / 2)) 
            toppoint = tur.getpos() 
            if c3 == 'true' or c4 == 'true':
                tur.pd()
            tur.backward((ht / 2)) 
            tur.pu()
            if c1 == 'true' or c2 == 'true':
                tur.pd()
            tur.backward((ht / 2))
            bottompoint = tur.getpos()
            tur.pu()
            tur.setpos(point)
            tur.right(90)
            tur.forward((wt / 2))
            rightpoint = tur.getpos()
            if c3 == 'true' or c2 == 'true':
                tur.pd()
            tur.backward((wt / 2))
            tur.pu()
            if c1 == 'true' or c4 == 'true':
                tur.pd()
            tur.backward((wt / 2))
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
            if c3 == 'true' or c2 == 'true':
                tur.pd()
            tur.backward((wt))
            cornerb = tur.getpos()
            tur.pu()
            if c2 == 'true' or c1 == 'true':
                tur.pd()
            tur.setpos((point[0], (cornera[1] - ht) ))
            cornerc = tur.getpos()
            tur.pu()
            if c1 == 'true' or c3 == 'true':
                tur.pd()            
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
            if c4 == 'true' or c3 == 'true': # We only draw the 2 lines that are part of these corners
                tur.pd()  # Pen Down
            tur.right(90)
            tur.forward(wt)
            secorner = tur.getpos()
            tur.pu()
            if c3 == 'true' or c2 == 'true': # We only draw the 2 lines that are part of these corners
                tur.pd()
            tur.right(90)
            tur.forward(ht)
            necorner = tur.getpos()
            tur.pu()
            if c1 == 'true' or c2 == 'true': # We only draw the 2 lines that are part of these corners
                tur.pd()
            tur.right(90)
            tur.forward(wt)
            nwcorner = tur.getpos()
            tur.right(90)
            tur.pu()
            if c4 == 'true' or c1 == 'true': # We only draw the 2 lines that are part of these corners
                tur.pd()
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
"""



if __name__ == "__main__":
    # execute only if run as a script
    parabola().run()
