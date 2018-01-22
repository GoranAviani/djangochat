$(document).ready(function(){
  var messageBody = document.getElementById('messageBody');
  if(messageBody !="undefined")
    messageBody.scrollTop = messageBody.scrollHeight - messageBody.clientHeight;
});
