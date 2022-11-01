import os

from fpdf import FPDF

class ControladorPdf:

    # Constructor
    def __init__(self) -> None:
        super().__init__()
        self.pdf = FPDF()

    def exportar_acta(self, st, controlador, acta_seleccionada):
        """
         Exporta el acta en self.pdf
        :param controlador:
        :param acta_seleccionada:
        :return:
        """
        numero = 1
        flag = False
        self.pdf.add_page()
        self.pdf.set_font("times", 'B', size=12)
        self.pdf.image("img/LogoJaverianaCali.jpg", 10, 8, 40)
        self.pdf.cell(200, 10, txt="ACTA DE EVALUACIÓN DE GRADO", ln=1, align='C')
        self.pdf.cell(200, 10, txt="Facultad de Ingeniería.", ln=2, align='C')
        self.pdf.set_font("times", size=12)
        self.pdf.multi_cell(185, 6,
                       txt="Trabajo de grado denominado: Análisis de la similitud en el código fuente de dos programas de computador usando técnicas de inteligencia artificial",
                       align='L')
        for acta in controlador.actas:
            if acta.autor == acta_seleccionada:
                flag = True
                self.pdf.cell(200, 10, txt=f"Autor:                                {acta.autor}", ln=1, align='L')
                self.pdf.cell(200, 10, txt=f"Fecha/Periodo:                  {acta.fecha_acta} Tesis II", ln=1, align='L')
                self.pdf.cell(200, 10, txt=f"Director:                            {acta.director}", ln=1, align='L')
                self.pdf.cell(200, 10, txt=f"Codirector:                        {acta.codirector}", ln=1, align='L')
                self.pdf.cell(200, 10, txt=f"Nombre Del Trabajo:        {acta.nombre_trabajo}", ln=1, align='L')
                self.pdf.cell(200, 10, txt=f"Tipo De Trabajo:               {acta.tipo_trabajo}", ln=1, align='L')
                self.pdf.cell(200, 10, txt=f"Jurado 1:                            {acta.jurado1}", ln=1, align='L')
                self.pdf.cell(200, 10, txt=f"Jurado 2:                            {acta.jurado2}", ln=1, align='L')
                self.pdf.multi_cell(185, 6,
                               txt="En atención al desarrollo de este Trabajo de Grado y al documento y sustentación que presentó el(la) autor(a), los Jurados damos las siguientes calificaciones parciales y observaciones (los criterios a evaluar y sus ponderaciones se estipulan en el artículo 7.1 de las Directrices para Trabajo de Grado de Maestría):",
                               align='L')
                for criterio in acta.criterios:
                    self.pdf.set_font("times", 'B', size=12)
                    self.pdf.multi_cell(185, 10, txt=f"{numero}. {criterio.descripcion}", align='L')
                    self.pdf.set_font("times", size=12)
                    self.pdf.cell(145, 7, txt=f"Calificación parcial: {round(criterio.nota, 2)}", ln=0, align='L')
                    self.pdf.cell(100, 7, txt=f"Ponderación: {criterio.porcentaje * 100}%", ln=1, align='L')
                    self.pdf.multi_cell(185, 7, txt=f"Observación: {criterio.observacion}", align='L')
                    self.pdf.multi_cell(185, 5,
                                   txt="_____________________________________________________________________________________",
                                   align='L')
                    self.pdf.multi_cell(185, 5,
                                   txt="_____________________________________________________________________________________",
                                   align='L')
                    numero += 1
                self.pdf.set_font("times", 'B', size=12)
                self.pdf.multi_cell(185, 10,
                               txt=f"Como resultado de estas calificaciones parciales y sus ponderaciones, la calificación del Trabajo de Grado es: {round(acta.nota_final, 2)}",
                               align='L')
                self.pdf.cell(100, 10, txt=f"{round(acta.nota_final, 2)}", ln=0, align='C')
                self.pdf.cell(30, 10, txt=f"{controlador.mostrar_de_numero_a_palabras(acta.nota_final)}", ln=1, align='C')
                self.pdf.cell(95, 10, txt="Números", ln=0, align='C')
                self.pdf.cell(35, 10, txt="Letras", ln=1, align='C')
                self.pdf.set_font("times", size=12)
                self.pdf.multi_cell(185, 5, txt="Observaciones adicionales: ", align='L')
                self.pdf.multi_cell(185, 5,
                               txt="_____________________________________________________________________________________",
                               align='L')
                self.pdf.multi_cell(185, 5,
                               txt="_____________________________________________________________________________________",
                               align='L')
                self.pdf.multi_cell(185, 5,
                               txt="_____________________________________________________________________________________",
                               align='L')
                self.pdf.multi_cell(185, 10,
                               txt="La calificación final queda sujeta a que se implementen las siguientes correcciones: Que se revise el abstract.",
                               align="L")
                self.pdf.multi_cell(185, 5,
                               txt="_____________________________________________________________________________________",
                               align='L')
                self.pdf.multi_cell(185, 5,
                               txt="_____________________________________________________________________________________",
                               align='L')
                self.pdf.multi_cell(185, 5,
                               txt="_____________________________________________________________________________________",
                               align='L')
                self.pdf.cell(200, 30, txt="________________________________   ________________________________", ln=2,
                         align='C')
                self.pdf.cell(200, 5, txt="Firma Jurado 1                                      Firma Jurado 2 ", ln=2,
                         align='C')

        if [acta.autor for acta in controlador.actas if acta.estado and flag]:
            self.pdf_nombre = f"outputs/Acta_{acta_seleccionada}.self.pdf"
            self.pdf.output(dest='F', name=self.pdf_nombre).encode('latin-1')
            full_path = os.path.join(os.getcwd(), self.pdf_nombre)
            # Abre el self.pdf
            os.startfile(full_path)
