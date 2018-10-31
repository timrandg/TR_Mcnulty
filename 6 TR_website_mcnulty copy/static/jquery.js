buttons_state = { };

  $('.btn').click(function() {
	var row_lbl = $(this).attr('id');
	console.log(row_lbl); //just for debugging not necessary
	if (row_lbl != 'submit') {
		//deselects others in button row
    	$('.btn#'+row_lbl).removeClass("btn-sel");
    	$(this).addClass("btn-sel");
    	//updates the global button dictionary with selection
    	var idClicked = $(this).attr("id");
		var idValue = $(this).attr("value");
		$(buttons_state[idClicked]=idValue);
	}
  });



$(".btn#submit").click(function(event){
	button_dict = JSON.stringify(buttons_state);
	console.log("submission button POST attempt: " + button_dict)
	
		$.ajax({
        	//contentType: "application/json; charset=utf-8",
			url: '/submission',
    		type: 'POST',
        	data: button_dict,
			success: function(response){
				alert(response);
				console.log(response);
			},
			error: function(error){
				console.log(error);
			}
		});

});



