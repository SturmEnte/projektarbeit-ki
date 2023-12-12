const URL = "http:/127.0.0.1:3000";

const colorPicker = document.getElementById("colorpicker");

colorPicker.oninput = () => {
	console.log(colorPicker.value);
	var root = document.querySelector(":root");
	root.style.setProperty("--main-color", colorPicker.value);
};
