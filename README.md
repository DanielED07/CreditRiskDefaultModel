# Credit Risk Model

## Desafio
Las entidades de crédito enfrentan de forma permanente la incertidumbre asociada al incumplimiento de las obligaciones por parte de sus clientes, lo que impacta directamente la rentabilidad y la calidad de los portafolios. Actualmente, muchas de las estrategias de gestión del riesgo son de carácter reactivo, enfocadas en la recuperación una vez ocurre el deterioro, lo que limita la capacidad de anticiparse al riesgo y mitigar oportunamente las pérdidas crediticias.

## Propuesta
Desarrollar un modelo predictivo basado en técnicas de machine learning que permita estimar la probabilidad de incumplimiento de los clientes a partir de información histórica crediticia, comportamental y financiera. Con esto, se habilitara fortalecer la gestión proactiva del riesgo mediante la identificación temprana de deterioro en el perfil de riesgo de los clientes.

## Solución
Mediante la identificación de temprana de clientes con un alto riesgo de incumplimiento, se habilitara campañas de noitificación y/o pago temprano dirigidas, reduciendo la incertidumbre del incumplimiento y mejorando el ciclo de vida de credito de los clientes.

## Estructura del Proyecto
```bash
Credit-Risk-Model
├── config/
│   ├── settings.py              # Define las CONSTANTES
│   └── functions.py             # Define las funciones auxiliares
├── data/
│   ├── clean/                   # Aqui se cargan los datos luego del proceso de limpieza
│   ├── processed/               # Aqui se cargan los datos procesados para la modelación
│   └── raw/                     # Aqui se cargan los datos crudos (.csv)
├── models/
│   ├── encoder.pkl              # Codificador para las variables categoricas
│   ├── model.pkl                # Modelo final
│   └── scaler.pkl               # Escalador para las variables numericas  
├── notebook/
│   ├── 00-Ingestion.ipynb             # Proceso de ingesta de datos
│   ├── 01-Limpieza.ipynb              # Proceso de limpieza de datos
│   ├── 02-EDA.ipynb                   # Analisis Exploratorio de datos
│   ├── 03-preprocessing.ipynb         # Proceso para organizar el dataframe
│   ├── 04-dataSplittingBalnce.ipynb   # Proceso para realizar la división y balanceo de datos
│   └── 05-modeling.ipynb              # Proceso de modelación
├── .gitignore                   # Archivos a ignorar en el repo
├── README.md                    # Documentación del proyecto
└── requirements.txt             # Paquetes necesarios
```

## 2. Requisitos Previos

* Python 3.8 o superior.

## 3. Instalación y Ejecución

1. Clona este repositorio:
   ```bash
   git clone [https://github.com/DanielED07/CreditRiskDefaultModel.git](https://github.com/DanielED07/CreditRiskDefaultModel.git)
   cd nombre-del-proyecto
   ```

2. Ejecutar los notebooks en orden