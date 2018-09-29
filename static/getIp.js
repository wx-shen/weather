jQuery(function($) {
var url = 'http://chaxun.1616.net/s.php?type=ip&output=json&callback=?&_=' + Math.random();
$.getJSON(url, function(data) {
alert(data.Ip); //弹出本地ip
});
});