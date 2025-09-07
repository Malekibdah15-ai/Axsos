function btn(el){
    
    console.log(el);
    
    if(el.innerText == "Login"){
        el.innerText ="Logout";
    }
    
    else{
    el.innerText ="Login";
    }
}
function removeElement(el){
    el.remove()
}
function showAlert(){
   alert("Ninja was liked");
}
    

