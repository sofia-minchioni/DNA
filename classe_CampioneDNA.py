class CampioneDNA:
    """
    questa classe rappresenta un campione di DNA, tracciandone la sequenza nucleotidica, i geni identificati
    e un registro delle mutazioni rilevate nel tempo
    """
    def __init__(self,__codice_campione,__sequenza,laboratorio,__geni_mappati=[],__mutazioni_rilevate={}):
        """
        inizializza una nuova istanza della classe DNA con alcuni parametri:
        codice_campione(str): identifica il campione
        sequenza(str): sequenza nucleotidica
        laboratorio(str): nome del laboratorio
        geni_mappati[str]: lista dei geni
        mutazioni_rilevate{int,str}: mutazioni del DNA rilevate
        """
        self.__codice_campione=__codice_campione
        self.__sequenza=__sequenza.upper()
        self.__geni_mappati=__geni_mappati
        self.__mutazioni_rilevate=__mutazioni_rilevate
        self.laboratorio=laboratorio
    
    def aggiungi_gene(self,gene):
        """
        aggiunge un nuovo gene alla lista solo se esso non è già presente all'interno della lista
        per evitare duplicati
        parametro:
        gene(str):è il nuovo gene che viene aggiunto alla lista solo nel caso in cui non è gia presente
        """
        if gene in self.__geni_mappati:
            print("il gene è gia presente")
        else:
            self.__geni_mappati.append(gene)
            print("il gene è stato aggiunto")

    def registra_mutazioni(self,posizione,tipo_mutazione):
        """
        inserisce o aggiorna una mutazione nel dizionario __mutazioni_rilevate
        parametri:
        posizione(int):indica la posizionedella mutazione
        tipo_mutazione(str):indicam il tipo di mutazione
        """
        self.__mutazioni_rilevate[posizione]=tipo_mutazione
        print("la mutazione è stata aggiunta")

    def calcola_percentuale_gc(self):
        """
        calcola la percentula di basi Guanina(G) e Citosina(C) all'interno della sequenza
        restituisce:
        percentuale(float):percentuale di basi guanina e citosina calcolata rispetto alla lunghezza della sequenza nucleotidica
        """
        if len(self.__sequenza) == 0:
            return 0.0
        somma_GC = 0
        for base in self.__sequenza:
            if base == "G" or base== "C":
                somma_GC = somma_GC + 1
        percentuale = (somma_GC / len(self.__sequenza)) * 100
        return percentuale
        
    def stampa_report(self):
        """
        permette di stampare a video la scheda riassuntiva con tutti i dati del campione
        """
        if len(self.__sequenza) > 20:
            seq_troncata = self.__sequenza[:20] + "..."
        else:
            seq_troncata=self.__sequenza
        print("--scheda riassuntiva dati campione--")
        print("codice: ",self.__codice_campione)
        print("laboratorio: ",self.laboratorio)
        print("sequenza: ",seq_troncata)
        print("geni mappati: ",self.__geni_mappati)
        print("mutazioni: ",self.__mutazioni_rilevate)
        print("Percentuale GC:", self.calcola_percentuale_gc(), "%")

if __name__=="__main__":
    listaGeni=["geneA","ampR2","lacZ"]
    dizionarioMutazioni={45:"sostituzione", 120:"delezione"}
    campioneUno=CampioneDNA("DNA-4029","ATCGGCT","LabGen-BioApp", listaGeni,dizionarioMutazioni)
    campioneUno.aggiungi_gene("geneA")
    campioneUno.registra_mutazioni(45, "sostituzione")
    campioneUno.calcola_percentuale_gc()
    campioneUno.stampa_report()
    
    

    