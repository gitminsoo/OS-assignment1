#%%
import matplotlib.pyplot as plt
plt.barh(['A', 'B', 'C'], [3, 7, 5])
plt.show()

# %%
import matplotlib.pyplot as plt

tasks = [("Task A", 1, 4), ("Task B", 2, 6), ("Task C", 4, 8)]
labels, start_times, end_times = zip(*tasks)

fig, ax = plt.subplots()
for idx, (label, start, end) in enumerate(tasks):
    ax.barh(idx, end - start, left=start, height=0.5, label=label)
    
ax.set_yticks(range(len(tasks)))
ax.set_yticklabels(labels)
ax.set_xlabel("Time")
ax.legend()
plt.show()

# %%
import matplotlib.pyplot as plt

intervals = [("Interval A", 0, 10), ("Interval B", 2, 8), ("Interval C", 5, 6)]
labels, start_times, end_times = zip(*intervals)

fig, ax = plt.subplots()

for idx, (label, start, end) in enumerate(intervals):
    ax.barh(idx, end - start, left=start, height=0.5, label=label)

ax.set_yticks(range(len(intervals)))
ax.set_yticklabels(labels)
ax.set_xlabel("Value")
ax.legend()
plt.show()

# %%
import matplotlib.pyplot as plt

intervals = [("Interval A", 0, 10), ("Interval B", 2, 8), ("Interval C", 5, 6)]

fig, ax = plt.subplots()

for label, start, end in intervals:
    ax.barh(0, end - start, left=start, height=0.5, label=label)

ax.set_yticks([0])
ax.set_yticklabels(["Intervals"])
ax.set_xlabel("Value")
ax.legend()
plt.show()

# %%
import matplotlib.pyplot as plt

intervals = [("Interval A", 0, 10), ("Interval B", 2, 8), ("Interval C", 5, 6)]

fig, ax = plt.subplots()

for label, start, end in intervals:
    ax.barh(0.3, end - start, left=start, height=0.3, label=label)

ax.set_yticks([0])
ax.set_yticklabels(["Intervals"])
ax.set_xlabel("Value")
ax.legend()
plt.show()

# %%
import matplotlib.pyplot as plt

intervals = [("Interval A", 0, 10), ("Interval B", 2, 8), ("Interval C", 5, 6)]

fig, ax = plt.subplots()

for label, start, end in intervals:
    ax.barh(0.5, end - start, left=start, height=0.2, label=label)

ax.set_yticks([0])
ax.set_yticklabels(["Intervals"])
ax.set_xlabel("Value")
ax.legend()

ax.set_ylim(0, 1)

plt.show()

# %%
