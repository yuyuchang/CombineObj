# CombineObj

* Download blender: we use blender-2.82-linux64.
* Add the extracted folder to the env PATH: https://docs.blender.org/manual/en/2.79/getting_started/installing/linux.html
* Run the script:
```
  $ blender -b -P gpu.py -E CYCLES --python combine.py -- --mesh_file /path/to/obj_file \
    --mtl_file /path/to/mtl_file \
    --results_path /path/to/combined_obj_file
```
