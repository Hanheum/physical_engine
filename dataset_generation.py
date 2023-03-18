import numpy as np
from physic_engine import ParticleCrashSimulator
import matplotlib.pyplot as plt

phys_en = ParticleCrashSimulator(dt=0.05, e=0.1)

def particle_crash_simulation(posA, posB, collide_position, mA, mB, step1, step2):
    Aseq, Bseq = phys_en(posA=posA, posB=posB, collision_pos=collide_position, mA=mA, mB=mB, steps1=step1, steps2=step2)
    plt.plot(*Aseq.T, 'ro')
    plt.plot(*Bseq.T, 'bo')
    combined = np.concatenate((Aseq.T, Bseq.T), axis=0)
    mA_arr = np.ones((1, Aseq.shape[0])) * mA
    mB_arr = np.ones((1, Aseq.shape[0])) * mB
    combined = np.concatenate((combined, mA_arr), axis=0)
    combined = np.concatenate((combined, mB_arr), axis=0)
    combined = combined.T
    return combined

posA = np.array([1, 1])
posB = np.array([5, 8])
collision_pos = np.array([3, -3])
mA = 3
mB = 2
step1 = 20
step2 = 20

dataset = particle_crash_simulation(posA, posB, collision_pos, mA, mB, step1, step2)
print(np.round(dataset, 3))
plt.show()