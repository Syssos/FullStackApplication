const urlParams = new URLSearchParams(window.location.search);
const product = urlParams.get('item');
const defaultValues = ["SKU", "ProductName", "ProductImage", "ProductDescription", "Price", "Amount", "Platform", "__class__"];

if ('caches' in window){    
    caches.open(HOCUS_CACHE).then(cache => {
        cache.match(HOCUS_API).then(settings => {
            if (settings && product) {
                settings.json().then(data => {
                    for (const thing of data) {
                        if (thing.SKU == product) {                            
                            var cat = document.getElementById("category")
                            cat.innerHTML = pretifyThis[thing.Platform];
                            cat.href= `browse?platform=${thing.Platform}`;
                            
                            var sub = document.getElementById("subcategory")
                            sub.innerHTML = pretifyThis[thing.__class__];
                            sub.href= `browse?sub=${thing.__class__}`;
                            
                            document.getElementById("category-list").innerHTML += `<li class="breadcrumb-item active" aria-current="page" id="product">${thing.ProductName}</li>`;
                            
                            var ele = `<div class="item-image"><img src="${thing.ProductImage}" width="60%" height="100%" /></div>
                                       <div class="item-title">${thing.ProductName}</div>
                                       <div class="item-description">${thing.ProductDescription}</div>
                                       <div class="item-details" id="item-details">
                                           <div class="item-detials-price">$${thing.Price}</div>
                                       </div>`
                            document.getElementById('item-container').innerHTML = ele;
                            var itemContainer = document.getElementById('item-details');
                            itemContainer.innerHTML+= '<br />';
                            for (const property in thing) {
                                if (!defaultValues.includes(property)) {
                                    itemContainer.innerHTML += `<div class="item-detials-bullet"><b>${property}</b>: ${thing[property]}</div>`;
                                }
                            }
                        }
                    }
                })
            } else {
                // No item in url
                console.log("no item found");
            }
        })
    })
}