# E-COMERCE COMPANY

E-COMERCE COMPANY es una aplicacion web integral disenada para gestionar y optimizar procesos de compra y venta en linea. Su objetivo principal es ofrecer una experiencia fluida, segura y eficiente tanto para los usuarios como para los administradores, integrando funcionalidades modernas de comercio electronico y gestion de usuarios.

## Descripcion General

- ⚡ **FastAPI** para el backend en Python.
- 🧰 **SQL Server** para la interaccion con la base de datos SQL (ORM).
- 🔍 **Pydantic** (usado por FastAPI) para validacion de datos y gestion de configuraciones.
- 💾 **PostgreSQL** como base de datos principal.
- 🐋 **Docker Compose** para entornos de desarrollo y produccion.
- 🔒 Hashing seguro de contrasenas por defecto.
- 🔑 Autenticacion mediante **JWT (JSON Web Token)**.
- ✅ **Pruebas automaticas**:
  - 🧪 Pytest para pruebas unitarias e integracion.
  - 📊 Pruebas de carga y estres con Apache JMeter.
- 🏭 **CI/CD** (integracion y despliegue continuo) basado en GitHub Actions.
- 🖥️ **Frontend**:
  - Desarrollado en tecnologias web modernas (especificar si es React, Vue, etc. si aplica).
  - Consumo del backend FastAPI via HTTP.
  - Interfaz de usuario intuitiva y responsiva.

## 🚀 Despliegue en Producción

La aplicación está disponible públicamente en los siguientes enlaces:

- 🔗 **Frontend (cliente web):**  
  [https://cozy-capybara-ce4155.netlify.app/](https://cozy-capybara-ce4155.netlify.app/)

- 🛠️ **Backend (API REST):**  
  [https://e-comercecompany-production.up.railway.app](https://e-comercecompany-production.up.railway.app)

---

## 🖼️ Vista previa del frontend

![Vista del frontend](https://i.postimg.cc/Vv7m7VVn/Captura-de-pantalla-2025-06-06-112935.png)


  ## Estructura del proyecto
  C:.
  └───E-ComerceCompany-main
      │   Dockerfile
      │   LICENSE
      │   Procfile
      │   README.md
      │   requirements.txt
      │   sonar-project.properties
      │
      ├───.github
      │   └───workflows
      │           build.yml
      │           sonarqube.yml           ## Tareas y funcionamiento de CI
      │           test.yml
      │
      ├───backend
      │   └───app
      │       ├───crud
      │       │       cart.py
      │       │       devolutions.py
      │       │       order.py             ## Operaciones principales
      │       │       product.py
      │       │       user.py
      │       │
      │       ├───logic
      │       │       database.py
      │       │       main.py              ## Logica de negocios y servicios
      │       │       models.py
      │       │       schemas.py
      │       │
      │       ├───routers
      │       │       cart.py
      │       │       devolutions.py
      │       │       order.py             ## Rutas de servicios
      │       │       product.py
      │       │       user.py
      │       │
      │       └───static
      │           └───images
      │                   001.jpg
      │                   002.jpg
      │                   003.jpg
      │                   004.jpg
      │                   005.jpg
      │                   006.jpg
      │                   007.jpg
      │                   008.jpg
      │                   009.jpg
      │                   010.jpg
      │                   011.jpg
      │                   012.jpg          ## Imagenes de productos
      │                   013.jpg
      │                   014.jpg
      │                   015.jpg           
      │                   016.jpg
      │                   017.jpg
      │                   018.jpg
      │                   019.jpg
      │                   020.jpg
      │                   021.jpg
      │                   022.jpg
      │                   023.jpg
      │                   024.jpg
      │                   025.jpg
      │                   026.jpg
      │                   027.jpg
      │                   028.jpg
      │                   029.jpg
      │                   030.jpg
      │
      ├───doc
      │       presentation
      │       Products_Data(Hoja1).csv    ## Documentacion, ruta e ID de cada producto
      │
      ├───frontend
      │   │   .gitignore
      │   │   index.html
      │   │   package-lock.json
      │   │   package.json                
      │   │   README.md
      │   │   view
      │   │   vite.config.js
      │   │
      │   ├───.vscode
      │   │       extensions.json         
      │   │
      │   ├───public
      │   │       vite.svg
      │   │
      │   └───src
      │       │   App.vue
      │       │   eventBus.js             ## Logica de funcionamiento
      │       │   main.js
      │       │   style.css
      │       │
      │       ├───assets
      │       │       vue.svg
      │       │
      │       └───components
      │               AdminPanel.vue
      │               Carrito.vue
      │               HelloWorld.vue
      │               PagoSimulado.vue
      │               Productos.vue
      │               Usuario.vue
      │
      └───test
          │   conftest.py
          │
          ├───db_test
          │       drivers_test.py
          │       test_database.py
          │
          ├───integration_test
          │       locustfile.py
          │       test_integracion.py             ## Test unitarios de cada producto
          │       test_integration_v1.py
          │
          └───services_test
                  test_create_cart.py
                  test_create_order.py
                  test_create_user.py
                  test_devolutions.py
                  test_product_service.py
  

## Equipo de Desarrollo
- Ellen ordoñez
- Kathy otero
- Jesus Hawasly


