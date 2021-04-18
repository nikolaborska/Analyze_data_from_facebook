import inline
import pandas as pd
import inline
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_json("/Users/nikolaborska/PYTHON_projects/Analyzing_my_FACEBOOK_data/facebook-nichiesvedova/posts/"
                  "your_posts_1.json")
df.rename(columns={"timestamp": "date"}, inplace=True)
df = df.drop(["attachments", "title", "tags"], axis=1)
pd.to_datetime(df["date"])
#=============================================================================================================
# zjištění počtu měsíčních příspěvků
df = df.set_index('date')
post_counts = df['data'].resample('MS').size() # MS pro začátek měsíce, převzorkování dat podle měsíce
print("Monthly Post Count")
print(post_counts)
#=============================================================================================================
# nastavení velikosti a velikosti písmen
sns.set(rc={'figure.figsize':(40,20)})
sns.set(font_scale=3)
#=============================================================================================================
# nastavení popisků
x_labels = post_counts.index
#=============================================================================================================
# sloupcový graf
sns.barplot(x_labels, post_counts, color="blue")
#=============================================================================================================
# jen leden prvního každý druhý rok
tick_positions = np.arange(10, len(x_labels), step=24)
#=============================================================================================================
# jen počty př
plt.xticks(tick_positions, x_labels[tick_positions].strftime("%Y"))


print("counting the rows", df.shape) # počet řádků, které analyzujeme
df.head(3)
print(df.head())
plt.show() # graf