from distutils.dir_util import copy_tree
import sys
import os
import shutil

if(len(sys.argv) < 2):
    print('Please input environment name')
    print('Right syntax: python [path to this file] [space] [environment name]')
    exit()

dirname, _ = os.path.split(os.path.abspath(sys.argv[0]))
name_env = sys.argv[1]
cwd = os.getcwd()
dest_env = os.path.join(cwd, name_env)
path_example = os.path.join(dirname, 'example')

copy_tree(path_example, dest_env)

dest_env_dic = os.path.join(dest_env, 'example')
dest_env_dic_name = os.path.join(dest_env, name_env)

shutil.move(dest_env_dic, dest_env_dic_name)
os.rename(os.path.join(dest_env_dic_name, 'envs', 'example.py'),
          os.path.join(dest_env_dic_name, 'envs', name_env+'.py'))
for dname, dirs, files in os.walk(dest_env):
    for fname in files:
        fpath = os.path.join(dname, fname)
        with open(fpath) as f:
            s = f.read()
        s = s.replace("Example", name_env.title())
        s = s.replace("example", name_env)
        with open(fpath, "w") as f:
            f.write(s)
