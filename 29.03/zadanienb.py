#1. Znaleźć na Kaggle dataset zawierający opinie/recenzje/teksty itd na którym można wykonać zadania klasyfikacji (najlepiej binarnej).
#2. Za pomocą make_pipeline stworzyć dwa pipeliny z `CountVectorizer`, a następnie `MultinomialNB` oraz `LogisticRegression`. Dobrać
#parametry do `CountVectorizer` tak, żeby odciąć najczęsciej oraz najrzadziej występujące słowa.
#3. Dla obu modeli:
#    - Nauczyć model na danych uczących.
#    - Pokazać dokładność predykcji na danych uczących i na danych testowych.
#    - Wygenerować macierz konfuzji dla obu klasyfikatorów (*: Zrobić tak, żeby obie macierzy były wygenerowane na jednym Figure (trzeba zrobić Figure z dwoma ax i sprawdzić w dokumentacji jak podać ax do funkcji generującej wykres macierzy konfuzji.))
#    - Przetestować kilka różnych zestawów parametrów, potencjalnie zwiększając jakość modeli.
#4. Dla regresji Logistycznej w regularyzacją L2: zastosować `GridSearchCV` do doboru optymalnej wartości C.
#5. Stworzyć model Regresji Logistycznej używając regularyzacji L1.
#6. Wygenerować wykres, przedstawiający wartości 20tu wag oraz cech dla tych wag, które najbardziej wpływają na odpowiedź modelu.

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, ConfusionMatrixDisplay
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression

df = pd.read_csv(r"C:\Users\aczac\Desktop\studia\analiza\analiza\spam.csv", encoding='latin-1')[['v1', 'v2']]
df.columns = ['label', 'text']
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

X = df['text']
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Parametry do CountVectorizera
vectorizer_params = {
    'stop_words': 'english',
    'max_df': 0.9,  # odrzucenie najczęstszych słów (>=90%)
    'min_df': 5     # odrzucenie bardzo rzadkich słów (wyst. < 5 razy)
}

# Pipeline 1: Naive Bayes
pipe_nb = make_pipeline(
    CountVectorizer(**vectorizer_params),
    MultinomialNB()
)

# Pipeline 2: Logistic Regression
pipe_lr = make_pipeline(
    CountVectorizer(**vectorizer_params),
    LogisticRegression(max_iter=1000)
)

# Trening modeli
pipe_nb.fit(X_train, y_train)
pipe_lr.fit(X_train, y_train)


# Predykcje
y_pred_nb = pipe_nb.predict(X_test)
y_pred_lr = pipe_lr.predict(X_test)

# Dokładność
print("Naive Bayes - Train accuracy:", pipe_nb.score(X_train, y_train))
print("Naive Bayes - Test accuracy:", accuracy_score(y_test, y_pred_nb))
print("Logistic Regression - Train accuracy:", pipe_lr.score(X_train, y_train))
print("Logistic Regression - Test accuracy:", accuracy_score(y_test, y_pred_lr))

# Macierze konfuzji
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

ConfusionMatrixDisplay.from_predictions(y_test, y_pred_nb, ax=axs[0])
axs[0].set_title('Naive Bayes')

ConfusionMatrixDisplay.from_predictions(y_test, y_pred_lr, ax=axs[1])
axs[1].set_title('Logistic Regression')

plt.tight_layout()
plt.show()


pipe_lr_l2 = make_pipeline(
    CountVectorizer(**vectorizer_params),
    LogisticRegression(penalty='l2', solver='liblinear', max_iter=1000)
)

param_grid = {
    'logisticregression__C': [0.01, 0.1, 1, 10, 100]
}

grid = GridSearchCV(pipe_lr_l2, param_grid, cv=5, scoring='accuracy')
grid.fit(X_train, y_train)

print("Best C:", grid.best_params_)
print("Best score on CV:", grid.best_score_)
print("Test accuracy:", grid.score(X_test, y_test))

pipe_lr_l1 = make_pipeline(
    CountVectorizer(**vectorizer_params),
    LogisticRegression(penalty='l1', solver='liblinear', C=grid.best_params_['logisticregression__C'], max_iter=1000)
)

pipe_lr_l1.fit(X_train, y_train)
print("Test accuracy (L1):", pipe_lr_l1.score(X_test, y_test))

# Pobieranie nazw cech i wag
vec = pipe_lr_l1.named_steps['countvectorizer']
clf = pipe_lr_l1.named_steps['logisticregression']

feature_names = np.array(vec.get_feature_names_out())
coefs = clf.coef_[0]

# Wybieramy 20 cech o największej wartości bezwzględnej współczynnika
top_indices = np.argsort(np.abs(coefs))[-20:]
top_features = feature_names[top_indices]
top_weights = coefs[top_indices]

# Tworzenie wykresu
plt.figure(figsize=(12, 6))
colors = ['red' if w < 0 else 'blue' for w in top_weights]

plt.barh(range(len(top_features)), top_weights, color=colors)
plt.yticks(range(len(top_features)), top_features)
plt.xlabel("Wartość współczynnika")
plt.title("Top 20 cech wpływających na klasyfikację (L1 Logistic Regression)")
plt.tight_layout()
plt.show()



# Przykładowa wiadomość
new_message = ["Wanna go on a date with me? I love flirting!"]

# Predykcja etykiety
prediction = pipe_lr_l1.predict(new_message)[0]

# Predykcja prawdopodobieństwa
proba = pipe_lr_l1.predict_proba(new_message)[0]  # to jest tablica: [p(ham), p(spam)]

# Wyniki
print(f"Predykcja: {'SPAM' if prediction == 1 else 'HAM'}")
print(f"Prawdopodobieństwo HAM: {proba[0]:.2f}, SPAM: {proba[1]:.2f}")





