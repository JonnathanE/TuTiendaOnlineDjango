// init Isotope
// Aquí seleccionamos el elemento con la clase .collection-list y lo pasamos a Isotope.
var gridElement = document.querySelector(".collection-list");
var iso = new Isotope(gridElement, {
  // opciones
});

// Función para restablecer los botones de filtro
// Esta función elimina la clase active-filter-btn de todos los botones dentro del grupo de botones de filtro.
function resetFilterBtns() {
  var filterBtns = document.querySelectorAll(".filter-button-group button");
  filterBtns.forEach(function (btn) {
    btn.classList.remove("active-filter-btn");
  });
}

// Manejar el clic en los botones de filtro
// Aquí añadimos un eventListener al contenedor de los botones de filtro para detectar los clics en los botones. Si el elemento clicado es un botón, obtiene el valor del filtro del atributo data-filter, resetea los botones de filtro, añade la clase active-filter-btn al botón clicado y aplica el filtro usando iso.arrange
var filterButtonGroup = document.querySelector(".filter-button-group");
filterButtonGroup.addEventListener("click", function (event) {
  if (event.target.tagName === "BUTTON") {
    var filterValue = event.target.getAttribute("data-filter");
    resetFilterBtns();
    event.target.classList.add("active-filter-btn");
    iso.arrange({ filter: filterValue });
  }
});

// Con estos cambios, tendrás el mismo comportamiento que en tu código jQuery pero utilizando JavaScript puro.
// // init Isotope
// var $grid = $(".collection-list").isotope({
//   // options
// });
// // filter items on button click
// $(".filter-button-group").on("click", "button", function () {
//   var filterValue = $(this).attr("data-filter");
//   resetFilterBtns();
//   $(this).addClass("active-filter-btn");
//   $grid.isotope({ filter: filterValue });
// });

// var filterBtns = $(".filter-button-group").find("button");
// function resetFilterBtns() {
//   filterBtns.each(function () {
//     $(this).removeClass("active-filter-btn");
//   });
// }
