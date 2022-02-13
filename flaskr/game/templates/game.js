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