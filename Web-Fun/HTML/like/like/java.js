function log(button){
     const likeCount = button.parentElement.querySelector(".lik");
     console.log(likeCount.textContent);

     
     let count = parseInt(likeCount.textContent);
          console.log(count);
     count++;
     console.log(count);
     
     likeCount.textContent = count + " like(s)";
          console.log(likeCount.textContent);

}