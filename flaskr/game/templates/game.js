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