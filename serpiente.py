from cgitb import text
import turtle #Librería para crear la ventana.
import time
import random


#Tiempo para que se vea lento
posponer = 0.1

#Marcador
score = 0
high_score = 0

#Creando Juego de la serpiente con algunas variaciones
#01/10/2022  Luciano Cabrera Jose

#CONFIGURACIÓN DE LA VENTANA#
#Creando una Ventana.
wn = turtle.Screen()

#Titulo del juego.
wn.title("Juego de la Serpiente")

#Color de fondo.
wn.bgcolor("black")

#Redimensionar la ventana.
wn.setup(width = 600, height = 600)

#Funció que hace las animaciones.
wn.tracer(0)

#Cabeza de la serpiente.
cabeza = turtle.Turtle()
cabeza.speed(0)
#Forma de lacabeza.
cabeza.shape("square")
#Color de la serpiente.
cabeza.color("white")
#Para no dejar rastro.
cabeza.penup()
#Posición en la pantalla
cabeza.goto(0,0)
cabeza.direction = "stop"

#Creando el objeto COMIDA
#Comida de la serpiente.
comida = turtle.Turtle()
comida.speed(0)
#Forma de la comida.
comida.shape("circle")
#Color de la comida.
comida.color("red")
#Para no dejar rastro.
comida.penup()
#Posición en la pantalla
comida.goto(0,200)

#AGREGANDO CUERPO A LA SERPIENTE
segmentos = []

#Agregando texto
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write("Score: 0       High Score 0", align="center", font=("Courier", 24, "normal"))


#FUNCIONES PARA MOVER A LA SERPIENTE

#Definimos la funcion para moverse hacia arriba, abajo, derecha e izquierda.
def arriba():
    cabeza.direction != "down"
    cabeza.direction = "up"
def abajo():
    cabeza.direction != "up"
    cabeza.direction = "down"
def izquierda():
    cabeza.direction != "right"
    cabeza.direction = "left"
def derecha():
    cabeza.direction != "left"
    cabeza.direction = "right"

#Función de movimiento
def mov():
    #Movimiento hacia arriba
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)
    #Movimiento hacia abajo
    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)
    
    #Movimiento a la izquierda
    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)

    #Movimiento a la derecha    
    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)

#Conexión con el teclado
wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(derecha, "Right")

#Bucle principal
while True:
    wn.update()
    
    #Colisión de bordes
    if (cabeza.xcor() > 285 or cabeza.xcor() < -285 or cabeza.ycor() > 285 or cabeza.ycor() < -285):
        time.sleep(1)
        cabeza.goto(0,0)
        #Para si colisiona con el borde.
        cabeza.direction = "stop"

        #Esconder los segmentos
        for segmento in segmentos:
            #Los mandamos a esta coordenada
            segmento.goto(1000,1000)
            #segmento.hideturtle()
        #Limpiamos la lista segmentos.
        segmentos.clear()
        #Iniciamos la comidad
            #comida.goto(0,0)

        #Resetear marcador
        score = 0 
        texto.clear()
        texto.write("Score:{}     High Score:{}".format(score,high_score), align="center", font=("Courier", 24, "normal"))
    

    #Colisión de la comida y serpiente.
    if cabeza.distance(comida) < 20: #20 es el numero de pixeles de la forma.
        #Posicón aleatoria donde aparecerá la comida.
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        comida.goto(x,y)

        #Agregamos lo ya creado para crear el cuerpo de la serpiente y que la comida aparaezca en un nuevo lugar
        #Comida de la serpiente.
        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        #Form5a de la comida.
        nuevo_segmento.shape("square")
        #Color de la comida.
        nuevo_segmento.color("gray")
        #Para no dejar rastro.
        nuevo_segmento.penup()
        segmentos.append(nuevo_segmento)

        #Aumentar el maarcador
        score += 10

        if score > high_score:
            high_score = score
        texto.clear()
        texto.write("Score:{}   High Score:{}".format(score,high_score), align="center", font=("Courier", 24, "normal"))

    #Para mover el cuerpo de la serpiente.
    
    #Total de segmentos.
    totalSeg = len(segmentos)
    #Para mover el cuerpo
    for index in range(totalSeg -1, 0, -1):
        #Movemos un elemento anterior
        x = segmentos[index -1].xcor()
        y = segmentos[index -1].ycor()
        #Obtenem(os la coordenada nueva.
        segmentos[index].goto(x,y)
    #Mover el primer segmento o cabeza.
    if totalSeg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x,y)

    #Llamo a la función movimiento
    mov()

    #Colisión con el cuerpo
    for segmento in segmentos:
        if segmento.distance(cabeza) < 20:
            time.sleep(1)
            cabeza.goto(0,0)
            cabeza.direction = "stop"

            #Esconder los segmentos
            for segmento in segmentos:
            #Los mandamos a esta coordenada
                segmento.goto(1000,1000)
                #segmento.hideturtle()
            #Limpiamos la lista segmentos.
            segmentos.clear()

            #Resetear marcador
            score = 0 
            texto.clear()
            texto.write("Score:{}     High Score:{}".format(score,high_score), align="center", font=("Courier", 24, "normal"))
    
    time.sleep(posponer)