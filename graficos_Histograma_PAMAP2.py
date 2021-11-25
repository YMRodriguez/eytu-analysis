import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

title_font = {'fontname':'Arial', 'size':'22', 'color':'black', 'weight':'bold', 'verticalalignment':'bottom', 'family':'monospace'}
plt.rcParams.update({'font.size': 15})

# ================PAMAP=============================================================

dfPamap_rep = pd.read_csv('energy/PAMAP2/energy_rep.fea_csv', delimiter=',', names=('energy_rep_1', 'energy_rep_2', 'energy_rep_3'))
dfPamap_no_rep = pd.read_csv('energy/PAMAP2/energy_no_rep.fea_csv', delimiter=',', names=('energy_no_rep_1', 'energy_no_rep_2', 'energy_no_rep_3'))
dfPamap_pos = pd.read_csv('energy/PAMAP2/energy_pos.fea_csv', delimiter=',', names=('energy_pos_1', 'energy_pos_2', 'energy_pos_3'))

# HAND 

plt.figure(figsize=(13, 5)) #Para cambiar el formato del gráfico, haciendolo más ancho

bins1 = np.linspace(0, 150, 250)

plt.hist(dfPamap_rep.energy_rep_1, bins1, alpha = 0.5, color="#1565CE", label='Movimientos repetitivos', edgecolor="#297EB9", linewidth=0.05)
plt.hist(dfPamap_no_rep.energy_no_rep_1, bins1, alpha = 0.6, color="#52B233", label='Gestos', edgecolor="#317D19", linewidth=0.05)
plt.hist(dfPamap_pos.energy_pos_1, bins1, alpha = 0.5, color="#DF5A04", label='Posturas', edgecolor="#A1500D", linewidth=0.05)

plt.xlim(0, 150)
plt.xticks(np.arange(0, 151, step=10))
plt.ylim(0, 20000)

plt.xlabel('Energía de la señal', verticalalignment ='top', fontstyle = 'italic', size='18', color = "#000000")
plt.ylabel('Número de ventanas', verticalalignment='bottom', fontstyle = 'italic', size='18', color = "#000000")

plt.legend(loc='upper right', fontsize=15)
plt.grid(color = '0.7', axis = 'y', linestyle= '-', linewidth=.2)

plt.title('Módulo de la energía por ventana de la muñeca - PAMAP2', title_font)
plt.savefig('img/PAMAP2/hand/energy_1.pdf', dpi=1000.0)
plt.savefig('img/PAMAP2/hand/energy_1.png', dpi=1000.0)
plt.show()

# ZOOM HAND
plt.figure(figsize=(13, 5)) #Para cambiar el formato del gráfico, haciendolo más ancho

bins2 = np.linspace(0, 50, 250)

plt.hist(dfPamap_rep.energy_rep_1, bins2, alpha = 0.5, color="#1565CE", label='Movimientos repetitivos', edgecolor="#297EB9", linewidth=0.05)
plt.hist(dfPamap_no_rep.energy_no_rep_1, bins2, alpha = 0.6, color="#52B233", label='Gestos', edgecolor="#317D19", linewidth=0.05)
plt.hist(dfPamap_pos.energy_pos_1, bins2, alpha = 0.5, color="#DF5A04", label='Posturas', edgecolor="#A1500D", linewidth=0.05)

plt.xlim(0, 40)
plt.xticks(np.arange(0, 51, step=5))
plt.ylim(0, 400)

plt.xlabel('Energía de la señal', verticalalignment ='top', fontstyle = 'italic', size='18', color = "#000000")
plt.ylabel('Número de ventanas', verticalalignment='bottom', fontstyle = 'italic', size='18', color = "#000000")

plt.legend(loc='upper right', fontsize=15)
plt.grid(color = '0.7', axis = 'y', linestyle= '-', linewidth=.2)

plt.title('Módulo de la energía por ventana de la muñeca - PAMAP2', title_font)
plt.savefig('img/PAMAP2/hand/energy_1_zoom.pdf', dpi=1000.0)
plt.savefig('img/PAMAP2/hand/energy_1_zoom.png', dpi=1000.0)
plt.show()

