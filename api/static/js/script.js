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
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {  // use OR so that it works on both Chrome, Firefox, and Safari
        scrollButton.style.display = "block";
    } else {
        scrollButton.style.display = "none";
    }
};
