import math

'''Important Note:  Try not to keep the rotation value getting larger and larger, that
might be bad...  Just try not to do that ok?  Set it back to 0 instead of 360; thanks.
I just realized that > 360 degrees makes the arccos input go above abs(1) ... so that's bad.
Don't do it.'''

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

    # Cap value.
    if form > 1:
        form = 1
    elif form < -1:
        form = -1

    # Do cosine law.
    return math.degrees( math.acos( form ) )

# Find what side of a line a 2d point is on.
def _2d_line_side(pnt_line1, pnt_line2, pnt):
    d = (pnt[0] - pnt_line1[0]) * (pnt_line2[1] - pnt_line1[1]) - (pnt[1] - pnt_line1[1]) * (pnt_line2[0] - pnt_line1[0])
    if d > 0:
        return 0
    else:
        return 1

class camera:
    """This class manages conversion between 3d and 2d points.  This camera can be rotated."""

    # Screen size is (width, height)
    def __init__(self, fov, screen_size):
        self._screen_size = screen_size
        self._fov = (fov, fov/(float(self._screen_size[0])/self._screen_size[1]))  # (horizontal fov, verticle fov)

        self._pos3d = (0, 0, 0)  # xyz
        self._anchor3d = (0, 0, MAX_RENDER_DISTANCE)  # Direction point.
        self._rotation_degrees3d = (0, 0, 0)

    # is_find_x is a boolean value.  start_pnt2d is (x, z) or (y, z)
    def _findPixelPos(self, circumfrence, fov_angle, screen_distance, start_pnt2d, cam_pnt2d, anchor_pnt2d):
        #print(start_pnt2d, cam_pnt2d, anchor_pnt2d)
        #print("-------------------------------------")

        # Find the perimeter of the fov cone.
        fov_range_distance = float(circumfrence) * float(fov_angle)/360

        #print(fov_range_distance)

        # Find the angle between the point and the edge of the fov.
        temp = _2d_line_side(cam_pnt2d, anchor_pnt2d, start_pnt2d)
        temp2 = _three_point_angle(start_pnt2d, cam_pnt2d, anchor_pnt2d)

        edge_angle = ( (fov_angle/2) - temp2 ) + (temp2 * temp)

        #print(edge_angle, temp)

        # Find distance to the side of the screen.
        edge_range_distance = circumfrence * (edge_angle/360)

        #print str(edge_range_distance/fov_range_distance)

        # Scale distance to the pixel value.
        return (edge_range_distance/fov_range_distance) * screen_distance

    # Converts (x, y, z) to (x, y) but as a screen position.
    def convertToScreenPoint(self, point3d, screen_size):
        circumfrence_x = 3.14159265 * _distance2d( (self._pos3d[0], self._pos3d[2]), (point3d[0], point3d[2]) ) ** 2  #TODO: only need distance 2d, not 3d.  I think.  IS THIS GOOD NOW? OK?
        circumfrence_y = 3.14159265 * _distance2d( (self._pos3d[1], self._pos3d[2]), (point3d[1], point3d[2]) ) ** 2  #TODO: only need distance 2d, not 3d.  I think.  IS THIS OK NOW? GOOD?

        # Rotate the points so they are flush with the z axis and numbers are constant.
        #new_anchor, new_point3d = self._get_rotated_back(self._anchor3d, point3d)  # TODO: dont need to rotate the anchor every time.
        new_anchor = self._anchor3d
        new_point3d = point3d

        # Find the x, y screen positions.
        pixel_pos_x = self._findPixelPos( circumfrence_x, self._fov[0], screen_size[0], (new_point3d[0], new_point3d[2]), (self._pos3d[0], self._pos3d[2]),  (new_anchor[0], new_anchor[2]) )
        pixel_pos_y = self._findPixelPos( circumfrence_y, self._fov[1], screen_size[1], (new_point3d[1], new_point3d[2]), (self._pos3d[1], self._pos3d[2]),  (new_anchor[1], new_anchor[2]) )

        print(pixel_pos_x, pixel_pos_y)
        print(self._pos3d)
        print("-----------------------")

        # Return the x, then y screen positions.
        return (pixel_pos_x, pixel_pos_y)

    def convertToScreenPointAngleMethod(self, point3d, screen_size):
        # X pixel -------------------------------------------------- (uses X and Z)

        # The radius is the distance between the point and the camera.
        radius = _distance2d( (self._pos3d[0], self._pos3d[2]), (point3d[0], point3d[2]) )

        corner_point = (self._pos3d[0], point3d[2])  # This point is (x, z)

        # Find the angle from the side of the field of view.
        x_angle = (self._fov[0] / 2) - math.degrees( math.acos( _distance2d( (corner_point[0], corner_point[1]), (self._pos3d[0], self._pos3d[2]) ) / radius ) )

        # If the vertex point is to the right of the main point fix the rotation value.
        if point3d[0] > self._pos3d[0]:
            x_angle = self._fov[0] - x_angle

            # If the point is behind the head, and to the right, fix rotation, again.
            if point3d[2] < self._pos3d[2]:
                x_angle = 180 - ( x_angle - self._fov[0] )
        else:
            # If the point is behind the head, and to the left, fix rotation
            if point3d[2] < self._pos3d[2]:
                x_angle = -(90 - (self._fov[0] / 2) + x_angle)

        # Finds the ratio between the two angles
        ratio = x_angle / self._fov[0]

        print (ratio)

        # Scale the ratio to the screen_size, yielding the pixel position.
        x_pixel_pos = screen_size[0] * ratio

        # Y pixel --------------------------------------------------

        radius = _distance2d( (self._pos3d[1], self._pos3d[2]), (point3d[1], point3d[2]) )

        corner_point = (self._pos3d[1], point3d[2])  # This point is (x, z)

        # Find the angle from the side of the field of view.
        y_angle = (self._fov[1] / 2) - math.degrees( math.acos( _distance2d( (corner_point[0], corner_point[1]), (self._pos3d[1], self._pos3d[2]) ) / radius ) )

        # If the vertex point is to the right of the main point fix the rotation value.
        if point3d[1] > self._pos3d[1]:
            y_angle = self._fov[1] - y_angle

            # If the point is behind the head, and to the right, fix rotation, again.
            if point3d[2] < self._pos3d[2]:
                y_angle = 180 - ( y_angle - self._fov[1] )
        else:
            # If the point is behind the head, and to the left, fix rotation
            if point3d[2] < self._pos3d[2]:
                y_angle = -(90 - (self._fov[1] / 2) + y_angle)

        # Finds the ratio between the two angles
        ratio = y_angle / self._fov[1]

        # Scale the ratio to the screen_size, yielding the pixel position.
        y_pixel_pos = screen_size[1] * ratio

        # Output ---------------------------------------------------

        print "----------------"
        return (x_pixel_pos, y_pixel_pos)

    def to_screen_point_straight_angle_method(self, point3d, screen_size):
        # Pre ------------------------------------------------------ (only z)

        # If the point is behind the head, tag it for line rendering and tri rendering.
        if point3d[2] < self._pos3d[2]:
            pass

        # X pixel -------------------------------------------------- (uses x and z)

        corner_point = (self._pos3d[0], point3d[2])  # This point is (x, z)

        # Find the size of the fov when scaled to the point.  (fov_size is aka "d")
        fov_size = math.tan(math.radians(self._fov[0]/2)) * _distance2d(corner_point, (self._pos3d[0], self._pos3d[2]))

        # The distance from the side of the fov.
        offset_value = (self._fov[0]/2) - _distance2d(corner_point, (point3d[0], point3d[2]))

        # If the vertex point is to the right of the main point fix the offset value.
        if point3d[0] > self._pos3d[0]:
            offset_value = fov_size - offset_value

        # TODO: MODIFY THE OFFSET VALUE WITH THE ROTATION VALUE.

        # The ratio between the distance from the side of the fov and the fov_size, used to calculate the x_pixel_pos.
        scale_ratio = offset_value / fov_size

        # Calculates the x position of the point, converted to pixels.
        x_pixel_pos = screen_size[0] * scale_ratio

        # Y pixel -------------------------------------------------- (uses y and z)

        corner_point = (self._pos3d[1], point3d[2])  # This point is (x, z)

        # Find the size of the fov when scaled to the point.  (fov_size is aka "d")
        fov_size = math.tan(math.radians(self._fov[1]/2)) * _distance2d(corner_point, (self._pos3d[1], self._pos3d[2]))

        # The distance from the side of the fov.
        offset_value = (self._fov[1]/2) - _distance2d(corner_point, (point3d[1], point3d[2]))

        # If the vertex point is to the right of the main point fix the offset value.
        if point3d[1] > self._pos3d[1]:
            offset_value = fov_size - offset_value

        # TODO: MODIFY THE OFFSET VALUE WITH THE ROTATION VALUE.

        # The ratio between the distance from the side of the fov and the fov_size, used to calculate the x_pixel_pos.
        scale_ratio = offset_value / fov_size

        # Calculates the x position of the point, converted to pixels.
        y_pixel_pos = screen_size[1] * scale_ratio

        # Output ---------------------------------------------------

        #print (x_pixel_pos, y_pixel_pos)
        print "----------------"
        return (x_pixel_pos, y_pixel_pos)

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
            x_rot = self._pos3d[0] + math.sin(math.radians(degrees3d[2])) * xy_extension
            y_rot = self._pos3d[1] + math.cos(math.radians(degrees3d[2])) * xy_extension
            self._anchor3d = (x_rot, y_rot, self._anchor3d[2])

        # Change the rotation variable.
        self._rotation_degrees3d = (self._rotation_degrees3d[0] + degrees3d[0], self._rotation_degrees3d[1] + degrees3d[0], self._rotation_degrees3d[2] + degrees3d[0])

    def rotate2d(self, degrees3d):
        pass  # Do rotation angle mod shit.

    # Gets two points rotated back to the start, equally.
    def _get_rotated_back(self, pnt3d1, pnt3d2):
        # Around the x axis, x stays the same.  z and y change.
        zy_extension = _distance2d( (self._pos3d[2], self._pos3d[1]), (pnt3d1[2], pnt3d1[1]) )
        z_rot = self._pos3d[2] + math.cos(math.radians(self._rotation_degrees3d[0])) * zy_extension
        y_rot = self._pos3d[1] + math.sin(math.radians(self._rotation_degrees3d[0])) * zy_extension
        pnt3d1 = (pnt3d1[0], y_rot, z_rot)

        # Around the y axis, y stays the same.  z and x change.
        zx_extension = _distance2d( (self._pos3d[2], self._pos3d[0]), (pnt3d1[2], pnt3d1[0]) )
        z_rot = self._pos3d[2] + math.cos(math.radians(self._rotation_degrees3d[1])) * zx_extension
        x_rot = self._pos3d[0] + math.sin(math.radians(self._rotation_degrees3d[1])) * zx_extension
        pnt3d1 = (x_rot, pnt3d1[1], z_rot)

        # Around the z axis, z stays the same.  x and y change.
        xy_extension = _distance2d( (self._pos3d[0], self._pos3d[1]), (pnt3d1[0], pnt3d1[1]) )
        x_rot = self._pos3d[0] + math.sin(math.radians(self._rotation_degrees3d[2])) * xy_extension
        y_rot = self._pos3d[1] + math.cos(math.radians(self._rotation_degrees3d[2])) * xy_extension
        pnt3d1 = (x_rot, y_rot, pnt3d1[2])

        # Do the same thing for pnt3d2 now.

        # Around the x axis, x stays the same.  z and y change.
        zy_extension = _distance2d( (self._pos3d[2], self._pos3d[1]), (pnt3d2[2], pnt3d2[1]) )
        z_rot = self._pos3d[2] + math.cos(math.radians(self._rotation_degrees3d[0])) * zy_extension
        y_rot = self._pos3d[1] + math.sin(math.radians(self._rotation_degrees3d[0])) * zy_extension
        pnt3d2 = (pnt3d2[0], pnt3d2[1] + y_rot, pnt3d2[2] + z_rot)

        # Around the y axis, y stays the same.  z and x change.
        zx_extension = _distance2d( (self._pos3d[2], self._pos3d[0]), (pnt3d2[2], pnt3d2[0]) )
        z_rot = self._pos3d[2] + math.cos(math.radians(self._rotation_degrees3d[1])) * zx_extension
        x_rot = self._pos3d[0] + math.sin(math.radians(self._rotation_degrees3d[1])) * zx_extension
        pnt3d2 = (pnt3d2[0] + x_rot, pnt3d2[1], pnt3d2[2] + z_rot)

        # Around the z axis, z stays the same.  x and y change.
        xy_extension = _distance2d( (self._pos3d[0], self._pos3d[1]), (pnt3d2[0], pnt3d2[1]) )
        x_rot = self._pos3d[0] + math.sin(math.radians(self._rotation_degrees3d[2])) * xy_extension
        y_rot = self._pos3d[1] + math.cos(math.radians(self._rotation_degrees3d[2])) * xy_extension
        pnt3d2 = (pnt3d2[0] + x_rot, pnt3d2[1] + y_rot, pnt3d2[2])

        return pnt3d1, pnt3d2

    # Moves (translates) the position by a point3d.
    def translate(self, point3d):
        self._pos3d = (self._pos3d[0] + point3d[0], self._pos3d[1] + point3d[1], self._pos3d[2] + point3d[2])
        self._anchor3d = (self._anchor3d[0] + point3d[0], self._anchor3d[1] + point3d[1], self._anchor3d[2] + point3d[2])

    def get_pos(self):
        return self._pos3d
