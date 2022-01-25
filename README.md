# Something Fruity

- [Something Fruity](#something-fruity)
  - [Assignment Brief](#assignment-brief)
  - [Customer Requirements](#customer-requirements)
  - [How to Deploy the Project Using Docker](#how-to-deploy-the-project-using-docker)
    - [Docker Installation Guides](#docker-installation-guides)
    - [Ubuntu Deployment Instructions](#ubuntu-deployment-instructions)
    - [Windows Deployment Instructions](#windows-deployment-instructions)
  - [How to Deploy the Project without Docker](#how-to-deploy-the-project-without-docker)
  - [How to run the unit tests and check the code coverage](#how-to-run-the-unit-tests-and-check-the-code-coverage)

## Assignment Brief

You are tasked with supporting the end-to-end life cycle of developing the software that can be used in a child’s toy. 
In this role, you will be required to collect the requirements of the customer requesting the toy, execute the 
development of the software that will be used in the toy, and deliver the software product to the customer. 
The customer should have ability to interact with the toy through an interface, and the capabilities of the 
programmable element of the toy should be supported using data structures and an algorithm. The development 
produced may not accommodate all the customer’s requirements; interactions will take place with the customer at 
various stages throughout the SDLC.

## Customer Requirements

- [ ] The system should run on L/W/IOS.  
- [ ] Data must be stored in the most efficient way.

- [ ] A player should be able to create a user profile.  
- [ ] A player should be able to create a persona.
- [ ] It should be possible to create a multi-player game.

- [ ] The device should be controllable via keyboard input.  
- [ ] Sounds should be able to be muted from the UI with a single keypress.  
- [ ] Additional languages should be available as free downloadable packs.

- [ ] Angela is a 35 year old mum. She wants the game to keep her son busy.  
- [ ] Jenna is a 5 year old girl. She doesn’t want to have to ask mum for help.

## How to Deploy the Project Using Docker

### Docker Installation Guides

[Docker Windows Installation Guide](https://docs.docker.com/desktop/windows/install/)

[Docker Ubuntu Installation Guide](https://docs.docker.com/engine/install/ubuntu/)

### Ubuntu Deployment Instructions

1. [Install Docker Environment](https://docs.docker.com/engine/install/ubuntu/)
2. [Install Docker-Compose](https://docs.docker.com/compose/install/)
3. Clone repository:

   ```Terminal

   git clone https://github.com/Something-Fruity/Something-Fruity.github.io.git
   
   ```

4. Change to the Project Directory

   ```Terminal

   cd Something-Fruity.github.io/
   
   ```

5. Build Docker Services

   ```Terminal

   sudo docker-compose build --no-cache
   
   ```

6. Start Docker Containers

   ```Terminal

   sudo docker-compose up
   
   ```

7. Access the Application [http://127.0.0.1:5000](http://127.0.0.1:5000)

### Windows Deployment Instructions

1. [Install Docker Desktop Environment](https://docs.docker.com/desktop/windows/install/)
2. Clone Repository

   ```Terminal

   git clone https://github.com/Something-Fruity/Something-Fruity.github.io.git
   
   ```

3. Change to the Project Directory

   ```Terminal

   cd .\Something-Fruity.github.io\
   
   ```

4. Build Docker Services

   ```Terminal

   docker-compose build --no-cache
   
   ```

5. Start Docker Containers

   ```Terminal

   docker-compose up
   
   ```

6. Access the Application [http://127.0.0.1:5000](http://127.0.0.1:5000)

## How to Deploy the Project without Docker

1. Clone repository:

   ```Terminal

   git clone https://github.com/Something-Fruity/Something-Fruity.github.io.git
   
   ```

2. Change to the Project Directory

   ```Terminal

   cd Something-Fruity.github.io/
   
   ```

3. Create Python Virtual Environment virtual environment:

   - ```Terminal
     python3 -m venv venv
     ```

4. Activate virtual environment:
   - Linux/MacOS

   ```Terminal
   source venv/bin/activate
   ```

   - Windows

   ```Terminal
   venv\Scripts\activate.bat
   ```

5. Install Python Requirements

   ```Terminal
   pip install -r flaskr\requirements
   ```

6. Export Environment Variables
   - Windows

   ```Terminal
   set FLASK_APP = flaskr.app
   ```

    ```Terminal
   set FLASK_ENV=development
   ```

   - Linux/MacOS

   ```Terminal
   export FLASK_APP=flaskr.app
   ```

   ```Terminal
   export FLASK_ENV=development
   ```

7. Start the server:
   - flask run

## How to run the unit tests and check the code coverage

1. Make sure the database is up and running.
   Linux:  sudo service mariadb restart
2. Run the unit tests.
   Linux:  python3 -m coverage run -m unittest tests/unit/*.py
3. Output the coverage report.
   Linux:  python3 -m coverage report -m --omit=/usr/*
