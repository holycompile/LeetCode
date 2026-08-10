/**
 * @param {number} n
 * @return {string[]}
 */
var fizzBuzz = function(n)
{
    let output=[];
    //an function to check the divisibility 
    let check = (i)=>{
        if(i%3 ===0 && i%5===0){
            return "FizzBuzz";
        }
        else if(i%3===0){
            return "Fizz";
        }
        else if(i%5===0){
            return "Buzz";
        }
        else{
            return "Nothing";
        }
    }

    for( let i=1;i<=n;i++)
    {
        let result=check(i);
        if(result==="Nothing"){
            output.push(i.toString());
        }
        else{
            output.push(result);
        }
        
    }
    return output;
};