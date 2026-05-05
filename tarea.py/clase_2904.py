#Junto con la investigacion, deben detectar 10 objetos y por cada objeto 5 atributos con 3 3 metodos de accion cada uno.
#Atributos prohibidos: color, marca, modelo, nombre y apellido
#No pueden ocupar los nombrados en clase

class Telefono:
    def __init__(self, sistema_operativo, capacidad_almacenamiento, tamaño_pantalla, peso, bateria):
        self.sistema_operativo = sistema_operativo
        self.capacidad_almacenamiento = capacidad_almacenamiento
        self.tamaño_pantalla = tamaño_pantalla
        self.peso = peso
        self.bateria = bateria


    def hacer_llamada(self, numero):
        print(f"Haciendo una llamada al número {numero}...")

    def enviar_mensaje(self, numero, mensaje):
        print(f"Enviando mensaje al número {numero}: {mensaje}")

    def tomar_foto(self):
        print("Tomando una foto...")

class Computadora:
    def __init__(self, procesador, memoria_ram, capacidad_almacenamiento, tarjeta_grafica, sistema_operativo):
        self.procesador = procesador
        self.memoria_ram = memoria_ram
        self.capacidad_almacenamiento = capacidad_almacenamiento
        self.tarjeta_grafica = tarjeta_grafica
        self.sistema_operativo = sistema_operativo
    def encender(self):
        print("Encendiendo la computadora...") 
    def apagar(self):
        print("Apagando la computadora...")
    def reiniciar(self):
        print("Reiniciando la computadora...")

class Televisor:
    def __init__(self, tamaño_pantalla, tipo_pantalla, resolución, sistema_operativo, puertos_hdmi):
        self.tamaño_pantalla = tamaño_pantalla
        self.tipo_pantalla = tipo_pantalla
        self.resolución = resolución
        self.sistema_operativo = sistema_operativo
        self.puertos_hdmi = puertos_hdmi

    def encender(self):
        print("Encendiendo el televisor...")

    def apagar(self):
        print("Apagando el televisor...")

    def cambiar_entrada(self, entrada):
        print(f"Cambiando a la entrada {entrada}...")

class Refrigerador:
    def __init__(self, capacidad, tipo, eficiencia_energetica, sistema_control, material):
        self.capacidad = capacidad
        self.tipo = tipo
        self.eficiencia_energetica = eficiencia_energetica
        self.sistema_control = sistema_control
        self.material = material
    def abrir_puerta(self):
        print("Abriendo la puerta del refrigerador...")
    def cerrar_puerta(self):
        print("Cerrando la puerta del refrigerador...")
    def ajustar_temperatura(self, temperatura):
        print(f"Ajustando la temperatura a {temperatura} grados...")

class Lavadora:
    def __init__(self, capacidad, tipo_carga, eficiencia_energetica, sistema_control, material):
        self.capacidad = capacidad
        self.tipo_carga = tipo_carga
        self.eficiencia_energetica = eficiencia_energetica
        self.sistema_control = sistema_control
        self.material = material

    def iniciar_ciclo(self):
        print("Iniciando el ciclo de lavado...")

    def detener_ciclo(self):
        print("Deteniendo el ciclo de lavado...")

    def ajustar_temperatura(self, temperatura):
        print(f"Ajustando la temperatura a {temperatura} grados...")
