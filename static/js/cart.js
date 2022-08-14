let user = '{{request.user}}' 

let updateBtns = document.getElementsByClassName("update-cart");

for (let i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener("click", function () {
        
        let productId = this.dataset.product;
        let action = updateBtns[i].dataset.action;
        
        console.log(productId);
        console.log(action);

        if (user === "AnonymousUser") {
            console.log("Not loged in");

        }else{
            updtaeUserOrder(productId, action);
        }
    })
}

function updtaeUserOrder(productId, action) {
    console.log("user is loged in sending data..")
    let url = "/update_item/"

    fetch(url, {
        method:'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken' : csrftoken
        },
        body:JSON.stringify({'productId': productId, 'action':action})
    })

    .then((response) => {
        return response.json()
    })

    .then((data) => {
        console.log('data',data)
        location.reload()
        
    })
    
}

    

