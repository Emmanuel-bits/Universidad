from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


class Aula(models.Model):
    idaula = models.AutoField(db_column='idAula', primary_key=True)  # Field name made lowercase.
    capacidad = models.CharField(max_length=20)
    aire = models.IntegerField()
    videobeam = models.IntegerField()
    pizarra = models.IntegerField()
    ubicacion = models.CharField(max_length=30)

    class Meta:
        
        db_table = 'aula'


class Carrera(models.Model):
    idcarrera = models.AutoField(db_column='idCarrera', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=20)
    numero_semestre = models.IntegerField()
    modalidad = models.CharField(max_length=15)
    mencion = models.CharField(max_length=30)

    class Meta:
        
        db_table = 'carrera'


class CarreraEstudiante(models.Model):
    idcarrera = models.ForeignKey(Carrera, models.DO_NOTHING, db_column='idCarrera')  # Field name made lowercase.
    idestudiante = models.ForeignKey('Estudiante', models.DO_NOTHING, db_column='idEstudiante')  # Field name made lowercase.

    class Meta:
        
        db_table = 'carreraestudiante'


class Estudiante(models.Model):
    idestudiante = models.AutoField(db_column='idEstudiante', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=20)
    direccion = models.CharField(max_length=80)
    telefeno = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    estado = models.CharField(max_length=20)
    fecha_nac = models.DateField()
    fecha_ing = models.DateField()

    class Meta:
        
        db_table = 'estudiante'


class HorarioEstudiante(models.Model):
    idmateria = models.ForeignKey('Materia', models.DO_NOTHING, db_column='idMateria')  # Field name made lowercase.
    idestudiante = models.ForeignKey(Estudiante, models.DO_NOTHING, db_column='idEstudiante')  # Field name made lowercase.
    dia = models.CharField(max_length=15)
    horario_inicio = models.CharField(max_length=15)
    horario_fin = models.CharField(max_length=15)
    idaula = models.ForeignKey(Aula, models.DO_NOTHING, db_column='idAula')  # Field name made lowercase.

    class Meta:
        
        db_table = 'horarioestudiante'


class HorarioProfesor(models.Model):
    idprofesor = models.ForeignKey('Profesor', models.DO_NOTHING, db_column='idProfesor')  # Field name made lowercase.
    idmateria = models.ForeignKey('Materia', models.DO_NOTHING, db_column='idMateria')  # Field name made lowercase.
    dia = models.CharField(max_length=15)
    horario_inicio = models.CharField(max_length=15)
    horario_fin = models.CharField(max_length=15)
    idaula = models.ForeignKey(Aula, models.DO_NOTHING, db_column='idAula')  # Field name made lowercase.

    class Meta:
        
        db_table = 'horarioprofesor'


class Materia(models.Model):
    idmateria = models.AutoField(db_column='idMateria', primary_key=True)  # Field name made lowercase.
    nombre_materia = models.CharField(max_length=20)
    unidades_creditos = models.IntegerField()
    modalidad = models.CharField(max_length=20)
    idcarrera = models.IntegerField(db_column='idCarrera')  # Field name made lowercase.

    class Meta:
        
        db_table = 'materia'


class MateriaProfesor(models.Model):
    idprofesor = models.ForeignKey('Profesor', models.DO_NOTHING, db_column='idProfesor')  # Field name made lowercase.
    idmateria = models.ForeignKey(Materia, models.DO_NOTHING, db_column='idMateria')  # Field name made lowercase.

    class Meta:
        
        db_table = 'materiaprofesor'


class Nota(models.Model):
    idmateria = models.ForeignKey(Materia, models.DO_NOTHING, db_column='idMateria')  # Field name made lowercase.
    idestudiante = models.ForeignKey(Estudiante, models.DO_NOTHING, db_column='idEstudiante')  # Field name made lowercase.
    nota = models.DecimalField(max_digits=4, decimal_places=2)

    class Meta:
        
        db_table = 'nota'


class Profesor(models.Model):
    idprofesor = models.AutoField(db_column='idProfesor', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=20)
    direccion = models.CharField(max_length=80)
    telefono = models.CharField(max_length=20)
    especialidad = models.CharField(max_length=80)
    email = models.CharField(max_length=30)
    fecha_ingreso = models.DateField()

    class Meta:
        
        db_table = 'profesor'
