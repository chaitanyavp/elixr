function getRec () {
    var request = new XMLHttpRequest();
    request.open('GET', 'http://127.0.0.1:5000/get_rec', true);
    request.responseText = "json";

    request.onreadystatechange = function () {
        var results;
        if (this.readyState === 4) {
            results = JSON.parse(this.response);
        }
        else {
            results = {};
        }

        console.log(results)

        var secondStatus = document.querySelector("#recStats");

        if (results[0] > results[1]) {
            secondStatus.innerHTML = "--Complete";
         }
         else {
             secondStatus.innerHTML = "--Incomplete";
         }

    };

    request.send(null);
}

window.onload = getRec();