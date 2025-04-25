import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(14, 7))
ax.set_xlim(0, 10)
ax.set_ylim(0, 8)
ax.axis('off')

# Função para desenhar caixas
def draw_box(text, xy, width=1.6, height=0.8, fc='lightblue'):
    box = patches.FancyBboxPatch((xy[0], xy[1]), width, height,
                                 boxstyle="round,pad=0.1", ec='black', fc=fc)
    ax.add_patch(box)
    ax.text(xy[0]+width/2, xy[1]+height/2, text,
            ha='center', va='center', fontsize=10, weight='bold')

# Função para desenhar setas com texto
def draw_arrow(start, end, label, color='black'):
    arrowprops = dict(arrowstyle='->', color=color)
    ax.annotate(label, xy=end, xytext=start,
                arrowprops=arrowprops, fontsize=9, ha='center')

# Posicionar os blocos
positions = {
    "IDL": (0.5, 6),
    "CC": (0.5, 4.8),
    "SS": (0.5, 3.6),
    "PS": (0.5, 2.4),
    "Comp": (2.5, 4.2),
    "Atitude": (4.5, 6),
    "NormaSubj": (4.5, 4.2),
    "Autoeficacia": (4.5, 2.4),
    "Intencao": (6.5, 4.2),
    "Comportamento": (8.5, 4.2),
}

# Desenhar os blocos
draw_box("Information & Data Literacy", positions["IDL"], fc='white')
draw_box("Communication & Collaboration", positions["CC"], fc='white')
draw_box("Digital Safety", positions["SS"], fc='white')
draw_box("Problem Solving", positions["PS"], fc='white')
draw_box("Digital Competence\n(2nd order)", positions["Comp"])
draw_box("Attitude", positions["Atitude"], fc='lightgreen')
draw_box("Subjective Norms", positions["NormaSubj"], fc='lightgreen')
draw_box("Self-Efficacy", positions["Autoeficacia"], fc='lightgreen')
draw_box("Entrepreneurial\nIntention", positions["Intencao"], fc='orange')
draw_box("Entrepreneurial\nBehavior", positions["Comportamento"], fc='orange')

# Setas da Competência Digital para os fatores cognitivos
draw_arrow((2.5+1.6, 4.2+0.4), (4.5, 6-0.4), "β = 0.691, H1a ✓")  # Atitude
draw_arrow((2.5+1.6, 4.2), (4.5, 4.2), "β = –0.160, H1b ✗")        # Normas Subj.
draw_arrow((2.5+1.6, 4.2-0.4), (4.5, 2.4+0.4), "β = 0.670, H1c ✓") # Autoeficácia

# Setas para Intenção
draw_arrow((4.5+1.6, 6), (6.5, 4.2+0.4), "β = 0.643, H2a ✓")
draw_arrow((4.5+1.6, 4.2), (6.5, 4.2), "β = –0.160, H2b ✗")
draw_arrow((4.5+1.6, 2.4), (6.5, 4.2-0.4), "β = 0.504, H2c ✓")

# Setas para Comportamento
draw_arrow((6.5+1.6, 4.2), (8.5, 4.2+0.2), "β = 0.449, H3a ✓")
draw_arrow((4.5+1.6, 2.4), (8.5, 4.2-0.2), "β = 0.440, H3b ✓")

# Título
plt.title("Structural Model – Digital Competence, TPB Cognitions, and Entrepreneurial Behavior",
          fontsize=12, weight='bold')

plt.tight_layout()
plt.show()
