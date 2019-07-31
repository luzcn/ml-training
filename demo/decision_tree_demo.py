import pandas as pd
from sklearn.tree import DecisionTreeClassifier


def exercise():
    data = pd.read_csv('../src/data/bcan.csv', na_values='?')
    data.drop('id', axis=1, inplace=True)
    data = data.dropna()

    y = data['Diag']
    x = data.drop('Diag', 1)

    # training the decision tree
    tree_clf = DecisionTreeClassifier(max_depth=3)
    tree_clf.fit(x, y)

    fnames = 'Clump Thickness,Cell Size,Cell Shape,Adhesion,Epithelial,Nuclei,Chromatin,Nucleoli,Mitoses'.split(',')
    from sklearn.tree import export_graphviz
    export_graphviz(tree_clf, out_file="bcan.dot",
                    feature_names=fnames,
                    class_names=['benign', 'malignant'],
                    rounded=True,
                    filled=True)

    # !dot -Tpng bcan.dot -o bcan.png
    # from IPython.display import Image
    # Image('bcan.png')

    # print(tree_clf)


exercise()
