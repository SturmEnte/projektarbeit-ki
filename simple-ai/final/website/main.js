const TARGET = "http:/127.0.0.1:3000";

const colorPicker = document.getElementById("colorpicker");

lastInput = 0;
requested = false;

colorPicker.oninput = () => {
	console.log(colorPicker.value);
	var root = document.querySelector(":root");
	root.style.setProperty("--main-color", colorPicker.value);
	requested = false;
	lastInput = Date.now();
};

setInterval(async () => {
	if (requested == false && lastInput + 1000 <= Date.now() && lastInput != 0) {
		console.log("Now");
		console.table([requested, lastInput]);

		colorPicker.disabled = true;
		requested = true;

		const regex = /^#([a-f0-9]{2})([a-f0-9]{2})([a-f0-9]{2})$/;
		const matches = regex.exec(colorPicker.value);

		let red = parseInt(matches[1], 16);
		let green = parseInt(matches[2], 16);
		let blue = parseInt(matches[3], 16);

		red = red / 255;
		green = green / 255;
		blue = blue / 255;

		let url = new URL(TARGET);
		url.search = new URLSearchParams({ r: red, g: green, b: blue }).toString();

		const res = await fetch(url);
		const data = await res.text();

		console.log("Data:", data);
		colorPicker.disabled = false;
	}
}, 100);
