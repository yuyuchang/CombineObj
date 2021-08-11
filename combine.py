import argparse, sys, os
import json
import bpy
import mathutils
import numpy as np
from mathutils import Vector, Euler
from math import pi

class ArgumentParserForBlender(argparse.ArgumentParser):
    def _get_argv_after_doubledash(self):
        try:
            idx = sys.argv.index("--")
            return sys.argv[idx+1:]
        except ValueError as e:
            return []

    def parse_args(self):
        return super().parse_args(args=self._get_argv_after_doubledash())

parser = ArgumentParserForBlender()
parser.add_argument('--mesh_file', type=str, default='')
parser.add_argument('--mtl_file', type=str, default='')
parser.add_argument('--results_path', type=str, default='')
##parser.add_argument('--text_file', type=str, default='')
args = parser.parse_args()

MESH_FILE = args.mesh_file
MTL_FILE = args.mtl_file
##TEXTURE_FILE = args.text_file

DEBUG = False

VIEWS = 500
#VIEWS = 40
RESOLUTION = 800
RESULTS_PATH = args.results_path
DEPTH_SCALE = 1.4
COLOR_DEPTH = 8
FORMAT = 'PNG'
RANDOM_VIEWS = True
#RANDOM_VIEWS = False
UPPER_VIEWS = False
CIRCLE_FIXED_START = (.3, 0, 0)

#bpy.ops.import_scene.obj(filepath=MESH_FILE, filter_glob=MTL_FILE)
#bpy.ops.object.origin_set(type="GEOMETRY_ORIGIN")
objs = bpy.data.objects
objs.remove(objs["Cube"], do_unlink=True)
bpy.ops.import_scene.obj(filepath=MESH_FILE, filter_glob=MTL_FILE)

scene = bpy.context.scene
obs = []
for ob in scene.objects:
    if ob.type == "MESH":
        obs.append(ob)

ctx = bpy.context.copy()
ctx['active_object'] = obs[0]
ctx['selected_editable_objects'] = obs
bpy.ops.object.join(ctx)
bpy.ops.export_scene.obj(filepath = RESULTS_PATH)