# Krok 1: Importy
import numpy as np
import matplotlib.pyplot as plt
from PIL.ImageColor import colormap
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
from mpl_toolkits.mplot3d import Axes3D
from sklearn.inspection import DecisionBoundaryDisplay

# Krok 2: Wczytanie zbioru danych Iris
iris = load_iris()
X = iris.data  # cechy
y = iris.target  # etykiety klas

# Krok 3: Podział na zbiór uczący i testowy (70% / 30%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Krok 4: Poszukiwanie najlepszego N (liczby sąsiadów)
accuracies = []
neighbors = range(3, 21)

for n in neighbors: 
    model = KNeighborsClassifier(n_neighbors=n)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    accuracies.append(acc)

# Wykres dokładności vs liczba sąsiadów
plt.plot(neighbors, accuracies, marker='o')
plt.title('Dokładność vs liczba sąsiadów')
plt.xlabel('Liczba sąsiadów (N)')
plt.ylabel('Dokładność')
plt.grid(True)
plt.show()

# Krok 5: Wybór najlepszego N
best_n = neighbors[np.argmax(accuracies)]
print(f'Najlepsza dokładność przy N = {best_n}')

# Krok 6: Trenowanie modelu z najlepszym N
model = KNeighborsClassifier(n_neighbors=best_n)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Krok 7: Macierz konfuzji
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=iris.target_names)
disp.plot()
plt.title("Macierz konfuzji")
plt.show()

# Krok 8: Wykresy 2D – rzeczywiste klasy
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis', edgecolor='k')
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.title('Rzeczywisty podział klas (2D)')
plt.show()

# Wykres 2D – klasyfikacja przez model
y_pred_all = model.predict(X)
plt.scatter(X[:, 0], X[:, 1], c=y_pred_all, cmap='viridis', edgecolor='k')
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.title('Predykcja modelu (2D)')
plt.show()

# Krok 9: Wykres 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=y, cmap='viridis', edgecolor='k')
ax.set_xlabel('Sepal length')
ax.set_ylabel('Sepal width')
ax.set_zlabel('Petal length')
plt.title('Rzeczywisty podział klas (3D)')
plt.show()

# Krok 10: Wizualizacja granicy decyzyjnej (2D)
X_2d = X[:, :2]

# Podział danych
X_train_2d, X_test_2d, y_train_2d, y_test_2d = train_test_split(X_2d, y, test_size=0.3, random_state=42)

# Trening modelu na 2D danych
model_2d = KNeighborsClassifier(n_neighbors=best_n)
model_2d.fit(X_train_2d, y_train_2d)

# Tworzenie wykresu
fig, ax = plt.subplots()

# Wyświetlanie granicy decyzyjnej
disp = DecisionBoundaryDisplay.from_estimator(
    model_2d,
    X_2d,
    response_method="predict",
    plot_method="pcolormesh",
    xlabel=iris.feature_names[0],  # "sepal length (cm)"
    ylabel=iris.feature_names[1],  # "sepal width (cm)"
    shading="auto",
    alpha=0.5,
    ax=ax,
)

# Dodanie punktów danych do wykresu
scatter = disp.ax_.scatter(X_2d[:, 0], X_2d[:, 1], c=y, edgecolors="k", cmap="viridis")

# Legenda klas
disp.ax_.legend(
    scatter.legend_elements()[0],
    iris.target_names,
    loc="lower left",
    title="Classes",
)

disp.ax_.set_title(f"3-Class classification\n(k={model_2d.n_neighbors})")

plt.show()