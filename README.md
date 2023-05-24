Hero battle simulator

Assumptions.
Una competencia requiere de dos equipos de cinco heroes/villanos por lado, donde son unicos, no se repetiran
en ningún equipo. 

El alignment del equipo se establece al inicio de la batalla, y este atributo no cambia en la medida que se
vayan eliminando personajes durante la batalla.

HP corresponde a los puntos de vida del personaje, los cuales se calculan en base a la fórmula prevista.

Especificaciones técnicas

Ejecución:

- Dockerfile


- Uvicorn


Módulo principal:

El proyecto esta desarrollado en FastAPI, con un módulo principal (app.py) que contiene dos rutas (GET y POST), 
posee además un Dockerfile con step para construir el contenedor.

El proyecto de hero-app esta organizado en dos módulos principales y un folder de templates:

- business: Contiene las funciones asociadas a la API de requests para solicitar la información asociada a un
personaje y enviar emails mediante mailgun, también contiene las funciones de utilidad (utils).

- models: Contiene los modelos vinculados a la simulación de la batalla, estan definidas las clases de Battle, Team y Hero, en la clase de Battle esta definido el método que permite simular una batalla. Sumado a lo anterior, contiene un archivo de schema que permite procesar las peticiones POST.


Botones:

Execute Attack: Inicializa la animación donde se detallan cada uno de los ataques y el daño causado.

Send Email: Ejecuta el envio del email mediante la API de mailgun, envia los detalles de los ataques de cada uno
de los personajes y cual es el equipo vencedor.
