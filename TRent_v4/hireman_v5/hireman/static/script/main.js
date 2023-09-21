

// var datetime = new Date();
// console.log(datetime);
// document.getElementById("time").textContent = datetime; //it will print on html page
// function refreshTime() {
//     const timeDisplay = document.getElementById("time");
//     const dateString = new Date().toLocaleString();
//     const formattedString = dateString.replace(", ", " - ");
//     timeDisplay.textContent = formattedString;
// }
// setInterval(refreshTime, 1000);



// var live_time = document.getElementById('live_time');

// function time() {
//     var d = new Date();
//     var s = d.getSeconds();
//     var m = d.getMinutes();
//     var h = d.getHours();
//     live_time.textContent = ("0" + h).substr(-2) + ":" + ("0" + m).substr(-2) + ":" + ("0" + s).substr(-2);
// }

// setInterval(time, 1000); 


// var live_time = document.getElementById('time');

// function time() {
//     var d = new Date();
//     var s = d.getSeconds();
//     var m = d.getMinutes();
//     var h = d.getHours();
//     live_time.textContent = ("0" + h).substr(-2) + ":" + ("0" + m).substr(-2) + ":" + ("0" + s).substr(-2);
//     live_time.style.color = "green"
// }

var live_date = document.getElementById('data');

function time() {
    var isziua = new Array("Luni", "Marti", "Miercuri", "Joi", "Vineri", "Sambata", "Duminica");
    // if (isziua[dd] == "Duminica") {
    //     live_date.style.color = "red" 
    // } if (isziua[dd] == "Sambata") {
    //     live_date.style.color = "orange" 
    // } else {
    //     live_date.style.color = "green"
    // }
    var today = new Date();
    var dd = today.getDate();
    var mm = today.getMonth()+1; //January is 0!
    var yyyy = today.getFullYear();
    live_date.textContent = "Data"+ ': ' + ("0" + dd).substr(-2) + "-" + ("0" + mm).substr(-2) + "-" + ("0" + yyyy).substr(-4);
    console.log(dd)
}

setInterval(time, 1000);
