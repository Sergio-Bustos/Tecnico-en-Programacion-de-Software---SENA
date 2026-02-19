# Busqueda y extraccion. Ejercicios y Practicas

print("----------- Ejercicios de busqueda y extraccion en clase -----------")

# Busqueda y extraccion de bloque de texto a partir de dos palabras

mensaje = """El oeste de Texas divide la frontera entre Mexico y Nuevo México. Es muy bella pero aspera, llena de cactus, en esta region se encuentran las Davis Mountains. Todo el terreno esta lleno de piedra caliza, torcidos arboles de mezquite y espinosos nopales. Para admirar la verdadera belleza desertica, visite el Parque Nacional de Big Bend, cerca de Brownsville. Es el lugar favorito para los excursionistas, acampadores y entusiastas de las rocas. Pequeños pueblos y ranchos se encuentran a lo largo de las planicies y cañones de esta region. El area solo tiene dos estaciones, tibia y realmente caliente. La mejor epoca para visitarla es de Diciembre a Marzo cuando los dias son tibios, las noches son frescas y florecen las plantas del desierto con la humedad en el aire."""

buscar = mensaje.find("oeste")  # .find busca la posicion de la palabra 'oeste' en el texto
buscar1 = mensaje.find("aire")  # .find busca la posicion de la palabra 'aire' en el texto
print(f"La posicion de la palabra 'oeste' en el texto es: {buscar}")  # Para recordar e imprimir la posicion de la palabra
print(f"La posicion de la palabra 'aire' en el texto es: {buscar1}")  # Para recordar e imprimir la posicion de la palabra
extraccion111 = mensaje[3:770]  # Para extraer un bloque de texto desde el string 'oeste' hasta el string 'aire'
print(extraccion111)  # Imprime la extraccion del texto






# Busqueda y extraccion de bloque de texto a partir de dos palabras

mensaje2 = """Las mujeres, vestidas y adornadas con lo que da de sí el contrabando, lucían pendientes de ostentosa filigrana, patenas fastuosas, pañuelos de seda de colorines; en las casas no faltaba ron jamaiqueño ni queso de Flandes, y los hombres poseían armas inglesas, bolsas de piel y tabaco Virginia y Macuba. Al través de Portugal, Inglaterra enviaba sus productos, y de España pasaban otros, cruzando el caudaloso río.

Algunos días del año se interrumpía el tráfico y la industria de Ribamoura. El pueblo entero se congregaba a celebrar las solemnidades consuetudinarias, que servían de pretexto para solaces y holgorio. Tal ocurría con el Carnaval, tal con la fiesta de la Patrona, tal con los días de la Semana Santa. A pesar de ser éstos de penitencia y mortificación, para los de Ribamoura tenían carácter de fiesta; en ellos se celebraba, en la iglesia principal, espacioso edificio de la época herreriana, la representación de la Pasión, con personajes de carne y hueso, y encargándose de los papeles gente del pueblo mismo."""


buscarr = mensaje2.find("Algunos") # .find busca la posicion de la palabra 'Algunos' en el texto
print(f"La posicion de la palabra 'algunos' en el texto es: {buscarr}") # Para recordar e imprimir la posicion de la palabra
buscarrr = mensaje2.find("mismo")  # .find busca la posicion de la palabra 'mismo' en el texto
print(f"La posicion de la palabra 'mismo' en el texto es: {buscarrr}") # Para recordar e imprimir la posicion de la palabra
extraccion1 = mensaje2[415:1025] # Para extraer el bloque de texto desde el string 'Algunos' hasta el string 'mismo'
print(extraccion1) # Imprime la extraccion del texto





# Busqueda de palabra

texto = ("Python es un lenguaje de programación muy popular debido a su simplicidad y potencia,se usa en desarrollo web, ciencia de datos, inteligencia artificial y muchas otras áreas.")
pos = texto.find("inteligencia")  # .find busca la posicion de la palabra 'inteligencia'
print(f"La posicion de la palabra 'inteligencia' en el texto es: {pos}") # Imprime la posicion de la palabra




# Busqueda de palabra

textos= "Doña Uzeada de Ribera Maldonado de Bracamonte y Anaya era baja, rechoncha, abigotada. Ya no existia razon para llamar talle al suyo. Sus colores vivos, sanos, podian mas que el albayalde y el soliman del afeite, con que se blanqueaba por simular melancolias. Gastaba dos parches oscuros, adheridos a las sienes y que fingian medicamentos. Tenia los ojitos ratoniles, maliciosos. Sabia dilatarlos duramente o desmayarlos con recato o levantarlos con disimulo. Caminaba contoneando las imposibles caderas y era dificil, al verla, no asociar su estampa achaparrada con la de ciertos palmipedos domesticos. Sortijas celestes y azules le ahorcaban las falanges"
pss = textos.find("Uzeada")  #  .find busca la posicion de la palabra 'Uzeada' 
print(f"La posicion de la palabra 'Uzeada' en el texto es: {pss}") # Imprime la posicion de la palabra




