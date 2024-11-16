function toggle() {
    document.getElementById("sidebar-wrapper").classList.toggle("toggled");
    window.fetch("/backend/toggle-sidebar").then((r) => {
        return r.json();
    })
}