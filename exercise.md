# Programació per a la ciència de dades - PEC4

En aquest Notebook trobareu l\'exercici que suposa la quarta i darrera
activitat d\'avaluació continuada (PAC) de l\'assignatura. Aquesta PAC
intenta presentar-vos un petit projecte en el qual heu de resoldre
diferents exercicis, que engloba molts dels conceptes coberts durant
l\'assignatura.

L\'objectiu d\'aquest exercici serà desenvolupar un **paquet de Python**
fora de l\'entorn de Notebooks, que ens permeti resoldre el problema
donat. Treballareu amb arxius Python plans `.py`. Aquest haurà
d\'incloure el corresponent codi organitzat lògicament (separat per
mòduls, organitzats per funcionalitat,\...), la documentació del codi
(*docstrings*) i tests. A més, haureu d\'incloure els corresponents
arxius de documentació d\'alt nivell (`README`) així com els arxius de
llicència i dependències (`requirements.txt`) comentats a la teoria.

Fer un setup.py és opcional, però si es fa es valorarà positivament de
cara a la nota de la pràctica i del curs.

# Enunciat:

La companyia de mitjans de comunicació Open Broadcast Corporation
s\'està plantejant adquirir llicències d\'emissió de programes de
televisió populars amb què espera augmentar significativament el nombre
de subscriptors. Per poder prendre les decisions de la millor manera
possible, ens han encarregat analitzar el contingut de la base de dades
*The Movie Database (TMDB)*, que conté informació de més de 159.000
programes de televisió. La informació d\'aquesta base de dades està
distribuïda en tres fitxers que contenen les variables següents:

**TMDB_info.csv**

-   **id**: identificador únic de la sèrie
-   **name**: nom de la sèrie
-   **number_of_seasons**: nombre de temporades de la sèrie
-   **number_of_episodes**: nombre d\'episodis de la sèrie
-   **original_language**: idioma original
-   **languages**: idiomes en què està disponible la sèrie
-   **spoken_languages**: idiomes parlats a la sèrie
-   **episode_run_time**: temps de durada de cada episodi en minuts
-   **vote_count**: nombre de vots
-   **vote_average**: valor mitjà dels vots
-   **popularity**: indicador de popularitat
-   **first_air_date**: data de la primera emissió
-   **last_air_date**: data de la darrera emissió
-   **adult**: si el contingut de la sèrie és per a adults
-   **in_production**: si la sèrie està en producció
-   **type**: tipus de programa
-   **status**: estat de la sèrie

**TMDB_overview.csv**

-   **id**: identificador únic de la sèrie
-   **original_name**: nom de la sèrie en el vostre idioma original
-   **tagline**: eslògan publicitari
-   **overview**: resum de la trama
-   **backdrop_path**: ruta del backdrop de la sèrie a la seva pàgina
    web
-   **homepage**: pàgina web de la sèrie
-   **poster_path**: ruta del pòster de la sèrie a la seva pàgina web

**TMDB_distribution.csv**

-   **id**: identificador únic de la sèrie
-   **genres**: gèneres de la sèrie
-   **created_by**: autors de la sèrie
-   **networks**: plataformes d\'emissió
-   **production_companies**: empreses productores
-   **origin_country**: països d\'origen
-   **production_countries**: països de producció

Aquests tres fitxers es troben a la carpeta comprimida **TMDB.zip**.

# Presentació dels resultats:

Per fer el lliurament més fàcil i homogeni us demanem que organitzeu el
codi de tal manera que **des del fitxer principal retorneu totes les
respostes que se us demani a la PAC** fent ús de funcions que haureu de
definir en mòduls. Per això, a cada exercici, us indicarem el format que
ha de tenir cada resposta, de manera que executant `main.py` es vagi
responent a tota la PAC. Per defecte, `main.py` ha d\'executar totes les
funcions de la PAC mostrant com funcionen però també ha de permetre
executar-les una per una si es desitja. Ho heu de documentar tot molt bé
al README perquè es pugui executar sense problema. Us recordem que al
README també heu d\'indicar com executar els tests i comprovar-ne la
cobertura.

### Exercici 1: Descompressió i lectura de fitxers. {#exercici-1-descompressió-i-lectura-de-fitxers}

#### Exercici 1.1. {#exercici-11}

Implementeu una funció que descomprimeixi fitxers en format zip i
tar.gz. La funció rebrà com a inputs la ruta amb el nom del fitxer que
es vol descomprimir. La funció detectarà automàticament si el fitxer
està comprimit en zip o tar.gz i mostrarà un missatge d\'error quan el
fitxer sigui dun altre tipus. Utilitzeu aquesta funció per descomprimir
el fitxer TMDB.zip.

#### Exercici 1.2. {#exercici-12}

Implementeu una funció que llegeixi els csv i els integri en un únic
dataframe utilitzant com a clau la columna \"id\" utilitzant la
llibreria **pandes**. Obtingueu el temps de processament.

#### Exercici 1.3. {#exercici-13}

Implementeu una funció que llegeixi els csv i els integri en un únic
diccionari utilitzant com a clau la columna \"id\" utilitzant la
llibreria **csv**. Obtingueu el temps de processament.

#### Exercici 1.4. {#exercici-14}

Quines diferències s\'observen en la lectura dels fitxers seguint tots
dos mètodes? Si els fitxers tinguessin una mida de 10GB quin mètode
seria més ràpid? Justifiqueu la resposta.