# GRANULADO HAND
plt.figure(figsize=(13, 5)) #Para cambiar el formato del gráfico, haciendolo más ancho

bins3 = np.linspace(0, 50, 600)

plt.hist(dfPamap_rep.energy_rep_1, bins3, alpha = 0.5, color="#1565CE", label='Movimientos repetitivos', edgecolor="#297EB9", linewidth=0.05)
plt.hist(dfPamap_no_rep.energy_no_rep_1, bins3, alpha = 0.6, color="#52B233", label='Gestos', edgecolor="#317D19", linewidth=0.05)
plt.hist(dfPamap_pos.energy_pos_1, bins3, alpha = 0.5, color="#DF5A04", label='Posturas', edgecolor="#A1500D", linewidth=0.05)

plt.xlim(0, 50)
plt.xticks(np.arange(0, 51, step=5))
plt.ylim(0, 160)

plt.xlabel('Energía de la señal', verticalalignment ='top', fontstyle = 'italic', size='18', color = "#000000")
plt.ylabel('Número de ventanas', verticalalignment='bottom', fontstyle = 'italic', size='18', color = "#000000")

plt.legend(loc='upper right', fontsize=15)
plt.grid(color = '0.7', axis = 'y', linestyle= '-', linewidth=.2)

plt.title('Módulo de la energía por ventana de la muñeca - PAMAP2', title_font)
plt.savefig('img/PAMAP2/hand/energy_1_granulado.pdf', dpi=1000.0)
plt.savefig('img/PAMAP2/hand/energy_1_granulado.png', dpi=1000.0)
plt.show()

# GRANULADO CON UMBRAL HAND
plt.figure(figsize=(13, 5)) #Para cambiar el formato del gráfico, haciendolo más ancho

bins4 = np.linspace(0, 50, 600)
umbral_pamap2_hand = 2.88

plt.axvline(x=umbral_pamap2_hand, ymin=0, ymax=160, color="#000608", label='Umbral', linewidth=2 )
plt.hist(dfPamap_rep.energy_rep_1, bins4, alpha = 0.5, color="#1565CE", label='Movimientos repetitivos', edgecolor="#297EB9", linewidth=0.05)
plt.hist(dfPamap_no_rep.energy_no_rep_1, bins4, alpha = 0.6, color="#52B233", label='Gestos', edgecolor="#317D19", linewidth=0.05)
plt.hist(dfPamap_pos.energy_pos_1, bins4, alpha = 0.5, color="#DF5A04", label='Posturas', edgecolor="#A1500D", linewidth=0.05)

plt.xlim(0, 50)
plt.xticks(np.arange(0, 51, step=5))
plt.ylim(0, 160)

plt.xlabel('Energía de la señal', verticalalignment ='top', fontstyle = 'italic', size='18', color = "#000000")
plt.ylabel('Número de ventanas', verticalalignment='bottom', fontstyle = 'italic', size='18', color = "#000000")

plt.legend(loc='upper right', fontsize=15)
plt.grid(color = '0.7', axis = 'y', linestyle= '-', linewidth=.2)

plt.title('Módulo de la energía por ventana de la muñeca - PAMAP2', title_font)
plt.savefig('img/PAMAP2/hand/energy_1_granulado_umbral.pdf', dpi=1000.0)
plt.savefig('img/PAMAP2/hand/energy_1_granulado_umbral.png', dpi=1000.0)
plt.show()


# CHEST 

plt.figure(figsize=(13, 5)) #Para cambiar el formato del gráfico, haciendolo más ancho

bins5 = np.linspace(0, 100, 250)

plt.hist(dfPamap_rep.energy_rep_2, bins5, alpha = 0.5, color="#1565CE", label='Movimientos repetitivos', edgecolor="#297EB9", linewidth=0.05)
plt.hist(dfPamap_no_rep.energy_no_rep_2, bins5, alpha = 0.6, color="#52B233", label='Gestos', edgecolor="#317D19", linewidth=0.05)
plt.hist(dfPamap_pos.energy_pos_2, bins5, alpha = 0.5, color="#DF5A04", label='Posturas', edgecolor="#A1500D", linewidth=0.05)

