
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

dice_options = np.arange(1, 6)


rolls = np.random.choice(dice_options, (100_000, 20)).sum(axis=1)
choice = np.array(rolls)
df = pd.DataFrame(choice)

sns.histplot(df, kde=True, bins=30)
#sns.histplot(df)
plt.grid()
plt.xlabel("sum of two number")
plt.show()