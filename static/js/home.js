function featureIsOk(featureId, country) {
	$.ajax({
		type: "POST",
		cache: false,
		data:{featureId:featureId, country:country},
		url: "http://127.0.0.1:5000/featureIsOk",
		dataType: "json",
		success: function(data) { 
			// if pub need to be show we recieve 1
			if ("1" == data) {
				$('#pub' + featureId).show();
			}
		},
		error: function(jqXHR) {
			console.log("error: " + jqXHR);            }
	})
}

$(document).ready(function() {
	featureIsOk("1", "EN");
	featureIsOk("2", "FR");
	featureIsOk("3", "EN");
});

$('#pub1').hide();
$('#pub2').hide();
$('#pub3').hide();
