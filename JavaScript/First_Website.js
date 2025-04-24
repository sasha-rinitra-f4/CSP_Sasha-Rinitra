function more(){
    if(document.getElementById("extra").style.display != "flex"){
        document.getElementById("extra").style.display = "flex"
        document.getElementById("shw").innerHTML ="Show Less"
    }else{
        document.getElementById("extra").style.display = "none"
        document.getElementById("shw").innerHTML ="Show More"
    }
    
}