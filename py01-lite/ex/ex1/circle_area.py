import sys 
import math

def conv_int(cmd_params):
  int_params = list(map(int, cmd_params))
  return int_params

def circle_area(int_params):
  radius = int_params[0]
  return math.pi * radius * radius

cmd_params = sys.argv[1:]