plt.xlim(0, 100)
plt.xticks(np.arange(0, 101, step=10))
plt.ylim(0, 20000)

plt.xlabel('Energía de la señal', verticalalignment ='top', fontstyle = 'italic', size='18', color = "#000000")
plt.ylabel('Número de ventanas', verticalalignment='bottom', fontstyle = 'italic', size='18', color = "#000000")

plt.legend(loc='upper right', fontsize=15)
plt.grid(color = '0.7', axis = 'y', linestyle= '-', linewidth=.2)

plt.title('Módulo de la energía por ventana del pecho - PAMAP2', title_font)
plt.savefig('img/PAMAP2/chest/energy_2.pdf', dpi=1000.0)
plt.savefig('img/PAMAP2/chest/energy_2.png', dpi=1000.0)
plt.show()

# CHEST ZOOM

plt.figure(figsize=(13, 5)) #Para cambiar el formato del gráfico, haciendolo más ancho

bins6 = np.linspace(0, 2, 200)

plt.hist(dfPamap_rep.energy_rep_2, bins6, alpha = 0.5, color="#1565CE", label='Movimientos repetitivos', edgecolor="#297EB9", linewidth=0.05)
plt.hist(dfPamap_no_rep.energy_no_rep_2, bins6, alpha = 0.6, color="#52B233", label='Gestos', edgecolor="#317D19", linewidth=0.05)
plt.hist(dfPamap_pos.energy_pos_2, bins6, alpha = 0.5, color="#DF5A04", label='Posturas', edgecolor="#A1500D", linewidth=0.05)

plt.xlim(0, 2)
plt.xticks(np.arange(0, 2.01, step=0.2))
plt.ylim(0, 200)

plt.xlabel('Energía de la señal', verticalalignment ='top', fontstyle = 'italic', size='18', color = "#000000")
plt.ylabel('Número de ventanas', verticalalignment='bottom', fontstyle = 'italic', size='18', color = "#000000")

plt.legend(loc='upper right', fontsize=15)
plt.grid(color = '0.7', axis = 'y', linestyle= '-', linewidth=.2)

plt.title('Módulo de la energía por ventana del pecho - PAMAP2', title_font)
plt.savefig('img/PAMAP2/chest/energy_2_zoom.pdf', dpi=1000.0)
plt.savefig('img/PAMAP2/chest/energy_2_zoom.png', dpi=1000.0)
plt.show()

# CHEST GRANULADO

plt.figure(figsize=(13, 5)) #Para cambiar el formato del gráfico, haciendolo más ancho

bins7 = np.linspace(0, 2, 500)

plt.hist(dfPamap_rep.energy_rep_2, bins7, alpha = 0.5, color="#1565CE", label='Movimientos repetitivos', edgecolor="#297EB9", linewidth=0.05)
plt.hist(dfPamap_no_rep.energy_no_rep_2, bins7, alpha = 0.6, color="#52B233", label='Gestos', edgecolor="#317D19", linewidth=0.05)
plt.hist(dfPamap_pos.energy_pos_2, bins7, alpha = 0.5, color="#DF5A04", label='Posturas', edgecolor="#A1500D", linewidth=0.05)

plt.xlim(0, 2)
plt.xticks(np.arange(0, 2.01, step=0.2))
plt.ylim(0, 60)

plt.xlabel('Energía de la señal', verticalalignment ='top', fontstyle = 'italic', size='18', color = "#000000")
plt.ylabel('Número de ventanas', verticalalignment='bottom', fontstyle = 'italic', size='18', color = "#000000")

plt.legend(loc='upper right', fontsize=15)
plt.grid(color = '0.7', axis = 'y', linestyle= '-', linewidth=.2)

plt.title('Módulo de la energía por ventana del pecho - PAMAP2', title_font)
plt.savefig('img/PAMAP2/chest/energy_2_granulado.pdf', dpi=1000.0)
plt.savefig('img/PAMAP2/chest/energy_2_granulado.png', dpi=1000.0)
plt.show()

# CHEST GRANULADO CON UMBRAL

plt.figure(figsize=(13, 5)) #Para cambiar el formato del gráfico, haciendolo más ancho

