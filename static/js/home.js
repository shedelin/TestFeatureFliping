function featureIsOk(featureId, country, pubId) {
	$.ajax({
		type: "POST",
		cache: false,
		data:{featureId:featureId, country:country},
		url: "http://127.0.0.1:5000/featureIsOk",
		dataType: "json",
		success: function(data) { 
			// if pub need to be show we recieve 1
			if ("1" == data) {
				$('#pub' + pubId).show();
			}
		},
		error: function(jqXHR) {
			console.log("error: " + jqXHR);            }
	})
}

$(document).ready(function() {
	featureIsOk("5e836863bf1593d84896b3b3", "US", "1");
	featureIsOk("5e836863bf1593d84896b3b3", "EN", "2");
	featureIsOk("5e836863bf1593d84896b3b3", "FR", "3");
});

$('#pub1').hide();
$('#pub2').hide();
$('#pub3').hide();
