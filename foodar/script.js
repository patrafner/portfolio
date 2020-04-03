//for banner
function openBanner() {
        document.getElementById("banner").style.height = "10vh";
        document.getElementById("banner").style.visibility = "visible";
        document.getElementById("banner").style.position = "relative";
      }
      setTimeout(openBanner, 3000);

function closeBanner() {
        document.getElementById("banner").style.height = "0";
        document.getElementById("banner").style.visibility = "hidden";
      };
      setTimeout(closeBanner, 10000);

//for zipcode

var cityElem = "zipResult";
var cityButton = "cityChecker";
var cityInput = "userZip";
var deliveryZip = [ 93001, 93002, 93003, 93020, 93021, 93022, 93023];

function findDriver(){
  //get zip and check if in valid area
  var btn = g("cityChecker");
  if (btn != null){

    btn.addEventListener("click", function zipChecker() {

      console.log("working...");
      var userZip = g(cityInput).value;
      var resultElem = g(cityElem);

      if(userZip != null)  {
        var inArea = false;

        //check array of cities served
        for(var i = 0; i < deliveryZip.length; i++) {
          if(userZip == deliveryZip[i]){
            inArea = true;
            break;}
        }

        if(inArea){
          resultElem.innerHTML = "We cover that area! Start your order <a href=\"./request.html\" style=\"color: black; text-decoration:underline;font-weight:bold;\">now</a>!";
          resultElem.style.color = "green";
        } else {
          resultElem.innerHTML = "Unfortunately, you are not in a delivery zone";
          resultElem.style.color = "red";
        }
    }});
  }
}
//shorthand
function g(id){
  return document.getElementById(id);
}

findDriver();
//updateCity();





var x = document.getElementById("greet");
var counter = 0;
var text = ["Welcome", "Hello", "Salut", "Bonjour", "Hola"];
setInterval(greets, 1000);


function greets(){
	
	x.innerHTML = text[counter];
	counter ++;
	if (counter >= text.length) {
    counter = 0;
	}
	
}

setInterval(setColor, 1300);

function setColor() {
  var x = document.getElementById("color");
	if(x.style.color=="black")
       x.style.color="red";
      else if (x.style.color=="red")
       x.style.color="blue";
      else if (x.style.color=="blue")
       x.style.color="yellow";
	  else if (x.style.color=="yellow")
       x.style.color="black";
      else x.style.color="black";
  
}

//for request page claculate total

var form = document.getElementById("foodForm");

form.addEventListener("change", calculateTotal);

function calculateTotal(){
  var result = 0;
  console.log("Calculating...");

  
  var foodStyle = document.getElementsByClassName("food-style");
  console.log(foodStyle)
  for(i=0; i < foodStyle.length; i++){
    if(foodStyle[i].checked){
      result = Number(foodStyle[i].value);
    }
  }


  
  var tip = document.getElementsByClassName("tip");
  for(i=0; i < tip.length; i++){
    if(tip[i].checked){
      result = result + (result*Number(tip[i].value));
    }
  }

  result = result.toFixed(2);

  var totalElem = document.getElementById('totalCost');
  totalElem.innerHTML = result;
}






