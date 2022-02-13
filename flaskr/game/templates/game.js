var loaderSceneConfig = {
    key: 'loader',
    active: true,
    preload: bootLoader,
    create: bootCreate
};

var demoSceneConfig = {
    key: 'demo',
    active: false,
    visible: false,
    create: create,
    update: update
};

var overSceneConfig = {
    key: 'over',
    active: false,
    visible: false,
    create: gameoverState
};

var scale = {
    X: window.innerWidth/320,
    Y: window.innerHeight/480,
}

var config = {
    type: Phaser.CANVAS,
    parent: 'phaser-example',
    width: window.innerWidth,
    height: window.innerHeight,
    physics: {
        default: 'arcade',
        arcade: {
            gravity: { y: 0 },
            debug: !!false
        }
    },
    scene: [ loaderSceneConfig, demoSceneConfig, overSceneConfig ],
    title:'sth-fruity',
    audio: {
        disableWebAudio: true
    }
};

var game = new Phaser.Game(config);
var cursors;
var gameCase = 0;
var gameCoins = 0;
var pointsText;
function bootLoader ()
{
    this.load.image('btnStart', 'assets/images/start.png');
    this.load.image('apple', 'assets/images/apple.png');
    this.load.image('banana', 'assets/images/banana.png');
    this.load.image('berry', 'assets/images/berry.png');
    this.load.image('berrya', 'assets/images/pear.png');
    this.load.image('bomb', 'assets/images/warm.png');
    this.load.image('background_image', 'assets/images/bj.jpg');
    this.load.image('player_role', 'assets/images/ren.png');
    this.load.image('blackboard', 'assets/images/blackboard.png');
}

function bootCreate ()
{
    this.bg = this.add.image(0, 0, 'background_image').setOrigin(0);
    this.bg.width = game.config.width;
    this.bg.height = game.config.height;
    this.bg.displayWidth = game.config.width;
    this.bg.displayHeight = game.config.height;

    this.btnStart = this.add.image(0,0,'btnStart').setOrigin(0).setInteractive();
    Phaser.Display.Align.In.Center(this.btnStart,this.bg);

    this.btnStart.on("pointerdown",function(pointer){
        gameCase = 1;
        stateStart('demo',this)
    },this);
}

function create ()
{
    this.bg = this.add.image(0, 0, 'background_image').setOrigin(0).setInteractive();
    this.bg.width = game.config.width;
    this.bg.height = game.config.height;
    this.bg.displayWidth = game.config.width;
    this.bg.displayHeight = game.config.height;

    this.player = this.add.sprite(0,0,'player_role').setOrigin(0.5,1).setScale(0.5);
    this.player.setScale(this.player.scaleX*scale.X,this.player.scaleY*scale.Y);
    Phaser.Display.Align.In.BottomCenter(this.player, this.bg);
    this.player.getCoins = 0;

    this.coins = this.physics.add.group();

	var style = { font: "bold 32px Arial", fill: "#fff", boundsAlignH: "center", boundsAlignV: "middle" };
	cursors = this.input.keyboard.createCursorKeys();
	pointsText = this.add.text(0,0,'Points: 0', style);
	pointsText.setShadow(3, 3, 'rgba(0,0,0,0.5)', 2);

    this.dt = 0;
}
function update ()
{
    
    if (gameCase!==1) {
        return false;
    }
	pointsText.setText('Points:'+this.player.getCoins);
	console.log(this.player.getCoins)

    this.dt++;
    if (this.dt%100==0) {
        for (let i = 0; i < 10; i++) {
            let coin = this.coins.create(0,0,'berry').setOrigin(0).setScale(0.5);
            let rnd = Phaser.rnd.between(1,5);
            switch (rnd) {
                case 1:
                    coin.setTexture("apple");
                    break;
                case 2:
                    coin.setTexture("banana");
                    break;
                case 3:
                    coin.setTexture("berry");
                    break;
                case 4:
                	coin.setTexture("berrya");
                	break;
                default:
                    coin.setTexture("bomb");
                    break;
            }
            coin.setGravityY(50);
            coin.setX(Phaser.rnd.between(0,game.config.width-this.coins.children.entries[i].width*this.coins.children.entries[i].scaleX));
            coin.setY(Phaser.rnd.between(0,-10000));
            coin.setScale(coin.scaleX*scale.X,coin.scaleY*scale.Y);
        }
    }

   	if (cursors.left.isDown){
   		this.player.x-= 10;
   	}
   	if (cursors.right.isDown){
   		this.player.x+= 10;
   	}
   	

    for (let i = 0; i < this.coins.children.entries.length; i++) {
        if (checkOverlap(this.player, this.coins.children.entries[i])) {
            let key = this.coins.children.entries[i].texture.key;
            switch (key) {
                case "apple":
                    this.player.getCoins += 1;
                    break;
                case "banana":
                    this.player.getCoins += 5;
                    break;
                case "berry":
                    this.player.getCoins += 10;
                    break;
                case "berrya":
                    this.player.getCoins += 15;
                    break;
                case "bomb":
                    gameCase = 3;
                    gameCoins = this.player.getCoins;
                    stateStart('over',this);
                    break;
                default:
                    break;
            }
            this.coins.children.entries[i].destroy();
         }
        
    } 
 }
