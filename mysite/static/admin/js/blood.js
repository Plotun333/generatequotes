function Blood(x,y) {
    this.x = x;
    this.y = y;

    var movedown = 60;
    this.Bobr = loadImage("/img/bobrbloodstain.png");
    this.show = function () {

        image(this.Bobr, this.x, this.y);
    }

}