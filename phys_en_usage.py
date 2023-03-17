import numpy as np
import matplotlib.pyplot as plt
from physic_engine import ParticleCrashSimulator

posA = np.array([1, 1])
posB = np.array([5, 8])
collision_pos = np.array([-3, 6])

mA = 2
mB = 2
step1 = 10
step2 = 10

phys_en = ParticleCrashSimulator()
Aseq, Bseq = phys_en(posA, posB, collision_pos, mA, mB, step1, step2)
Aseq, Bseq = Aseq.T, Bseq.T

plt.plot(*Aseq, 'ro')
plt.plot(*Bseq, 'bo')

plt.show()