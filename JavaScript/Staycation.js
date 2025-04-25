let images = ["https://upload.wikimedia.org/wikipedia/commons/f/f0/Delicate_arch_sunset.jpg", "https://boardingpasstraveler.com/wp-content/uploads/2021/07/arches-national-park.jpg", "https://i0.wp.com/www.firefallphotography.com/wp-content/uploads/2019/06/2019-Arches-04-24-1467-HDR-Pano-Skew-1.jpg?resize=960%2C576&ssl=1"]

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