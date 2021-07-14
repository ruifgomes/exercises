//console.log("Hello world!")

var GOOD_DAY = true 

if (GOOD_DAY==true) {
    console.log("Bom dia")
} else {
    console.log("Mau dia")

} 

for (i=1; i<=100; i=i+1)
{   
    if(i%3==0 && i%5==0){
        console.log("OLAADEUS")
    }else if(i%3==0){
        console.log("OLA")
    }else if(i%5==0){
        console.log("ADEUS")
    }else {
        console.log(i)
    }
    
}
