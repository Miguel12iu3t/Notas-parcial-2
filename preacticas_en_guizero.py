#Metodo de practica 1
from guizero import App

app = App(title="Hello world")
app.display();

#Metodo de practica 2
from guizero import App, Text, PushButton

app = App("ICI App")
message = Text(app, text="Welcome to the ICI App!")

app.display()

#Metodo de practica 3
from guizero import App, Text, PushButton

app = App("ICI App")

message = Text(app, text="Welcome to the ICI App!")
button = PushButton(app, text="Click me!")

app.display()

#Metodo de practica 4
from guizero import App, Text, PushButton

def say_hello():
    message_2.value = "ICI Rocks!"
    
app = App("ICI App")

message = Text(app, text="Welcome to the ICI App!")
message_2 = Text(app)
button = PushButton(app, text="Click me!", command=say_hello)
app.display()

#Metodo de practica 5
from guizero import App, Text, PushButton

def say_hello():
    message_2.value = "ICI Rocks!"
    
app = App("ICI App")

message = Text(app, text="Welcome to the ICI App!")
message_2 = Text(app)
button = PushButton(app, text="Click me!", command=say_hello)
app.display()

#Metodo de practica 6
from guizero import App, Text, PushButton, TextBox

def say_hello():
    app.info("Saludos", text= f"Hola {name.value}")
    #message_2.value = "Hola " + name.value
    
app = App(title="ICI App")

message = Text(app, text="¿Como te llamas?", color="Red")
name = TextBox(app, width=30, height=1, multiline=True)
message_2 = Text(app)
button = PushButton(app, text="Click me!", command=say_hello)

app.display()

#Metodo de practica 7
from guizero import App, Text, PushButton, TextBox

def say_hello():
    app.info("Suma", text=f"La suma es: {int(num_1.value)+int(num_2.value)}")
    
app = App(title="ICI App")

message = Text(app, text="Ingrese el primer numero")
num_1 = TextBox(app, width=30)
message_2= Text(app, text="Ingrese el segundo numero")
num_2 = TextBox(app, width=30)
button = PushButton(app, text="Click me!", command=say_hello)

app.display()