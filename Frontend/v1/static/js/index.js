/**
* Loads data into carousel found on homepage
*/
async function LoadCarousel() {
    var data = fetch("http://localhost:5000/api/v1/items/featured").then(x => {return x.text()});
    var count = 1
    data.then(featuredItems => {
        for (const obj of JSON.parse(featuredItems)) {
            var element = document.getElementById(`carousel-${count}`)
            element.innerHTML = obj.ProductName;
            element.href = `/view?item=${obj.SKU}`;
            element.style.backgroundImage = `url('${obj.ProductImage}')`;
            element.style.backgroundSize = `350px 275px`;
            element.style.backgroundRepeat ='no-repeat';
            element.style.backgroundPosition ='top, center';
            element.style.lineHeight ='225px';
            count++;
        }
    });
}

LoadCarousel();
// collectCartData();