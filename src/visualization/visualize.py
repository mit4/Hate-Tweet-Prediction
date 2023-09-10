import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

train_data = pd.read_csv("../../data/processrd/train_data.csv")
test_data = pd.read_csv("../../data/processrd/test_data.csv")

hate_docs = train_data[train_data["label"] == 1]
nohate_docs = train_data[train_data["label"] == 0]

hate_words = " ".join(text for text in hate_docs["tweet"])
nohate_words = " ".join(text for text in nohate_docs["tweet"])

hate_word_cloud = WordCloud(collocations=False, background_color="white").generate(
    hate_words
)
nohate_words_cloud = WordCloud(collocations=False, background_color="white").generate(
    nohate_words
)
figure = plt.figure(figsize=[15, 7])
figure.patch.set_facecolor("xkcd:mint green")
plt.subplot(1, 2, 1)
plt.imshow(hate_word_cloud, interpolation="bilinear", aspect="auto")
plt.title(label="Plot Showing Hate Words", size=16)
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(nohate_words_cloud, interpolation="bilinear", aspect="auto")
plt.title(label="Plot Showing No Hate Words", size=16)
plt.axis("off")
plt.tight_layout()
plt.show()
