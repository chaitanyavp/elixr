var button = document.querySelector("#add-new");
button.onclick = sendFireBase;


function sendFireBase () {

	var request = new XMLHttpRequest();
	request.open('POST', 'http://127.0.0.1:5000/add_goal', true);

	request.setRequestHeader("Content-Type", "application/json");
	request.onreadystatechange = function () {
	    if (request.readyState === 4 && request.status === 200) {
	        getAllGoals();
	    }
	};
	var data = JSON.stringify({"text": document.querySelector("#input_one").value});
	request.send(data);
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
        var element = document.querySelector("#rewards");
    	while (element.firstChild) {
			element.removeChild(element.firstChild);
		}
        for (var i = 0; i < results.length; i++) {
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