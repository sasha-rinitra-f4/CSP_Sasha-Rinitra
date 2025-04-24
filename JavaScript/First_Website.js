let images = ["https://oca-wp-journals.s3.eu-west-2.amazonaws.com/wp-content/uploads/sites/2229/2021/10/Untitled-1024x791.png", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSTo8qfvL3lLIo8a6g81krHF35U2jwrdsQnng&s", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQkFAfGc-INVp75THKKuWPLwEvQ0wJTxRle9g&s"]

function more(){
    if(document.getElementById("extra").style.display != "flex"){
        document.getElementById("extra").style.display = "flex"
        document.getElementById("shw").innerHTML ="Show Less"
    }else{
        document.getElementById("extra").style.display = "none"
        document.getElementById("shw").innerHTML ="Show More"
    }
    
}
count = 0
function change(){
    document.getElementById("img").src = images[count]
    if(count === 2){
        count =0
    }else{
        count+=1
    }
}