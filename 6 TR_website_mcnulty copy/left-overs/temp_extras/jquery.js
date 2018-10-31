buttons_state = { };

  $('.btn').click(function() {
	var row_lbl = $(this).attr('id');
	console.log(row_lbl); //just for debugging not necessary
	if (row_lbl != 'submit') {
		//deselects others in buttor row
    	$('.btn#'+row_lbl).removeClass("btn-sel");
    	$(this).addClass("btn-sel");
    	//updates teh global button dictionary with selection
    	var idClicked = $(this).attr("id");
		var idValue = $(this).attr("value");
		$(buttons_state[idClicked]=idValue);
	}
  });

$(".btn#submit").click(function(){
  	console.log(buttons_state);	
});