### Exercici 2: Processament de dades. {#exercici-2-processament-de-dades}

#### Exercici 2.1. {#exercici-21}

Afegiu una variable air_days al dataframe que consisteixi en el nombre
de dies que una sèrie ha estat en emissió. Mostreu per pantalla els 10
registres del dataset que més dies han estat en emissió.

#### Exercici 2.2. {#exercici-22}

Creeu un diccionari ordenat la clau del qual serà el nom de la sèrie
(name) i el valor del qual serà l\'adreça web completa del vostre pòster
(homepage i poster_path). En cas que homepage o poster_path tinguin el
valor NaN o \"\", el valor serà el string "NOT AVAILABLE". Mostreu per
pantalla els primers 5 registres del diccionari.

### Exercici 3: Filtratge de dades. {#exercici-3-filtratge-de-dades}

#### Exercici 3.1. {#exercici-31}

Obtingueu i mostreu per pantalla els noms de les sèries l\'idioma
original (original_language) de les quals sigui l\'anglès i en el resum
de les quals (overview) apareguin les paraules "mystery" o "crime",
sense tenir en compte majúscules ni minúscules.

#### Exercici 3.2. {#exercici-32}

Obtingueu una llista de les sèries que han començat el 2023 i han estat
cancel·lades. Mostreu per pantalla els primers 20 elements d\'aquesta
llista.

#### Exercici 3.3. {#exercici-33}

Obtingueu un dataframe amb els noms, els noms originals, les plataformes
d\'emissió i les empreses productores de totes les sèries l\'idioma
(variable languages) de les quals sigui el japonès i mostrar els primers
20 registres per pantalla. Nota: tingueu en compte que considerem sèries
en japonès també aquelles que tinguin idiomes addicionals, per exemple,
un registre amb idioma "en, ja, ko" s\'inclouria.

### Exercici 4: Anàlisi gràfica. {#exercici-4-anàlisi-gràfica}

#### Exercici 4.1. {#exercici-41}

Mostreu en un gràfic de barres el nombre de sèries per any d\'inici.

#### Exercici 4.2. {#exercici-42}

Construïu un gràfic de línies que mostri el nombre de sèries de cada
categoria de la variable "type" produïdes a cada dècada des de 1940.
Quins canvis de tendència s\'observen?

#### Exercici 4.3. {#exercici-43}

Obtingueu el nombre de sèries per gènere i mostreu el percentatge
respecte al total en un gràfic circular. Els gèneres que representin
menys de l\'1% del total s\'inclouran a la categoria \"Other\". Tingueu
en compte que una sèrie que tingui més d\'un gènere s\'haurà d\'incloure
a totes les categories en què estigui classificada i que les sèries amb
el camp \"genres\" buit no s\'inclouen.

### Exercici 5: Conclusions. {#exercici-5-conclusions}

Redacteu un breu informe que recopili les conclusions obtingudes a
l\'anàlisi realitzada.

## Criteris de correcció

Aquesta PAC es valorarà seguint els criteris següents:

-   **Funcionalitat** (6 punts): Es valorarà que el codi implementi tot
    el que es demana.
    -   Exercici 1 (1.5 punts)
    -   Exercici 2 (1 punt)
    -   Exercici 3 (1.5 punts)
    -   Exercici 4 (1.5 punts)
    -   Exercici 5 (0.5 punts)
-   **Documentació** (0.5 punts): Totes les funcions dels exercicis
    d\'aquesta PAC hauran d\'estar degudament documentades utilitzant
    docstrings (en el format que preferiu).
-   **Modularitat** (0.5 punts): Es valorarà la modularitat del codi
    (tant l\'organització del codi en mòduls com la creació de
    funcions).
-   **Estil** (0.5 punts): El codi ha de seguir la guia d\'estil de
    Python (PEP8), exceptuant els casos on fer-ho compliqui la
    llegibilitat del codi.
-   **Tests** (1.5 punts): El codi ha de contenir una o diverses suites
    de tests que permetin comprovar que el codi funciona correctament,
    amb un mínim del 50% de cobertura.
-   **Requeriments** (0.5 punts): Heu d\'incloure un fitxer de
    *requirements* que contingui la llista de llibreries necessàries per
    executar el codi.
-   **README** i **llicencia** (0.5 punts): Heu d\'afegir també un
    fitxer README, que presenti el projecte i expliqui com executar-lo,
    així com la inclusió de la llicència sota la qual es distribueix el
    codi (podeu triar la que vulgueu).

### Important

**Nota 1**: De la mateixa manera que a les PACs anteriors, els criteris
transversals es valoraran de manera proporcional a la part de
funcionalitat implementada.

Per exemple, si el codi només implementa la meitat de la PAC i la
documentació està perfecta, la puntuació corresponent a documentació
serà de 0.25.

**Nota 2**: És imprescindible que el paquet que lliureu s\'executi
correctament a la màquina virtual i que el fitxer de REAMDE expliqui
clarament com executar el codi per generar els resultats demanats. A
més, al README s\'ha d\'explicar també com s\'executaran els tests i com
se\'n comprova la cobertura.

**Nota 3**: Lliureu el paquet com un únic fitxer .zip que contingui
només el codi al Registre d\'Avaluació Contínua. **El codi de Python
haurà d\'estar escrit en fitxers plans de Python.**

