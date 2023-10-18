// function solution(want, number, discount) {
//     var answer = 0;    
//     var len = discount.length - 10;
//     for(let i=0; i<len+1; i++){
//         var newDiscount = discount.slice(i, i+10);
//         for(let j=0; j<10; j++){
//             if(want.includes(newDiscount[0])){
//                 newDiscount.shift();
//             }
//         }
//         if(newDiscount.length===0){
//             return i;
//         }
//     }
//     return 0;
// }

function solution(want, number, discount) {
    let result = 0
    discount.forEach((v,i)=>{

     let copy=[...discount].slice(i,i+10)
     if(copy.length<10)return result

     let flag=0
     for(let j=0;j<want.length;j++){
      if([...copy].filter(el=>el==want[j]).length==number[j]) 
       flag++

      else break
     }

     if(flag==want.length)result++

  })

    return result
}