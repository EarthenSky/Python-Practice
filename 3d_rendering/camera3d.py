import math

# Max render distance.  I don't know what happens if you go over it.
# Incremenmting it before runtime should be safe though.
MAX_RENDER_DISTANCE = 100000  # 100 000

def distance3d(pnt1, pnt2):
    """Find distance between two 3d points. pnt -> (x, y, z)"""
    dif_pnt = ( pnt1[0] - pnt2[0], pnt1[1] - pnt2[1], pnt1[2] - pnt2[2] )

    # Find xy distance.
    xy_distance = math.sqrt( (dif_pnt[0] ** 2) + (dif_pnt[1] ** 2) )

    # Find total distance
    return math.sqrt( (xy_distance ** 2) + (dif_pnt[2] ** 2) )

# Find distance between two 2d points. pnt -> (x, y)
def _distance2d(pnt1, pnt2):
    dif_pnt = ( pnt1[0] - pnt2[0], pnt1[1] - pnt2[1] )

    # Find xy distance.
    return math.sqrt( (dif_pnt[0] ** 2) + (dif_pnt[1] ** 2) )

# Find angle between 3 points.  pnt2 is centre.
def _three_point_angle(pnt1, pnt2, pnt3):
    # Make triangle
    x = _distance2d(pnt1, pnt2)
    y = _distance2d(pnt2, pnt3)
    z = _distance2d(pnt3, pnt1)

    # Actually do cosine law *here*
    form = (y**2 + x**2 - z**2) / (2 * x * y)

    # Do cosine law.
    return math.degrees( math.acos( form ) )

def _2d_line_side(pnt_line1, pnt_line2, pnt):
    d = (pnt[0] - pnt_line1[0]) * (pnt_line2[1] - pnt_line1[1]) - (pnt[1] - pnt_line1[1]) * (pnt_line2[0] - pnt_line1[0])
    if d > 0:
        return 1
    else:
        return -1

class camera:
    """This class manages conversion between 3d and 2d points.  This camera can be rotated."""

    # Screen size is (width, height)
    def __init__(self, fov, screen_size):
        self._screen_size = screen_size
        self._fov = (fov, fov/(float(self._screen_size[0])/self._screen_size[1]))  # (horizontal fov, verticle fov)

        self._pos3d = (0, 0, 0)  # xyz
        self._anchor3d = (0, 0, MAX_RENDER_DISTANCE)  # Direction point.

    # is_find_x is a boolean value.  start_pnt2d is (x, z) or (y, z)
    def _findPixelPos(self, circumfrence, fov_angle, screen_distance, start_pnt2d, cam_pnt2d, anchor_pnt2d):
        # Find the perimeter of the fov cone.
        fov_range_distance = float(circumfrence) * float(fov_angle)/360

        # Find the angle between the point and the edge fo the fov.
        edge_angle = ( (fov_angle/2) - _three_point_angle(start_pnt2d, cam_pnt2d, anchor_pnt2d) ) * -_2d_line_side(cam_pnt2d, anchor_pnt2d, start_pnt2d)

        #print (edge_angle)

        # Find distance to the side of the screen.
        edge_range_distance = circumfrence * (edge_angle/360)

        # Scale distance to the pixel value.
        return (edge_range_distance/fov_range_distance) * screen_distance

    # Converts (x, y, z) to (x, y) but as a screen position.
    def convertToScreenPoint(self, point3d, screen_size):
        circumfrence_x = 3.14159265 * _distance2d( (self._pos3d[0], self._pos3d[2]), (point3d[0], point3d[2]) ) ** 2  #TODO: only need distance 2d, not 3d.  I think.
        circumfrence_y = 3.14159265 * _distance2d( (self._pos3d[1], self._pos3d[2]), (point3d[1], point3d[2]) ) ** 2  #TODO: only need distance 2d, not 3d.  I think.

        # Find the xy screen positions.
        pixel_pos_x = self._findPixelPos( circumfrence_x, self._fov[0], screen_size[0], (point3d[0], point3d[2]), (self._pos3d[0], self._pos3d[2]),  (self._anchor3d[0], self._anchor3d[2]) )
        pixel_pos_y = self._findPixelPos( circumfrence_y, self._fov[1], screen_size[1], (point3d[1], point3d[2]), (self._pos3d[1], self._pos3d[2]),  (self._anchor3d[1], self._anchor3d[2]) )

        #print(pixel_pos_x)
        #print(pixel_pos_y)
        #print("|")
        # Return the x, then y screen positions.
        return (pixel_pos_x/2, pixel_pos_y/2)

    # Rotates the camera by the x, y, then z.  degrees3d -> (x_rot, y_rot, z_rot)
    def rotate(self, degrees3d):
        # Around the x axis, x stays the same.  z and y change.
        if degrees3d[0] != 0:
            zy_extension = _distance2d( (self._pos3d[2], self._pos3d[1]), (self._anchor3d[2], self._anchor3d[1]) )
            z_rot = self._pos3d[2] + math.cos(math.radians(degrees3d[0])) * zy_extension
            y_rot = self._pos3d[1] + math.sin(math.radians(degrees3d[0])) * zy_extension
            self._anchor3d = (self._anchor3d[0], y_rot, z_rot)

        # Around the y axis, y stays the same.  z and x change.
        if degrees3d[1] != 0:
            zx_extension = _distance2d( (self._pos3d[2], self._pos3d[0]), (self._anchor3d[2], self._anchor3d[0]) )
            z_rot = self._pos3d[2] + math.cos(math.radians(degrees3d[1])) * zx_extension
            x_rot = self._pos3d[0] + math.sin(math.radians(degrees3d[1])) * zx_extension
            self._anchor3d = (x_rot, self._anchor3d[1], z_rot)

        # Around the z axis, z stays the same.  x and y change.
        if degrees3d[2] != 0:
            xy_extension = _distance2d( (self._pos3d[0], self._pos3d[1]), (self._anchor3d[0], self._anchor3d[1]) )
            x_rot = self._pos3d[0] + math.sin(math.radians(degrees3d[2])) * distance3d(self._pos3d, self._anchor3d)
            y_rot = self._pos3d[1] + math.cos(math.radians(degrees3d[2])) * distance3d(self._pos3d, self._anchor3d)
            self._anchor3d = (x_rot, y_rot, self._anchor3d[2])

    # Moves (translates) the position by a point3d.
    def translate(self, point3d):
        self._pos3d = (self._pos3d[0] + point3d[0], self._pos3d[1] + point3d[1], self._pos3d[2] + point3d[2])
        self._anchor3d = (self._anchor3d[0] + point3d[0], self._anchor3d[1] + point3d[1], self._anchor3d[2] + point3d[2])

    def get_pos(self):
        return self._pos3d
