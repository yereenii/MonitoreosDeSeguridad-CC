from django.db import models

class ActosInsegurosMod(models.Model):
    BLOQUEVPO = [
        ('1.2','1.2 Procesos de Alto Riesgo'),
        ('1.5','1.5 Sustancias Químicas'),
        ('1.6','1.6 Espacios Confinados'),
        ('1.8','1.8 Seguridad Vial y de Conducción'),
        ('1.9','1.9 Trabajos en Alturas/Protección contra caídas'),
        ('2.1','2.1 Monitoreo y entrenamiento de seguridad'),
        ('2.3','2.3 Cumplimiento a las Instalaciones.'),
        ('2.4','2.4 Salud Ocupacional'),
        ('3.1','3.1 Cultura de Seguridad conductual'),
    ]

    CLASIFICACIONAI = [
        ('1','Análisis de riesgo, mal efectuado y supervición nula en procesos de alto riesgo'),
        ('2','Incumplimiento a controles establecidos en el área'),
        ('3','Incumplimiento a controles establecidos para trabajos de alto riesgo, análisis de riesgo u omisión en las reglas de oro'),
        ('4','Incumplimiento de controles para el manejo de SQP'),
        ('5','Incumplimiento en los controles establecidos para trabajos en altura'),
        ('6','No colocar calsas'),
        ('7','No ejecuta análisis de riesgo'),
        ('8','No notificar sobre la realización de una tarea'),
        ('9','No respetar lo indicado en las señalizaciones de tipo informativo, prohibitivo y restrictivo'),
        ('10','No respetar lineamientos para trabajos en alturas, mal uso de equipos o violación a normativas'),
        ('11','No seguir las reglas para operar vehiculos automotores (Exceder límites de velocidad, no uso de cinturón de seguridad, etc.'),
        ('12','No sujetar el pasamanos'),
        ('13','No usar los pasamanos en el uso de escaleras'),
        ('14','No usar pasillos peatonales en áreas proceso con afluencia vehicular / Deambula en área de carga - descarga'),
        ('15','Omisión a la rutina de seguridad'),
        ('16','Omisión en el registro de actividades de alto riesgo'),
        ('17','Uso inadecuado de linea de vida, mal uso de andamio, escalera, punto de anclaje no autorizado o mal efectuado'),
        ('18','Uso inseguro de celular'),
    ]

    DESCRIPCIONSANCION =[
        ('1','Retroalimentación'),
        ('2','Suspención Temporal'),
    ]

    DEPARTAMENTO = [
        ('CC','Compañía Contratista'),
        ('A','Ambiental'),
        ('E','Envasado'),
        ('EP','Envasado Producción'),
        ('G','Global'),
        ('L','Logística'),
        ('MG','Mantenimiento General'),
        ('SG','Servicios Generales'),
    ]

    AREA = [
        ('A','Arsenico'),
        ('BG','B. Grits'),
        ('BF','Bloque Frío'),
        ('B','BTS'),
        ('C','Cocimientos'),
        ('CM','Comedor Morita'),
        ('CR','CRP'),
        ('E','Envasado'),
        ('EG','Estacionamiento General'),
        ('FBF','Frente B. Frío'),
        ('FCG','Frente Comedor General'),
        ('FCM','Frente Comedor Morita'),
        ('FE','Frente Envasado'),
        ('FM','Frente MTTO'),
        ('FP','Frente P.R.A.'),
        ('FSM','Frente SM'),
        ('LB','LAB BTS'),
        ('OG','Oficinas Generales'),
        ('PR','P.R.A.'),
        ('T','Terciarios VETERINARIA'),
        ('VPO','VPO Room'),
    ]

    GRUPOSCOMP = [
        ('1','CIRCULACIÓN SEGURA DE MONTACARGAS VEHÍCULOS'),
        ('2','DESPLAZAMIENTO SEGURO DE PERSONAS'),
        ('3','MANIPULACIÓN ADECUADA DE MATERIALES'),
        ('4','USO CORRECTO DE EQUIPOS Y HERRAMIENTA'),
    ]

    PRECURSOR = [
        ('1','SI'),
        ('2','NO'),
    ]

    bloqueVPO = models.CharField('Bloque VPO ', max_length=3,choices=BLOQUEVPO, default='1.2')
    clasificacionAI = models.CharField('Clasificación de Acto Inseguro ', max_length =2, choices=CLASIFICACIONAI, default='1')
    nombre_reportado = models.TextField('Nombre persona observada', max_length=250, default='')
    desc_sancion = models.CharField('Descripción de Sanción ', max_length=1, choices= DESCRIPCIONSANCION, default='1')
    departamento = models.CharField('Departamento al que se detecta el Acto Inseguro ',max_length=2,choices=DEPARTAMENTO,default='CC')
    es_contratista = models.TextField('En caso de ser Contratista, especificar de cuál se trata ', max_length=250, null=True)
    area = models.CharField('Área ', max_length=3, choices=AREA, default='A')
    nombre_reportador = models.TextField('Nombre de quién detecta ', max_length=300, default='')
    observaciones = models.TextField('Observaciones ', max_length = 500,default='')
    grupos = models.CharField('Grupos de Comportamiento ', max_length = 1, choices=GRUPOSCOMP, default='1')
    precursor = models.CharField('Este acto puede ser precursor SIF', max_length=1, choices=PRECURSOR, default='2')
    fecha = models.DateTimeField(auto_now=True)
