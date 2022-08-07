from django.db import models
from django.utils import timezone
from simple_history.models import HistoricalRecords
from tutorias_itsvc.users.models import User
from tutorias_itsvc.common.models import (
    Gender,
    Address,
    HousingType,
    HomeStatus,
    # Income,
    AcademicDegree,
    Phone,
    Disability,
    # MaritalStatus,
    SchoolCycle
)
from tutorias_itsvc.academy.models import (
    AcademicGroup,
    Subject,
    SubjectType,
    SubjectFailureMetric,
    PeriodNumber
)
from tutorias_itsvc.users.models import Sibling, Person
# from tutorias.students.model_permissions import student_permissions


class Student(models.Model):
    user = models.OneToOneField(User, related_name='student', on_delete=models.CASCADE)
    enrollment = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.user.first_name

    class Meta:
        default_permissions = ()
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'


class StudentAcademicInformation(models.Model):
    student = models.ForeignKey(Student, related_name="academic", on_delete=models.CASCADE)
    academic_information = models.ForeignKey(
        AcademicGroup,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    is_active = models.BooleanField(default=True)
    registered_at = models.DateTimeField(default=timezone.now)

    class Meta:
        default_permissions = ()
        verbose_name = 'Carrera de estudiante'
        verbose_name_plural = 'Carreras de estudiante'
        unique_together = ('student', 'is_active')


class StudentAddress(Address):
    student = models.OneToOneField(Student, related_name="address", on_delete=models.CASCADE)
    housing_type = models.ForeignKey(HousingType, on_delete=models.CASCADE)
    home_status = models.ForeignKey(HomeStatus, on_delete=models.CASCADE)
    home_status_description = models.CharField(max_length=255, null=True, blank=True)
    family_relationship = models.CharField(max_length=255)
    members = models.IntegerField()

    history = HistoricalRecords()

    class Meta:
        default_permissions = ()
        verbose_name = 'Dirección de estudiantes'
        verbose_name_plural = 'Direcciones de estudiantes'


class StudentPhone(Phone):
    student = models.ForeignKey(Student, related_name='student_phone', on_delete=models.CASCADE)
    # order = models.PositiveIntegerField(default=1)

    class Meta:
        default_permissions = ()


class StudentInstitute(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    institute_name = models.CharField(max_length=255)
    academic_degree = models.ForeignKey(AcademicDegree, on_delete=models.CASCADE)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    class Meta:
        default_permissions = ()


class StudentSibling(models.Model):
    student = models.ForeignKey(Student, related_name="siblings", on_delete=models.CASCADE)
    sibling = models.ForeignKey(Sibling, on_delete=models.CASCADE)

    class Meta:
        default_permissions = ()


# class StudentIncome(Income):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#
#     class Meta:
#         default_permissions = ()
#
#
# class FamilyIncome(Income):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#
#     class Meta:
#         default_permissions = ()

class StudentIncome(models.Model):
    student = models.OneToOneField(Student, related_name="income", on_delete=models.PROTECT)
    income = models.FloatField(null=True)
    family_income = models.FloatField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        default_permissions = ()


class StudentMedicalInformation(models.Model):
    student = models.ForeignKey(Student, related_name="disabilities", on_delete=models.CASCADE)
    disability = models.ForeignKey(Disability, on_delete=models.CASCADE)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        default_permissions = ()


class StudentScholarship(models.Model):
    student = models.OneToOneField(Student, related_name="scholarship", on_delete=models.PROTECT)
    has_scholarship = models.BooleanField(null=False, default=False)
    institute_name = models.CharField(null=True, blank=True, max_length=150)
    dependence_name = models.CharField(null=True, blank=True, max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        default_permissions = ()


class StudentJob(models.Model):
    student = models.OneToOneField(Student, related_name="job", on_delete=models.PROTECT)
    has_job = models.BooleanField(null=False, default=False)
    company_name = models.CharField(null=True, blank=True, max_length=150)
    schedule = models.CharField(null=True, blank=True, max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        default_permissions = ()


# class StudentMaritalStatus(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     marital_status = models.ForeignKey(MaritalStatus, on_delete=models.CASCADE)
#     description = models.TextField(null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True, null=True)
#     history = HistoricalRecords()
#
#     class Meta:
#         default_permissions = ()


class StudentParent(Person):
    FATHER = "father"
    MOTHER = "mother"
    PARENTS_TYPES = [
        (FATHER, "Padre"),
        (MOTHER, "Madre"),
    ]
    student = models.ForeignKey(Student, related_name='student_parent', on_delete=models.CASCADE)
    type = models.CharField(max_length=25, choices=PARENTS_TYPES)
    birth_date = models.DateField(null=True, blank=True)
    academic_degree = models.ForeignKey(AcademicDegree, on_delete=models.CASCADE)
    has_job = models.BooleanField(null=True, blank=True)
    workplace = models.CharField(max_length=255, null=True, blank=True)
    type_of_job = models.CharField(max_length=255, null=True, blank=True)
    profession_occupation = models.CharField(max_length=255, null=True, blank=True)
    is_alive = models.BooleanField(null=True, blank=True)
    address = models.ForeignKey(Address, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        default_permissions = ()
        verbose_name = 'Padre'
        verbose_name_plural = 'Padres'
        unique_together = ('student', 'type')


class StudentSubject(models.Model):
    student = models.ForeignKey(Student, related_name='subject', on_delete=models.CASCADE)
    tutor_subject = models.ForeignKey("tutor.TutorSubject", on_delete=models.CASCADE, null=True)
    type = models.ForeignKey(SubjectType, on_delete=models.CASCADE)
    approved = models.BooleanField(null=True)
    final_score = models.FloatField(null=True)
    failure_metric = models.ForeignKey(SubjectFailureMetric, null=True, blank=True, on_delete=models.CASCADE)
    comment = models.TextField(null=True, blank=True)
    school_cycle = models.ForeignKey(SchoolCycle, on_delete=models.CASCADE)
    unsubscribed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        default_permissions = ()
        verbose_name = 'Materia de estudiante'
        verbose_name_plural = 'Materias de estudiante'
        # permissions = student_permissions

    def __str__(self):
        return f"{self.student.user.first_name}"


# Interview

class EstadoPsicofisiologico(models.Model):
    RESPONSE_TYPES = [
        ("Frecuente", "Frecuente"),
        ("Muy frecuente", "Muy frecuente"),
        ("Nunca", "Nunca"),
        ("Antes", "Antes"),
        ("A veces", "A veces"),
    ]
    student = models.OneToOneField(Student, related_name="estado_psicofisiologico", on_delete=models.PROTECT)
    p1 = models.CharField(max_length=20, choices=RESPONSE_TYPES)  # Manos y/o pies hinchados
    p2 = models.CharField(max_length=20, choices=RESPONSE_TYPES)  # Dolores en el vientre
    p3 = models.CharField(max_length=20, choices=RESPONSE_TYPES)  # Dolores de cabeza y/o vómitos
    p4 = models.CharField(max_length=20, choices=RESPONSE_TYPES)  # Pérdida del equilibrio
    p5 = models.CharField(max_length=20, choices=RESPONSE_TYPES)  # Fatiga y agotamiento
    p6 = models.CharField(max_length=20, choices=RESPONSE_TYPES)  # Pérdida de vista u oído
    p7 = models.CharField(max_length=20, choices=RESPONSE_TYPES)  # Dificultades para dormir
    p8 = models.CharField(max_length=20, choices=RESPONSE_TYPES)  # Pesadillas o terrores nocturnos
    p8_1 = models.TextField(null=True, blank=True)  # a que
    p9 = models.CharField(max_length=20, choices=RESPONSE_TYPES)  # Incontinencia (orina, heces)
    p10 = models.CharField(max_length=20, choices=RESPONSE_TYPES)  # Tartamudeos al explicarse
    p11 = models.CharField(max_length=20, choices=RESPONSE_TYPES)  # Miedos intensos ante cosas
    p12 = models.TextField(null=True, blank=True)  # Observaciones de Higiene

    class Meta:
        default_permissions = ()


class AreaIntegracion(models.Model):
    RESPONSE_TYPES = [
        ("Buena", "Buena"),
        ("Bien", "Bien"),
        ("Regular", "Regular"),
        ("Mala", "Mala"),
        ("Mal", "Mal"),
    ]
    RELATIVE_TYPES = [
        ("Madre", "Madre"),
        ("Padre", "Padre"),
        ("Hermano", "Hermano"),
        ("Otros", "Otros"),
    ]
    student = models.OneToOneField(Student, related_name="area_integracion", on_delete=models.PROTECT)
    p1 = models.CharField(max_length=20, choices=RESPONSE_TYPES)  # ¿Cómo es la relación con tu familia?
    p2 = models.BooleanField()  # ¿Existen dificultades?
    p2_1 = models.TextField(null=True, blank=True)  # ¿De qué tipo?
    p3 = models.CharField(max_length=20, choices=RESPONSE_TYPES)  # ¿Qué actitud tienes con tu familia o?
    # Padre
    p4 = models.CharField(max_length=20, choices=RESPONSE_TYPES)  # ¿Cómo te relacionas con tu Padre?
    p5 = models.CharField(max_length=20, choices=RESPONSE_TYPES)  # ¿Qué actitud tienes hacia tu Padre?
    # Madre
    p6 = models.CharField(max_length=20, choices=RESPONSE_TYPES)  # ¿Cómo te relacionas con tu Madre?
    p7 = models.CharField(max_length=20, choices=RESPONSE_TYPES)  # ¿Qué actitud tienes hacia tu Madre?
    p8 = models.CharField(max_length=20, choices=RELATIVE_TYPES)  # ¿Con quién te sientes más ligado afectivamente?
    p8_1 = models.TextField(null=True, blank=True)  # Especifica por que
    p9 = models.CharField(max_length=20, choices=RELATIVE_TYPES)  # ¿Quién se ocupa más directamente de tu educación?
    p10 = models.CharField(max_length=20, choices=RELATIVE_TYPES)  # ¿Quién ha influido más en tu decisión para estudiar esta carrera?
    p11 = models.TextField(null=True, blank=True)  # Consideras importante facilitar algún otro dato sobre tu ambiente familiar
    # Social
    p12 = models.CharField(max_length=20, choices=RESPONSE_TYPES)  # ¿Cómo es tu relación con los compañeros?
    p13 = models.TextField(null=True, blank=True)  # ¿Por qué?
    p14 = models.CharField(max_length=20, choices=RESPONSE_TYPES)  # ¿Cómo es tu relación con tus amigos?
    p15 = models.BooleanField()  # ¿Tienes Pareja?
    p15_1 = models.CharField(max_length=20, choices=RESPONSE_TYPES, null=True, blank=True)  # ¿Cómo es tu relación con tu pareja?
    p16 = models.CharField(max_length=20, choices=RESPONSE_TYPES)  # ¿Cómo es tu relación con tus profesores?
    p17 = models.CharField(max_length=20, choices=RESPONSE_TYPES)  # ¿Cómo es tu relación con las autoridades académicas?
    p18 = models.TextField()  # ¿Qué haces en tu tiempo libre?
    p19 = models.TextField(null=True, blank=True)  # ¿Cuál es tu actividad recreativa?

    class Meta:
        default_permissions = ()


class CaracteristicasPersonales(models.Model):
    RESPONSE_TYPES = [
        ("No", "No"),
        ("Poco", "Poco"),
        ("Frecuente", "Frecuente"),
        ("Mucho", "Mucho"),
    ]
    student = models.OneToOneField(Student, related_name="caracteristicas_personales", on_delete=models.PROTECT)
    p1 = models.CharField(max_length=20, choices=RESPONSE_TYPES)  # Puntual
    p2 = models.CharField(max_length=20, choices=RESPONSE_TYPES)  # Tímido/a
    p3 = models.CharField(max_length=20, choices=RESPONSE_TYPES)  # Alegre
    p4 = models.CharField(max_length=20, choices=RESPONSE_TYPES)  # Agresivo/a
    p5 = models.CharField(max_length=20, choices=RESPONSE_TYPES)  # Abierto/a a las ideas de otros
    p6 = models.CharField(max_length=20, choices=RESPONSE_TYPES)  # Reflexivo/a
    p7 = models.CharField(max_length=20, choices=RESPONSE_TYPES)  # Constante
    p8 = models.CharField(max_length=20, choices=RESPONSE_TYPES)  # Optimista
    p9 = models.CharField(max_length=20, choices=RESPONSE_TYPES)  # Impulsivo/a
    p10 = models.CharField(max_length=20, choices=RESPONSE_TYPES)  # Silencioso/a
    p11 = models.CharField(max_length=20, choices=RESPONSE_TYPES)  # Generoso/a
    p12 = models.CharField(max_length=20, choices=RESPONSE_TYPES)  # Inquieto/a
    p13 = models.CharField(max_length=20, choices=RESPONSE_TYPES)  # Cambios de humor
    p14 = models.CharField(max_length=20, choices=RESPONSE_TYPES)  # Dominante
    p15 = models.CharField(max_length=20, choices=RESPONSE_TYPES)  # Egoísta
    p16 = models.CharField(max_length=20, choices=RESPONSE_TYPES)  # Sumiso/a
    p17 = models.CharField(max_length=20, choices=RESPONSE_TYPES)  # Confiado/a en si mismo/a
    p18 = models.CharField(max_length=20, choices=RESPONSE_TYPES)  # Imaginativo/a
    p19 = models.CharField(max_length=20, choices=RESPONSE_TYPES)  # Con iniciativa propia
    p20 = models.CharField(max_length=20, choices=RESPONSE_TYPES)  # Sociable
    p21 = models.CharField(max_length=20, choices=RESPONSE_TYPES)  # Responsable
    p22 = models.CharField(max_length=20, choices=RESPONSE_TYPES)  # Perseverante
    p23 = models.CharField(max_length=20, choices=RESPONSE_TYPES)  # Motivado/a
    p24 = models.CharField(max_length=20, choices=RESPONSE_TYPES)  # Activo/a
    p25 = models.CharField(max_length=20, choices=RESPONSE_TYPES)  # Independiente

    class Meta:
        default_permissions = ()


class AreaPsicopedagogica(models.Model):
    RESPONSE_TYPES = [
        ("Bueno", "Bueno"),
        ("Regular", "Regular"),
        ("Malo", "Malo"),
    ]
    PROBLEM_TYPES = [
        ("Económicos", "Económicos"),
        ("Salud", "Salud"),
        ("Familiares", "Familiares"),
        ("Sociales", "Sociales"),
    ]
    student = models.OneToOneField(Student, related_name="area_psicopedagogica", on_delete=models.PROTECT)
    p1 = models.TextField()  # ¿Cómo te gustaría ser?
    p2 = models.BooleanField()  # ¿Recibes ayuda en tu casa para la realización de tareas escolares?
    p3 = models.CharField(max_length=20, choices=PROBLEM_TYPES)  # ¿Qué problemas personales intervienen en tus estudios?
    p4 = models.CharField(max_length=20, choices=RESPONSE_TYPES)  # ¿Cuál es tu rendimiento escolar?
    p5 = models.TextField()  # ¿Por qué vienes al Tecnológico?
    p6 = models.TextField()  # ¿Qué te motiva para venir al Tecnológico?
    p7 = models.FloatField()  # ¿Cuál es tu promedio general del ciclo escolar anterior?
    p8 = models.BooleanField()  # ¿Tienes asignaturas reprobadas?
    p8_1 = models.IntegerField(null=True, blank=True)  # ¿Cuántas?
    # Plan de vida y carrera
    p9 = models.TextField()  # ¿Cuáles son tus planes inmediatos?
    p10 = models.TextField()  # ¿Cuáles son tus metas en la vida?
    # Características Personales
    p11 = models.TextField()  # Yo Soy...
    p12 = models.TextField()  # Mi Carácter es...
    p13 = models.TextField()  # A mí me gusta que...
    p14 = models.TextField()  # Yo Aspiro en la Vida...
    p15 = models.TextField()  # Yo tengo miedo que...
    p16 = models.TextField()  # Pero pienso que podré lograr...

    class Meta:
        default_permissions = ()


class OrganizacionEstudio(models.Model):
    student = models.OneToOneField(Student, related_name="organizacion_estudio", on_delete=models.PROTECT)
    p1 = models.BooleanField()  # A.- ¿Sueles dejar para el último la preparación de tus trabajos?
    p2 = models.BooleanField()  # B.- ¿Crees que el sueño o el cansancio te impidan estudiar eficazmente en muchas ocasiones?
    p3 = models.BooleanField()  # C.- ¿Es frecuente que no termines tu tarea a tiempo?
    p4 = models.BooleanField()  # D.- ¿Tiendes a emplear tiempo en leer revistas, ver televisión o charlar cuando debieras dedicarlos a estudiar?
    p5 = models.BooleanField()  # E.- Tus actividades sociales o deportivas. ¿te llevan a descuidar, a menudo, tus tareas escolares?
    p6 = models.BooleanField()  # F.- ¿Sueles dejar pasar un día o más antes de repasarlos apuntes tomados en clase?
    p7 = models.BooleanField()  # G.- ¿Sueles dedicar tu tiempo libre entre las 4:00 de la tarde y las 9:00 de la noche a otras actividades que no sean estudiar?
    p8 = models.BooleanField()  # H.- ¿Descubres algunas veces de pronto, que debes entregar una tarea antes de lo que creías?
    p9 = models.BooleanField()  # I.- ¿Te retrasas, con frecuencia, en una asignatura debido a que tienes que estudiar otra?
    p10 = models.BooleanField()  # J.- ¿Te parece que tu rendimiento es muy bajo, en relación con el tiempo que dedicas al estudio?
    p11 = models.BooleanField()  # K.- ¿Está situado tu escritorio directamente frente a una ventana, puerta u otra fuente de distracción?
    p12 = models.BooleanField()  # L.- ¿Sueles tener fotografías, trofeos o recuerdos sobre tu mesa de escritorio?
    p13 = models.BooleanField()  # M.- ¿Sueles estudiar recostado en la cama o arrellanado en un asiento cómodo?
    p14 = models.BooleanField()  # N.- ¿Produce resplandor la lámpara que utilizas al estudiar?
    p15 = models.BooleanField()  # O.- Tu mesa de estudio ¿está tan desordenada y llena de objetos, que no dispones de sitio suficiente para estudiar con eficacia?
    p16 = models.BooleanField()  # P.- ¿Sueles interrumpir tu estudio, por personas que vienen a visitarte?
    p17 = models.BooleanField()  # Q.- ¿Estudias, con frecuencia, mientras tienes puesta la televisión y/o la radio?
    p18 = models.BooleanField()  # R.- En el lugar donde estudias, ¿se pueden ver con facilidad revistas, fotos de jóvenes o materiales pertenecientes a tu afición?
    p19 = models.BooleanField()  # S.- ¿Con frecuencia, interrumpen tu estudio, actividades o ruidos que provienen del exterior?
    p20 = models.BooleanField()  # T.- ¿Suele hacerse lento tu estudio debido a que no tienes a la mano los libros y los materiales necesarios?

    class Meta:
        default_permissions = ()


class TecnicaEstudio(models.Model):
    student = models.OneToOneField(Student, related_name="tecnica_estudio", on_delete=models.PROTECT)
    p1 = models.BooleanField()  # A.- ¿Tiendes a comenzar la lectura de un libro de texto sin hojear previamente los subtítulos y las ilustraciones?
    p2 = models.BooleanField()  # B.- ¿Te saltas por lo general las figuras, gráficas y tablas cuando estudias un tema?
    p3 = models.BooleanField()  # C.- ¿Suelo serte difícil seleccionar los puntos de los temas de estudio?
    p4 = models.BooleanField()  # D.- ¿Te sorprendes con cierta frecuencia, pensando en algo que no tiene nada que ver con lo que estudias?
    p5 = models.BooleanField()  # E.- ¿Sueles tener dificultad en entender tus apuntes de clase cuando tratas de repasarlos, después de cierto tiempo?
    p6 = models.BooleanField()  # F.- Al tomar notas, ¿te sueles quedar atrás con frecuencia debido a que no puedes escribir con suficiente rapidez?
    p7 = models.BooleanField()  # G.- Poco después de comenzar un curso, ¿sueles encontrarte con tus apuntes formando un “revoltijo"?
    p8 = models.BooleanField()  # H.- ¿Tomas normalmente tus apuntes tratando de escribir las palabras exactas del docente?
    p9 = models.BooleanField()  # I.- Cuando tomas notas de un libro, ¿tienes la costumbre de copiar el material necesario, palabra por Palabra?
    p10 = models.BooleanField()  # J.- ¿Te es difícil preparar un temario apropiado para una evaluación?
    p11 = models.BooleanField()  # K.- ¿Tienes problemas para organizar los datos o el contenido de una evaluación?
    p12 = models.BooleanField()  # L.- ¿Al repasar el temario de una evaluación formulas un resumen de este?
    p13 = models.BooleanField()  # M.- ¿Te preparas a veces para un evaluación memorizando fórmulas, definiciones o reglas que no entiendes con claridad?
    p14 = models.BooleanField()  # N.- ¿Te resulta difícil decidir qué estudiar y cómo estudiarlo cuando preparas una evaluación?
    p15 = models.BooleanField()  # O.- ¿Sueles tener dificultades para organizar, en un orden lógico, las asignaturas que debes estudiar por temas?
    p16 = models.BooleanField()  # P.- Al preparar evaluación, ¿sueles estudiar toda la asignatura, en el último momento?
    p17 = models.BooleanField()  # Q.- ¿Sueles entregar tus exámenes sin revisarlos detenidamente, para ver si tienen algún error cometido por descuido?
    p18 = models.BooleanField()  # R.- ¿Te es posible con frecuencia terminar una evaluación de exposición de un tema en el tiempo prescrito?
    p19 = models.BooleanField()  # S.- ¿Sueles perder puntos en exámenes con preguntas de “Verdadero - falso", debido a que no lees detenidamente?
    p20 = models.BooleanField()  # T.- ¿Empleas normalmente mucho tiempo en contestar la primera mitad de la prueba y tienes que apresurarte en la segunda?

    class Meta:
        default_permissions = ()


class MotivacionEstudio(models.Model):
    student = models.OneToOneField(Student, related_name="motivacion_estudio", on_delete=models.PROTECT)
    p1 = models.BooleanField()  # A.- Después de los primeros días o semanas del curso, ¿tiendes a perder interés por el estudio?
    p2 = models.BooleanField()  # B.- ¿Crees que en general, basta estudiar lo necesario para obtener un "aprobado” en las asignaturas.
    p3 = models.BooleanField()  # C.- ¿Te sientes frecuentemente confuso o indeciso sobre cuáles deben ser tus metas formativas y profesionales?
    p4 = models.BooleanField()  # D.- ¿Sueles pensar que no vale la pena el tiempo y el esfuerzo que son necesarios para lograr una educación universitaria?
    p5 = models.BooleanField()  # E.- ¿Crees que es más importante divertirte y disfrutar de la vida, que estudiar?
    p6 = models.BooleanField()  # F.- ¿Sueles pasar el tiempo de clase en divagaciones o soñando despierto en lugar de atender al docente?
    p7 = models.BooleanField()  # G.- ¿Te sientes habitualmente incapaz de concentrarte en tus estudios debido a que estas inquieto, aburrido o de mal humor?
    p8 = models.BooleanField()  # H.- ¿Piensas con frecuencia que las asignaturas que estudias tienen poco valor practico para ti?
    p9 = models.BooleanField()  # I.- ¿Sientes, frecuentes deseos de abandonar la escuela y conseguir un trabajo?
    p10 = models.BooleanField()  # J.- ¿Sueles tener la sensación de lo que se enseña en los centros docentes no te prepara para afrontar los problemas de la vida adulta?
    p11 = models.BooleanField()  # K.- ¿Sueles dedicarte de modo casual, según el estado de ánimo en que te encuentres?
    p12 = models.BooleanField()  # L.- ¿Te horroriza estudiar libros de textos porque son insípidos y aburridos?
    p13 = models.BooleanField()  # M.- ¿Esperas normalmente a que te fijen la fecha de un evaluación para comenzar a estudiar los textos o repasar tus apuntes de clases?
    p14 = models.BooleanField()  # N - ¿Sueles pensar que los exámenes son pruebas penosas de las que no se puede escapar y respecto a las cuales lo que debe hacerse es sobrevivir, del modo que sea?
    p15 = models.BooleanField()  # O.- ¿Sientes con frecuencia que tus docentes no comprenden las necesidades de los estudiantes?
    p16 = models.BooleanField()  # P.- ¿Tienes normalmente la sensación de que tus docentes exigen demasiadas horas de estudio fuera de clase?
    p17 = models.BooleanField()  # Q.- ¿Dudas por lo general, en pedir ayuda a tus docentes en tareas que te son difíciles?
    p18 = models.BooleanField()  # R.- ¿Sueles pensar que tus docentes no tienen contacto con los temas y sucesos de actualidad?
    p19 = models.BooleanField()  # S.- ¿Te sientes reacio, por lo general, a hablar con tus docentes de tus proyectos futuros, de estudio o profesionales?
    p20 = models.BooleanField()  # T.- ¿Criticas con frecuencia a tus docentes cuando charlas con tus compañeros?

    class Meta:
        default_permissions = ()


class EstiloAprendizaje(models.Model):
    RESPONSE_TYPES = [
        (1, "Nunca"),
        (2, "Raramente"),
        (3, "Ocasionalmente"),
        (4, "Usualmente"),
        (5, "Siempre"),
    ]
    student = models.OneToOneField(Student, related_name="estilo_aprendizaje", on_delete=models.PROTECT)
    p1 = models.IntegerField(choices=RESPONSE_TYPES)  # Me ayuda trazar o escribir a mano las palabras cuando tengo que aprenderlas de memoria
    p2 = models.IntegerField(choices=RESPONSE_TYPES)  # Recuerdo mejor un tema al escuchar una conferencia en vez de leer un libro de texto
    p3 = models.IntegerField(choices=RESPONSE_TYPES)  # Prefiero las clases que requieren una prueba sobre lo que se lee en el libro de texto
    p4 = models.IntegerField(choices=RESPONSE_TYPES)  # Me gusta comer bocados y mascar chicle, cuando estudio
    p5 = models.IntegerField(choices=RESPONSE_TYPES)  # Al prestar atención a una conferencia, puedo recordar las ideas principales sin anotarlas
    p6 = models.IntegerField(choices=RESPONSE_TYPES)  # Prefiero las instrucciones escritas sobre las orales
    p7 = models.IntegerField(choices=RESPONSE_TYPES)  # Yo resuelvo bien los rompecabezas y los laberintos
    p8 = models.IntegerField(choices=RESPONSE_TYPES)  # Prefiero las clases que requieran una prueba sobre lo que se presenta durante una conferencia
    p9 = models.IntegerField(choices=RESPONSE_TYPES)  # Me ayuda ver diapositivas y videos para comprender un tema
    p10 = models.IntegerField(choices=RESPONSE_TYPES)  # Recuerdo más cuando leo un libro que cuando escucho una conferencia
    p11 = models.IntegerField(choices=RESPONSE_TYPES)  # Por lo general, tengo que escribir los números del teléfono para recordarlos bien
    p12 = models.IntegerField(choices=RESPONSE_TYPES)  # Prefiero recibir las noticias escuchando la radio en vez de leerlas en un periódico
    p13 = models.IntegerField(choices=RESPONSE_TYPES)  # Me gusta tener algo como un bolígrafo o un lápiz en la mano cuando estudio
    p14 = models.IntegerField(choices=RESPONSE_TYPES)  # Necesito copiar los ejemplos de la pizarra del maestro para examinarlos más tarde
    p15 = models.IntegerField(choices=RESPONSE_TYPES)  # Prefiero las instrucciones orales del maestro a aquellas escritas en un examen o en la pizarra
    p16 = models.IntegerField(choices=RESPONSE_TYPES)  # Prefiero que un libro de texto tenga diagramas gráficos y cuadros porque me ayudan mejor a entender el material
    p17 = models.IntegerField(choices=RESPONSE_TYPES)  # Me gusta escuchar música al estudiar una obra, novela, etc.
    p18 = models.IntegerField(choices=RESPONSE_TYPES)  # Tengo que apuntar listas de cosas que quiero hacer para recordarlas
    p19 = models.IntegerField(choices=RESPONSE_TYPES)  # Puedo corregir mi tarea examinándola y encontrando la mayoría de los errores
    p20 = models.IntegerField(choices=RESPONSE_TYPES)  # Prefiero leer el periódico en vez de escuchar las noticias
    p21 = models.IntegerField(choices=RESPONSE_TYPES)  # Puedo recordar los números de teléfono cuando los oigo
    p22 = models.IntegerField(choices=RESPONSE_TYPES)  # Gozo el trabajo que me exige usar la mano o herramientas
    p23 = models.IntegerField(choices=RESPONSE_TYPES)  # Cuando escribo algo, necesito leerlo en voz alta para oír como suena
    p24 = models.IntegerField(choices=RESPONSE_TYPES)  # Puedo recordar mejor las cosas cuando puedo moverme mientras estoy aprendiéndolas, por ej. caminar al estudiar, o participar en una actividad que me permita moverme, etc.

    class Meta:
        default_permissions = ()
