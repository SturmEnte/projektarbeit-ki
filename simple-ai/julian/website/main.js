const colorPicker = document.getElementById("colorpicker")

colorPicker.oninput = (event) => {
    console.log(colorPicker.value);
    var root = document.querySelector(":root");
    root.style.setProperty("--main-color", colorPicker.value);
}
 