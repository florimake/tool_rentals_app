

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



var live_time = document.getElementById('live_time');

function time() {
    var d = new Date();
    var s = d.getSeconds();
    var m = d.getMinutes();
    var h = d.getHours();
    live_time.textContent = ("0" + h).substr(-2) + ":" + ("0" + m).substr(-2) + ":" + ("0" + s).substr(-2);
}

setInterval(time, 1000); 