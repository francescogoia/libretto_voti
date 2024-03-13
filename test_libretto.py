from voto import Libretto, Voto

lib = Libretto()
def main():
    voto_1 = Voto("Analisi 1", 10, 25, False, '2022-02-10')
    voto_2 = Voto("Fisica 1", 10, 27, False, '2022-06-15')
    voto_3 = Voto("Analisi 2", 8, 23, False, '2023-02-16')
    voto_4 = Voto("Basi di Dati", 8, 30, True, '2023-01-30')
    voto_5 = Voto("Fisica 2", 6, 25, False, '2023-02-05')
    voto_6 = Voto("Statistica", 10, 20, False, '2022-02-14')
    voto_7 = Voto("Algebra", 10, 30, False, '2022-06-27')
    voto_8 = Voto("Informatica", 8, 23, False, '2022-02-04')
    voto_9 = Voto("Economia", 8, 28, False, '2023-07-18')
    voto_10 = Voto("Sistemi di produzione", 8, 30, True, '2023-07-15')
    voto_11 = Voto("Sistemi elettrici", 8, 30, False, '2023-06-30')
    voto_12 = Voto("Programmazione a oggetti", 8, 29, False, '2024-02-8')

    lista_voti = [voto_1, voto_2, voto_3, voto_4, voto_5, voto_6, voto_7, voto_8, voto_9, voto_10, voto_11, voto_12]
    for v in lista_voti:
        lib.append(v)

    voti_25 = lib.findByPunteggio(25, False)
    for v in voti_25:
        print(v.esame)

    voto_analisi2 = lib.findByEsame("Analisi 27")
    """
    if voto_analisi2.punteggio == 30 and voto_analisi2.lode == True:
        print(f"Hai preso 30 e lode")
    else:
        print(f"Hai preso {voto_analisi2.punteggio}")
    """
    if voto_analisi2 is None:                   ## il chiamante deve ricordarsi di controllare
        print("Nessun voto trovato")
    else:
        print(f"{voto_analisi2.esame} voto: {voto_analisi2.str_punteggio()}")

    try:
        voto_analisi2 = lib.findByEsame2("Analisi 27")      ## scatena un eccezione che non vine gestita dal programma chiamante
        print(f"{voto_analisi2.esame} voto: {voto_analisi2.str_punteggio()}")
    except ValueError:                                                ## obbligo il chiamante a controllare
        print("Nessun voto trovato, secondo metodo")


    nuovo1 = Voto("Fisica 1", 10, 27, False, "2022-06-15")
    nuovo2 = Voto("Fisica 2", 6, 30, False, '2023-02-05')
    print("1", lib.has_voto(nuovo1))
    print("2", lib.has_voto(nuovo2))



main()