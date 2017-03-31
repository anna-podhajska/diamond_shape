# choinka gora plus dol


gwiazdka = "*"
spacja = ' '
ilosc_gwiazdek = 0  # w rzedzie #
ilosc_spacji = 0

raw = raw_input('wpisz maksymalna ilosc gwiazdek: ')

try:

    max_liczba_gwiazdek = int(raw)  # zmiana na int
    
except:
    print ' error ' 
    
    
ilosc_spacji = int(raw)  # zmiana na int

gora = True
dol = False

while gora:

	ilosc_gwiazdek = ilosc_gwiazdek + 1
	ilosc_spacji = ilosc_spacji - 1

	print ilosc_spacji * spacja,
	print '*',
	print (ilosc_gwiazdek * gwiazdka) * 2,
	print '*'

	if ilosc_gwiazdek == max_liczba_gwiazdek:
		dol = True
		gora = False

while dol:

	ilosc_gwiazdek = ilosc_gwiazdek - 1
	ilosc_spacji = ilosc_spacji + 1

	print ilosc_spacji * spacja,
	print '*',
	print (ilosc_gwiazdek * gwiazdka) * 2,
	print '*'

	if ilosc_spacji == max_liczba_gwiazdek: break
	#dol = False
            #gora = True
        


