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
ª   estructura.txt
ª   
+---E-ComerceCompany-main
    ª   Dockerfile
    ª   LICENSE
    ª   Procfile
    ª   README.md
    ª   requirements.txt
    ª   sonar-project.properties
    ª   
    +---.github
    ª   +---workflows
    ª           build.yml
    ª           sonarqube.yml
    ª           test.yml
    ª           
    +---backend
    ª   +---app
    ª       +---crud
    ª       ª       cart.py
    ª       ª       devolutions.py
    ª       ª       order.py
    ª       ª       product.py
    ª       ª       user.py
    ª       ª       
    ª       +---logic
    ª       ª       database.py
    ª       ª       main.py
    ª       ª       models.py
    ª       ª       schemas.py
    ª       ª       
    ª       +---routers
    ª       ª       cart.py
    ª       ª       devolutions.py
    ª       ª       order.py
    ª       ª       product.py
    ª       ª       user.py
    ª       ª       
    ª       +---static
    ª           +---images
    ª                   001.jpg
    ª                   002.jpg
    ª                   003.jpg
    ª                   004.jpg
    ª                   005.jpg
    ª                   006.jpg
    ª                   007.jpg
    ª                   008.jpg
    ª                   009.jpg
    ª                   010.jpg
    ª                   011.jpg
    ª                   012.jpg
    ª                   013.jpg
    ª                   014.jpg
    ª                   015.jpg
    ª                   016.jpg
    ª                   017.jpg
    ª                   018.jpg
    ª                   019.jpg
    ª                   020.jpg
    ª                   021.jpg
    ª                   022.jpg
    ª                   023.jpg
    ª                   024.jpg
    ª                   025.jpg
    ª                   026.jpg
    ª                   027.jpg
    ª                   028.jpg
    ª                   029.jpg
    ª                   030.jpg
    ª                   
    +---doc
    ª       presentation
    ª       Products_Data(Hoja1).csv
    ª       
    +---frontend
    ª   ª   .gitignore
    ª   ª   index.html
    ª   ª   package-lock.json
    ª   ª   package.json
    ª   ª   README.md
    ª   ª   view
    ª   ª   vite.config.js
    ª   ª   
    ª   +---.vscode
    ª   ª       extensions.json
    ª   ª       
    ª   +---public
    ª   ª       vite.svg
    ª   ª       
    ª   +---src
    ª       ª   App.vue
    ª       ª   eventBus.js
    ª       ª   main.js
    ª       ª   style.css
    ª       ª   
    ª       +---assets
    ª       ª       vue.svg
    ª       ª       
    ª       +---components
    ª               AdminPanel.vue
    ª               Carrito.vue
    ª               HelloWorld.vue
    ª               PagoSimulado.vue
    ª               Productos.vue
    ª               Usuario.vue
    ª               
    +---test
        ª   conftest.py
        ª   
        +---db_test
        ª       drivers_test.py
        ª       test_database.py
        ª       
        +---integration_test
        ª       locustfile.py
        ª       test_integracion.py
        ª       test_integration_v1.py
        ª       
        +---services_test
                test_create_cart.py
                test_create_order.py
                test_create_user.py
                test_devolutions.py
                test_product_service.py
                

  

## Equipo de Desarrollo
- Ellen ordoñez
- Kathy otero
- Jesus Hawasly


