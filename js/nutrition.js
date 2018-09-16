var grocStores = []
var restStores = [];
var grocSpending = [];
var restSpending = [];

function sum(arr) {
    return arr.reduce(function (a, b) {
        return a + b;
    }, 0);
}

function spendingGroc () {
    var request = new XMLHttpRequest();
    request.open('GET', 'http://127.0.0.1:5000/grocery_spending', true);
    request.responseText = "json";

    request.onreadystatechange = function () {
        var results;
        if (this.readyState === 4) {
            results = JSON.parse(this.response);
        }
        else {
            results = {};
        }

        grocSpending = [];
        for (var i = 0; i < results.length; i++){
            var base = results[i];
            grocStores[i] = base.category;
            grocSpending[i] = base.spending;

        }

        var ctx = document.getElementById("grocChart").getContext('2d');
        var grocChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: grocStores,
                datasets: [{
                    label: '$ Spent',
                    data: grocSpending,
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(255, 206, 86, 0.2)',
                        'rgba(75, 192, 192, 0.2)',
                        'rgba(153, 102, 255, 0.2)'
                    ],
                    borderColor: [
                        'rgba(255,99,132,1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 206, 86, 1)',
                        'rgba(75, 192, 192, 1)',
                        'rgba(153, 102, 255, 1)'
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                // responsive: false,
                scales: {
                    yAxes: [{
                        ticks: {
                            max: 600,
                            beginAtZero:true
                        }
                    }]
                }
            }
        });

        var totalSum = sum(grocSpending);
        document.querySelector("#totalSumGroc").innerHTML = " $" + totalSum;
    }

    request.send(null);
}

window.onload = spendingGroc();

function spendingRest () {
    var request = new XMLHttpRequest();
    request.open('GET', 'http://127.0.0.1:5000/eatingout_spending', true);
    request.responseText = "json"

    request.onreadystatechange = function () {
        var results2;
        if (this.readyState === 4) {
            results2 = JSON.parse(this.response);
        }
        else {
            results2 = {};
        }

        restSpending = [];
        for (var i = 0; i < results2.length; i++){
            var base2 = results2[i];
            restSpending[i] = base2.spending;
            restStores[i] = base2.category;
        }

        var ctx2 = document.getElementById("restChart").getContext('2d');
        var restChart = new Chart(ctx2, {
            type: 'bar',
            data: {
                labels: restStores,
                datasets: [{
                    label: '$ Spent',
                    data: restSpending,
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(255, 206, 86, 0.2)',
                        'rgba(75, 192, 192, 0.2)',
                        'rgba(153, 102, 255, 0.2)',
                        'rgba(255, 159, 64, 0.2)'
                    ],
                    borderColor: [
                        'rgba(255,99,132,1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 206, 86, 1)',
                        'rgba(75, 192, 192, 1)',
                        'rgba(153, 102, 255, 1)',
                        'rgba(255, 159, 64, 1)',
                        'rgba(255, 159, 64, 1)'
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                // responsive: false,
                display: true,
                scales: {
                    yAxes: [{
                        ticks: {
                            max: 600,
                            beginAtZero:true
                        }
                    }]
                }
            }
        });

        var totalSum = sum(restSpending);
        document.querySelector("#totalSumRest").innerHTML = " $" + totalSum;
    }

    request.send(null);
}

window.onload = spendingRest();

function getGroceries () {
    var request = new XMLHttpRequest();
    request.open('GET', 'http://127.0.0.1:5000/get_groceries', true);
    request.responseText = "json";

    request.onreadystatechange = function () {
        var results2;
        if (this.readyState === 4) {
            results2 = JSON.parse(this.response);
        }
        else {
            results2 = {};
        }

        var firstStatus = document.querySelector("#grocMore");

        if (results2[2] > results2[0]) {
            firstStatus.innerHTML = "--Complete";
        }
        else {
            firstStatus.innerHTML = "--Incomplete";
        }

    };

    request.send(null);
}

window.onload = getRest();

function getRest () {
    var request = new XMLHttpRequest();
    request.open('GET', 'http://127.0.0.1:5000/get_rest', true);
    request.responseText = "json";

    request.onreadystatechange = function () {
        var results3;
        if (this.readyState === 4) {
            results3 = JSON.parse(this.response);
        }
        else {
            results3 = {};
        }

        var secondStatus = document.querySelector("#restLess");

        if (results3[2] < results3[0]) {
            secondStatus.innerHTML = "--Complete";
        }
        else {
            secondStatus.innerHTML = "--Incomplete";
        }

    };

    request.send(null);
}

window.onload = getGroceries();




