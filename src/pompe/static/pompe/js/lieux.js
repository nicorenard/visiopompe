// Script for controling the opening of tabs and put red border

function openPlace(evt, place) {
  var i, x, tabs;
  x = document.getElementsByClassName("lieux");
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
  }
  tabs = document.getElementsByClassName("tabs");
  for (i = 0; i < x.length; i++) {
    tabs[i].className = tabs[i].className.replace(" w3-border-red", "");
  }
  document.getElementById(place).style.display = "block";
  evt.currentTarget.firstElementChild.className += " w3-border-red";
}