bins8 = np.linspace(0, 2, 500)
umbral_pamap2_chest = 0.35

plt.axvline(x=umbral_pamap2_chest, ymin=0, ymax=160, color="#000608", label='Umbral' , linewidth=2)
plt.hist(dfPamap_rep.energy_rep_2, bins8, alpha = 0.5, color="#1565CE", label='Movimientos repetitivos', edgecolor="#297EB9", linewidth=0.05)
plt.hist(dfPamap_no_rep.energy_no_rep_2, bins8, alpha = 0.6, color="#52B233", label='Gestos', edgecolor="#317D19", linewidth=0.05)
plt.hist(dfPamap_pos.energy_pos_2, bins8, alpha = 0.5, color="#DF5A04", label='Posturas', edgecolor="#A1500D", linewidth=0.05)

plt.xlim(0, 2)
plt.xticks(np.arange(0, 2.01, step=0.2))
plt.ylim(0, 60)

plt.xlabel('Energía de la señal', verticalalignment ='top', fontstyle = 'italic', size='18', color = "#000000")
plt.ylabel('Número de ventanas', verticalalignment='bottom', fontstyle = 'italic', size='18', color = "#000000")

plt.legend(loc='upper right', fontsize=15)
plt.grid(color = '0.7', axis = 'y', linestyle= '-', linewidth=.2)

plt.title('Módulo de la energía por ventana del pecho - PAMAP2', title_font)
plt.savefig('img/PAMAP2/chest/energy_2_granulado_umbral.pdf', dpi=1000.0)
plt.savefig('img/PAMAP2/chest/energy_2_granulado_umbral.png', dpi=1000.0)
plt.show()

# ANKLE 

plt.figure(figsize=(13, 5)) #Para cambiar el formato del gráfico, haciendolo más ancho

bins9 = np.linspace(0, 250, 250)

plt.hist(dfPamap_rep.energy_rep_3, bins9, alpha = 0.5, color="#1565CE", label='Movimientos repetitivos', edgecolor="#297EB9", linewidth=0.05)
plt.hist(dfPamap_no_rep.energy_no_rep_3, bins9, alpha = 0.6, color="#52B233", label='Gestos', edgecolor="#317D19", linewidth=0.05)
plt.hist(dfPamap_pos.energy_pos_3, bins9, alpha = 0.5, color="#DF5A04", label='Posturas', edgecolor="#A1500D", linewidth=0.05)

plt.xlim(0, 250)
plt.xticks(np.arange(0, 251, step=10))
plt.ylim(0, 20000)

plt.xlabel('Energía de la señal', verticalalignment ='top', fontstyle = 'italic', size='18', color = "#000000")
plt.ylabel('Número de ventanas', verticalalignment='bottom', fontstyle = 'italic', size='18', color = "#000000")

plt.legend(loc='upper right', fontsize=15)
plt.grid(color = '0.7', axis = 'y', linestyle= '-', linewidth=.2)

plt.title('Módulo de la energía por ventana del tobillo - PAMAP2', title_font)
plt.savefig('img/PAMAP2/ankle/energy_3.pdf', dpi=1000.0)
plt.savefig('img/PAMAP2/ankle/energy_3.png', dpi=1000.0)
plt.show()

# ANKLE ZOOM

plt.figure(figsize=(13, 5)) #Para cambiar el formato del gráfico, haciendolo más ancho

bins10 = np.linspace(0, 0.4, 200)

plt.hist(dfPamap_rep.energy_rep_3, bins10, alpha = 0.5, color="#1565CE", label='Movimientos repetitivos', edgecolor="#297EB9", linewidth=0.05)
plt.hist(dfPamap_no_rep.energy_no_rep_3, bins10, alpha = 0.6, color="#52B233", label='Gestos', edgecolor="#317D19", linewidth=0.05)
plt.hist(dfPamap_pos.energy_pos_3, bins10, alpha = 0.5, color="#DF5A04", label='Posturas', edgecolor="#A1500D", linewidth=0.05)

plt.xlim(0, 0.4)
plt.xticks(np.arange(0, 0.41, step=0.05))
plt.ylim(0, 200)

