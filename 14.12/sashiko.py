import matplotlib.pyplot as plt

# Wymiary prostokąta w milimetrach
rectangle_width = 50  # 5 cm = 50 mm
rectangle_height = 170  # 17 cm = 170 mm

# Pozycja początku rysowania linii (6 mm nad prawym dolnym rogiem prostokąta)
start_x = rectangle_width
start_y = 6

# Definiujemy pierwszy krok i powtarzalne kroki rysowania linii
initial_step = (-6, 0)  # 6 mm w lewo (tylko raz na początku)
repeating_steps = [
    (0, 6),   # 6 mm w górę
    (-12, 0), # 12 mm w lewo
]

# Tworzymy wykres
fig, ax = plt.subplots()

# Rysujemy tło prostokąta
rect = plt.Rectangle((0, 0), rectangle_width, rectangle_height, edgecolor='black', facecolor='white')
ax.add_patch(rect)

# Rysujemy pierwszą linię
x, y = start_x, start_y

# Wykonujemy pierwszy krok
x += initial_step[0]
y += initial_step[1]
ax.plot([start_x, x], [start_y, y], color='black')

# Kontynuujemy z powtarzalnymi krokami
while x > 0 or y <= rectangle_height:
    for dx, dy in repeating_steps:
        new_x = x + dx
        new_y = y + dy

# Rysujemy drugą linię 18 mm nad punktem początkowym pierwszej linii
second_start_x = start_x
second_start_y = start_y + 18  # 18 mm wyżej

# Definiujemy kroki dla drugiej linii
second_line_steps = [
    (-12, 0), # 12 mm w lewo
    (0, 6),   # 6 mm w górę
]

x, y = second_start_x, second_start_y
while x > 0 or y <= rectangle_height:
    for dx, dy in second_line_steps:
        new_x = x + dx
        new_y = y + dy

# Ustawiamy proporcje osi i granice wykresu
ax.set_aspect('equal')
ax.set_xlim(-10, rectangle_width + 10)
ax.set_ylim(-10, rectangle_height + 10)

# Dodajemy siatkę dla lepszej orientacji
ax.grid(True, which='both', linestyle='--', linewidth=0.5)

# Wyświetlamy wykres
plt.show()
