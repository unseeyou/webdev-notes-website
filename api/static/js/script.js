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