plt.xlabel('Energía de la señal', verticalalignment ='top', fontstyle = 'italic', size='18', color = "#000000")
plt.ylabel('Número de ventanas', verticalalignment='bottom', fontstyle = 'italic', size='18', color = "#000000")

plt.legend(loc='upper right', fontsize=15)
plt.grid(color = '0.7', axis = 'y', linestyle= '-', linewidth=.2)

plt.title('Módulo de la energía por ventana del tobillo - PAMAP2', title_font)
plt.savefig('img/PAMAP2/ankle/energy_3_zoom.pdf', dpi=1000.0)
plt.savefig('img/PAMAP2/ankle/energy_3_zoom.png', dpi=1000.0)
plt.show()

# ANKLE GRANULADO

plt.figure(figsize=(13, 5)) #Para cambiar el formato del gráfico, haciendolo más ancho

bins11 = np.linspace(0, 0.4, 500)

plt.hist(dfPamap_rep.energy_rep_3, bins11, alpha = 0.5, color="#1565CE", label='Movimientos repetitivos', edgecolor="#297EB9", linewidth=0.05)
plt.hist(dfPamap_no_rep.energy_no_rep_3, bins11, alpha = 0.6, color="#52B233", label='Gestos', edgecolor="#317D19", linewidth=0.05)
plt.hist(dfPamap_pos.energy_pos_3, bins11, alpha = 0.5, color="#DF5A04", label='Posturas', edgecolor="#A1500D", linewidth=0.05)

plt.xlim(0, 0.4)
plt.xticks(np.arange(0, 0.41, step=0.05))
plt.ylim(0, 70)

plt.xlabel('Energía de la señal', verticalalignment ='top', fontstyle = 'italic', size='18', color = "#000000")
plt.ylabel('Número de ventanas', verticalalignment='bottom', fontstyle = 'italic', size='18', color = "#000000")

plt.legend(loc='upper right', fontsize=15)
plt.grid(color = '0.7', axis = 'y', linestyle= '-', linewidth=.2)

plt.title('Módulo de la energía por ventana del tobillo - PAMAP2', title_font)
plt.savefig('img/PAMAP2/ankle/energy_3_granulado.pdf', dpi=1000.0)
plt.savefig('img/PAMAP2/ankle/energy_3_granulado.png', dpi=1000.0)
plt.show()

# ANKLE GRANULADO UMBRAL

plt.figure(figsize=(13, 5)) #Para cambiar el formato del gráfico, haciendolo más ancho

bins12 = np.linspace(0, 0.4, 500)
umbral_pamap2_ankle = 0.06

plt.axvline(x=umbral_pamap2_ankle, ymin=0, ymax=160, color="#000608", label='Umbral' , linewidth=2)
plt.hist(dfPamap_rep.energy_rep_3, bins12, alpha = 0.5, color="#1565CE", label='Movimientos repetitivos', edgecolor="#297EB9", linewidth=0.05)
plt.hist(dfPamap_no_rep.energy_no_rep_3, bins12, alpha = 0.6, color="#52B233", label='Gestos', edgecolor="#317D19", linewidth=0.05)
plt.hist(dfPamap_pos.energy_pos_3, bins12, alpha = 0.5, color="#DF5A04", label='Posturas', edgecolor="#A1500D", linewidth=0.05)

plt.xlim(0, 0.4)
plt.xticks(np.arange(0, 0.41, step=0.05))
plt.ylim(0, 70)

plt.xlabel('Energía de la señal', verticalalignment ='top', fontstyle = 'italic', size='18', color = "#000000")
plt.ylabel('Número de ventanas', verticalalignment='bottom', fontstyle = 'italic', size='18', color = "#000000")

plt.legend(loc='upper right', fontsize=15)
plt.grid(color = '0.7', axis = 'y', linestyle= '-', linewidth=.2)

plt.title('Módulo de la energía por ventana del tobillo - PAMAP2', title_font)
plt.savefig('img/PAMAP2/ankle/energy_3_granulado_umbral.pdf', dpi=1000.0)
plt.savefig('img/PAMAP2/ankle/energy_3_granulado_umbral.png', dpi=1000.0)
plt.show()