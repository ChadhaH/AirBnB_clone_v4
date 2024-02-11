document.ready(function () {
	const amenities_id = {};
	$("li input[type=checkbox]").change(function () {
		if (this.checked) {
			amenities_id[this.dataset.name] = this.dataset.id;
		} else {
			delete amenities_id[this.dataset.name];
		}
		$(".amenities h4").text(Object.keys(amenities_id).sort().join(", "));
	});

	$.getJSON("http://0.0.0.0:5001/api/v1/status/", (data) => {
		if (data.status === "OK") {
			$("div#api_status").addClass("available");
		} else {
			$("div#api_status").removeClass("available");
		}
	});
});
