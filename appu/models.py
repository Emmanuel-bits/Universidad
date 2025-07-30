from django.db import models

class Aula(models.Model):
    
    idaula = models.AutoField(db_column='idAula', primary_key=True, verbose_name="ID Aula")
    capacidad = models.CharField(max_length=20, verbose_name="Capacidad")
    aire = models.IntegerField(verbose_name="Aire Acondicionado") 
    videobeam = models.IntegerField(verbose_name="Video Beam")   
    pizarra = models.IntegerField(verbose_name="Pizarra")      
    ubicacion = models.CharField(max_length=30, verbose_name="Ubicación")

    class Meta:
        verbose_name = "Aula"
        verbose_name_plural = "Aulas"
        db_table = 'aula'

    def __str__(self):
        return f"{self.ubicacion} (Capacidad: {self.capacidad})"

class Carrera(models.Model):
    idcarrera = models.AutoField(db_column='idCarrera', primary_key=True, verbose_name="ID Carrera")
    nombre = models.CharField(max_length=40, verbose_name="Nombre de Carrera")
    numero_semestre = models.IntegerField(verbose_name="Número de Semestres")
    modalidad = models.CharField(max_length=15, verbose_name="Modalidad")
    mencion = models.CharField(max_length=40, verbose_name="Mención")

    class Meta:
        verbose_name = "Carrera"
        verbose_name_plural = "Carreras"
        db_table = 'carrera'

    def __str__(self):
        return self.nombre

class Estudiante(models.Model):
    idestudiante = models.AutoField(db_column='idEstudiante', primary_key=True, verbose_name="ID Estudiante")
    imagen = models.ImageField(upload_to='estudiantes/', blank=True, null=True, verbose_name="Foto")
    nombre = models.CharField(max_length=30, verbose_name="Nombre")
    apellido = models.CharField(max_length=30, verbose_name="Apellido")
    direccion = models.CharField(max_length=80, verbose_name="Dirección")
    telefono = models.CharField(max_length=20, verbose_name="Teléfono")
    email = models.CharField(max_length=30, verbose_name="Email")
    estado = models.CharField(max_length=20, verbose_name="Estado") # Considerar usar choices o un BooleanField si aplica
    fecha_nac = models.DateField(verbose_name="Fecha de Nacimiento")
    fecha_ing = models.DateField(verbose_name="Fecha de Ingreso")

    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"
        db_table = 'estudiante'

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# Tabla intermedia para la relación Many-to-Many entre Carrera y Estudiante
class CarreraEstudiante(models.Model):
    # Cambiar DO_NOTHING a CASCADE
    idcarrera = models.ForeignKey(Carrera, on_delete=models.CASCADE, db_column='idCarrera', verbose_name="Carrera")
    idestudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, db_column='idEstudiante', verbose_name="Estudiante")

    class Meta:
        verbose_name = "Registro de Estudiante en Carrera"
        verbose_name_plural = "Registros de Estudiantes en Carreras"
        db_table = 'carreraestudiante'
        # Puedes añadir unique_together si una pareja carrera-estudiante solo puede existir una vez
        unique_together = (('idcarrera', 'idestudiante'),) 

    def __str__(self):
        return f"{self.idestudiante} - {self.idcarrera}"

class Materia(models.Model):
    idmateria = models.AutoField(db_column='idMateria', primary_key=True, verbose_name="ID Materia")
    nombre_materia = models.CharField(max_length=40, verbose_name="Nombre de Materia")
    unidades_creditos = models.IntegerField(verbose_name="Unidades de Créditos")
    modalidad = models.CharField(max_length=20, verbose_name="Modalidad")
    idcarrera = models.ForeignKey(Carrera, on_delete=models.CASCADE, db_column='idCarrera', verbose_name="Carrera") 

    class Meta:
        verbose_name = "Materia"
        verbose_name_plural = "Materias"
        db_table = 'materia'

    def __str__(self):
        return self.nombre_materia

