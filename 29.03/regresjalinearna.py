#1. Wczytać dataset diabetis
#2. Wybrać ze wczytanego zbioru danych kolumny (zmienne) pod indeksami 0, 2, 3. Zgodnie z dokumentacją są
#to zmienne: age age in years, bmi body mass index, bp average blood pressure.
#3. Narysować 3 wykresy punktowe, pokazujące jak zmienna zależna (y) zależy od zmiennych niezależnych (3
#poprzednio wybrane kolumny z X).
#4. Podzielić zbiór danych na dane uczące i testujące w proporcji 80% danych uczących i 20% danych testowych.
#5. Utworzyć obiekt regresji liniowej i nauczyć go na danych uczących
#6. Wykonać predykcje na danych testowych i obliczyć błąd średniokwadratowy pomiędzy rzeczywistymi danymi a predykcją
#7. Sprawdzić, czy dodanie innych zmiennych poza tymi wybranymi może polepszyć jakość regresji (zmniejszyć
#błąd na danych testowych). W celu tego proszę powtórzyć w pętli punkty 2-6 wybierając poza zmiennymi
#wskazanymi w punkcie 2 jedną z pozostałych zmiennych (inną w każdej iteracji).
#8. Proszę wykonać raport w postaci PDF. W raporcie proszę umieścić wyniki poszczególnych etapów wykonywania zadania,
#jak to wygenerowane wykresy, otrzymane wartości błędów na zbiorze testowym, informacje o tym czy inne zmienne poprawiają
#czy pogarszają jakość regresji, wyniki błędu średniokwadrotowego dla innych zestawów zmiennych.

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split


# 1. Wczytanie zbioru danych
diabetes = load_diabetes()
X = diabetes.data
y = diabetes.target
feature_names = diabetes.feature_names

# 2. Wybranie kolumn: age (0), bmi (2), bp (3)
selected_indices = [0, 2, 3]
X_selected = X[:, selected_indices]

# 3. Wykresy punktowe
for idx, feature_idx in enumerate(selected_indices):
    plt.figure()
    plt.scatter(X[:, feature_idx], y)
    plt.xlabel(feature_names[feature_idx])
    plt.ylabel('target')
    plt.title(f'{feature_names[feature_idx]} vs Target')
    plt.grid(True)
    plt.show()

# 4. Podział danych
X_train, X_test, y_train, y_test = train_test_split(X_selected, y, test_size=0.2, random_state=42)

# 5. Regresja liniowa
reg = LinearRegression()
reg.fit(X_train, y_train)

# 6. Predykcja i MSE
y_pred = reg.predict(X_test)
mse_selected = mean_squared_error(y_test, y_pred)
print(f"Średni błąd MSE (age, bmi, bp): {mse_selected:.2f}")

# 7. Dodawanie dodatkowych zmiennych
results = []
for i in range(X.shape[1]):
    if i not in selected_indices:
        # Dodanie nowej zmiennej
        X_extended = np.column_stack((X_selected, X[:, i]))

        # Podział na zbiór uczący i testowy
        X_train_ext, X_test_ext, y_train_ext, y_test_ext = train_test_split(X_extended, y, test_size=0.2,
                                                                            random_state=42)

        # Trening
        model_ext = LinearRegression()
        model_ext.fit(X_train_ext, y_train_ext)

        # Predykcja
        y_pred_ext = model_ext.predict(X_test_ext)

        # Obliczenie błędu
        mse_ext = mean_squared_error(y_test_ext, y_pred_ext)

        results.append({
            'dodana_zmienna': feature_names[i],
            'mse': mse_ext
        })

# 8. Wyniki
results_df = pd.DataFrame(results)
print("\nWyniki dla różnych dodatkowych zmiennych:")
print(results_df)

# Najlepsza dodatkowa zmienna
best = results_df.loc[results_df['mse'].idxmin()]
print(f"\nNajlepsza dodatkowa zmienna: {best['dodana_zmienna']} z MSE = {best['mse']:.4f}")

