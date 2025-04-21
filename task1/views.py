from django.http import JsonResponse

def index(request):
    agents_list = [
        {
            "id": 1,
            "title": "Atención al Cliente",
            "description": "Descripción",
            "industry": "No tecnológicos",
            "activacion": 3,
            "calificacion": 4.5,
            "usedBy": {
                "name": "Empresa X",
                "used": [
                    { "agent": "Atención al Cliente", "times": 12 }
                ]
            }
        },
        {
            "id": 2,
            "title": "Ventas",
            "description": "Descripción",
            "industry": "No tecnológicos",
            "activacion": 4,
            "calificacion": 4.2,
            "usedBy": {
                "name": "Empresa Y",
                "used": [
                    { "agent": "Ventas", "times": 8 }
                ]
            }
        },
        {
            "id": 3,
            "title": "Marketing Digital",
            "description": "Descripción",
            "industry": "No tecnológicos",
            "activacion": 5,
            "calificacion": 4.6,
            "usedBy": {
                "name": "Agencia Creativa",
                "used": [
                    { "agent": "Marketing Digital", "times": 10 }
                ]
            }
        },
        {
            "id": 4,
            "title": "Servicio de Recursos Humanos",
            "description": "Descripción",
            "industry": "No tecnológicos",
            "activacion": 2,
            "calificacion": 4.0,
            "usedBy": {
                "name": "Corporativo RH",
                "used": [
                    { "agent": "Servicio de Recursos Humanos", "times": 6 }
                ]
            }
        },
        {
            "id": 5,
            "title": "Gestor de Proyectos",
            "description": "Descripción",
            "industry": "No tecnológicos",
            "activacion": 6,
            "calificacion": 4.8,
            "usedBy": {
                "name": "Tech Project Ltd.",
                "used": [
                    { "agent": "Gestor de Proyectos", "times": 14 }
                ]
            }
        },
        {
            "id": 6,
            "title": "Asistente Personal",
            "description": "Descripción",
            "industry": "No tecnológicos",
            "activacion": 2,
            "calificacion": 4.3,
            "usedBy": {
                "name": "CEO Services",
                "used": [
                    { "agent": "Asistente Personal", "times": 9 }
                ]
            }
        },
        {
            "id": 7,
            "title": "Contador",
            "description": "Descripción",
            "industry": "No tecnológicos",
            "activacion": 3,
            "calificacion": 4.1,
            "usedBy": {
                "name": "Finanzas Corp",
                "used": [
                    { "agent": "Contador", "times": 7 }
                ]
            }
        },
        {
            "id": 8,
            "title": "Agente Inmobiliario",
            "description": "Descripción",
            "industry": "No tecnológicos",
            "activacion": 5,
            "calificacion": 4.4,
            "usedBy": {
                "name": "Casas y Más",
                "used": [
                    { "agent": "Agente Inmobiliario", "times": 11 }
                ]
            }
        },
        {
            "id": 9,
            "title": "Redactor de Contenidos",
            "description": "Descripción",
            "industry": "No tecnológicos",
            "activacion": 4,
            "calificacion": 4.6,
            "usedBy": {
                "name": "Blog Experts",
                "used": [
                    { "agent": "Redactor de Contenidos", "times": 13 }
                ]
            }
        },
        {
            "id": 10,
            "title": "Médico Generalista",
            "description": "Descripción",
            "industry": "No tecnológicos",
            "activacion": 3,
            "calificacion": 4.7,
            "usedBy": {
                "name": "Clínica Salud",
                "used": [
                    { "agent": "Médico Generalista", "times": 5 }
                ]
            }
        },
        {
          "id": 11,
          "title": "Desarrollador de Software",
          "description": "Descripción",
          "industry": "Tecnológicos",
          "activacion": 5,
          "calificacion": 4.9,
          "usedBy": {
            "name": "TechCorp",
            "used": [
              { "agent": "Desarrollador de Software", "times": 25 }
            ]
          }
        },
        {
          "id": 12,
          "title": "Analista de Datos",
          "description": "Descripción",
          "industry": "Tecnológicos",
          "activacion": 4,
          "calificacion": 4.7,
          "usedBy": {
            "name": "DataPlus",
            "used": [
              { "agent": "Analista de Datos", "times": 18 }
            ]
          }
        },
        {
          "id": 13,
          "title": "Ingeniero DevOps",
          "description": "Descripción",
          "industry": "Tecnológicos",
          "activacion": 5,
          "calificacion": 4.8,
          "usedBy": {
            "name": "DeployMasters",
            "used": [
              { "agent": "Ingeniero DevOps", "times": 20 }
            ]
          }
        },
        {
          "id": 14,
          "title": "Administrador de Sistemas",
          "description": "Descripción",
          "industry": "Tecnológicos",
          "activacion": 3,
          "calificacion": 4.4,
          "usedBy": {
            "name": "InfraSolutions",
            "used": [
              { "agent": "Administrador de Sistemas", "times": 12 }
            ]
          }
        },
        {
          "id": 15,
          "title": "Soporte Técnico",
          "description": "Descripción",
          "industry": "Tecnológicos",
          "activacion": 4,
          "calificacion": 4.3,
          "usedBy": {
            "name": "HelpDesk Pro",
            "used": [
              { "agent": "Soporte Técnico", "times": 15 }
            ]
          }
        },
        {
          "id": 16,
          "title": "Ingeniero de Pruebas de Software",
          "description": "Descripción",
          "industry": "Tecnológicos",
          "activacion": 4,
          "calificacion": 4.6,
          "usedBy": {
            "name": "QA Labs",
            "used": [
              { "agent": "Ingeniero de Pruebas de Software", "times": 17 }
            ]
          }
        },
        {
          "id": 17,
          "title": "Consultor de Ciberseguridad",
          "description": "Descripción",
          "industry": "Tecnológicos",
          "activacion": 5,
          "calificacion": 4.9,
          "usedBy": {
            "name": "CyberSafe",
            "used": [
              { "agent": "Consultor de Ciberseguridad", "times": 21 }
            ]
          }
        },
        {
          "id": 18,
          "title": "Administrador de Bases de Datos",
          "description": "Descripción",
          "industry": "Tecnológicos",
          "activacion": 3,
          "calificacion": 4.2,
          "usedBy": {
            "name": "DataKeep",
            "used": [
              { "agent": "Administrador de Bases de Datos", "times": 13 }
            ]
          }
        },
        {
          "id": 19,
          "title": "Desarrollador de IA/ML",
          "description": "Descripción",
          "industry": "Tecnológicos",
          "activacion": 5,
          "calificacion": 4.8,
          "usedBy": {
            "name": "AIWorks",
            "used": [
              { "agent": "Desarrollador de IA/ML", "times": 19 }
            ]
          }
        },
        {
          "id": 20,
          "title": "Especialista en Redes",
          "description": "Descripción",
          "industry": "Tecnológicos",
          "activacion": 4,
          "calificacion": 4.5,
          "usedBy": {
            "name": "NetSecure",
            "used": [
              { "agent": "Especialista en Redes", "times": 16 }
            ]
          }
        },
        {
          "id": 21,
          "title": "Diseñador Gráfico",
          "description": "Descripción",
          "industry": "Creativos",
          "activacion": 2,
          "calificacion": 4.2,
          "usedBy": {
            "name": "Agencia Creativa",
            "used": [
              { "agent": "Diseñador Gráfico", "times": 8 }
            ]
          }
        },
        {
          "id": 22,
          "title": "Productor de Contenidos",
          "description": "Descripción",
          "industry": "Creativos",
          "activacion": 3,
          "calificacion": 4.4,
          "usedBy": {
            "name": "MediaHub",
            "used": [
              { "agent": "Productor de Contenidos", "times": 10 }
            ]
          }
        },
        {
          "id": 23,
          "title": "Editor de Video",
          "description": "Descripción",
          "industry": "Creativos",
          "activacion": 3,
          "calificacion": 4.3,
          "usedBy": {
            "name": "VisualWorks",
            "used": [
              { "agent": "Editor de Video", "times": 9 }
            ]
          }
        },
        {
          "id": 24,
          "title": "Investigador Académico",
          "description": "Descripción",
          "industry": "Creativos",
          "activacion": 2,
          "calificacion": 4.1,
          "usedBy": {
            "name": "Instituto Saber",
            "used": [
              { "agent": "Investigador Académico", "times": 7 }
            ]
          }
        },
        {
          "id": 25,
          "title": "Traductor",
          "description": "Descripción",
          "industry": "Creativos",
          "activacion": 2,
          "calificacion": 4.0,
          "usedBy": {
            "name": "Global Text",
            "used": [
              { "agent": "Traductor", "times": 6 }
            ]
          }
        },
        {
          "id": 26,
          "title": "Ingeniero de Pruebas de Software",
          "description": "Descripción",
          "industry": "Creativos",
          "activacion": 3,
          "calificacion": 4.5,
          "usedBy": {
            "name": "CreativeTesters",
            "used": [
              { "agent": "Ingeniero de Pruebas de Software", "times": 11 }
            ]
          }
        },
        {
          "id": 27,
          "title": "Asistente Administrativo",
          "description": "Descripción",
          "industry": "Administrativos",
          "activacion": 3,
          "calificacion": 4.1,
          "usedBy": {
            "name": "OfiGestión",
            "used": [
              { "agent": "Asistente Administrativo", "times": 12 }
            ]
          }
        },
        {
          "id": 28,
          "title": "Secretaría Legal",
          "description": "Descripción",
          "industry": "Administrativos",
          "activacion": 4,
          "calificacion": 4.6,
          "usedBy": {
            "name": "Bufete Central",
            "used": [
              { "agent": "Secretaría Legal", "times": 15 }
            ]
          }
        },
        {
          "id": 29,
          "title": "Operador de Call Center",
          "description": "Descripción",
          "industry": "Administrativos",
          "activacion": 2,
          "calificacion": 3.9,
          "usedBy": {
            "name": "CallTech",
            "used": [
              { "agent": "Operador de Call Center", "times": 20 }
            ]
          }
        },
        {
          "id": 30,
          "title": "Planificador Financiero",
          "description": "Descripción",
          "industry": "Administrativos",
          "activacion": 4,
          "calificacion": 4.7,
          "usedBy": {
            "name": "FinPlan SA",
            "used": [
              { "agent": "Planificador Financiero", "times": 14 }
            ]
          }
        },
        {
          "id": 31,
          "title": "Agente de Viajes",
          "description": "Descripción",
          "industry": "Administrativos",
          "activacion": 3,
          "calificacion": 4.2,
          "usedBy": {
            "name": "ViajaFácil",
            "used": [
              { "agent": "Agente de Viajes", "times": 9 }
            ]
          }
        },
        {
          "id": 32,
          "title": "Ingeniero de Pruebas de Software",
          "description": "Descripción",
          "industry": "Administrativos",
          "activacion": 3,
          "calificacion": 4.5,
          "usedBy": {
            "name": "SoftCheck",
            "used": [
              { "agent": "Ingeniero de Pruebas de Software", "times": 10 }
            ]
          }
        }
    ]
    
    return JsonResponse(agents_list, safe=False)