# SGE_Proyecto2Eva

Este proyecto es una API RESTful desarrollada con FastAPI, que permite gestionar un sistema de proyectos, tareas y usuarios. Utiliza SQLAlchemy como ORM para interactuar con una base de datos PostgreSQL, definida con las tablas correspondientes para usuarios, proyectos y tareas. Además, emplea Pydantic para la validación de datos de entrada y salida a través de modelos y esquemas.

La API está dividida en varios routers para cada entidad: proyecto, tarea, y usuario, lo que facilita la organización y mantenimiento del código. Los routers ofrecen las siguientes funcionalidades:
  1. Proyectos: Crear, obtener todos, obtener por ID, modificar y eliminar proyectos.
  2. Usuarios: Crear, obtener todos, obtener por ID, modificar y eliminar usuarios, con la posibilidad de asignar proyectos a cada uno.
  3. Tareas: Crear, obtener todas, obtener por ID, modificar y eliminar tareas, asociándolas con proyectos específicos.

PostgreSQL se emplea como base de datos para almacenar la información, y se utiliza Psycopg2 para la conexión con la base de datos. Además, las fechas y la gestión de tiempo se manejan con Datetime para asegurar la precisión en los registros de creación y actualización.

El proyecto también cuenta con la capacidad de modificar ciertos campos de los registros, como fechas y estados, a través de clases específicas de actualización (UpdateUsuario, UpdateProyecto, UpdateTarea), facilitando la modificación parcial de los datos sin necesidad de reescribir toda la información.

El servidor Uvicorn se usa para ejecutar la aplicación de manera eficiente y permitir el recargado automático durante el desarrollo. En resumen, el proyecto implementa una API robusta y flexible para la gestión de proyectos, tareas y usuarios, con validación de datos, manejo de relaciones entre entidades y persistencia de datos en una base de datos PostgreSQL.

[Enlace a la memoria](https://github.com/leire-yagfer/SGE_Proyecto2Eva/blob/main/SGE_proyecto2Eva_LeireYagueFernandez.pdf)
