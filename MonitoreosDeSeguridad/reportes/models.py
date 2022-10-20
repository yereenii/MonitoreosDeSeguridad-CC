from django.db import models
from django.contrib.auth.models import User

#Tuplas Generales
BLOQUEVPO = [
    ('1.1', '1.1 Reporte de Incidentes'),
    ('1.2', '1.2 Procesos de Alto Riesgo'),
    ('1.3', '1.3 Workplace Transport Safety'),
    ('1.4', '1.4 Manipulación de materiales y ergonomía'),
    ('1.5', '1.5 Sustancias Químicas'),
    ('1.6', '1.6 Espacios Confinados'),
    ('1.7', '1.7 Prevención de Violencia'),
    ('1.8', '1.8 Seguridad Vial y de Conducción'),
    ('1.9', '1.9 Trabajos en Alturas/Protección contra caídas'),
    ('1.10', '1.10 LOTOTO y seguridad de máquinas'),
    ('2.1', '2.1 Monitoreo y entrenamiento de seguridad'),
    ('2.2', '2.2 Gestión de la seguridad operacional'),
    ('2.3', '2.3 Cumplimiento a las Instalaciones.'),
    ('2.4', '2.4 Salud Ocupacional'),
    ('2.5', '2.5 Gestión de Proveedores de servicios y contratistas'),
    ('2.6', '2.6 Respuesta a emergencias'),
    ('3.1', '3.1 Cultura de Seguridad conductual'),
    ('3.2', '3.2 Gestión de SIF'),
]

DEPARTAMENTO = [
    ('CC', 'Compañía Contratista'),
    ('A', 'Ambiental'),
    ('E', 'Envasado'),
    ('EP', 'Envasado Producción'),
    ('G', 'Global'),
    ('L', 'Logística'),
    ('MG', 'Mantenimiento General'),
    ('SG', 'Servicios Generales'),
]
SINO = [
    ('1', 'SI'),
    ('2', 'NO'),
]

class ActosInsegurosMod(models.Model):
    CLASIFICACIONAI = [
        ('1', 'Análisis de riesgo, mal efectuado y supervición nula en procesos de alto riesgo'),
        ('2', 'Incumplimiento a controles establecidos en el área'),
        ('3', 'Incumplimiento a controles establecidos para trabajos de alto riesgo, análisis de riesgo u omisión en las reglas de oro'),
        ('4', 'Incumplimiento de controles para el manejo de SQP'),
        ('5', 'Incumplimiento en los controles establecidos para trabajos en altura'),
        ('6', 'No colocar calsas'),
        ('7', 'No ejecuta análisis de riesgo'),
        ('8', 'No notificar sobre la realización de una tarea'),
        ('9', 'No respetar lo indicado en las señalizaciones de tipo informativo, prohibitivo y restrictivo'),
        ('10', 'No respetar lineamientos para trabajos en alturas, mal uso de equipos o violación a normativas'),
        ('11', 'No seguir las reglas para operar vehiculos automotores (Exceder límites de velocidad, no uso de cinturón de seguridad, etc.'),
        ('12', 'No sujetar el pasamanos'),
        ('13', 'No usar los pasamanos en el uso de escaleras'),
        ('14', 'No usar pasillos peatonales en áreas proceso con afluencia vehicular / Deambula en área de carga - descarga'),
        ('15', 'Omisión a la rutina de seguridad'),
        ('16', 'Omisión en el registro de actividades de alto riesgo'),
        ('17', 'Uso inadecuado de linea de vida, mal uso de andamio, escalera, punto de anclaje no autorizado o mal efectuado'),
        ('18', 'Uso inseguro de celular'),
    ]

    DESCRIPCIONSANCION = [
        ('1', 'Retroalimentación'),
        ('2', 'Suspención Temporal'),
    ]


    GRUPOSCOMP = [
        ('1', 'CIRCULACIÓN SEGURA DE MONTACARGAS VEHÍCULOS'),
        ('2', 'DESPLAZAMIENTO SEGURO DE PERSONAS'),
        ('3', 'MANIPULACIÓN ADECUADA DE MATERIALES'),
        ('4', 'USO CORRECTO DE EQUIPOS Y HERRAMIENTA'),
    ]

    reporte_generado_el = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, verbose_name="Usuario", related_name="usuariogenerador", on_delete=models.CASCADE)

    bloqueVPO = models.CharField('Bloque VPO ', max_length=4, choices=BLOQUEVPO)
    clasificacionAI = models.CharField('Clasificación de Acto Inseguro ', max_length=2, choices=CLASIFICACIONAI)
    nombre_reportado = models.TextField('Nombre persona observada', max_length=250)
    desc_sancion = models.CharField('Descripción de Sanción ', max_length=1, choices=DESCRIPCIONSANCION)
    departamento = models.CharField('Departamento al que se detecta el Acto Inseguro ', max_length=2,
                                    choices=DEPARTAMENTO)
    es_contratista = models.TextField('En caso de ser Contratista, especificar de cuál se trata ', max_length=250,
                                      null=True)
    area = models.TextField('Área ', max_length=350)
    nombre_reportador = models.TextField('Nombre de quién detecta ', max_length=300)
    observaciones = models.TextField('Observaciones ', max_length=500)
    grupos = models.CharField('Grupos de Comportamiento ', max_length=1, choices=GRUPOSCOMP)
    precursor = models.CharField('Este acto puede ser precursor SIF', max_length=1, choices=SINO)



