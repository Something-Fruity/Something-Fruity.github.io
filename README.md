# Something Fruity

## Assignment Brief:  
You are tasked with supporting the end-to-end life cycle of developing the software that can be used in a child’s toy. In this role, you will be required to collect the requirements of the customer requesting the toy, execute the development of the software that will be used in the toy, and deliver the software product to the customer. 
The customer should have ability to interact with the toy through an interface, and the capabilities of the programmable element of the toy should be supported using data structures and an algorithm. The development produced may not accommodate all of the customer’s requirements; interactions will take place with the customer at various stages throughout the SDLC. 

## Customer Requirements:  
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

## How to install and run the code using DOCKER:

1. Clone repository:
 - git clone git@github.com:Something-Fruity/Something-Fruity.github.io.git
2. Inside the project folder:
 - Create image using docker setup files:
   - Linux/MacOs: sudo docker-compose build --no-cache
   - Windows: !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
 - run images: 
   - Linux/MacOs: sudo docker-compose up
<!---  - Linux/MacOs: sudo docker run -p 5000:5000 something-fruitygithubio_flask-app -->


## How to install and run the code without DOCKER:

1. Clone repository:
 - git clone git@github.com:Something-Fruity/Something-Fruity.github.io.git
2. Create virual environment:
 - go inside the folder created by cloning github repository
 - run in command line: python3 -m venv [directory]
   - e.g. python3 -m venv venv
3. Activate virtual environment:
 - in command line: 
  - Linux/MacOS: source venv/bin/activate
  - Windows: venv\Scripts\activate.bat
4. Install requirements in virtual environment:
 - pip install -r flaskr\requirements
5. Set environment variables:
 - export FLASK_APP=flaskr.app
 - export FLASK_ENV=development
6. Start the server:
 - flask run

