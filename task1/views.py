from django.http import JsonResponse

def index(request):
    agents_list = [
        {
          "id": 1,
          "title": "Customer Support",
          "description": "Description",
          "industry": "Non-tech",
          "activations": 3,
          "rate": 4.5,
          "usedBy": [
            {
              "id": "ub1",
              "agentId": 1,
              "client": {
                "id": "c1",
                "name": "Company X",
                "lastName": "Placeholder",
                "email": "companyx@example.com",
                "password": "secure123"
              },
              "useDate": "2024-01-15",
              "startedTime": "2024-01-15T09:00:00Z",
              "endedTime": "2024-01-15T18:00:00Z"
            }
          ],
          "feedback": [
            {
              "id": "f1",
              "agentId": 1,
              "clientId": "c1",
              "text": "Great service!",
              "value": 4.5
            }
          ],
          "rateEntries": [
            {
              "id": "r1",
              "rate": 4.5,
              "clientId": "c1",
              "agentId": 1
            }
          ]
        },
        {
          "id": 2,
          "title": "Sales",
          "description": "Description",
          "industry": "Non-tech",
          "activations": 4,
          "rate": 4.2,
          "usedBy": [
            {
              "id": "ub2",
              "agentId": 2,
              "client": {
                "id": "c2",
                "name": "Company Y",
                "lastName": "Placeholder",
                "email": "companyy@example.com",
                "password": "secure123"
              },
              "useDate": "2024-02-12",
              "startedTime": "2024-02-12T09:00:00Z",
              "endedTime": "2024-02-12T18:00:00Z"
            }
          ],
          "feedback": [
            {
              "id": "f2",
              "agentId": 2,
              "clientId": "c2",
              "text": "Very effective.",
              "value": 4.2
            }
          ],
          "rateEntries": [
            {
              "id": "r2",
              "rate": 4.2,
              "clientId": "c2",
              "agentId": 2
            }
          ]
        },
        {
          "id": 3,
          "title": "Digital Marketing",
          "description": "Description",
          "industry": "Non-tech",
          "activations": 5,
          "rate": 4.6,
          "usedBy": [
            {
              "id": "ub3",
              "agentId": 3,
              "client": {
                "id": "c3",
                "name": "Creative Agency",
                "lastName": "Placeholder",
                "email": "agency@example.com",
                "password": "secure123"
              },
              "useDate": "2024-03-10",
              "startedTime": "2024-03-10T10:00:00Z",
              "endedTime": "2024-03-10T17:00:00Z"
            }
          ],
          "feedback": [
            {
              "id": "f3",
              "agentId": 3,
              "clientId": "c3",
              "text": "Highly recommend.",
              "value": 4.6
            }
          ],
          "rateEntries": [
            {
              "id": "r3",
              "rate": 4.6,
              "clientId": "c3",
              "agentId": 3
            }
          ]
        },
        {
          "id": 4,
          "title": "Human Resources Service",
          "description": "Description",
          "industry": "Non-tech",
          "activations": 2,
          "rate": 4.0,
          "usedBy": [
            {
              "id": "ub4",
              "agentId": 4,
              "client": {
                "id": "c4",
                "name": "RH Corp",
                "lastName": "Placeholder",
                "email": "rhcorp@example.com",
                "password": "secure123"
              },
              "useDate": "2024-04-01",
              "startedTime": "2024-04-01T08:00:00Z",
              "endedTime": "2024-04-01T17:00:00Z"
            }
          ],
          "feedback": [
            {
              "id": "f4",
              "agentId": 4,
              "clientId": "c4",
              "text": "Professional and efficient.",
              "value": 4.0
            }
          ],
          "rateEntries": [
            {
              "id": "r4",
              "rate": 4.0,
              "clientId": "c4",
              "agentId": 4
            }
          ]
        },
        {
          "id": 5,
          "title": "Project Manager",
          "description": "Description",
          "industry": "Non-tech",
          "activations": 6,
          "rate": 4.8,
          "usedBy": [
            {
              "id": "ub5",
              "agentId": 5,
              "client": {
                "id": "c5",
                "name": "Tech Project Ltd.",
                "lastName": "Placeholder",
                "email": "techproject@example.com",
                "password": "secure123"
              },
              "useDate": "2024-04-05",
              "startedTime": "2024-04-05T09:00:00Z",
              "endedTime": "2024-04-05T18:00:00Z"
            }
          ],
          "feedback": [
            {
              "id": "f5",
              "agentId": 5,
              "clientId": "c5",
              "text": "Outstanding project management.",
              "value": 4.8
            }
          ],
          "rateEntries": [
            {
              "id": "r5",
              "rate": 4.8,
              "clientId": "c5",
              "agentId": 5
            }
          ]
        },
        {
          "id": 6,
          "title": "Personal Assistant",
          "description": "Description",
          "industry": "Non-tech",
          "activations": 2,
          "rate": 4.3,
          "usedBy": [
            {
              "id": "ub6",
              "agentId": 6,
              "client": {
                "id": "c6",
                "name": "CEO Services",
                "lastName": "Placeholder",
                "email": "ceoservices@example.com",
                "password": "secure123"
              },
              "useDate": "2024-04-10",
              "startedTime": "2024-04-10T07:30:00Z",
              "endedTime": "2024-04-10T15:30:00Z"
            }
          ],
          "feedback": [
            {
              "id": "f6",
              "agentId": 6,
              "clientId": "c6",
              "text": "Reliable and responsive.",
              "value": 4.3
            }
          ],
          "rateEntries": [
            {
              "id": "r6",
              "rate": 4.3,
              "clientId": "c6",
              "agentId": 6
            }
          ]
        },
        {
          "id": 7,
          "title": "Accountant",
          "description": "Description",
          "industry": "Non-tech",
          "activations": 3,
          "rate": 4.1,
          "usedBy": [
            {
              "id": "ub7",
              "agentId": 7,
              "client": {
                "id": "c7",
                "name": "Finance Corp",
                "lastName": "Placeholder",
                "email": "financecorp@example.com",
                "password": "secure123"
              },
              "useDate": "2024-04-15",
              "startedTime": "2024-04-15T09:30:00Z",
              "endedTime": "2024-04-15T17:30:00Z"
            }
          ],
          "feedback": [
            {
              "id": "f7",
              "agentId": 7,
              "clientId": "c7",
              "text": "Accurate and trustworthy.",
              "value": 4.1
            }
          ],
          "rateEntries": [
            {
              "id": "r7",
              "rate": 4.1,
              "clientId": "c7",
              "agentId": 7
            }
          ]
        },
        {
          "id": 8,
          "title": "Real Estate Agent",
          "description": "Description",
          "industry": "Non-tech",
          "activations": 5,
          "rate": 4.4,
          "usedBy": [
            {
              "id": "ub8",
              "agentId": 8,
              "client": {
                "id": "c8",
                "name": "Casas y Más",
                "lastName": "Placeholder",
                "email": "casasymas@example.com",
                "password": "secure123"
              },
              "useDate": "2024-04-18",
              "startedTime": "2024-04-18T10:00:00Z",
              "endedTime": "2024-04-18T19:00:00Z"
            }
          ],
          "feedback": [
            {
              "id": "f8",
              "agentId": 8,
              "clientId": "c8",
              "text": "Helped us find the perfect place.",
              "value": 4.4
            }
          ],
          "rateEntries": [
            {
              "id": "r8",
              "rate": 4.4,
              "clientId": "c8",
              "agentId": 8
            }
          ]
        },
        {
          "id": 9,
          "title": "Content Writer",
          "description": "Description",
          "industry": "Non-tech",
          "activations": 4,
          "rate": 4.6,
          "usedBy": [
            {
              "id": "ub9",
              "agentId": 9,
              "client": {
                "id": "c9",
                "name": "Blog Experts",
                "lastName": "Placeholder",
                "email": "blogexperts@example.com",
                "password": "secure123"
              },
              "useDate": "2024-04-21",
              "startedTime": "2024-04-21T11:00:00Z",
              "endedTime": "2024-04-21T16:00:00Z"
            }
          ],
          "feedback": [
            {
              "id": "f9",
              "agentId": 9,
              "clientId": "c9",
              "text": "High-quality content delivered fast.",
              "value": 4.6
            }
          ],
          "rateEntries": [
            {
              "id": "r9",
              "rate": 4.6,
              "clientId": "c9",
              "agentId": 9
            }
          ]
        },
        {
          "id": 10,
          "title": "General Practitioner",
          "description": "Description",
          "industry": "Non-tech",
          "activations": 3,
          "rate": 4.7,
          "usedBy": [
            {
              "id": "ub10",
              "agentId": 10,
              "client": {
                "id": "c10",
                "name": "Health Clinic",
                "lastName": "Placeholder",
                "email": "healthclinic@example.com",
                "password": "secure123"
              },
              "useDate": "2024-04-22",
              "startedTime": "2024-04-22T08:30:00Z",
              "endedTime": "2024-04-22T15:30:00Z"
            }
          ],
          "feedback": [
            {
              "id": "f10",
              "agentId": 10,
              "clientId": "c10",
              "text": "Excellent care and support.",
              "value": 4.7
            }
          ],
          "rateEntries": [
            {
              "id": "r10",
              "rate": 4.7,
              "clientId": "c10",
              "agentId": 10
            }
          ]
        },
        {
          "id": 11,
          "title": "Desarrollador de Software",
          "description": "Especialista en el diseño, desarrollo y mantenimiento de aplicaciones informáticas.",
          "industry": "Tecnológicos",
          "activations": 5,
          "rate": 4.9,
          "usedBy": [
            {
              "id": "ub11",
              "agentId": 11,
              "client": {
                "id": "c11",
                "name": "TechCorp",
                "lastName": "Solutions",
                "email": "contacto@techcorp.com",
                "password": "securepass11"
              },
              "useDate": "2024-04-19",
              "startedTime": "2024-04-19T09:00:00Z",
              "endedTime": "2024-04-19T17:00:00Z"
            }
          ],
          "feedback": [
            {
              "id": "f11",
              "agentId": 11,
              "clientId": "c11",
              "text": "Desarrolló una plataforma eficiente y robusta.",
              "value": 4.9
            }
          ],
          "rateEntries": [
            {
              "id": "r11",
              "rate": 4.9,
              "clientId": "c11",
              "agentId": 11
            }
          ]
        },
         {
           "id": 12,
           "title": "Analista de Datos",
           "description": "Descripción",
           "industry": "Tecnológicos",
           "activations": 4,
           "rate": 4.7,
           "usedBy": [
             {
               "id": "ub12",
               "agentId": 12,
               "client": {
                 "id": "c12",
                 "name": "DataPlus",
                 "lastName": "Placeholder",
                 "email": "dataplus@example.com",
                 "password": "secure12"
               },
               "useDate": "2024-04-17",
               "startedTime": "2024-04-17T09:00:00Z",
               "endedTime": "2024-04-17T17:00:00Z"
             }
           ],
           "feedback": [
             {
               "id": "f12",
               "agentId": 12,
               "clientId": "c12",
               "text": "Excelente desempeño como analista de datos.",
               "value": 4.7
             }
           ],
           "rateEntries": [
             {
               "id": "r12",
               "rate": 4.7,
               "clientId": "c12",
               "agentId": 12
             }
           ]
         },
         {
           "id": 13,
           "title": "Ingeniero DevOps",
           "description": "Descripción",
           "industry": "Tecnológicos",
           "activations": 4,
           "rate": 4.8,
           "usedBy": [
             {
               "id": "ub13",
               "agentId": 13,
               "client": {
                 "id": "c13",
                 "name": "DeployMasters",
                 "lastName": "Placeholder",
                 "email": "deploymasters@example.com",
                 "password": "secure13"
               },
               "useDate": "2024-04-14",
               "startedTime": "2024-04-14T09:00:00Z",
               "endedTime": "2024-04-14T17:00:00Z"
             }
           ],
           "feedback": [
             {
               "id": "f13",
               "agentId": 13,
               "clientId": "c13",
               "text": "Excelente desempeño como ingeniero devops.",
               "value": 4.8
             }
           ],
           "rateEntries": [
             {
               "id": "r13",
               "rate": 4.8,
               "clientId": "c13",
               "agentId": 13
             }
           ]
         },
         {
           "id": 14,
           "title": "Administrador de Sistemas",
           "description": "Descripción",
           "industry": "Tecnológicos",
           "activations": 3,
           "rate": 4.4,
           "usedBy": [
             {
               "id": "ub14",
               "agentId": 14,
               "client": {
                 "id": "c14",
                 "name": "InfraSolutions",
                 "lastName": "Placeholder",
                 "email": "infrasolutions@example.com",
                 "password": "secure14"
               },
               "useDate": "2024-04-15",
               "startedTime": "2024-04-15T09:00:00Z",
               "endedTime": "2024-04-15T17:00:00Z"
             }
           ],
           "feedback": [
             {
               "id": "f14",
               "agentId": 14,
               "clientId": "c14",
               "text": "Excelente desempeño como administrador de sistemas.",
               "value": 4.4
             }
           ],
           "rateEntries": [
             {
               "id": "r14",
               "rate": 4.4,
               "clientId": "c14",
               "agentId": 14
             }
           ]
         },
         {
           "id": 15,
           "title": "Soporte Técnico",
           "description": "Descripción",
           "industry": "Tecnológicos",
           "activations": 3,
           "rate": 4.3,
           "usedBy": [
             {
               "id": "ub15",
               "agentId": 15,
               "client": {
                 "id": "c15",
                 "name": "HelpDesk Pro",
                 "lastName": "Placeholder",
                 "email": "helpdeskpro@example.com",
                 "password": "secure15"
               },
               "useDate": "2024-04-16",
               "startedTime": "2024-04-16T09:00:00Z",
               "endedTime": "2024-04-16T17:00:00Z"
             }
           ],
           "feedback": [
             {
               "id": "f15",
               "agentId": 15,
               "clientId": "c15",
               "text": "Excelente desempeño como soporte técnico.",
               "value": 4.3
             }
           ],
           "rateEntries": [
             {
               "id": "r15",
               "rate": 4.3,
               "clientId": "c15",
               "agentId": 15
             }
           ]
         },
         {
           "id": 16,
           "title": "Ingeniero de Pruebas de Software",
           "description": "Descripción",
           "industry": "Tecnológicos",
           "activations": 5,
           "rate": 4.6,
           "usedBy": [
             {
               "id": "ub16",
               "agentId": 16,
               "client": {
                 "id": "c16",
                 "name": "QA Labs",
                 "lastName": "Placeholder",
                 "email": "qalabs@example.com",
                 "password": "secure16"
               },
               "useDate": "2024-04-10",
               "startedTime": "2024-04-10T09:00:00Z",
               "endedTime": "2024-04-10T17:00:00Z"
             }
           ],
           "feedback": [
             {
               "id": "f16",
               "agentId": 16,
               "clientId": "c16",
               "text": "Excelente desempeño como ingeniero de pruebas de software.",
               "value": 4.6
             }
           ],
           "rateEntries": [
             {
               "id": "r16",
               "rate": 4.6,
               "clientId": "c16",
               "agentId": 16
             }
           ]
         },
         {
           "id": 17,
           "title": "Consultor de Ciberseguridad",
           "description": "Descripción",
           "industry": "Tecnológicos",
           "activations": 3,
           "rate": 4.9,
           "usedBy": [
             {
               "id": "ub17",
               "agentId": 17,
               "client": {
                 "id": "c17",
                 "name": "CyberSafe",
                 "lastName": "Placeholder",
                 "email": "cybersafe@example.com",
                 "password": "secure17"
               },
               "useDate": "2024-04-17",
               "startedTime": "2024-04-17T09:00:00Z",
               "endedTime": "2024-04-17T17:00:00Z"
             }
           ],
           "feedback": [
             {
               "id": "f17",
               "agentId": 17,
               "clientId": "c17",
               "text": "Excelente desempeño como consultor de ciberseguridad.",
               "value": 4.9
             }
           ],
           "rateEntries": [
             {
               "id": "r17",
               "rate": 4.9,
               "clientId": "c17",
               "agentId": 17
             }
           ]
         },
         {
           "id": 18,
           "title": "Administrador de Bases de Datos",
           "description": "Descripción",
           "industry": "Tecnológicos",
           "activations": 3,
           "rate": 4.2,
           "usedBy": [
             {
               "id": "ub18",
               "agentId": 18,
               "client": {
                 "id": "c18",
                 "name": "DataKeep",
                 "lastName": "Placeholder",
                 "email": "datakeep@example.com",
                 "password": "secure18"
               },
               "useDate": "2024-04-19",
               "startedTime": "2024-04-19T09:00:00Z",
               "endedTime": "2024-04-19T17:00:00Z"
             }
           ],
           "feedback": [
             {
               "id": "f18",
               "agentId": 18,
               "clientId": "c18",
               "text": "Excelente desempeño como administrador de bases de datos.",
               "value": 4.2
             }
           ],
           "rateEntries": [
             {
               "id": "r18",
               "rate": 4.2,
               "clientId": "c18",
               "agentId": 18
             }
           ]
         },
         {
           "id": 19,
           "title": "Desarrollador de IA/ML",
           "description": "Descripción",
           "industry": "Tecnológicos",
           "activations": 3,
           "rate": 4.8,
           "usedBy": [
             {
               "id": "ub19",
               "agentId": 19,
               "client": {
                 "id": "c19",
                 "name": "AIWorks",
                 "lastName": "Placeholder",
                 "email": "aiworks@example.com",
                 "password": "secure19"
               },
               "useDate": "2024-04-19",
               "startedTime": "2024-04-19T09:00:00Z",
               "endedTime": "2024-04-19T17:00:00Z"
             }
           ],
           "feedback": [
             {
               "id": "f19",
               "agentId": 19,
               "clientId": "c19",
               "text": "Excelente desempeño como desarrollador de ia/ml.",
               "value": 4.8
             }
           ],
           "rateEntries": [
             {
               "id": "r19",
               "rate": 4.8,
               "clientId": "c19",
               "agentId": 19
             }
           ]
         },
         {
           "id": 20,
           "title": "Especialista en Redes",
           "description": "Descripción",
           "industry": "Tecnológicos",
           "activations": 5,
           "rate": 4.5,
           "usedBy": [
             {
               "id": "ub20",
               "agentId": 20,
               "client": {
                 "id": "c20",
                 "name": "NetSecure",
                 "lastName": "Placeholder",
                 "email": "netsecure@example.com",
                 "password": "secure20"
               },
               "useDate": "2024-04-13",
               "startedTime": "2024-04-13T09:00:00Z",
               "endedTime": "2024-04-13T17:00:00Z"
             }
           ],
           "feedback": [
             {
               "id": "f20",
               "agentId": 20,
               "clientId": "c20",
               "text": "Excelente desempeño como especialista en redes.",
               "value": 4.5
             }
           ],
           "rateEntries": [
             {
               "id": "r20",
               "rate": 4.5,
               "clientId": "c20",
               "agentId": 20
             }
           ]
         },

         {
          "id": 21,
          "title": "Diseñador Gráfico",
          "description": "Especialista en la creación de conceptos visuales, utilizando software para comunicar ideas que inspiren, informen o cautiven a los consumidores.",
          "industry": "Creativos",
          "activations": 2,
          "rate": 4.2,
          "usedBy": [
            {
              "id": "ub21",
              "agentId": 21,
              "client": {
                "id": "c21",
                "name": "Agencia Creativa",
                "lastName": "Agencia",
                "email": "contacto@agenciacreativa.com",
                "password": "securepass21"
              },
              "useDate": "2024-04-12",
              "startedTime": "2024-04-12T09:00:00Z",
              "endedTime": "2024-04-12T17:00:00Z"
            }
          ],
          "feedback": [
            {
              "id": "f21",
              "agentId": 21,
              "clientId": "c21",
              "text": "Diseñó una campaña visual impactante y creativa.",
              "value": 4.2
            }
          ],
          "rateEntries": [
            {
              "id": "r21",
              "rate": 4.2,
              "clientId": "c21",
              "agentId": 21
            }
          ]
        },
        {
          "id": 22,
          "title": "Productor de Contenidos",
          "description": "Responsable de la creación y gestión de contenido multimedia, desde la concepción de la idea hasta la ejecución final.",
          "industry": "Creativos",
          "activations": 3,
          "rate": 4.4,
          "usedBy": [
            {
              "id": "ub22",
              "agentId": 22,
              "client": {
                "id": "c22",
                "name": "MediaHub",
                "lastName": "Hub",
                "email": "contacto@mediahub.com",
                "password": "securepass22"
              },
              "useDate": "2024-04-14",
              "startedTime": "2024-04-14T10:00:00Z",
              "endedTime": "2024-04-14T18:00:00Z"
            }
          ],
          "feedback": [
            {
              "id": "f22",
              "agentId": 22,
              "clientId": "c22",
              "text": "El contenido producido fue excepcional y cumplió con los objetivos de la campaña.",
              "value": 4.4
            }
          ],
          "rateEntries": [
            {
              "id": "r22",
              "rate": 4.4,
              "clientId": "c22",
              "agentId": 22
            }
          ]
        },
        {
          "id": 23,
          "title": "Editor de Video",
          "description": "Encargado de editar y ensamblar material de video, mejorando la calidad visual y sonora según las necesidades del proyecto.",
          "industry": "Creativos",
          "activations": 3,
          "rate": 4.3,
          "usedBy": [
            {
              "id": "ub23",
              "agentId": 23,
              "client": {
                "id": "c23",
                "name": "VisualWorks",
                "lastName": "Works",
                "email": "contacto@visualworks.com",
                "password": "securepass23"
              },
              "useDate": "2024-04-16",
              "startedTime": "2024-04-16T09:00:00Z",
              "endedTime": "2024-04-16T17:00:00Z"
            }
          ],
          "feedback": [
            {
              "id": "f23",
              "agentId": 23,
              "clientId": "c23",
              "text": "La edición del video fue precisa y cumplió con nuestras expectativas.",
              "value": 4.3
            }
          ],
          "rateEntries": [
            {
              "id": "r23",
              "rate": 4.3,
              "clientId": "c23",
              "agentId": 23
            }
          ]
        },
        {
          "id": 24,
          "title": "Investigador Académico",
          "description": "Responsable de llevar a cabo investigaciones en áreas académicas, realizando estudios y análisis detallados para avanzar en el conocimiento.",
          "industry": "Creativos",
          "activations": 2,
          "rate": 4.1,
          "usedBy": [
            {
              "id": "ub24",
              "agentId": 24,
              "client": {
                "id": "c24",
                "name": "Instituto Saber",
                "lastName": "Saber",
                "email": "contacto@institutosaber.com",
                "password": "securepass24"
              },
              "useDate": "2024-04-18",
              "startedTime": "2024-04-18T08:00:00Z",
              "endedTime": "2024-04-18T16:00:00Z"
            }
          ],
          "feedback": [
            {
              "id": "f24",
              "agentId": 24,
              "clientId": "c24",
              "text": "La investigación proporcionó insights valiosos para nuestro estudio.",
              "value": 4.1
            }
          ],
          "rateEntries": [
            {
              "id": "r24",
              "rate": 4.1,
              "clientId": "c24",
              "agentId": 24
            }
          ]
        },
        {
          "id": 25,
          "title": "Traductor",
          "description": "Profesional encargado de traducir textos de un idioma a otro, manteniendo la fidelidad y precisión del contenido original.",
          "industry": "Creativos",
          "activations": 2,
          "rate": 4.0,
          "usedBy": [
            {
              "id": "ub25",
              "agentId": 25,
              "client": {
                "id": "c25",
                "name": "Global Text",
                "lastName": "Text",
                "email": "contacto@globaltext.com",
                "password": "securepass25"
              },
              "useDate": "2024-04-20",
              "startedTime": "2024-04-20T11:00:00Z",
              "endedTime": "2024-04-20T19:00:00Z"
            }
          ],
          "feedback": [
            {
              "id": "f25",
              "agentId": 25,
              "clientId": "c25",
              "text": "Las traducciones fueron precisas y entregadas a tiempo.",
              "value": 4.0
            }
          ],
          "rateEntries": [
            {
              "id": "r25",
              "rate": 4.0,
              "clientId": "c25",
              "agentId": 25
            }
          ]
        },
        {
          "id": 26,
          "title": "Ingeniero de Pruebas de Software",
          "description": "Responsable de crear y ejecutar pruebas para asegurar la calidad de las aplicaciones y sistemas de software.",
          "industry": "Creativos",
          "activations": 3,
          "rate": 4.5,
          "usedBy": [
            {
              "id": "ub26",
              "agentId": 26,
              "client": {
                "id": "c26",
                "name": "CreativeTesters",
                "lastName": "Testers",
                "email": "contacto@creativetesters.com",
                "password": "securepass26"
              },
              "useDate": "2024-04-22",
              "startedTime": "2024-04-22T08:30:00Z",
              "endedTime": "2024-04-22T16:30:00Z"
            }
          ],
          "feedback": [
            {
              "id": "f26",
              "agentId": 26,
              "clientId": "c26",
              "text": "Las pruebas fueron exhaustivas y contribuyeron significativamente al lanzamiento del producto.",
              "value": 4.5
            }
          ],
          "rateEntries": [
            {
              "id": "r26",
              "rate": 4.5,
              "clientId": "c26",
              "agentId": 26
            }
          ]
        },
        {
          "id": 27,
          "title": "Asistente Administrativo",
          "description": "Especialista en la gestión de tareas administrativas, organización de agendas y apoyo en la coordinación de actividades diarias.",
          "industry": "Administrativos",
          "activations": 3,
          "rate": 4.1,
          "usedBy": [
            {
              "id": "ub27",
              "agentId": 27,
              "client": {
                "id": "c27",
                "name": "OfiGestión",
                "lastName": "Gestión",
                "email": "contacto@ofigestion.com",
                "password": "securepass27"
              },
              "useDate": "2024-04-22",
              "startedTime": "2024-04-22T09:00:00Z",
              "endedTime": "2024-04-22T17:00:00Z"
            }
          ],
          "feedback": [
            {
              "id": "f27",
              "agentId": 27,
              "clientId": "c27",
              "text": "Excelente apoyo en la organización de tareas y gestión administrativa.",
              "value": 4.1
            }
          ],
          "rateEntries": [
            {
              "id": "r27",
              "rate": 4.1,
              "clientId": "c27",
              "agentId": 27
            }
          ]
        },
        {
          "id": 28,
          "title": "Secretaría Legal",
          "description": "Profesional encargado de la organización y gestión de documentos legales, así como el apoyo a abogados y equipos legales en diversas tareas administrativas.",
          "industry": "Administrativos",
          "activations": 4,
          "rate": 4.6,
          "usedBy": [
            {
              "id": "ub28",
              "agentId": 28,
              "client": {
                "id": "c28",
                "name": "Bufete Central",
                "lastName": "Legal",
                "email": "contacto@bufetecentral.com",
                "password": "securepass28"
              },
              "useDate": "2024-04-21",
              "startedTime": "2024-04-21T08:30:00Z",
              "endedTime": "2024-04-21T17:30:00Z"
            }
          ],
          "feedback": [
            {
              "id": "f28",
              "agentId": 28,
              "clientId": "c28",
              "text": "Gran eficiencia en la organización de documentos y apoyo legal.",
              "value": 4.6
            }
          ],
          "rateEntries": [
            {
              "id": "r28",
              "rate": 4.6,
              "clientId": "c28",
              "agentId": 28
            }
          ]
        },
        {
          "id": 29,
          "title": "Operador de Call Center",
          "description": "Encargado de atender llamadas entrantes y salientes, resolver dudas de clientes y gestionar solicitudes dentro de un centro de atención telefónica.",
          "industry": "Administrativos",
          "activations": 2,
          "rate": 3.9,
          "usedBy": [
            {
              "id": "ub29",
              "agentId": 29,
              "client": {
                "id": "c29",
                "name": "CallTech",
                "lastName": "Support",
                "email": "contacto@calltech.com",
                "password": "securepass29"
              },
              "useDate": "2024-04-20",
              "startedTime": "2024-04-20T10:00:00Z",
              "endedTime": "2024-04-20T18:00:00Z"
            }
          ],
          "feedback": [
            {
              "id": "f29",
              "agentId": 29,
              "clientId": "c29",
              "text": "Buena atención, pero necesita mejorar en la resolución de problemas.",
              "value": 3.9
            }
          ],
          "rateEntries": [
            {
              "id": "r29",
              "rate": 3.9,
              "clientId": "c29",
              "agentId": 29
            }
          ]
        },
        {
          "id": 30,
          "title": "Planificador Financiero",
          "description": "Profesional encargado de asesorar y planificar las finanzas de individuos o empresas, ayudando a establecer objetivos económicos a largo plazo.",
          "industry": "Administrativos",
          "activations": 4,
          "rate": 4.7,
          "usedBy": [
            {
              "id": "ub30",
              "agentId": 30,
              "client": {
                "id": "c30",
                "name": "FinPlan SA",
                "lastName": "Planificación",
                "email": "contacto@finplan.com",
                "password": "securepass30"
              },
              "useDate": "2024-04-19",
              "startedTime": "2024-04-19T08:00:00Z",
              "endedTime": "2024-04-19T17:00:00Z"
            }
          ],
          "feedback": [
            {
              "id": "f30",
              "agentId": 30,
              "clientId": "c30",
              "text": "Excelente en la gestión financiera y planificación de metas.",
              "value": 4.7
            }
          ],
          "rateEntries": [
            {
              "id": "r30",
              "rate": 4.7,
              "clientId": "c30",
              "agentId": 30
            }
          ]
        },
        {
          "id": 31,
          "title": "Agente de Viajes",
          "description": "Responsable de asistir a clientes en la planificación y reserva de viajes, incluyendo vuelos, hoteles, y otros servicios turísticos.",
          "industry": "Administrativos",
          "activations": 3,
          "rate": 4.2,
          "usedBy": [
            {
              "id": "ub31",
              "agentId": 31,
              "client": {
                "id": "c31",
                "name": "ViajaFácil",
                "lastName": "Viajes",
                "email": "contacto@viajafacil.com",
                "password": "securepass31"
              },
              "useDate": "2024-04-18",
              "startedTime": "2024-04-18T09:00:00Z",
              "endedTime": "2024-04-18T18:00:00Z"
            }
          ],
          "feedback": [
            {
              "id": "f31",
              "agentId": 31,
              "clientId": "c31",
              "text": "Muy buen servicio de asesoramiento y reservas.",
              "value": 4.2
            }
          ],
          "rateEntries": [
            {
              "id": "r31",
              "rate": 4.2,
              "clientId": "c31",
              "agentId": 31
            }
          ]
        },
        {
          "id": 32,
          "title": "Ingeniero de Pruebas de Software",
          "description": "Encargado de diseñar, implementar y ejecutar pruebas para garantizar que el software sea funcional y libre de errores.",
          "industry": "Administrativos",
          "activations": 3,
          "rate": 4.5,
          "usedBy": [
            {
              "id": "ub32",
              "agentId": 32,
              "client": {
                "id": "c32",
                "name": "SoftCheck",
                "lastName": "Pruebas",
                "email": "contacto@softcheck.com",
                "password": "securepass32"
              },
              "useDate": "2024-04-17",
              "startedTime": "2024-04-17T08:30:00Z",
              "endedTime": "2024-04-17T16:30:00Z"
            }
          ],
          "feedback": [
            {
              "id": "f32",
              "agentId": 32,
              "clientId": "c32",
              "text": "Las pruebas fueron muy exhaustivas y contribuyeron al éxito del proyecto.",
              "value": 4.5
            }
          ],
          "rateEntries": [
            {
              "id": "r32",
              "rate": 4.5,
              "clientId": "c32",
              "agentId": 32
            }
          ]
        }
    ]
    
    return JsonResponse(agents_list, safe=False)