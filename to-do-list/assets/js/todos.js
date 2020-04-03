//check off specifc todos by clicking

// $("li").click(function(){
// 	$(this).css("color", "grey");
// 	$(this).css("text-decoration", "line-through");
// })

//better way is to put all css in object
// $("li").click(function(){
	// if li is gray
// 	if ($(this).css("color") === "rgb(128, 128, 128)"){
// 		//turn it black
// 		$(this).css({
// 			color: "black",
// 			textDecoration:"none"
// 		});
// 	}
// 	else {
// 		//turn it gray
// 		$(this).css({
// 			color: "gray",
// 			textDecoration:"line-through"
// 		});
// 	}
// });
//instead of all this if statement we can do a lot easier with toggle
// use on instead of click and apply to ul not li so it works when you add more lis

$("ul").on("click", "li", (function(){
	$(this).toggleClass("completed")
}));

//click on X to delete todo and prevent the bubble effect by doing the li effect
$("ul").on("click", "span", (function(event){
	$(this).parent().fadeOut(500, function(){
		$(this).remove();//use parent to remove the entire li
	});
	event.stopPropagation();
}));

// creating new todos by clicking enter
$("input[type='text']").keypress(function(event){
	if(event.which === 13){
		//grabbing new todo from input
		var todoText = $(this).val();
		$(this).val("");
		//create a new li and add to ul with append
		$("ul").append("<li><span><i class='fas fa-trash'></i></span> " + todoText + "</li>");
	}

})

//to make + button work
$("#toggle-form").click(function(){
	$("input[type='text']").fadeToggle();
})