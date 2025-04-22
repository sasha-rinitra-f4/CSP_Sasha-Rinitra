let images = ["https://www.earthdiver.com/cdn-cgi/image/width=4000,quality=75,format=auto/https://assets.earthdiver.com/media/media-image-2760238.jpg?w=2500&h=1443&tick=1685654097009?yyy", "https://www.fs.usda.gov/wildflowers/regions/intermountain/MtTimpanogos/images/MtTimpanogosinSpring_FrankJensen_lg.jpg", "https://assets.simpleviewinc.com/simpleview/image/upload/c_fill,h_506,q_75,w_900/v1/clients/utahvalley/temp_c99a8c67_d5ca_41dd_ae83_9c5f674da77e_ef94838d-878d-4283-8262-88d4532e5344.jpg"]
function hello(){
    document.getElementById("title").innerHTML = "Hello World!"
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

function highlight(){
    document.getElementById("btn").style.backgroundColor ="orange"
    document.getElementById("btn").style.color ="white"
}

function normal(){
    document.getElementById("btn").style.backgroundColor ="gray"
    document.getElementById("btn").style.color ="black"
}

function show(){
    document.getElementById("hidden").style.display ="black"
}

