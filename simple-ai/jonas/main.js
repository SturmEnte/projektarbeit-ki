const trainElement = document.getElementById("train");
const colorElement = document.getElementById("color");
const writeWithWhiteElement = document.getElementById("font-color");
const buttonElement = document.getElementById("button");

let train = false;

let trainingData = [];

trainElement.oninput = () => {
	train = trainElement.checked;
	updatePage();
};

function updatePage() {
	writeWithWhiteElement.disabled = !train;
}

buttonElement.onclick = () => {
	if (train) {
		values = colorElement.value.split("#")[1];
		console.log(values);
		red = parseInt(Number(values.slice(0, 2)), 16);
		green = parseInt(Number(values.slice(2, 4)), 16);
		blue = parseInt(Number(values.slice(4, 6)), 16);
		writeWithWhite = writeWithWhiteElement.checked;
		trainingData.push([[red, green, blue], writeWithWhite]);
	} else {
		// Give output
	}
};

updatePage();

// AI
