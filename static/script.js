/**
 * <!-- <img src="{{data.uploaded_image}}">
    </img>
    <br>
    <h2><label>Result: </label><b>{{ data.result }}</b></h2>
    <h4>About</h4>
    {{data.about}}
    <ul>
        {% for prediction in data.predictions %}
        <li>
            {{ prediction.name }} : {{ prediction.probability }} %
        </li>
        {% endfor %}
    </ul> -->
 */
console.log("hello")
function displayImage(input) {

    const imageCont = document.getElementById("selectedImageFile");
    imageCont.style.display = "inline";
    var reader = new FileReader();
    reader.onload = function (e) {
        document.querySelector("#selectedImageFile").setAttribute("src", e.target.result);
    };
    reader.readAsDataURL(input.files[0]);
}

function selectFile() {
    const fileSelector = document.getElementById("fileInputBar");
    fileSelector.click();
}