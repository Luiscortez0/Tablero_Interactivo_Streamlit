import streamlit as st

# Opciones del menú
menu_opciones = ["Inicio", "Saludo", "Suma de dos números", "Área de un triángulo", 
                 "Calculadora de descuento", "Suma de lista", "Funciones con valores predeterminados", 
                 "Pares e impares", "Multiplicación con *args", "Información personal con **kwargs", 
                 "Calculadora flexible", "Acerca de"]
selected_option = st.sidebar.selectbox("Selecciona una opción", menu_opciones)

# Funciones de utilidad
def saludar(nombre: str) -> str:
    return f"Hola, {nombre}"

def sumar(n1: float, n2: float) -> str:
    return f"El resultado es: {n1 + n2}"

def calcular_area_triangulo(base: float, altura: float) -> str:
    return f"El área del triángulo es: {(base * altura) / 2}"

def calcular_precio_final(precio_original: float, descuento: float = 10, impuesto: float = 16) -> str:
    precio_con_descuento = precio_original * (1 - descuento / 100)
    precio_final = precio_con_descuento * (1 + impuesto / 100)
    return f"El precio final con un {descuento}% de descuento y {impuesto}% de impuesto es: {round(precio_final, 2)}"

def sumar_lista(numeros: list) -> float:
    return sum(numeros)

def producto(nombre: str, cantidad: int = 1, precio: float = 10.0) -> str:
    return f"El total a pagar por {cantidad} {nombre} es: {cantidad * precio}"

def numeros_pares_e_impares(numeros: list) -> tuple:
    pares = [n for n in numeros if n % 2 == 0]
    impares = [n for n in numeros if n % 2 != 0]
    return pares, impares

def multiplicar_todos(*args) -> int:
    resultado = 1
    for numero in args:
        resultado *= numero
    return resultado

def informacion_personal(**kwargs):
    for clave, valor in kwargs.items():
        st.write(f"{clave.capitalize()}: {valor}")

def calculadora_flexible(num1, num2, operacion="suma"):
    operaciones = {
        "suma": num1 + num2,
        "resta": num1 - num2,
        "multiplicación": num1 * num2,
        "división": num1 / num2 if num2 != 0 else "Error: División por cero"
    }
    return operaciones.get(operacion, "Operación no válida")

# Lógica de las opciones del menú
if selected_option == "Inicio":
    st.image("https://portal.ucol.mx/content/micrositios/188/image/Escudo2021/1_Linea/UdeC%20Abajo_Negro_40_.png", width=600)
    st.title("Tablero Interactivo de Ejercicios")
    st.markdown("---")
    st.markdown(
        """
        <div style="text-align: center; font-size:20px; color: #4CAF50;">
        Explora las opciones del menú lateral y elige el ejercicio que más te interese.
        </div>
        """, unsafe_allow_html=True
    )
    if st.button("¡Comenzar!"):
        st.write("Selecciona un ejercicio del menú lateral para empezar.")
        
elif selected_option == "Saludo":
    st.title("Saludo")
    nombre = st.text_input("Ingresa tu nombre: ")
    if st.button("Saludar"):
        st.write(saludar(nombre))

elif selected_option == "Suma de dos números":
    st.title("Suma de dos números")
    n1 = st.number_input("Ingresa el primer número: ")
    n2 = st.number_input("Ingresa el segundo número: ")
    if st.button("Sumar"):
        st.write(sumar(n1, n2))

elif selected_option == "Área de un triángulo":
    st.title("Área de un triángulo")
    base = st.number_input("Ingresa la base: ")
    altura = st.number_input("Ingresa la altura: ")
    if st.button("Calcular área"):
        st.write(calcular_area_triangulo(base, altura))

elif selected_option == "Calculadora de descuento":
    st.title("Calculadora de Descuento")
    precio = st.number_input("Precio original:", min_value=0.0)
    descuento = st.number_input("Descuento (%):", value=10.0, min_value=0.0)
    impuesto = st.number_input("Impuesto (%):", value=16.0, min_value=0.0)
    if st.button("Calcular"):
        st.write(calcular_precio_final(precio, descuento, impuesto))

elif selected_option == "Suma de lista":
    st.title("Suma de una lista")
    numeros_str = st.text_input("Ingresa una lista de números separados por comas:")
    if st.button("Sumar lista"):
        try:
            numeros = [float(num) for num in numeros_str.split(",")]
            st.write(f"La suma es: {sumar_lista(numeros)}")
        except ValueError:
            st.write("Por favor, ingresa una lista válida de números.")

elif selected_option == "Funciones con valores predeterminados":
    st.title("Cálculo de Precio de Productos")
    producto_nombre = st.text_input("Producto:")
    cantidad = st.number_input("Cantidad:", min_value=1, value=1)
    precio_unidad = st.number_input("Precio por unidad:", min_value=0.0, value=10.0)
    if st.button("Calcular"):
        st.write(producto(producto_nombre, cantidad, precio_unidad))

elif selected_option == "Pares e impares":
    st.title("Números Pares e Impares")
    numeros_str = st.text_input("Ingresa una lista de números separados por comas:")
    if st.button("Separar"):
        try:
            numeros = [int(num) for num in numeros_str.split(",")]
            pares, impares = numeros_pares_e_impares(numeros)
            st.write(f"Pares: {pares}")
            st.write(f"Impares: {impares}")
        except ValueError:
            st.write("Por favor, ingresa una lista válida de números.")

elif selected_option == "Multiplicación con *args":
    st.title("Multiplicación de Números")
    numeros_str = st.text_input("Ingresa una lista de números separados por comas:")
    if st.button("Multiplicar"):
        try:
            numeros = [float(num) for num in numeros_str.split(",")]
            st.write(f"Resultado: {multiplicar_todos(*numeros)}")
        except ValueError:
            st.write("Por favor, ingresa una lista válida de números.")

elif selected_option == "Información personal con **kwargs":
    st.title("Información Personal")
    nombre = st.text_input("Nombre:")
    edad = st.number_input("Edad:", min_value=0)
    direccion = st.text_input("Dirección:")
    email = st.text_input("Email:")
    if st.button("Mostrar"):
        informacion_personal(nombre=nombre, edad=edad, direccion=direccion, email=email)

elif selected_option == "Calculadora flexible":
    st.title("Calculadora Flexible")
    num1 = st.number_input("Primer número:")
    num2 = st.number_input("Segundo número:")
    operacion = st.selectbox("Operación", ["suma", "resta", "multiplicación", "división"])
    if st.button("Calcular"):
        st.write(f"Resultado: {calculadora_flexible(num1, num2, operacion)}")

elif selected_option == "Acerca de":
    st.title("Acerca de")
    st.write("Última actualización: 25/09/2024")
    st.write("Autor: Luis Carlos Cortez Guzmán")
    st.write("Contacto: lcortez8@ucol.mx")
