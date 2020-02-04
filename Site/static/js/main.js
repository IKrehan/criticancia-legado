var sound = document.getElementById('podcast-play');
var forward = document.getElementById('forwardButton');
var backward = document.getElementById('backwardButton');

/* Play\Pause Button */ 
function playAudio() {
	if (sound.paused) {
		sound.play();
		playB.className = "";
		playB.className = "fas fa-pause";
	} else {
		sound.pause();
		playB.className = "";
		playB.className = "fas fa-play";
	}
}

/* Move 5 seconds back */ 
back_button.addEventListener("click", function() 
{            	
  sound.currentTime -= 5    	
}, false);


/* Move 5 seconds forward */ 
forw_button.addEventListener("click", function() 
{    	    	
  sound.currentTime += 5    	
}, false);