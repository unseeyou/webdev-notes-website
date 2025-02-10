function toggle() {
    document.getElementById("sidebar-wrapper").classList.toggle("toggled");
    fetch("/backend/toggle-sidebar").then((r) => {
        console.log(r.json());
        return r.json();
    })
}

function scrollToTop() {
    document.body.scrollTop = 0; // For Safari
    document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE, and Opera
}

window.onscroll = function() {
    var scrollButton = document.getElementById("scrollButton");
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {  // use OR so that it works on Chrome, Firefox, and Safari
        scrollButton.style.display = "block";
    } else {
        scrollButton.style.display = "none";
    }
};

function filterGlossary() {  // from https://www.w3schools.com/howto/howto_js_filter_table.asp NOT MINE
  // Declare variables
  var input, filter, table, tr, td, i, txtValue;
  input = document.getElementById("glossarySearchTerm");
  filter = input.value.toUpperCase();
  table = document.getElementById("glossary");
  tr = table.getElementsByTagName("tr");

  // Loop through all table rows, and hide those who don't match the search query
  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[0];
    if (td) {
      txtValue = td.textContent || td.innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }
  }
}
