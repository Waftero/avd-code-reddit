def caratteri_ripetuti(stringa):
    ripetizioni = []
    caratteri_esaminati = set()

    for char in stringa:
        if char not in caratteri_esaminati:
            if char != 'J':
                # Controlla quante volte il carattere si ripete
                conteggio = conta_carattere_ripetuto(stringa, char)

                # Se si ripete più di una volta, aggiungilo alla lista
                if conteggio > 1:
                    ripetizioni.append(conteggio)
            
            caratteri_esaminati.add(char)
    ripetizioni.append(conta_carattere_ripetuto(stringa, 'J'))
    return ripetizioni

def conta_carattere_ripetuto(stringa, carattere):
    conteggio = 0
    for char in stringa:
        if char == carattere:
            conteggio += 1
    return conteggio

def ordina_lista_stringhe_con_valore(lista):
    simboli_ordinati = "J23456789TQKA"
    def chiave_di_ordinamento(item):
        # Utilizza il valore associato come secondo criterio di ordinamento
        # (primo criterio è l'ordine della stringa)
        stringa, valore = item
        return [simboli_ordinati.index(char) for char in stringa], valore

    # Usa la chiave di ordinamento personalizzata per ordinare la lista
    lista_ordinata = sorted(lista, key=chiave_di_ordinamento)

    return lista_ordinata
class es14:
    games = []
    with open("es13", 'r') as f:
        for line in f:
            game = line.split()
            games.append(game)
    
    high = []
    one = []
    two = []
    three = []
    full = []
    four = []
    five = []

    for game in games:
        #print(caratteri_ripetuti(game[0]))
        if(caratteri_ripetuti(game[0]) == [0]):
            high.append(game)  
        if(caratteri_ripetuti(game[0]) == [2, 0] or caratteri_ripetuti(game[0]) == [1]):
            one.append(game)
        if(caratteri_ripetuti(game[0]) == [2, 2, 0]):
            two.append(game) 
        if(caratteri_ripetuti(game[0]) == [3, 0] or caratteri_ripetuti(game[0]) == [2, 1] or caratteri_ripetuti(game[0]) == [2]):
            three.append(game) 
        if(caratteri_ripetuti(game[0]) == [2, 3, 0] or caratteri_ripetuti(game[0]) == [3, 2, 0] or caratteri_ripetuti(game[0]) == [2, 2, 1]):
            full.append(game)
        if(caratteri_ripetuti(game[0]) == [4, 0] or caratteri_ripetuti(game[0]) == [3, 1] or caratteri_ripetuti(game[0]) == [2, 2] or caratteri_ripetuti(game[0]) == [3]):
            four.append(game)
        if(caratteri_ripetuti(game[0]) == [5, 0] or caratteri_ripetuti(game[0]) == [5] or caratteri_ripetuti(game[0]) == [4] or caratteri_ripetuti(game[0]) == [3, 2] 
           or caratteri_ripetuti(game[0]) == [2, 3] or caratteri_ripetuti(game[0]) == [4, 1]):
            five.append(game) 
       
    high = ordina_lista_stringhe_con_valore(high)
    tot = 0
    for i in range(len(high)):
        tot += int(high[i][1]) * (i+1)

    one = ordina_lista_stringhe_con_valore(one)
    for i in range(len(one)):
        tot += int(one[i][1]) * (i+len(high)+1)

    two = ordina_lista_stringhe_con_valore(two)
    for i in range(len(two)):
        tot += int(two[i][1]) * (i+1+len(one)+len(high))
    
    three = ordina_lista_stringhe_con_valore(three)
    for i in range(len(three)):
        tot += int(three[i][1]) * (i+len(two)+len(one)+len(high)+1)

    full = ordina_lista_stringhe_con_valore(full)
    for i in range(len(full)):
        tot += int(full[i][1]) * (i+len(three)+len(two)+len(one)+len(high)+1)    

    four = ordina_lista_stringhe_con_valore(four)
    for i in range(len(four)):
        tot += int(four[i][1]) * (i+len(full)+len(three)+len(two)+len(one)+len(high)+1)    

    five = ordina_lista_stringhe_con_valore(five)
    for i in range(len(five)):
        tot += int(five[i][1]) * (i+len(four)+len(full)+len(three)+len(two)+len(one)+len(high)+1)
    print(high, one, two, three, full, four, five)
    print(tot)
    