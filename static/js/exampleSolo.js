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
	// ajouter ici des pubs si tu veux en tester plus
	featureIsOk("5e83812bdc4aa21f03d3ee8c", "EN", "1");
	featureIsOk("5e83815ddc4aa21f03d3ee8d", "FR", "2");
	featureIsOk("5e8381addc4aa21f03d3ee8e", "US", "3");
});

// oublie pas de cacher la pub ici
$('#pub1').hide();
$('#pub2').hide();
$('#pub3').hide();
