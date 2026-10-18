print("_" * 70)
print("Bienvenido: Criterios de clasificacion de obesidad")
print("Propuesta reciente de la Comisión de The Lancet sobre Obesidad Clínica (2025)")
print("_" * 70)
class Paciente:

  def __init__(self, nombre, edad, sexo, peso, talla, cintura, porcentaje_grasa, diabetes, hipertension, apnea, masld, limitacion):
    self.nombre = nombre
    self.edad= edad
    self.sexo= sexo
    self.peso= peso
    self.talla= talla
    self.cintura= cintura 
    self.porcentaje_grasa= porcentaje_grasa
    self.diabetes= diabetes
    self.hipertension= hipertension
    self.apnea= apnea
    self.masld= masld
    self.limitacion= limitacion 
  def calcular_imc(self):
     imc = self.peso / (self.talla**2)
     return imc    
  def clasificar_imc(self): 
      imc = self.calcular_imc()
      if imc < 18.5:
            clasificacion = "Peso bajo"
      elif imc < 25:
            clasificacion = "Peso normal"
      elif imc < 30:
            clasificacion = "Sobrepeso"
      elif imc < 35:
            clasificacion = "Obesidad Grado 1"
      elif imc < 40:
            clasificacion = "Obesidad Grado 2"
      else:
            clasificacion = "Obesidad Grado 3"
      return clasificacion
 
  def evaluar_adiposidad(self):
       imc = self.calcular_imc()
       if imc>= 30:
            exceso_adiposidad = "SI"
            motivo= "IMC >=30"
       elif self.sexo.upper()== "H" and self.cintura>=90:
            exceso_adiposidad = "SI"
            motivo = "Circunferencia de cintura elevada"
       elif self.sexo.upper()== "M" and self.cintura>=80:
            exceso_adiposidad = "SI"
            motivo = "Circunferencia de cintura elevada"    
       elif self.sexo.upper()== "H" and self.porcentaje_grasa>=25:
            exceso_adiposidad = "SI"
            motivo = "Porcentaje de grasa elevada"
       elif self.sexo.upper()== "M" and self.porcentaje_grasa>=35:
            exceso_adiposidad = "SI"
            motivo = "Porcentaje de grasa elevada"
       else:
            exceso_adiposidad= "NO"
            motivo = "No presenta exceso de adiposidad"
       return exceso_adiposidad, motivo 
  def diagnosticar_obesidad(self):
       exceso_adiposidad, motivo = self.evaluar_adiposidad()
       if exceso_adiposidad== "NO":
            diagnostico = "NO PRESENTA OBESIDAD"
       elif (self.diabetes.upper() == "S"
             or self.hipertension.upper()== "S"
             or sef.apnea.upper()== "S"
             or self.masld.upper()== "S"
             or self.limitacion.upper()== "S"):
             diagnostico = "OBESIDAD CLINICA"
       else: 
            diagnostico = "OBESIDAD PRECLINICA"
       return diagnostico                  
  def generar_resumen (self):
       imc = self.calcular_imc()
       clasificacion = self.clasificar_imc()
       exceso, motivo = self.evaluar_adiposidad()
       diagnostico = self.diagnosticar_obesidad()
       print("\n===RESUMEN DEL PACIENTE===")
       print("Nombre:", self.nombre)
       print("Edad:", self.edad)
       print("Sexo:", self.sexo)
       print("Peso:", self.peso)
       print("Talla:", self.talla)
       print("Cintura:", self.cintura)
       print("Porcentaje de grasa:", self.porcentaje_grasa, "%")
       print("IMC:", round(imc,2))
       print("Clasificacion del IMC:", clasificacion)
       print("Exceso de adiposidad:", exceso)
       print("Motivo:", motivo)
       print("Diagnostico:", diagnostico)
       if  diagnostico == "OBESIDAD PRECLINICA":
            print("\nRECOMENDACIONES")
            print("- Plan de alimentación individualizado.")
            print("- Incrementar actividad física.")
            print("- Seguimiento nutricional periódico.")
            print("- Prevención de progresión a obesidad clínica.")
       elif diagnostico == "OBESIDAD CLINICA":
            print("\nRECOMENDACIONES")
            print("- Manejo multidisciplinario.")
            print("- Terapia nutricional intensiva.")
            print("- Valorar tratamiento farmacológico.")
            print("- Considerar cirugía metabólica si cumple criterios.")
            print("- Tratamiento de las complicaciones.")
       
def registrar_paciente(): 
    print("\n REGISTRO DE PACIENTE")
    nombre = input("Ingrese el nombre: ")
    edad = int(input("Ingrese la edad: "))
    sexo = input("Ingrese el sexo (H/M):").upper()
    peso = float(input("Ingrese el peso (kg): "))
    talla = float (input("Ingrese la talla(m): "))
    cintura = float(input("Ingrese la circuferencia de cintura (cm): "))
    porcentaje_grasa = float(input("Ingrese el porcentaje de grasa (%):  "))
    diabetes = input("EL paciente presenta Diabetes (S/N): ").upper()
    hipertension = input("EL paciente presenta Hipertension (S/N): ").upper()
    apnea = input("EL paciente presenta APNEA (S/N): ").upper()
    masld = input("EL paciente presenta Enfermedad Hepatica esteatósica asociada a disfuncion metabolica(S/N): ").upper()
    limitacion = input("EL paciente presenta alguna limitacion: ").upper()   
    paciente = Paciente(nombre, edad, sexo, peso, talla, cintura, porcentaje_grasa, diabetes, hipertension, apnea, masld, limitacion)    
    return paciente 



paciente = registrar_paciente()
paciente. generar_resumen()
pacientes = []
for i in range (5):
    print(f"\nRegistro del paciente {i+2}")
    paciente = registrar_paciente()
    pacientes.append(paciente)
for paciente in pacientes:
     paciente.generar_resumen()



