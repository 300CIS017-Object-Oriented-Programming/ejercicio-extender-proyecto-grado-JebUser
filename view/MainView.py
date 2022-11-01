"""
Contiene la clase MainView,
la cual se encarga de definir el menu y su visualización.
Asignatura: POO
"""

import streamlit as st

from streamlit_option_menu import option_menu
from controller.Controlador import Controlador
from view.EvaluacionActaPartial import ver_historico_acta, agregar_acta, evaluar_criterios, exportar_acta

# Este archivo contiene las funcionalidades de la vista relacionado con la evaluación de las actas


class MainView:

    # Constructor
    def __init__(self) -> None:
        super().__init__()

        # Estrategia para manejar el "estado" del controlador y del modelo entre cada cambio de ventana
        if 'main_view' not in st.session_state:
            self.menu_actual = "Inicio"

            # Conexión con el controlador
            self.controller = Controlador()

            st.session_state['main_view'] = self
        else:

            # Al existir en la sesión entonces se actualizan los valores
            self.menu_actual = st.session_state.main_view.menu_actual
            self.controller = st.session_state.main_view.controller

        self._dibujar_layout()

    def _dibujar_layout(self):
        st.set_page_config(page_title="Actas De Grado", page_icon=':)', layout="wide", initial_sidebar_state="expanded")
        self.col1, self.col2, self.col3, self.col4 = st.columns([1, 1, 1, 1])

        # Definimos lo que abra en la barra de menu
        with st.sidebar:
            st.image("img/LogoJaverianaCali.jpg", width=297)
            self.menu_actual = option_menu("Menu", ["Inicio", 'Crear acta', 'Evaluar acta', 'Ver históricos'],
                                           icons=['house', 'mortarboard', 'people', 'person-check-fill'], menu_icon="cast", default_index=0)

    def mostrar_bienvenida(self):
        return """
            # ¡Bienvenido!
            Esta es la pagina web donde podrás registras registrar el acta, modificarlo, entre otras opciones.\n
            Recuerda que debes entrar a tu bloque de selección dependiendo de la opción deseada:
            >Nota: Cualquier Inconveniente porfavor comunicarse con: ayudaactas@javerianacali.edu.co
            >> Autores: *Miguel Angel Nivia Ortega* Y *Jose Manuel Garcia Lopez* 😎️
            >> Modificado por: Luisa Rincón\n
            """

    def controlar_menu(self):
        if self.menu_actual == "Inicio":
            # Se llama con self pq en metodo de la clase MainView
            texto = self.mostrar_bienvenida()
            st.write(texto)
        elif self.menu_actual == "Crear acta":
            # No necesitan self pq son funciones del archivo EvaluacionActaPartial
            agregar_acta(st, self.controller)
            ver_historico_acta(st, self.controller)
        elif self.menu_actual == "Evaluar acta":
            evaluar_criterios(st, self.controller)
            exportar_acta(st, self.controller)
        elif self.menu_actual == "Ver históricos":
            ver_historico_acta(st, self.controller)


# Main call
if __name__ == "__main__":
    gui = MainView()
    gui.controlar_menu()
