function addNewInput(){
  var newInputBox = document.createElement('div');
  newInputBox.innerHTML = "<input type = 'datetime-local' id = 'new' name = 'availability'>";
  document.getElementById("newInputBox").appendChild(newInputBox);
}
