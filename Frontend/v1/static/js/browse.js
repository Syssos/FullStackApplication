const urlParams = new URLSearchParams(window.location.search);
const product = urlParams.get('platform');
const sub = urlParams.get('sub');

if ('caches' in window){    
    caches.open(HOCUS_CACHE).then(cache => {
        cache.match(HOCUS_API).then(settings => {
            if (settings) {
                document.getElementById("product-list").innerHTML = "";

                settings.json().then(data => {
                    // Code for initial page load goes here
                    if (product && sub) {
                        document.getElementById("Category").innerHTML = pretifyThis[product];
                        document.getElementById("Category").href = `/browse?platform=${product}`;
                        document.getElementById("Subcategory").innerHTML = pretifyThis[sub];

                        for (const thing of data) {
                            if (thing.__class__ == sub && thing.Platform == product) {
                                document.getElementById("product-list").innerHTML += `<div class=\"product-list-item\">\
                                                                                            <div class=\"product-item-image\"><a href=\"/view?item=${thing.SKU}\"><img src="${thing.ProductImage}" width="100%" height="100%" /></a></div>\
                                                                                            <div class=\"product-details\">\
                                                                                                <div class=\"product-detail-title\"><a href=\"/view?item=${thing.SKU}\">${thing.ProductName}</a></div>\
                                                                                                <div class=\"product-detail-price\"><a href=\"/view?item=${thing.SKU}\">$${thing.Price}</a></div>\
                                                                                                <div class=\"product-detail-description\">${thing.ProductDescription}</div>\
                                                                                            </div>\
                                                                                        </div>`
                            }
                        }
                    } else if (product && !sub) {
                        // Unknown category or subcategory clause
                        document.getElementById("Category").innerHTML = pretifyThis[product];
                        document.getElementById("Category").href = `/browse?platform=${product}`;
                        document.getElementById("Subcategory").style.display = 'none';
                        for (const thing of data) {
                            if (thing.Platform == product) {
                                document.getElementById("product-list").innerHTML += `<div class=\"product-list-item\">\
                                                                                            <div class=\"product-item-image\"><a href=\"/view?item=${thing.SKU}\"><img src="${thing.ProductImage}" width="100%" height="100%" /></a></div>\
                                                                                            <div class=\"product-details\">\
                                                                                                <div class=\"product-detail-title\"><a href=\"/view?item=${thing.SKU}\">${thing.ProductName}</a></div>\
                                                                                                <div class=\"product-detail-price\"><a href=\"/view?item=${thing.SKU}\">$${thing.Price}</a></div>\
                                                                                                <div class=\"product-detail-description\">${thing.ProductDescription}</div>\
                                                                                            </div>\
                                                                                        </div>`
                            }
                        }
                    } else if (sub && !product) {
                        document.getElementById("Category").innerHTML = pretifyThis[sub];
                        document.getElementById("Category").href = `/browse?sub=${sub}`;
                        document.getElementById("Subcategory").style.display = 'none';
                        for (const thing of data) {
                            if (thing.__class__ == sub) {
                                document.getElementById("product-list").innerHTML += `<div class=\"product-list-item\">\
                                                                                            <div class=\"product-item-image\"><a href=\"/view?item=${thing.SKU}\"><img src="${thing.ProductImage}" width="100%" height="100%" /></a></div>\
                                                                                            <div class=\"product-details\">\
                                                                                                <div class=\"product-detail-title\"><a href=\"/view?item=${thing.SKU}\">${thing.ProductName}</a></div>\
                                                                                                <div class=\"product-detail-price\"><a href=\"/view?item=${thing.SKU}\">$${thing.Price}</a></div>\
                                                                                                <div class=\"product-detail-description\">${thing.ProductDescription}</div>\
                                                                                            </div>\
                                                                                        </div>`
                            }
                        }
                    }
                });
            } else {
                // collects cache and reloads
                CollectCacheData();
                location.reload();
                document.getElementById("product-list").innerHTML = "No Cached Data";
            }
        })
    });
}