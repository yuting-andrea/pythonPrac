
import matplotlib.pyplot as plt
print(dir(matplotlib))

plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.ylabel('some numbers')
plt.xlabel('x-axis')
plt.axis([0, 6, 0, 20])
plt.show()
