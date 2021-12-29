window.onload = function() {
    const emoji = document.getElementById("emoji-container");
	
    for(let i = 0; i < 4; i++){
  	    setTimeout(function(){
            if(i == 0)
			    emoji.children[i].style.transition = "transform 500ms ease-in-out 0s";
            else
            emoji.children[i].style.transition = "transform 500ms ease-in-out  "+i/2+"s";
    	    emoji.children[i].style.transform = "scale(1)";
        },1000);
    }
}

function cardHover(title){
    const card = document.getElementById(title);
    gridItemContainer = card.children[1];
    let offset = gridItemContainer.children[0].offsetWidth;
    let scroll = gridItemContainer.children[0].scrollWidth;
    if(scroll > offset){
        transformLen = ((scroll - offset)/offset)*-100;
        transitionDuration = scroll/offset;
        gridItemContainer.children[0].style.transition = "transform " +transitionDuration + "s linear";
        gridItemContainer.children[0].style.transform = "translateX(" + transformLen + "%)";
    }
}

function cardLeave(title){
    const card = document.getElementById(title);
    gridItemContainer = card.children[1];
    gridItemContainer.children[0].style.transition = "transform 2s ease-out";
    gridItemContainer.children[0].style.transform = "translateX(0%)";
    console.log("left");
}

function cardSubmit(title){
    const card = document.getElementById(title);
    hiddenForm = card.children[2];
    hiddenForm.submit();
}

function controlsClick(){
    const btn = document.getElementById("controls");
    const preview_src = document.getElementById("audio");
    console.log(btn.dataset.status);
    console.log("clicked");
    if(btn.dataset.status === "paused"){
  	    btn.style.transition = "clip-path 200ms ease-out";
  	    btn.style.clipPath = "polygon(0 0, 40% 0, 40% 100%, 60% 100%, 60% 0, 100% 0, 100% 100%,0 100%)";
        preview_src.play();
        btn.dataset.status = "played";
    }
    else if(btn.dataset.status === "played"){
  	    btn.style.clipPath = "polygon(0 0, 50% 25%, 50% 75%, 50% 75%, 50% 25%, 100% 50%, 100% 50%, 0% 100%)";
        preview_src.pause();
        btn.dataset.status = "paused";
    }
}

function previewHover(){
    const card = document.getElementById("preview-grid");
    gridItemContainer = card.children[4];
    let offset = gridItemContainer.children[0].offsetWidth;
    let scroll = gridItemContainer.children[0].scrollWidth;
    if(scroll > offset){
        transformLen = ((scroll - offset)/offset)*-100;
        transitionDuration = scroll/offset;
        gridItemContainer.children[0].style.transition = "transform " +transitionDuration + "s linear";
        gridItemContainer.children[0].style.transform = "translateX(" + transformLen + "%)";
    }
}

function previewLeave(){
    const card = document.getElementById("preview-grid");
    gridItemContainer = card.children[4];
    gridItemContainer.children[0].style.transition = "transform 2s ease-out";
    gridItemContainer.children[0].style.transform = "translateX(0%)";
    console.log("left");
}

function accordion(id){
	const item = document.getElementById(id);
    item.classList.toggle("active");
}