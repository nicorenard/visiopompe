//
function filtreFabriquant() {
  var input, filter, tr, i;
  input = document.getElementById('recherche');
  filter = input.value.toUpperCase();
  tr = document.getElementsByTagName("tr");

  // boucle basé sur la recherche par nom de classe d'element.
  //https://developer.mozilla.org/en-US/docs/Web/API/Document/getElementsByClassName
  for (i = 0; i < tr.length; i++) {
    tdFabriquant = tr[i].getElementsByClassName("nom")[0];
    if (tdFabriquant) {
      txtValueNom = tdFabriquant.textContent || tdFabriquant.innerText;
      if (txtValueNom.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }
  }
}