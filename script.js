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


//colors
setInterval(setColor, 2000);

function setColor() {
  var x = document.getElementById("color");
	if(x.style.backgroundColor=="rgb(117, 164, 240)")
       x.style.backgroundColor="rgb(62, 133, 247)";
      else if (x.style.backgroundColor=="rgb(62, 133, 247)")
       x.style.backgroundColor="rgb(9, 94, 230)";
      else if (x.style.backgroundColor=="rgb(9, 94, 230)")
       x.style.backgroundColor="rgb(11, 67, 156)";
	  else if (x.style.backgroundColor=="rgb(11, 67, 156)")
       x.style.backgroundColor="rgb(117, 164, 240)";
      else x.style.backgroundColor="rgb(117, 164, 240)";
  
}

// When the user scrolls the page, execute myFunction
window.onscroll = function() {myFunction()};

// Get the header
var header = document.getElementById("color");

// Get the offset position of the navbar
var sticky = header.offsetTop;

// Add the sticky class to the header when you reach its scroll position. Remove "sticky" when you leave the scroll position
function myFunction() {
  if (window.pageYOffset > sticky) {
    header.classList.add("sticky");
  } else {
    header.classList.remove("sticky");
  }
} 
