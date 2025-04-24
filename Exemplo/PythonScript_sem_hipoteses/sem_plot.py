import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyArrowPatch

fig, ax = plt.subplots(figsize=(16, 12))
ax.set_xlim(0, 15)
ax.set_ylim(0, 12)
ax.axis('off')

box_w, box_h = 2.2, 1.0

def draw_box(text, xy):
    box = patches.FancyBboxPatch(xy, box_w, box_h,
                                 boxstyle="round,pad=0.1", ec="black", fc="lightblue")
    ax.add_patch(box)
    ax.text(xy[0] + box_w / 2, xy[1] + box_h / 2, text,
            ha='center', va='center', fontsize=10, weight='bold')

def draw_arrow(start_xy, end_xy, curve=False, offset=0.3):
    x0, y0 = start_xy[0] + box_w, start_xy[1] + box_h / 2
    x1, y1 = end_xy[0], end_xy[1] + box_h / 2
    if curve:
        style = f"arc3,rad={offset}"
    else:
        style = "arc3,rad=0"
    arrow = FancyArrowPatch((x0, y0), (x1, y1),
                            connectionstyle=style,
                            arrowstyle='->', mutation_scale=15, color='black')
    ax.add_patch(arrow)

# Coordenadas ajustadas
positions = {
    'IDL': (1, 10),
    'CC': (1, 8),
    'SS': (1, 6),
    'PS': (1, 4),
    'CompDigitais': (4, 8),
    'Atitude': (7.5, 10),
    'NormaSubj': (7.5, 8),
    'Autoeficacia': (7.5, 6),
    'Intencao': (10.5, 8),
    'Comportamento': (13, 8),  # Ajustado para ficar visível
}

# Desenhar blocos
for label, pos in positions.items():
    draw_box(label, pos)

# Relações para CompDigitais
draw_arrow(positions['IDL'], positions['CompDigitais'])
draw_arrow(positions['CC'], positions['CompDigitais'])
draw_arrow(positions['SS'], positions['CompDigitais'])
draw_arrow(positions['PS'], positions['CompDigitais'])

# CompDigitais → variáveis endógenas
draw_arrow(positions['CompDigitais'], positions['Atitude'])
draw_arrow(positions['CompDigitais'], positions['NormaSubj'])
draw_arrow(positions['CompDigitais'], positions['Autoeficacia'])

# CompDigitais → Intencao (única seta curva justificada)
draw_arrow(positions['CompDigitais'], positions['Intencao'], curve=True, offset=0.35)

# Atitude, NormaSubj, Autoeficacia → Intencao
draw_arrow(positions['Atitude'], positions['Intencao'])
draw_arrow(positions['NormaSubj'], positions['Intencao'])
draw_arrow(positions['Autoeficacia'], positions['Intencao'])

# Intencao → Comportamento (direta)
draw_arrow(positions['Intencao'], positions['Comportamento'])

# Seta de Autoeficacia → Comportamento, conectando por baixo do retângulo de Comportamento
start = (positions['Autoeficacia'][0] + box_w, positions['Autoeficacia'][1] + box_h / 2)
end = (positions['Comportamento'][0] + box_w / 2, positions['Comportamento'][1])
arrow = FancyArrowPatch(start, end, arrowstyle='->', mutation_scale=15, color='black')
ax.add_patch(arrow)

plt.title("Modelo D01 – Competências Digitais e Comportamento (SEM Corrigido)",
          fontsize=14, weight='bold')
plt.tight_layout()
plt.show()
