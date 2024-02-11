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
});
