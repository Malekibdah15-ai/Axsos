// function alwaysHungry(arr) {
//     var isyummy=false;
//     for (let i = 0; i < arr.length; i++) {
//         if (arr[i] == "food") {
//             console.log("yemmy");
//             isyummy=true;
//         }

//     }
//     if(isyummy==false){
//         console.log("im hungry");
        
//     }
// }


// alwaysHungry([3.14, "food", "pie", true, "food"]);


// function highPass(arr, cutoff){
// var filterdArr = [];
// for( var i = 0; i < arr.length; i++){
//     if( arr[i] > 5){
//         console.log(arr[i]);
        
//       filterdArr.push(arr[i])

//     }
// }
// return filterdArr;

// }

// var result = highPass([6, 8, 3, 10, -2, 5, 9], 5);
// console.log(result);


function betterThanAverage(arr){

var sum = 0;
for( i = 0; i < arr.length; i++){
  sum += arr[i];
  var average = sum/arr[i];


  for( i = 0; i < arr.length; i++)

   if(arr[i] > average)
    console.log (i)
// sum = i+
// return s
}

}
var result = betterThanAverage([6, 8, 3, 10, -2, 5]);


