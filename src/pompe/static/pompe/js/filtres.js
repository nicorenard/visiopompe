// filtre fabriquant
function filtreFabriquant() {
  var input, filter, tr, i;
  input = document.getElementById('recherche');
  filter = input.value.toUpperCase();
  tr = document.getElementsByTagName("tr");

  // boucle basée sur la recherche par nom de classe d'élément.
  // https://developer.mozilla.org/en-US/docs/Web/API/Document/getElementsByClassName
  for (i = 0; i < tr.length; i++) {
    // récupère les td avec les images
    var tdFabriquant = tr[i].getElementsByClassName("nom")[0];
    if (tdFabriquant) {
      // on récupère toutes les images dans les td
      var fabs = tdFabriquant.querySelectorAll('img');
      var found = false;
      for (var j = 0; j < fabs.length; j++) {
        // on regarde si les attributs alt sont identiques au filtre que l'on recherche
        if (fabs[j].getAttribute('alt').toUpperCase() === filter) {
          found = true;
          break;
        }
      }
      // on affiche ou masque l'élément du tableau en fonction du résultat de recherche
      if (found) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }
  }
}