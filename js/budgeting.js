var months = []
var merc = [];
var monthSpending = [];
var mercSpending = [];

function sum(arr) {
    return arr.reduce(function (a, b) {
        return a + b;
    }, 0);
}

function spendingByMonth () {
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

        monthSpending = [];
       for (var i = 0; i < results.length; i++){
            var base = results[i];
            months[i] = base.month;
            monthSpending[i] = base.spending;

        }

        var monthLen = months.length;
        var monthSave = (months[monthLen] - months[monthLen-1])/months[monthLen-1];

        var firstStatus = document.querySelector("#monthSpend");

        if (monthSave > 0.05*months[monthLen-1]) {
            firstStatus.innerHTML = "--Complete";
        }
        else {
            firstStatus.innerHTML = "--Incomplete";
        }

        var ctx = document.getElementById("monthChart").getContext('2d');
        var monthChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: months,
                datasets: [{
                    label: '$ Spent',
                    data: monthSpending,
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(255, 206, 86, 0.2)',
                        'rgba(75, 192, 192, 0.2)',
                        'rgba(153, 102, 255, 0.2)',
                        'rgba(255, 159, 64, 0.2)',
                        'rgba(75, 159, 64, 0.2)'
                    ],
                    borderColor: [
                        'rgba(255,99,132,1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 206, 86, 1)',
                        'rgba(75, 192, 192, 1)',
                        'rgba(153, 102, 255, 1)',
                        'rgba(255, 159, 64, 1)',
                        'rgba(75, 159, 64, 1)'
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                // responsive: false,
                scales: {
                    yAxes: [{
                        ticks: {
                            max: 10000,
                            beginAtZero:true
                        }
                    }]
                }
            }
        });

        var totalSum = Math.round(sum(monthSpending));
        document.querySelector("#totalSum").innerHTML = " $" + totalSum;
    }

    request.send(null);
}

window.onload = spendingByMonth();

function spendingByCompany () {
    var request = new XMLHttpRequest();
    request.open('GET', 'http://127.0.0.1:5000/company_spending', true);
    request.responseText = "json"

    request.onreadystatechange = function () {
        var results2;
        if (this.readyState === 4) {
            results2 = JSON.parse(this.response);
        }
        else {
            results2 = {};
        }

        mercSpending = [];
        for (var i = 0; i < results2.length; i++){
            var base2 = results2[i];
            mercSpending[i] = base2.spending;
            merc[i] = base2.merc;
        }

        var ctx2 = document.getElementById("companyChart").getContext('2d');
        var companyChart = new Chart(ctx2, {
            type: 'bar',
            data: {
                labels: merc,
                datasets: [{
                    label: '$ Spent',
                    data: mercSpending,
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(255, 206, 86, 0.2)',
                        'rgba(75, 192, 192, 0.2)',
                        'rgba(153, 102, 255, 0.2)',
                        'rgba(255, 159, 64, 0.2)',
                        'rgba(125, 75, 64, 0.2)',
                        'rgba(91, 102, 255, 0.2)',
                        'rgba(153, 159, 64, 0.2)',
                    ],
                    borderColor: [
                        'rgba(255,99,132,1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 206, 86, 1)',
                        'rgba(75, 192, 192, 1)',
                        'rgba(153, 102, 255, 1)',
                        'rgba(255, 159, 64, 1)',
                        'rgba(255, 159, 64, 1)',
                        'rgba(125, 75, 64, 1)',
                        'rgba(91, 102, 255, 1)',
                        'rgba(153, 102, 255, 1)'
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
                            max: 1200,
                            beginAtZero:true
                        }
                    }]
                }
            }
        });
    }

    request.send(null);
}

window.onload = spendingByCompany();

function totalIncome () {
    var request = new XMLHttpRequest();
    request.open('GET', 'http://127.0.0.1:5000/total_income', true);
    request.responseText = "json"

    request.onreadystatechange = function () {
        var results3;
        if (this.readyState === 4) {
            results3 = JSON.parse(this.response);
        }
        else {
            results3 = {};
        }

        var totalIncome = Math.round(results3.points);
        document.querySelector("#totalIncome").innerHTML = " $" + totalIncome;

    }

    request.send(null);
}

window.onload = totalIncome();

function savingsAccount () {
    var request = new XMLHttpRequest();
    request.open('GET', 'http://127.0.0.1:5000/get_bank_total', true);
    request.responseText = "json";

    request.onreadystatechange = function () {
        var results4;
        if (this.readyState === 4) {
            results4 = JSON.parse(this.response);
        }
        else {
            results4 = {};
        }

        var savings = results4.result;
        var goal = 10000;

        var secondStatus = document.querySelector("#savingsProgress");

        if (savings > goal) {
            secondStatus.innerHTML = "--Complete";
        }
        else {
            secondStatus.innerHTML = "--Incomplete";
        }

    };

    request.send(null);
}

window.onload = savingsAccount();




