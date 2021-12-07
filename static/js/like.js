var dishes = document.getElementsByClassName("like_dish");
console.log(dishes)
for(let i = 0; i < dishes.length; i++){
    dishes[i].addEventListener("click", function(event){
        console.log("DSADA SDA SDASD")
        var dish_pk = this.getAttribute("dish_pk");
        var endpoint = this.getAttribute("endpoint");
        console.log(logged_in)
        fetch(endpoint, {
            method: 'POST',
            headers: {
                "X-CSRFToken": getCookie('csrftoken'),
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                "dish_pk": dish_pk
            }),
        })
      .then(response => response.json())
      .then(data => {
        console.log(data)
          if(data){
            dishes[i].classList.add("liked")
            dishes[i].innerHTML = "Saved"
          }
          else{
            dishes[i].classList.remove("liked")
            dishes[i].innerHTML = "Save"
          }
      });
    })
}