$(document).ready(function(){
var url = window.location.pathname;
var filename = url.substring(url.lastIndexOf('/')+1);
console.log(filename)

if(filename == 'payment'){
    $('#cart').addClass('disabled');
}
if(filename == 'review'){
    $('#cart').addClass('disabled');
}
if(filename == 'confirmation'){
    $('#cart').addClass('disabled');
}
});