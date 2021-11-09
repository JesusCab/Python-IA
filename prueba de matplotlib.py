from matplotlib import pyplot as plt

years=[1950,1960,1970,1980,1990,2000,2010]
pib=[300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

plt.plot(years,pib, color='blue',marker='o',linestyle='solid')
plt.title('PIB')
plt.ylabel('Miles de Millones')
plt.xlabel('Año')
plt.show()

#	plt.title('Gráfica de Temperatura y Humedad')	
#   plt.xlabel('Observación')
#	plt.ylabel('Lectura')
#	plt.show()