# Busqueda de palabra

textos = "El rápido zorro marrón salta sobre el perro perezoso en una tarde soleada de otoño en el parque."
psss = textos.find("zorro") # .find busca la posicion de la palabra 'zorro'
print(f"La posicion de la palabra 'zorro' en el texto es: {psss}") # Imprime la posicion de la palabra




# Busqueda y extraccion de una palabra

texto2 = "Los Estados Generales eran una asamblea, compuesta por tres ordenes separados: el clero, la nobleza y el grupo formado por burguesía y campesinado. Este último orden se conoce como el tercer estadeo, término que usaremos para referirnos a él en lo sucesivo. Dicha asamblea se había citado por ultima vez en 1614 y el dramatismo de la situación obligó al gobierno a convocarla nuevamente."
busqueda = texto2.find("campesinado")   # .find busca la posicion de la palabra 'campesinado' en el texto
print(f"La posicion de la palabra 'campesinado' es: {busqueda}")   # Para recordar e imprimir la posicion de la palabra
extraccion = texto2[135:146]    # Para extraer la palabra
print(f"La palabra de la posicion 135:145 segun la previa busqueda es: {extraccion}")   # Imprime la extraccion





# Busqueda y extraccion de una palabra

texto3 = "Durante la Revolución Francesa, los ideales de libertad, igualdad y fraternidad se difundieron rápidamente, transformando el panorama político y social de Europa en los siglos posteriores."

busqueda2 = texto3.find("transformando") # .find busca la posicion de la palabra 'transformando' en el texto
print(f"La posicion de la palabra 'transformando' en el texto es: {busqueda2}")  # Para recordar e imprimir la posicion de la palabra
extraccion2 = texto3[108:121]
print(f"La posicion de la palabra 108:121 segun la previa busqueda es: {extraccion2} ") # Imprime la extraccion 




# Busqueda y extraccion de bloque de texto a partir de dos palabras

texto3 = "A fines de 1792 comenzó el proceso de Convención contra Luis XVI, quien fue juzgado y condenado a la guillotina por mayoría de votos. El 21 de enero de 1793, Luis subió al cadalso, inconmovible hasta el último momento en el sentimiento de su inocencia. La noticia de la muerte del rey produjo indignación en Inglaterra, la que despidió al embajador o representante francés. Francia contestó declarando la guerra a Inglaterra y a Holanda, su aliada."

busqueda3 = texto3.find("XVI") # .find busca la posicion de la palabra 'XVI' en el texto
busqueda4 = texto3.find("Inglaterra") # .find busca la posicion de la palabra 'Inglaterra' en el texto
print(f"La posicion de la palabra 'XVI' en el texto es: {busqueda3} ") # Para recordar e imprimir la posicion de la palabra
print(f"La posicion de la palabra 'Inglaterra' en el texto es: {busqueda4}") # Para recordar e imprimir la posicion de la palabra
extraccion3 = texto3[61:318] # Para extraer el bloque de texto desde el string 'XVI' hasta el string 'Inglaterra'
print(extraccion3) # Imprime la extraccion





# Busqueda y extraccion de una palabra

texto4 = "Organizado por la Subsecretaría de Fortalecimiento Institucional y encabezado por Beatriz de Anchorena, el encuentro contó con la presencia de más de 28 funcionarias y funcionarios de 17 ministerios, la Jefatura de Gabinete de Ministros de la Nación y 6 organismos descentralizados y entes del Sector Público Nacional, todos miembros de la Red de Fortalecimiento de la Gestión Pública. La jornada se centró en reflexionar sobre los logros del trabajo conjunto desarrollado durante estos dos años y acordar los objetivos para un plan de fortalecimiento de desarrollo institucional para el 2022."

busqueda = texto4.find("funcionarias") # .find busca la posicion de la palabra 'funcionarias' en el texto
busqueda2 = texto4.find("Red") # .find busca la posicion de la palabra 'Red' en el texto
print(f"La posicion de la palabra 'funcionarias' en el texto es: {busqueda}") # Para recordar e imprimir la posicion de la palabra
print(f"La posicion de la palabra 'Red' en el texto es: {busqueda2}") # Para recordar e imprimir la posicion de la palabra
extraccion4 = texto4[153:343] # Para extraer el bloque de texto desde el string 'funcionarias' hasta el string 'Red'
print(extraccion4) # Imprime la extraccion