class ActosSegurosMod(models.Model):
    reporte_generado_el = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, verbose_name="Usuario", on_delete=models.CASCADE)

    bloqueVPO = models.CharField('Bloque VPO ', max_length=4, choices=BLOQUEVPO, default='1.1')
    nombre_reportado = models.TextField('Nombre persona observada', max_length=250, default='')
    felicitacion = models.CharField('Felicitó o Reconoció al personal', max_length=2, choices=SINO, default='1')
    nombre_jefinm = models.TextField('Nombre del Jefe Inmediato/Función', max_length=250, default='')
    departamento = models.CharField('Departamento al que se detecta el Acto Inseguro ', max_length=2, choices=DEPARTAMENTO, default='CC')
    es_contratista = models.TextField('En caso de ser Contratista, especificar de cuál se trata ', max_length=250, null=True, default='')
    area = models.TextField('Área ', max_length=350, default='')
    nombre_reportador = models.TextField('Nombre de quién detecta ', max_length=300, default='')
    descripcion_as = models.TextField('Descripción del Acto Seguro ', max_length=500, default='')
    fecha = models.DateTimeField(auto_now=True)

class IncidentesMenoresMod(models.Model):
    TURNO = [
        ('1', 'Primero'),
        ('2', 'Segundo'),
        ('3', 'Tercero'),
    ]

    TIPOINCIDENTE = [
        ('DE','Descarga Eléctrica Estática'),
        ('GC','Golpe Contra'),
        ('CI','Condición Insegura'),
        ('CF','Contacto Con Fauna'),
        ('TSC','Tropezar sin caer'),
        ('RSC','Resbalar sin caer'),
        ('EBC','Exceso de botella caida'),
        ('FA','Fuga de Agua'),
        ('DP','Desprendimiento de particulas'),
        ('CPC','Contacto con presión contendida'),
        ('A','Atoramiento'),
        ('C','Contacto con fluidos, materiales o áreas calientes'),
        ('CO','Caída de Objeto'),
        ('CH','Choque entre dos personas'),
        ('EB','Explosión de Botella'),
        ('CC','Corto Circuito'),
        ('FQ','Fuga de químico'),
    ]

    CAUSA = [
        ('AI','Acto Inseguro'),
        ('CI','Condición Insegura'),
    ]

    PROPOTERC = [
        ('P','Propio'),
        ('C','Contratista'),
    ]

    PUESTO = [
        ('O','Operador'),
        ('S','Supervisor'),
    ]

    reporte_generado_el = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, verbose_name="Usuario", on_delete=models.CASCADE)

    turno = models.CharField('Turno', max_length=1, choices=TURNO, default='1')
    nombre_reportador = models.TextField('Nombre de quién detecta ', max_length=300, default='')
    tipo_incidente = models.CharField('Topo de Incidente Reportado', max_length=3, choices=TIPOINCIDENTE, default='DE')
    departamento = models.TextField('Departamento', max_length=250, default='')
    area = models.TextField('Área', max_length=250, default='')
    maqoequipo = models.TextField('Máquina o Equipo', max_length=300, default='')
    propoterc = models.CharField('Propio o Terceria', max_length=1, choices=PROPOTERC ,default='P')
    puesto = models.CharField('Puesto de quien reporta', max_length=1,choices=PUESTO, default='O')
    descripcion = models.TextField('Descripción General del Incidente', max_length=500, default='')
    semana = models.TextField('Semana', max_length='2',default='')
    mes = models.TextField('Mes', max_length='12', default='')

class CondicionesInsegurasMod(models.Model):
    STATUS= [
        ('C','COMPLETO'),
        ('P','EN PROCESO'),
    ]

    CLASIFICACION = [
        ('2A','2 ALTA'),
        ('3M','3 MEDIA'),
        ('4B','4 BAJA'),
    ]

    ALCANCE = [
        ('DP','DEPARTAMENTO'),
        ('MT','MANTENIMIENTO'),
    ]

    reporte_generado_el = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, verbose_name="Usuario", on_delete=models.CASCADE)

    descr_condicion = models.TextField('Condición Insegura Detectada', max_length= 500, default='')
    fecha_inicio = models.DateTimeField('Fecha Inicio')
    fecha_fin = models.DateTimeField('Fecha Fin')
    estatus = models.CharField('Estatus', max_length=1, choices=STATUS, default='C')
    departamento = models.TextField('Departamento o Compañía', max_length=250,default='')
    area = models.TextField('Área', max_length=250, default='')
    nombre_reportador = models.TextField('Nombre de quién la detectó ', max_length=300, default='')
    clas_condic = models.CharField('Clasificación de la condición', max_length=2, choices=CLASIFICACION, default='4B')
    alcance = models.CharField('Alcance', max_length=2,choices=ALCANCE, default='DP')
    num_aviso = models.TextField('Número de Aviso', max_length=100,default='')
    time_corre = models.TextField('Tiempo de Corrección', max_length=100, default='')
    precursor = models.CharField('¿Es precursor SIF?1', max_length=1, choices=SINO)
    grupoycond = models.TextField('Grupo de Condiciones', max_length=250, default='')



