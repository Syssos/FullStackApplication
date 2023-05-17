// // canvas control for login menu needed on all pages
var myOffcanvas = document.getElementById('offcanvasLogin')
myOffcanvas.addEventListener('hide.bs.offcanvas', function () {
    document.getElementById('login-canvas').style.opacity=0;
})

myOffcanvas.addEventListener('show.bs.offcanvas', function () {
    document.getElementById('login-canvas').style.opacity=1;
})