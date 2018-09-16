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

// var grocSpending = [];
// var restSpending = [];

// function sum(arr) {
//     return arr.reduce(function (a, b) {
//         return a + b;
//     }, 0);
// }

var stepsArray = [];

function fitnessLevel () {
    var request = new XMLHttpRequest();
    request.open('GET', 'http://127.0.0.1:5000/points_steps', true);
    request.responseText = "json";

    request.onreadystatechange = function () {
        var results2;
        if (this.readyState === 4) {
            results2 = JSON.parse(this.response);
        }
        else {
            results2 = {};
        }

        console.log(results2.steps)

        var totalSteps = results2.steps;
        var stepsGoal = 1000;
        var deficit = stepsGoal - totalSteps;
        stepsArray = [totalSteps, deficit];

        var stepsTodayAttr = document.querySelector("#stepsToday");
        var remStepsAttr = document.querySelector("#remSteps");

        stepsTodayAttr.innerHTML = totalSteps;
        remStepsAttr.innerHTML = deficit;


        var ctx = document.getElementById("fitnessData").getContext('2d');
        var myPieChart = new Chart(ctx,{
            type: 'pie',
            data: [{
                data: stepsArray
            }],
            labels: [
                'Steps Today',
                'Remaining Steps'
            ],
            options: {
                animation: {
                    animateRotate: true
                }
            }
        });
    }

    request.send(null);
}

window.onload = fitnessLevel();