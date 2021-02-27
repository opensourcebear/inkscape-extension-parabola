# Parabola

Parabola is an [Inkscape](https://inkscape.org) extension that renders a series of lines in selected shapes to form an optical illusion of a curved line (Parabolic lines)


**NOTE:** *Parabola was developed on a Macintosh running Inkscape version 1.0.  It has NOT been tested on any other platforms or Inkscape versions*


## How to install
To install parabola, place the following files in your Inkscape extensions folder and then restart Inkscape.

You can find your Inkscape extensions folder listed at Edit > Preferences > System: User extensions.

* [parabola.inx](https://github.com/opensourcebear/inkscape-extensions/tree/main/parabola/parabola.inx)
* [parabola.py](https://github.com/opensourcebear/inkscape-extensions/tree/main/parabola/parabola.py)

## Parabola usage
### Starting the Parabola extension

Parabola is accessed from the extensions menu.  Go to Extensions => Render => Parabola

If Parabola doesn't appear in the render list, check that you have installed both files listed above in the correct folder, and that Inkscape has been restarted.

<img src="support_images/extensions_menu.png" height="400" width="400" alt="Extensions Menu" />

### Configuring your render
Parabola will allow you to set the following options:

1. Shape Height - Overall height of object (100 - 1000)
2. Shape Width - Overall width of the object (100 - 1000)
3. Number of line segments (5 - 100)
4. Shape - Cross, Square, or Triangle
5. Border - a path that outlines the shape. At this time, not having the border may cause undesirable edges.

**Hint:** Turn on live preview and observe how the preview result will appear as you change settings to become more familiar with the options.

<img alt="Main Options" src="support_images/basic_options.png" width="250" height="255" />

### Corners
On the Corners tab of the Parabola settings you can mix and match which corners are rendered. 

<img alt="Corner Options" src="support_images/corners.png" width="250" height="255" />

### Example Renders

**Triangle Shape with 3 corners active**


<img alt="Triangle Render" src="examples/triangle_500.png" width="300" height="300" />


**NOTE:** Renders are all black, The color seen here was added as a gradient stroke after rendering.

**Cross Shape with 4 corners active**

<img alt="Cross Render" src="examples/cross_500.png" width="300" height="300" />

**NOTE:** Renders are all black, The color seen here was added as a gradient stroke after rendering.

**Square Shape with 4 corners active**

<img alt="Square Render" src="examples/square_500.png" width="300" height="300" />
