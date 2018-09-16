var button = document.getElementbyId("testButton");
button.onclick = functionTest;

function functionTest() {
    var request = new XMLHttpRequest();
    request.open('GET', 'http://127.0.0.1:5000/test', true);

    request.onload = function () {
        console.log(request.responseText)
    };

    request.send(null);
}
