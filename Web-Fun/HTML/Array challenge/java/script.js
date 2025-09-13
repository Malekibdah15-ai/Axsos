function alwaysHungry(arr) {
    var isyummy=false;
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] == "food") {
            console.log("yemmy");
            isyummy=true;
        }

    }
    if(isyummy==false){
        console.log("im hungry");

    }
}


alwaysHungry([3.14, "food", "pie", true, "food"]);


function highPass(arr, cutoff){
var filterdArr = [];
for( var i = 0; i < arr.length; i++){
    if( arr[i] > 5){
        console.log(arr[i]);

      filterdArr.push(arr[i])

    }
}
return filterdArr;

}

var result = highPass([6, 8, 3, 10, -2, 5, 9], 5);
console.log(result);


function betterThanAverage(arr) {

  var sum = 0;
  for (i = 0; i < arr.length; i++) {
    sum += arr[i];
    var average = sum / arr[i];
  }

  var count = 0;
  for (var i = 0; i < arr.length; i++) {



    if (arr[i] > average) {

      count++;
    }
  }
  return count;
}


var result = betterThanAverage([6, 8, 3, 10, -2, 5]);
console.log(result);


function reverse(arr) {
    var reversed = [];
    // loop from end to start
    for (var i = arr.length - 1; i >= 0; i--) {
        reversed.push(arr[i]);
    }
    return reversed;
}

var result = reverse(["a", "b", "c", "d", "e"]);
console.log(result); // we expect back ["e", "d", "c", "b", "a"]


function fibonacciArray(n) {
    
    var fibArr = [0, 1];

    
    for (var i = 2; i < n; i++) {
        fibArr.push(fibArr[i - 1] + fibArr[i - 2]);
    }

    return fibArr;
}

var result = fibonacciArray(10);
console.log(result); 
// we expect back [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]