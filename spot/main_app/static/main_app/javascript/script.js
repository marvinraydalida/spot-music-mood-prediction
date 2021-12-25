function cardHover(title){
    const card = document.getElementById(title);
    gridItemContainer = card.children[1];
    if(gridItemContainer.children[0].innerHTML.length > 24){
        gridItemContainer.children[0].style.animation = "slide 8s";
    }
}

function cardLeave(title){
    const card = document.getElementById(title);
    gridItemContainer = card.children[1];
    gridItemContainer.children[0].style.animation = "slideCancel";
}
