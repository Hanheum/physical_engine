import numpy as np
import matplotlib.pyplot as plt
from physic_engine_updating import ParticleCrashSimulator

posA = np.array([1, 1])
posB = np.array([90, 90])
collision_pos = np.array([100, 1000])

mA = 2
mB = 2
step1 = 20
step2 = 20

phys_en = ParticleCrashSimulator(dt=0.1)
Aseq, Bseq = phys_en(posA, posB, collision_pos, mA, mB, step1, step2)
if np.sum(Bseq) != 0:
    Aseq, Bseq = Aseq.T, Bseq.T

    plt.plot(*Aseq, 'ro')
    plt.plot(*Bseq, 'bo')

    plt.show()
else:
    print(Aseq)