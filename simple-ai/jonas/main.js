const trainElement = document.getElementById("train");
const colorElement = document.getElementById("color");
const fontColorElement = document.getElementById("font-color");
const buttonElement = document.getElementById("button");

let train = false;

trainElement.oninput = () => {
	train = trainElement.checked;
	updatePage();
};

function updatePage() {
	fontColorElement.disabled = !train;
}

buttonElement.oninput = () => {
	if (train) {
		// Train ai
	} else {
		// Give output
	}
};

updatePage();
