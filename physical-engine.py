import numpy as np

dt = 0.1           #const
e = 0.5            #const
posA = np.array([10, 20])           #input
posB = np.array([5, 8])             #input
collision_pos = np.array([6, 15])   #input
mA = 3     #input
mB = 2     #input
steps= 10  #input

steps2 = 10

VecA = collision_pos-posA
VecB = collision_pos-posB

def get_vec_size(vec):
    return (vec[0]**2 + vec[1]**2)**0.5

def normalize(vec):
    size = get_vec_size(vec)
    return vec/size

def distance2D(pos1, pos2):
    return ((pos2[0]-pos1[0])**2+(pos2[1]-pos1[1])**2)**0.5

VecA = normalize(VecA)
VecB = normalize(VecB)

disA = distance2D(posA, collision_pos)
disB = distance2D(posB, collision_pos)

timegap = dt*steps

vA = disA/timegap
vB = disB/timegap

VecA *= vA
VecB *= vB

Aseq = [posA]
Bseq = [posB]

for step in range(1, steps+1):
    new_posA = posA-VecA*(dt*step)
    new_posB = posB-VecB*(dt*step)
    Aseq.append(new_posA)
    Bseq.append(new_posB)
    
