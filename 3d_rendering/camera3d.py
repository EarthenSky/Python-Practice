import math

# Max render distance.  I don't know what happens if you go over it.
# Incremenmting it before runtime should be safe though.
MAX_RENDER_DISTANCE = 100000  # 100 000



class camera:
    """This class manages conversion between 3d and 2d points.  This camera can be rotated."""

    # Screen size is (width, height)
    def __init__(self, fov, screen_size):
        self._screen_size = screen_size
        self._fov = (fov, fov/(self._screen_size[0]/self._screen_size[1]))  # (horizontal fov, verticle fov)

        self._pos3d = (0, 0, 0)  # xyz
        self._anchor3d = (0, 0, MAX_RENDER_DISTANCE)  # Direction point.

    # Converts (x, y, z) to (x, y).
    def convertToScreenPoint(point3d):
        pass

    # Rotates the camera by the x, y, then z.
    def rotate(degrees3d):
        # Around the x axis, x stays the same.  z and y change.
        z_rot = self._pos3d[2] + math.cos(math.radians(degrees3d[0])) * MAX_RENDER_DISTANCE
        y_rot = self._pos3d[1] - math.sin(math.radians(degrees3d[0])) * MAX_RENDER_DISTANCE
        zy_rotation_mod = (z_rot, y_rot)

        # Around the y axis, x stays the same.  z and x change.
        z_rot = self._pos3d[2] + math.cos(math.radians(degrees3d[1])) * MAX_RENDER_DISTANCE
        x_rot = self._pos3d[0] - math.sin(math.radians(degrees3d[1])) * MAX_RENDER_DISTANCE
        zx_rotation_mod = (z_rot, x_rot)

        # Around the z axis, x stays the same.  z and x change.
        z_rot = self._pos3d[2] + math.cos(math.radians(degrees3d[1])) * MAX_RENDER_DISTANCE
        x_rot = self._pos3d[0] - math.sin(math.radians(degrees3d[1])) * MAX_RENDER_DISTANCE
        zx_rotation_mod = (z_rot, x_rot)

        self._anchor3d = (0, 0, MAX_RENDER_DISTANCE)

    # Moves (translates) the position by a point3d.
    def translate(point3d):
        self._pos3d = (self._pos3d[0] + point3d[0], self._pos3d[1] + point3d[1], self._pos3d[2] + point3d[2])
        self._anchor3d = (self._anchor3d[0] + point3d[0], self._anchor3d[1] + point3d[1], self._anchor3d[2] + point3d[2])
