function toggle() {
    document.getElementById("sidebar-wrapper").classList.toggle("toggled");
    fetch("/backend/toggle-sidebar").then((r) => {
        console.log(r.json());
        return r.json();
    })
}