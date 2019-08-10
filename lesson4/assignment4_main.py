from gensim.models import word2vec
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt


JIEBA_PATH = "../files/lesson4/zhwiki_jieba.txt"
MODEL_PATH = "../files/lesson4/word2vec.model"

def create_gensim_model(file_path=JIEBA_PATH):
    sentence = word2vec.LineSentence(file_path)
    model = word2vec.Word2Vec(sentence, size=300)
    model.save("word2vec.model")


def test_gensim_model(file_path=MODEL_PATH):
    model = word2vec.Word2Vec.load(file_path)
    while True:
        word = input("请输入单词：")
        try:
            print(model.most_similar(word.strip()))
        except KeyError:
            print("您输入的单词: {} , 不存在，请重新输入！".format(word))


def tsne_plot(model):
    "Creates and TSNE model and plots it"
    labels = []
    tokens = []

    for word in model.wv.vocab:
        tokens.append(model[word])
        labels.append(word)

    tsne_model = TSNE(perplexity=40, n_components=2, init='pca', n_iter=2500, random_state=23)
    new_values = tsne_model.fit_transform(tokens)

    x = []
    y = []
    for value in new_values:
        x.append(value[0])
        y.append(value[1])

    plt.figure(figsize=(16, 16))
    for i in range(len(x)):
        plt.scatter(x[i], y[i])
        plt.annotate(labels[i],
                     xy=(x[i], y[i]),
                     xytext=(5, 2),
                     textcoords='offset points',
                     ha='right',
                     va='bottom')
    plt.show()


def visualisation_model(file_path=MODEL_PATH):
    model = word2vec.Word2Vec.load(file_path)
    tsne_plot(model)


if __name__ == '__main__':
    visualisation_model()

