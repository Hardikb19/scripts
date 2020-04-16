var a = document.getElementById('timeline_story_column');
var b = a.getElementsByClassName(' _6a-y _3l2t  _18vj');
console.log(b);
var i = 0;
function test(){
    if(b.length==i){
        console.log("done");
        return;
    }
	console.log(b[i]);
    b[i].click();
    window.setTimeout(function() {
        i=i+1;
        test();
    }, 800);
}

test(b);
