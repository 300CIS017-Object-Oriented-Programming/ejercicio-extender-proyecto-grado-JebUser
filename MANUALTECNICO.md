# Manual Técnico

## Entradas Y Salidas
Este programa tiene como entradas la información de atributos en InfoActa, siendo este la base para que el programa funcione de forma adecuada
puesto que estos son usados en todos los métodos, el cual son los siguientes:
* autor
* fecha_acta
* nombre_trabajo
* tipo_trabajo
* director
* codirector
* jurado1
* jurado2
* criterios
* nota_final
* estado

Mientras que por las salidas vamos a tener como resultado estos mismos datos, pero de forma
impresa a través del uso de inputs y funcionalidades que nos trae la librería de streamlit, además también
se realiza la generación de un PDF con información obtenida de las actas creadas, esto gracias a la
librería de fpdf.

## Principales Clases
Las principales clases son "InfoActa" y "Controlador", de estas dependen el correcto funcionamiento de todo 
el sistema ya que estas son las que manejan la información principal y la controla con métodos.
Además, podría incluir a "EvaluarActa", porque esta tiene internamente los métodos principales que funcionan
en Streamlit y son usados por las personas de asistente, jurado y director, dependiendo del caso es diferente.
