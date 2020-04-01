function featuresAreOk(listFeature) {
	// requete Ajax pour un envoi de liste
	$.ajax({
		type: "POST",
		cache: false,
		url: "http://127.0.0.1:5000/featuresAreOk",
		contentType: "application/json;charset=utf-8",
		dataType: "json",
		data: JSON.stringify({listFeature}),
		success: function(data) { 
			$.each( data, function(key, value) {
				if ("1" == value) {
					$('#' + key).show();
				}
			});
		},
		error: function(jqXHR) {
			console.log("error: " + jqXHR);            }
	})
}

$(document).ready(function() {
	// ajouter ici des pubs si tu veux en tester plus
	featuresAreOk(
		{
			1: {id: "5e83812bdc4aa21f03d3ee8c", country: "EN", pubId: 'pub1'},
			2: {id: "5e83815ddc4aa21f03d3ee8d", country: "FR", pubId: 'pub2'},
			3: {id: "5e8381addc4aa21f03d3ee8e", country: "US", pubId: 'pub3'}
		}
	);
});

// oublie pas de cacher la pub ici
$('#pub1').hide();
$('#pub2').hide();
$('#pub3').hide();
