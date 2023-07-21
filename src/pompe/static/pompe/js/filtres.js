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
// filtre des huiles
function filtreHuile() {
  // Variables
  var input, filter, para, div;
  input = document.getElementById('recherche');
  filter = input.value.toUpperCase();
  para = document.querySelectorAll('p.nom');
  div = document.querySelectorAll('div.filtre')

  // boucle sur les éléments
  for (var i = 0; i < para.length; i++) {
    var currentPara = para[i].innerText.toUpperCase();
    if (currentPara.indexOf(filter) > -1) {
      div[i].style.display = ""; // Show the paragraph
    } else  {
      div[i].style.display = "none"; // Hide the paragraph
    }
  }
}
// filtre des kits
function filtreKit() {
  // Variables
  var input, filter, para, div;
  input = document.getElementById('recherche');
  filter = input.value.toUpperCase();
  para = document.querySelectorAll('p.nom');
  div = document.querySelectorAll('div.filtre');

  // Loop through para elements
  for (var i = 0; i < para.length; i++) {

        var currentPara = para[i].innerText.toUpperCase();
    console.log("currentpara= ", currentPara);
    if (currentPara.indexOf(filter) > -1) {
            div[i].style.display = ""; // Show the div}
    } else {
            div[i].style.display = "none"; // Hide the div}
    }
  }
}
// filtre des pieces détachées
function filtrePieceD() {
  // Variables
  var input, filter, para, div;
  input = document.getElementById('recherche');
  filter = input.value.toUpperCase();
  para = document.querySelectorAll('p.nom');
  para2 = document.querySelectorAll('p.marque');
  div = document.querySelectorAll('div.filtre');
  console.log("para=", para);
  console.log("div =", div);
   console.log("filter =", filter);

  // Loop through para elements
  for (var i = 0; i < para.length; i++) {
    var currentPara = para[i].innerText.toUpperCase();
    var currentPara2 = para2[i].innerText.toUpperCase();
    console.log("currentpara= ", currentPara);
    if (currentPara.includes(filter) || currentPara2.includes(filter)) {
            div[i].style.display = ""; // Show the div
    } else {
            div[i].style.display = "none"; // Hide the div
    }
  }
}



