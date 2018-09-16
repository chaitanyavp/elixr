var button = document.querySelector("#add-new");
button.onclick = sendFireBase;


function sendFireBase () {
    var request = new XMLHttpRequest();
    request.open('GET', 'http://127.0.0.1:5000/monthly_spending', true);
    request.responseText = "json"

    request.onreadystatechange = function () {
        var results;
        if (this.readyState === 4) {
            results = JSON.parse(this.response);
        }
        else {
            results = {};
        }
    }
}

function getAllGoals () {
    var request = new XMLHttpRequest();
    request.open('GET', 'http://127.0.0.1:5000/get_goals', true);
    request.responseText = "json"

    request.onreadystatechange = function () {
        var results;
        if (this.readyState === 4) {
            results = JSON.parse(this.response);
        }
        else {
            results = {};
        }
        for (var i = results.length - 1; i >= 0; i--) {
        	var element = document.querySelector("#rewards");
        	newlink = document.createElement('a');
			newlink.setAttribute('class', 'collection-item');
			newlink.setAttribute('href', '#!');
			newlink.textContent = results[i];
			element.appendChild(newlink);
        }
        console.log("not bad");
    }
    request.send(null);
}
window.onload = getAllGoals();