class Profesor(models.Model):
    idprofesor = models.AutoField(db_column='idProfesor', primary_key=True, verbose_name="ID Profesor")
    imagen = models.ImageField(upload_to='profesores/', blank=True, null=True, verbose_name="Foto")
    nombre = models.CharField(max_length=30, verbose_name="Nombre")
    apellido = models.CharField(max_length=30, verbose_name="Apellido")
    direccion = models.CharField(max_length=80, verbose_name="Dirección")
    telefono = models.CharField(max_length=20, verbose_name="Teléfono")
    especialidad = models.CharField(max_length=80, verbose_name="Especialidad")
    email = models.CharField(max_length=30, verbose_name="Email")
    fecha_ingreso = models.DateField(verbose_name="Fecha de Ingreso")

    class Meta:
        verbose_name = "Profesor"
        verbose_name_plural = "Profesores"
        db_table = 'profesor'

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# Tabla intermedia para la relación Many-to-Many entre Profesor y Materia
class MateriaProfesor(models.Model):
    # Cambiar DO_NOTHING a CASCADE
    idprofesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, db_column='idProfesor', verbose_name="Profesor")
    idmateria = models.ForeignKey(Materia, on_delete=models.CASCADE, db_column='idMateria', verbose_name="Materia")

    class Meta:
        verbose_name = "Asignación de Materia a Profesor"
        verbose_name_plural = "Asignaciones de Materias a Profesores"
        db_table = 'materiaprofesor'
        unique_together = (('idprofesor', 'idmateria'),)

    def __str__(self):
        return f"{self.idprofesor} - {self.idmateria}"

class HorarioEstudiante(models.Model):
    # Cambiar DO_NOTHING a CASCADE 
    idmateria = models.ForeignKey(Materia, on_delete=models.CASCADE, db_column='idMateria', verbose_name="Materia")
    idestudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, db_column='idEstudiante', verbose_name="Estudiante")
    dia = models.CharField(max_length=15, verbose_name="Día")
    horario_inicio = models.CharField(max_length=15,verbose_name="Hora de Inicio") 
    horario_fin = models.CharField(max_length=15,verbose_name="Hora de Fin")     
    idaula = models.ForeignKey(Aula, on_delete=models.CASCADE, db_column='idAula', verbose_name="Aula")

    class Meta:
        verbose_name = "Horario de Estudiante"
        verbose_name_plural = "Horarios de Estudiantes"
        db_table = 'horarioestudiante'
        # Puedes añadir unique_together si no puede haber dos mismos horarios
        unique_together = (('idmateria', 'idestudiante', 'dia', 'horario_inicio', 'idaula'),)

    def __str__(self):
        return f"Estudiante: {self.idestudiante}, Materia: {self.idmateria}, Día: {self.dia}, Hora: {self.horario_inicio}"

class HorarioProfesor(models.Model):
    # Cambiar DO_NOTHING a CASCADE 
    idprofesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, db_column='idProfesor', verbose_name="Profesor")
    idmateria = models.ForeignKey(Materia, on_delete=models.CASCADE, db_column='idMateria', verbose_name="Materia")
    dia = models.CharField(max_length=15, verbose_name="Día")
    horario_inicio = models.CharField(max_length=15,verbose_name="Hora de Inicio") 
    horario_fin = models.CharField(max_length=15,verbose_name="Hora de Fin")          
    idaula = models.ForeignKey(Aula, on_delete=models.CASCADE, db_column='idAula', verbose_name="Aula")

    class Meta:
        verbose_name = "Horario de Profesor"
        verbose_name_plural = "Horarios de Profesores"
        db_table = 'horarioprofesor'
        unique_together = (('idprofesor', 'idmateria', 'dia', 'horario_inicio', 'idaula'),)

    def __str__(self):
        return f"Profesor: {self.idprofesor}, Materia: {self.idmateria}, Día: {self.dia}, Hora: {self.horario_inicio}"

class Nota(models.Model):
    # Cambiar DO_NOTHING a CASCADE
    idmateria = models.ForeignKey(Materia, on_delete=models.CASCADE, db_column='idMateria', verbose_name="Materia")
    idestudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, db_column='idEstudiante', verbose_name="Estudiante")
    nota = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="Nota")

    class Meta:
        verbose_name = "Nota"
        verbose_name_plural = "Notas"
        db_table = 'nota'
        # Una nota para una materia y estudiante debería ser única
        unique_together = (('idmateria', 'idestudiante'),)

    def __str__(self):
        return f"Nota de {self.idestudiante} en {self.idmateria}: {self.nota}"