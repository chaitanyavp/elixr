var button = document.querySelector("#testButton");
button.onclick = functionTest;

function functionTest() {
    var request = new XMLHttpRequest();
    request.open('GET', 'http://127.0.0.1:5000/test', true);
    request.responseText = "text"

    request.onreadystatechange = function () {
        if (this.readyState === 4) {
            console.log('Status:', this.status);
            console.log('Headers:', this.getAllResponseHeaders());
            console.log('Body:', this.response);
        }
    };

    request.send(null);
}
