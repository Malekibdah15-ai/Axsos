
function pizzaOven(crustType, sauceType, cheeses, toppings) {
    let pizza = {};
    pizza.crustType = crustType;
    pizza.sauceType = sauceType;
    pizza.cheeses = cheeses;
    pizza.toppings = toppings;
    return pizza;
}


let pizza1 = pizzaOven("deep dish", "traditional", ["mozzarella"], ["pepperoni", "sausage"]);
console.log(pizza1);

let pizza2 = pizzaOven("hand tossed", "marinara", ["mozzarella", "feta"], ["mushrooms", "olives", "onions"]);
console.log(pizza2);


let pizza3 = pizzaOven("thin crust", "alfredo", ["cheddar", "parmesan"], ["chicken", "spinach", "tomatoes"]);
console.log(pizza3);

let pizza4 = pizzaOven("stuffed crust", "bbq", ["mozzarella"], ["bacon", "onions", "pineapple"]);
console.log(pizza4);


function randomPizza() {
    let crustTypes = ["deep dish", "hand tossed", "thin crust", "stuffed crust"];
    let sauceTypes = ["traditional", "marinara", "alfredo", "bbq"];
    let cheeses = [["mozzarella"], ["cheddar"], ["feta"], ["parmesan"], ["mozzarella", "cheddar"]];
    let toppings = [
        ["pepperoni", "sausage"],
        ["mushrooms", "olives", "onions"],
        ["chicken", "spinach", "tomatoes"],
        ["bacon", "pineapple"],
        ["green peppers", "jalapenos"]
    ];

    function randomChoice(arr) {
        return arr[Math.floor(Math.random() * arr.length)];
    }

    return pizzaOven(randomChoice(crustTypes), randomChoice(sauceTypes), randomChoice(cheeses), randomChoice(toppings));
}

let randomOne = randomPizza();
console.log(randomOne);
